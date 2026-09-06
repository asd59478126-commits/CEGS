#!/usr/bin/env python3
"""
Stage 1 Evaluator
Evaluates baseline (D) and Construction (C1) representations
against gold_answers.json
"""

import json
import time
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, field
from collections import defaultdict

@dataclass
class AnswerSet:
    name: str
    answers: Dict[str, Any]
    cpu_time_ms: float = 0.0
    context_tokens: int = 0
    e2e_time_ms: float = 0.0

@dataclass
class EvaluationResult:
    name: str
    overall_accuracy: float = 0.0
    q4_accuracy: float = 0.0
    q1_accuracy: float = 0.0
    q2_accuracy: float = 0.0
    q3_accuracy: float = 0.0
    q5_accuracy: float = 0.0
    q6_accuracy: float = 0.0
    q7_accuracy: float = 0.0
    q8_accuracy: float = 0.0
    q9_accuracy: float = 0.0
    q10_accuracy: float = 0.0
    ucr: float = 0.0
    contradiction_rate: float = 0.0
    cpu_ms: float = 0.0
    e2e_ms: float = 0.0
    context_tokens: int = 0
    total_correct: int = 0
    total_questions: int = 0
    q4_correct: int = 0
    q4_total: int = 0
    details: Dict[str, Any] = field(default_factory=dict)

class Stage1Evaluator:
    def __init__(self, gold_answers_path: str):
        with open(gold_answers_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.gold_answers = data['answers']

        # Organize by category
        self.by_category = defaultdict(list)
        for qid in self.gold_answers.keys():
            category = qid.split('-')[0]
            self.by_category[category].append(qid)

    def normalize_answer(self, answer: Any) -> str:
        """Normalize answer to standard form"""
        if answer is None:
            return "UNKNOWN"
        if isinstance(answer, bool):
            return "YES" if answer else "NO"
        return str(answer).upper().strip()

    def is_correct(self, predicted: str, gold: str) -> bool:
        """Check if prediction matches gold answer"""
        pred_norm = self.normalize_answer(predicted)
        gold_norm = self.normalize_answer(gold)
        return pred_norm == gold_norm

    def calculate_ucr(self, answers: Dict[str, Any]) -> float:
        """
        Calculate Unknown-Correct Rate (UCR)
        Ratio of correctly handled UNKNOWN answers to all UNKNOWN questions
        """
        unknown_qids = [qid for qid, gold in self.gold_answers.items()
                       if gold == "UNKNOWN"]

        if not unknown_qids:
            return 0.0

        correct_unknowns = sum(
            1 for qid in unknown_qids
            if qid in answers and self.is_correct(answers[qid], "UNKNOWN")
        )

        return correct_unknowns / len(unknown_qids) if unknown_qids else 0.0

    def calculate_contradiction_rate(self, answers: Dict[str, Any]) -> float:
        """
        Calculate rate of contradictory answers
        Questions with contradictory relationships should not both be true
        """
        contradiction_pairs = [
            ("Q1-02", "Q1-03"),  # bob vs charlie managing team_alpha
            ("Q7-01", "Q7-03"),  # contradictory claims
            ("Q7-04", "Q7-05"),  # claim_c1 vs claim_c2
        ]

        violations = 0
        for q1, q2 in contradiction_pairs:
            if q1 in answers and q2 in answers:
                ans1 = self.normalize_answer(answers.get(q1))
                ans2 = self.normalize_answer(answers.get(q2))
                # Both should not be YES for contradictory questions
                if ans1 == "YES" and ans2 == "YES":
                    violations += 1

        return violations / len(contradiction_pairs) if contradiction_pairs else 0.0

    def evaluate_answer_set(self, answer_set: AnswerSet,
                           gold_answers: Dict[str, Any]) -> EvaluationResult:
        """Evaluate a complete answer set"""
        result = EvaluationResult(name=answer_set.name)
        result.cpu_ms = answer_set.cpu_time_ms
        result.e2e_ms = answer_set.e2e_time_ms
        result.context_tokens = answer_set.context_tokens

        answers = answer_set.answers

        # Calculate overall accuracy
        correct = 0
        total = 0
        category_correct = defaultdict(int)
        category_total = defaultdict(int)

        for qid, gold in gold_answers.items():
            total += 1
            predicted = answers.get(qid, "UNKNOWN")

            if self.is_correct(predicted, gold):
                correct += 1
                category = qid.split('-')[0]
                category_correct[category] += 1

            category = qid.split('-')[0]
            category_total[category] += 1

        result.total_correct = correct
        result.total_questions = total
        result.overall_accuracy = correct / total if total > 0 else 0.0

        # Calculate category-specific accuracies
        for category in ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']:
            cat_total = category_total.get(category, 0)
            if cat_total > 0:
                cat_acc = category_correct.get(category, 0) / cat_total
                setattr(result, f"{category.lower()}_accuracy", cat_acc)
                if category == 'Q4':
                    result.q4_correct = category_correct.get('Q4', 0)
                    result.q4_total = cat_total
                    result.q4_accuracy = cat_acc

        # Calculate special metrics
        result.ucr = self.calculate_ucr(answers)
        result.contradiction_rate = self.calculate_contradiction_rate(answers)

        return result

    def compare_results(self, result_d: EvaluationResult,
                       result_c1: EvaluationResult) -> Dict[str, Any]:
        """Compare Baseline (D) vs Construction (C1)"""
        comparison = {
            "overall_delta": result_c1.overall_accuracy - result_d.overall_accuracy,
            "q4_delta": result_c1.q4_accuracy - result_d.q4_accuracy,
            "ucr_delta": result_c1.ucr - result_d.ucr,
            "contradiction_delta": result_d.contradiction_rate - result_c1.contradiction_rate,
            "cpu_overhead": result_c1.cpu_ms - result_d.cpu_ms,
            "result_d": result_d,
            "result_c1": result_c1,
        }
        return comparison

    def generate_report(self, comparison: Dict[str, Any]) -> str:
        """Generate evaluation report"""
        report_lines = []
        report_lines.append("=" * 70)
        report_lines.append("STAGE 1 EVALUATION REPORT")
        report_lines.append("=" * 70)
        report_lines.append("")

        d = comparison['result_d']
        c1 = comparison['result_c1']

        report_lines.append("BASELINE (D) RESULTS")
        report_lines.append("-" * 70)
        report_lines.append(f"Overall Accuracy      : {d.overall_accuracy:.2%} ({d.total_correct}/{d.total_questions})")
        report_lines.append(f"Q4 Accuracy           : {d.q4_accuracy:.2%} ({d.q4_correct}/{d.q4_total})")
        report_lines.append(f"Q1 Accuracy           : {d.q1_accuracy:.2%}")
        report_lines.append(f"Q2 Accuracy           : {d.q2_accuracy:.2%}")
        report_lines.append(f"Q3 Accuracy           : {d.q3_accuracy:.2%}")
        report_lines.append(f"Q5 Accuracy           : {d.q5_accuracy:.2%}")
        report_lines.append(f"Q6 Accuracy (Unknown) : {d.q6_accuracy:.2%}")
        report_lines.append(f"Q7 Accuracy (Contr.)  : {d.q7_accuracy:.2%}")
        report_lines.append(f"Q8 Accuracy (Correct) : {d.q8_accuracy:.2%}")
        report_lines.append(f"Q9 Accuracy (Current) : {d.q9_accuracy:.2%}")
        report_lines.append(f"Q10 Accuracy (History): {d.q10_accuracy:.2%}")
        report_lines.append(f"UCR (Unknown Correct) : {d.ucr:.2%}")
        report_lines.append(f"Contradiction Rate    : {d.contradiction_rate:.2%}")
        report_lines.append(f"CPU Time              : {d.cpu_ms:.3f} ms")
        report_lines.append(f"E2E Time              : {d.e2e_ms if d.e2e_ms > 0 else 'N/A'}")
        report_lines.append(f"Context Tokens        : {d.context_tokens if d.context_tokens > 0 else 'N/A'}")
        report_lines.append("")

        report_lines.append("CONSTRUCTION (C1) RESULTS")
        report_lines.append("-" * 70)
        report_lines.append(f"Overall Accuracy      : {c1.overall_accuracy:.2%} ({c1.total_correct}/{c1.total_questions})")
        report_lines.append(f"Q4 Accuracy           : {c1.q4_accuracy:.2%} ({c1.q4_correct}/{c1.q4_total})")
        report_lines.append(f"Q1 Accuracy           : {c1.q1_accuracy:.2%}")
        report_lines.append(f"Q2 Accuracy           : {c1.q2_accuracy:.2%}")
        report_lines.append(f"Q3 Accuracy           : {c1.q3_accuracy:.2%}")
        report_lines.append(f"Q5 Accuracy           : {c1.q5_accuracy:.2%}")
        report_lines.append(f"Q6 Accuracy (Unknown) : {c1.q6_accuracy:.2%}")
        report_lines.append(f"Q7 Accuracy (Contr.)  : {c1.q7_accuracy:.2%}")
        report_lines.append(f"Q8 Accuracy (Correct) : {c1.q8_accuracy:.2%}")
        report_lines.append(f"Q9 Accuracy (Current) : {c1.q9_accuracy:.2%}")
        report_lines.append(f"Q10 Accuracy (History): {c1.q10_accuracy:.2%}")
        report_lines.append(f"UCR (Unknown Correct) : {c1.ucr:.2%}")
        report_lines.append(f"Contradiction Rate    : {c1.contradiction_rate:.2%}")
        report_lines.append(f"CPU Time              : {c1.cpu_ms:.3f} ms")
        report_lines.append(f"E2E Time              : {c1.e2e_ms if c1.e2e_ms > 0 else 'N/A'}")
        report_lines.append(f"Context Tokens        : {c1.context_tokens if c1.context_tokens > 0 else 'N/A'}")
        report_lines.append("")

        report_lines.append("C1 vs D COMPARISON")
        report_lines.append("-" * 70)
        overall_delta = comparison['overall_delta']
        q4_delta = comparison['q4_delta']
        ucr_delta = comparison['ucr_delta']
        contr_delta = comparison['contradiction_delta']

        delta_symbol_overall = "↑" if overall_delta >= 0 else "↓"
        delta_symbol_q4 = "↑" if q4_delta >= 0 else "↓"
        delta_symbol_ucr = "↑" if ucr_delta >= 0 else "↓"
        delta_symbol_contr = "↑" if contr_delta >= 0 else "↓"

        report_lines.append(f"Overall Accuracy Δ    : {delta_symbol_overall} {abs(overall_delta):+.2%}")
        report_lines.append(f"Q4 Accuracy Δ         : {delta_symbol_q4} {abs(q4_delta):+.2%}")
        report_lines.append(f"UCR Δ                 : {delta_symbol_ucr} {abs(ucr_delta):+.2%}")
        report_lines.append(f"Contradiction Δ       : {delta_symbol_contr} {abs(contr_delta):+.2%} (lower is better)")
        report_lines.append("")

        report_lines.append("INTERPRETATION")
        report_lines.append("-" * 70)
        if overall_delta > 0.05:
            report_lines.append("✓ Construction shows >5% overall improvement")
        elif overall_delta > 0:
            report_lines.append("△ Construction shows positive but small overall improvement")
        elif overall_delta == 0:
            report_lines.append("= No overall accuracy difference between C1 and D")
        else:
            report_lines.append("✗ Construction shows lower overall accuracy than baseline")

        if q4_delta > 0.10:
            report_lines.append("✓ Construction shows >10% Q4 improvement (strong signal)")
        elif q4_delta > 0.05:
            report_lines.append("△ Construction shows 5-10% Q4 improvement")
        elif q4_delta == 0:
            report_lines.append("= No Q4 accuracy difference")
        else:
            report_lines.append("✗ Construction shows lower Q4 accuracy")

        if ucr_delta > 0:
            report_lines.append("✓ Construction better handles UNKNOWN states")
        else:
            report_lines.append("= No improvement in UNKNOWN state handling")

        if contr_delta > 0:
            report_lines.append("✓ Construction better detects/avoids contradictions")

        report_lines.append("")
        report_lines.append("NOTES")
        report_lines.append("-" * 70)
        report_lines.append("CPU time is for local rule evaluation only, not API latency.")
        report_lines.append("This Stage 1 test measures Construction logic correctness,")
        report_lines.append("not token efficiency (Stage 0) or end-to-end latency (not measured).")
        report_lines.append("")
        report_lines.append("=" * 70)

        return "\n".join(report_lines)

if __name__ == "__main__":
    print("Stage 1 Evaluator loaded successfully")
