#!/usr/bin/env python3
"""
Stage 1 Test Runner
Validates schema and runs comparative evaluation
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from stage1_evaluator import Stage1Evaluator, AnswerSet
from baseline_representation import BaselineRepresentation
from construction_representation import ConstructionRepresentation

class Stage1TestRunner:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.events_path = self.root_dir / "events.json"
        self.questions_path = self.root_dir / "questions.json"
        self.gold_answers_path = self.root_dir / "gold_answers.json"

    def validate_schema(self) -> tuple[bool, list[str]]:
        """Validate that all requirements are met"""
        errors = []

        # Check files exist
        if not self.events_path.exists():
            errors.append(f"Missing: {self.events_path}")
        if not self.questions_path.exists():
            errors.append(f"Missing: {self.questions_path}")
        if not self.gold_answers_path.exists():
            errors.append(f"Missing: {self.gold_answers_path}")

        if errors:
            return False, errors

        try:
            # Load and validate events
            with open(self.events_path, 'r', encoding='utf-8') as f:
                events_data = json.load(f)
                events = events_data.get('events', [])

            if len(events) != 75:
                errors.append(f"Events: expected 75, got {len(events)}")

            # Validate event structure
            required_event_fields = ['event_id', 'event_type', 'subject', 'relation',
                                     'object', 'valid_from', 'valid_to',
                                     'establishment_state', 'condition_ref']
            for i, evt in enumerate(events):
                for field in required_event_fields:
                    if field not in evt:
                        errors.append(f"Event[{i}] ({evt.get('event_id')}): missing field '{field}'")
                        break

            # Load and validate questions
            with open(self.questions_path, 'r', encoding='utf-8') as f:
                questions_data = json.load(f)
                questions = questions_data.get('questions', [])

            if len(questions) != 96:
                errors.append(f"Questions: expected 96, got {len(questions)}")

            # Validate question structure
            required_question_fields = ['question_id', 'category', 'question',
                                       'current_time', 'relevant_event_ids',
                                       'gold_answer']
            for i, q in enumerate(questions):
                for field in required_question_fields:
                    if field not in q:
                        errors.append(f"Question[{i}] ({q.get('question_id')}): missing field '{field}'")
                        break

            # Validate question categories and counts
            category_counts = defaultdict(int)
            for q in questions:
                cat = q.get('category', 'UNKNOWN')
                category_counts[cat] += 1

            expected_counts = {
                'Q1': 10, 'Q2': 10, 'Q3': 12, 'Q4': 16, 'Q5': 12,
                'Q6': 8, 'Q7': 8, 'Q8': 8, 'Q9': 8, 'Q10': 4
            }

            for category, expected in expected_counts.items():
                actual = category_counts.get(category, 0)
                if actual != expected:
                    errors.append(f"Category {category}: expected {expected}, got {actual}")

            # Validate gold_answers
            with open(self.gold_answers_path, 'r', encoding='utf-8') as f:
                answers_data = json.load(f)
                answers = answers_data.get('answers', {})

            if len(answers) != 96:
                errors.append(f"Gold answers: expected 96, got {len(answers)}")

            # Check all questions have answers
            for q in questions:
                qid = q['question_id']
                if qid not in answers:
                    errors.append(f"Missing gold answer for {qid}")

            # Validate that C1 and D use same data
            # (This is implicit if we load from same files)

        except Exception as e:
            errors.append(f"Validation exception: {str(e)}")

        return len(errors) == 0, errors

    def run_test(self) -> dict:
        """Run full test pipeline"""
        results = {
            'validation': None,
            'baseline_answers': None,
            'construction_answers': None,
            'evaluation': None,
        }

        print("=" * 70)
        print("STAGE 1 TEST RUNNER")
        print("=" * 70)
        print()

        # Step 1: Validate schema
        print("STEP 1: Schema Validation")
        print("-" * 70)
        is_valid, errors = self.validate_schema()

        if is_valid:
            print("✓ Schema validation PASSED")
        else:
            print("✗ Schema validation FAILED")
            for error in errors:
                print(f"  - {error}")
            return results

        print()
        print("STEP 2: Loading Data")
        print("-" * 70)

        try:
            with open(self.events_path, 'r') as f:
                events_data = json.load(f)
            with open(self.questions_path, 'r') as f:
                questions_data = json.load(f)
            with open(self.gold_answers_path, 'r') as f:
                answers_data = json.load(f)

            print(f"✓ Loaded {len(events_data['events'])} events")
            print(f"✓ Loaded {len(questions_data['questions'])} questions")
            print(f"✓ Loaded {len(answers_data['answers'])} gold answers")
        except Exception as e:
            print(f"✗ Failed to load data: {e}")
            return results

        print()
        print("STEP 3: Running Baseline (D) Representation")
        print("-" * 70)

        try:
            baseline = BaselineRepresentation(str(self.events_path))
            baseline_answers, baseline_cpu = baseline.process_questions(str(self.questions_path))
            baseline_set = AnswerSet(
                name="Baseline (D)",
                answers=baseline_answers,
                cpu_time_ms=baseline_cpu
            )
            print(f"✓ Baseline processed {len(baseline_answers)} answers")
            print(f"  CPU time: {baseline_cpu:.3f} ms")
            results['baseline_answers'] = baseline_set
        except Exception as e:
            print(f"✗ Baseline failed: {e}")
            import traceback
            traceback.print_exc()
            return results

        print()
        print("STEP 4: Running Construction (C1) Representation")
        print("-" * 70)

        try:
            construction = ConstructionRepresentation(str(self.events_path))
            construction_answers, construction_cpu = construction.process_questions(str(self.questions_path))
            construction_set = AnswerSet(
                name="Construction (C1)",
                answers=construction_answers,
                cpu_time_ms=construction_cpu
            )
            print(f"✓ Construction processed {len(construction_answers)} answers")
            print(f"  CPU time: {construction_cpu:.3f} ms")
            results['construction_answers'] = construction_set
        except Exception as e:
            print(f"✗ Construction failed: {e}")
            import traceback
            traceback.print_exc()
            return results

        print()
        print("STEP 5: Evaluation")
        print("-" * 70)

        try:
            evaluator = Stage1Evaluator(str(self.gold_answers_path))

            result_d = evaluator.evaluate_answer_set(baseline_set, answers_data['answers'])
            result_c1 = evaluator.evaluate_answer_set(construction_set, answers_data['answers'])

            comparison = evaluator.compare_results(result_d, result_c1)

            report = evaluator.generate_report(comparison)
            print(report)

            results['evaluation'] = {
                'baseline': result_d,
                'construction': result_c1,
                'comparison': comparison,
                'report': report
            }

        except Exception as e:
            print(f"✗ Evaluation failed: {e}")
            import traceback
            traceback.print_exc()
            return results

        return results

    def save_results(self, results: dict, output_path: str = "stage1_results.json"):
        """Save test results"""
        def serialize(obj):
            if hasattr(obj, '__dict__'):
                return obj.__dict__
            raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, default=serialize)

        print(f"Results saved to {output_path}")

if __name__ == "__main__":
    runner = Stage1TestRunner()
    results = runner.run_test()

    # Save results
    if results.get('evaluation'):
        runner.save_results(results, "stage1_results.json")

    print()
    print("=" * 70)
    print("Test run complete")
    print("=" * 70)
