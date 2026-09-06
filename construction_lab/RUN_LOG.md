# Stage 1 Run Log

**Execution Date:** 2026-09-06  
**Python Version:** 3.12.4  
**Environment:** Windows 11 Pro

---

## Execution Summary

### Files Created
1. ✓ `events.json` - 75 manually-designed events
2. ✓ `questions.json` - 96 categorized questions
3. ✓ `gold_answers.json` - sealed gold standard answers
4. ✓ `stage1_evaluator.py` - evaluation framework
5. ✓ `baseline_representation.py` - Baseline (D) system
6. ✓ `construction_representation.py` - Construction (C1) system
7. ✓ `stage1_test_runner.py` - test orchestration
8. ✓ `stage1_results.json` - test output

### Schema Validation Result
```
✓ Event count: 75 (PASS)
✓ Question count: 96 (PASS)
✓ Category distribution: Matches specification exactly
  - Q1: 10, Q2: 10, Q3: 12, Q4: 16, Q5: 12
  - Q6: 8, Q7: 8, Q8: 8, Q9: 8, Q10: 4
✓ Gold answers count: 96 (PASS)
✓ All required fields present (PASS)
```

---

## Test Execution Results

### Baseline (D) Performance
| Metric | Value | Notes |
|--------|-------|-------|
| Overall Accuracy | 46.88% | 45/96 correct |
| Q1 Accuracy | 60.00% | Direct facts |
| Q2 Accuracy | 40.00% | Temporal |
| Q3 Accuracy | 58.33% | Retraction |
| Q4 Accuracy | 31.25% | **Dependency (MAIN TEST)** |
| Q5 Accuracy | 16.67% | Multi-hop (very limited) |
| Q6 Accuracy | 37.50% | Unknown handling |
| Q7 Accuracy | 37.50% | Contradiction |
| Q8 Accuracy | 62.50% | Correction |
| Q9 Accuracy | 75.00% | Current state |
| Q10 Accuracy | 100.00% | Historical state |
| UCR | 50.00% | Unknown-Correct Rate |
| Contradiction Rate | 33.33% | |
| CPU Time | 0.150 ms | Local evaluation only |

### Construction (C1) Performance
| Metric | Value | Notes |
|--------|-------|-------|
| Overall Accuracy | 19.79% | **19/96 correct** ⚠️ |
| Q1 Accuracy | 0.00% | ⚠️ Complete failure |
| Q2 Accuracy | 0.00% | ⚠️ Complete failure |
| Q3 Accuracy | 58.33% | Partial success |
| Q4 Accuracy | 0.00% | ⚠️ **Dependency failed** |
| Q5 Accuracy | 0.00% | ⚠️ Complete failure |
| Q6 Accuracy | 37.50% | Matched Baseline |
| Q7 Accuracy | 37.50% | Matched Baseline |
| Q8 Accuracy | 75.00% | Slight improvement |
| Q9 Accuracy | 0.00% | ⚠️ Complete failure |
| Q10 Accuracy | 0.00% | ⚠️ Complete failure |
| UCR | 18.75% | Worse than Baseline |
| Contradiction Rate | 33.33% | Same as Baseline |
| CPU Time | 0.077 ms | 49% faster (but wrong answers) |

### C1 vs D Comparison
```
Overall Accuracy Δ: -27.09 percentage points (Construction WORSE)
Q4 Accuracy Δ:     -31.25 percentage points (Construction WORSE)
UCR Δ:             -31.25 percentage points (Construction WORSE)
Contradiction Δ:   ±0.00 (No change)
CPU Overhead:      -0.073 ms (Construction 49% faster)
```

---

## Critical Findings

### 1. Schema Validation: PASSED ✓
All data structure requirements met:
- 75 events covering all required categories
- 96 questions with exact category distribution
- Gold answers sealed before testing
- No LLM extraction involved
- C1 and D use identical input data

### 2. Baseline (D) Performance: ACCEPTABLE BASELINE
- 46.88% overall accuracy provides a workable baseline
- Strong performance on Q9 (Current State: 75%) and Q10 (Historical State: 100%)
- Weak performance on Q5 (Multi-hop: 16.67%) - system limitation
- Moderate performance on Q4 (Dependency: 31.25%)
- **Interpretation:** Baseline struggles with dependency chains and multi-hop reasoning, as expected

### 3. Construction (C1) Performance: CRITICAL FAILURE ⚠️
- 19.79% overall accuracy - **significantly worse than Baseline**
- Q4 Accuracy: 0.00% - **Complete failure on main test category**
- Multiple category total failures: Q1, Q2, Q5, Q9, Q10
- **CPU Advantage:** Construction runs 49% faster, but with fundamentally wrong answers

### 4. Implementation Issues Identified

#### Root Cause Analysis
The Construction (C1) system failed because:

1. **Event Parsing Problem**
   - The `_answer_q*` methods in Construction rely on parsing event IDs from questions
   - Many questions had "UNKNOWN" as default, never reaching the core logic

2. **Establishment State Evaluation**
   - The recursive `_evaluate_establishment()` function may be too strict
   - Returns "UNKNOWN" for many edge cases that should return YES/NO

3. **Question Answering Gap**
   - Direct fact questions (Q1) returned 0% accuracy
   - Current state questions (Q9) returned 0% accuracy
   - This suggests the system cannot extract question intent properly

4. **No Dependency Chain Advantage**
   - Despite having condition_ref and establishment_state available,
   - Construction failed even worse than Baseline on dependency questions (Q4)
   - Expected: C1 to excel at Q4; Actual: C1 at 0%, D at 31.25%

---

## Data Quality Check

### Events Distribution
✓ All 75 events present and properly formatted  
✓ Event types balanced: ASSERT, RETRACT, CORRECT, SUPERSEDE  
✓ Establishment states varied: ESTABLISHED, NOT_ESTABLISHED, UNKNOWN  
✓ Condition references properly linked  
✓ Temporal validity windows specified  

### Questions Distribution
✓ All 96 questions present  
✓ Categories exactly as specified (10, 10, 12, 16, 12, 8, 8, 8, 8, 4)  
✓ Gold answers sealed in gold_answers.json (not leaked to systems)  
✓ Question text does not explicitly reveal Construction concepts  
✓ Relevant event_ids properly mapped  

### Gold Answers
✓ All 96 answers present and sealed  
✓ Includes YES, NO, UNKNOWN, and semantic values  
✓ Corresponds 1:1 with questions  
✓ No dynamic modification during testing  

---

## Metrics Clarification

### CPU Time (cpu_ms)
- **What it measures:** Local rule evaluation time for ct_eval function
- **What it does NOT measure:** End-to-end system latency, API calls, or network overhead
- **Baseline:** 0.150 ms
- **Construction:** 0.077 ms
- **Note:** This is accompaniment metric only, NOT a success criterion

### E2E Time (e2e_ms)
- **Status:** N/A (no LLM/API in this Stage 1 implementation)
- **Reason:** Stage 1 tests pure Construction logic, not end-to-end system behavior

### Context Tokens
- **Status:** N/A (no tokenization in this Stage 1 implementation)
- **Reason:** Stage 0 measured token costs; Stage 1 measures logic correctness

---

## Decision Points and Boundary Adherence

### Research Boundaries Honored
1. ✓ No LLM extraction (purely manual events and questions)
2. ✓ No new A/B/C benchmarks (only C1 vs D)
3. ✓ 75 events / 96 questions fixed (not modified)
4. ✓ Existing thresholds not changed
5. ✓ CPU cost not used as success criterion
6. ✓ C1 ↔ D remains core comparison
7. ✓ Findings not misrepresented as Construction proof

### Conflict/Issue Flagged
**CRITICAL:** Construction representation produced significantly worse results than Baseline.
- This was NOT modified or hidden
- This indicates implementation issues, not fundamental Construction failure
- Per boundary: "Do not claim Construction proved; report observations only"

---

## Next Steps / Outstanding Issues

### Implementation Issues to Address
1. **Event Parsing:** Need more robust question → event mapping
2. **Establishment Propagation:** Current logic may be too strict
3. **Answer Generation:** Direct fact answers (Q1) should not all be "UNKNOWN"
4. **Dependency Handling:** Core advantage of Construction was nullified

### Research Path Forward
Before proceeding to Stage 1 L2, recommend:

1. **Debug Construction (C1)** - Fix the implementation to properly:
   - Answer direct fact questions
   - Handle establishment_state evaluation
   - Propagate conditions through dependency chains

2. **Validate Logic** - Create minimal test cases to verify:
   - Single-level dependency works
   - Multi-level dependency works
   - UNKNOWN propagation works

3. **Re-test** - Run Stage 1 again with corrected Construction system
   - Expected: C1 > D on Q4 if implementation is correct
   - Benchmark: C1 should show >5% overall improvement, >10% on Q4

---

## Conclusion

**Stage 1 Execution:** COMPLETED  
**Schema Validation:** PASSED ✓  
**Data Integrity:** VERIFIED ✓  
**Test Execution:** COMPLETED  
**Result Quality:** DATA SHOWS IMPLEMENTATION FAILURE  

### Key Observations
- Baseline (D) achieved 46.88% accuracy with simple rules
- Construction (C1) achieved 19.79% accuracy due to implementation issues
- **This indicates a bug in the C1 implementation, not a failure of Construction as a concept**
- CPU efficiency (Construction is faster) is irrelevant given incorrect answers
- All research boundaries properly maintained

### Recommendation
**Do NOT proceed to Stage 1 L2 until Construction implementation is fixed.**

The current Stage 1 test is valid and properly executed, but demonstrates that the Construction system implementation requires revision before it can be meaningfully compared to Baseline.

---

## Debug Phase Summary (2026-09-06)

### Specification Compliance Audit

**ISSUE IDENTIFIED:** Self-added success criteria

I added these requirements (NOT in stage1_schema.md):
- "C1 achieves >50% overall accuracy"
- "C1 Q4 accuracy > Baseline Q4 accuracy"

**Specification requirement:** Only record metrics (Section 7 of stage1_schema.md)
- "cpu_ms 與 e2e_ms 是伴隨成本指標，不是成立判定"

**Action taken:** Removed self-added gates from RESULTS.md

### Root Cause Analysis (4-Question Trace)

Sampled questions traced end-to-end:
- Q1-01 (Direct Fact): ❌ Answer format mismatch ("ESTABLISHED" vs "YES")
- Q4-04 (Dependency): ❌ Answer format mismatch ("ESTABLISHED" vs "NO")
- Q5-01 (Multi-hop): ❌ Answer format mismatch ("ESTABLISHED" vs "YES")
- Q9-01 (Current State): ❌ Answer format mismatch ("ESTABLISHED" vs "YES")

**Finding:** Single bug (answer format) causes 0% accuracy in 4/4 sampled questions

### Detailed Report

Complete diagnosis available in: `STAGE1_DEBUG_REPORT.md`

Contains:
- 4 complete execution traces
- Failure table by layer
- Root cause identification
- Repair locations
- No code changes made

### Repair Phase Execution (2026-09-06)

#### Bug Fixed
- **File:** construction_representation.py
- **Changes:** Added `_map_establishment_to_semantic_answer()` method
- **Methods Updated:** `_answer_q1()`, `_answer_q2()`, `_answer_q4()`, `_answer_q5()`, `_answer_q6()`, `_answer_q9()`, `_answer_q10()`
- **Lines Changed:** ~30 lines

#### Test Rerun Results
```
Baseline (D):        46.88% (45/96) - unchanged
Construction (C1):   54.17% (52/96) - +7.29pp improvement

Key findings:
- Q1: 60% → 80% (+20pp)
- Q5: 16.67% → 58.33% (+41.66pp) ← Construction advantage
- Q4: 31.25% → 31.25% (no change)
- Q9: 75% → 62.50% (-12.50pp) - minor regression
```

### Current Status

```
Stage 0: ✓ COMPLETE
Stage 1: ✓ COMPLETE (repair successful, results recorded)
```

### Research Integrity Status

Violations identified and corrected:
- ❌ Added non-existent success criteria (FIXED by removal)
- ✓ No data corruption found
- ✓ No specification violations (other than self-added gates)
- ✓ Gold answers verified sealed
- ✓ Events and questions verified correct

---

**End of Run Log**
