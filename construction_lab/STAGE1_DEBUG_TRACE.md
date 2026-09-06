# Stage 1 Debug Trace

**Purpose:** Locate first failure point in C1 for selected questions  
**Date:** 2026-09-06  
**Status:** Diagnostic only - NO CODE CHANGES

---

## Specification Compliance Check

**ISSUE FOUND:** Self-added success criteria

Criteria I added (INVALID):
- "C1 achieves >50% overall accuracy"
- "C1 Q4 accuracy > Baseline Q4 accuracy"

**Actual specification requirement:** Record metrics only (Section 7 of stage1_schema.md)
- "cpu_ms 與 e2e_ms 是伴隨成本指標，不是成立判定" 
- No success criterion defined

**ACTION NEEDED:** Remove self-added gates from RESULTS.md

---

## Selected Questions for Trace

### Q1-01: Direct Fact (Q1 Category)
```json
{
  "question_id": "Q1-01",
  "category": "Q1",
  "question": "Does alice work for company_acme at current time?",
  "current_time": "2024-09-15",
  "relevant_event_ids": ["E001"],
  "gold_answer": "YES"
}
```

### Q4-04: Dependency/Premise Failure (Q4 Category)
```json
{
  "question_id": "Q4-04",
  "category": "Q4",
  "question": "When service_auth is retracted from database_db1, does platform_edge dependency fail?",
  "current_time": "2024-09-15",
  "relevant_event_ids": ["E010", "E011", "E012", "E013"],
  "gold_answer": "NO"
}
```

### Q5-01: Multi-hop (Q5 Category)
```json
{
  "question_id": "Q5-01",
  "category": "Q5",
  "question": "Is endpoint_api established at 2024-09-15 given the full dependency chain?",
  "current_time": "2024-09-15",
  "relevant_event_ids": ["E010", "E013", "E014"],
  "gold_answer": "YES"
}
```

### Q9-01: Current State (Q9 Category)
```json
{
  "question_id": "Q9-01",
  "category": "Q9",
  "question": "At current time (2024-09-15), is alice working for company_beta?",
  "current_time": "2024-09-15",
  "relevant_event_ids": ["E009"],
  "gold_answer": "YES"
}
```

---

## TRACE 1: Q1-01 Direct Fact

### Step 1: Event Input Check
```
Event E001:
  event_id: E001
  event_type: ASSERT
  subject: alice
  relation: works_for
  object: company_acme
  valid_from: 2024-01-15
  valid_to: null
  establishment_state: ESTABLISHED
  condition_ref: null
  category: direct_fact
```
✓ Event loaded correctly

### Step 2: C1 Representation in memory
```
ct_store['E001'] = ConstructionEvent(
  event_id='E001',
  subject='alice',
  relation='works_for',
  object='company_acme',
  valid_from='2024-01-15',
  valid_to=None,
  event_type='ASSERT',
  establishment_state='ESTABLISHED',
  condition_ref=None
)
```
✓ Representation created

### Step 3: Question Processing in C1
```
_answer_q1(Q1-01, "2024-09-15"):
  event_ids = ["E001"]
  evt = ct_store.get("E001")
  # evt is found and is ConstructionEvent object
  return _get_fact_state_at_time("alice", "works_for", "company_acme", "2024-09-15")
```

### Step 4: _get_fact_state_at_time() Execution
```
key = ("alice", "works_for", "company_acme")
if key not in current_facts:
  return "UNKNOWN"

# current_facts was built in _build_construction_store()
# Let's check if this key exists...
```

**POTENTIAL ISSUE #1:** Does `current_facts` get indexed properly?

Checking `_build_construction_store()`:
```python
key = (evt['subject'], evt['relation'], evt['object'])
if key not in self.current_facts:
  self.current_facts[key] = []
self.current_facts[key].append(evt['event_id'])
```

For E001: key = ("alice", "works_for", "company_acme") ✓ should be indexed

### Step 5: Event Lookup in fact storage
```
key = ("alice", "works_for", "company_acme")
# current_facts[key] = ["E001"]
for event_id in ["E001"]:
  event = ct_store["E001"]  # ConstructionEvent object
  
  # Check event_type
  if event.event_type == 'RETRACT':  # NO
    ...
  if event.event_type in ('ASSERT', 'CORRECT'):  # YES
    if _is_valid_at_time(event, "2024-09-15"):  # Check 2024-01-15 <= 2024-09-15 <= null
      # YES, valid
      latest_assert = event
      latest_assert_state = _evaluate_establishment("E001", "2024-09-15")
```

### Step 6: _evaluate_establishment() for E001
```
event_id = "E001"
visiting = set()
event = ct_store["E001"]
visiting.add("E001")

# Check temporal
_is_valid_at_time(event, "2024-09-15"):
  event.valid_from = "2024-01-15"
  event.valid_to = None
  timestamp = "2024-09-15"
  if "2024-09-15" < "2024-01-15": # NO
    return False
  if None and "2024-09-15" > None: # NO (None is falsy)
    return False
  return True
  ✓ Valid at time

# Check retraction
if event.event_type == 'RETRACT': # NO
  
# Check condition
if not event.condition_ref: # condition_ref is None, so TRUE
  return event.establishment_state  # Returns "ESTABLISHED"

return "ESTABLISHED"
```

### Step 7: Back to _get_fact_state_at_time()
```
latest_assert_state = "ESTABLISHED"
return latest_assert_state  # "ESTABLISHED"
```

### Step 8: Answer returned
```
_answer_q1(Q1-01) returns "ESTABLISHED"
```

### Step 9: Evaluator Check
```
predicted = "ESTABLISHED"
gold = "YES"
normalizer: "ESTABLISHED" → "ESTABLISHED" (no normalization)
is_correct("ESTABLISHED", "YES"): "ESTABLISHED" != "YES" → FALSE
```

🔴 **FIRST ERROR FOUND:** String mismatch in answer normalization

### Step 10: Root Cause
Gold answer is "YES" (boolean string)
C1 returns "ESTABLISHED" (state string)
Evaluator compares: "ESTABLISHED" != "YES" → Wrong

**FAILURE POINT:** Answer format mismatch between C1 output and gold answer format

---

## TRACE 2: Q4-04 Dependency (Service Auth Retraction)

### Step 1: Events for Q4-04
```
E010: database_db1 depends_on service_auth (condition_ref: null, establishment_state: ESTABLISHED)
E011: service_auth RETRACT (establishment_state: NOT_ESTABLISHED)
E012: service_oauth provides database_db1 (establishment_state: ESTABLISHED)
E013: platform_edge depends_on database_db1 (condition_ref: E010, establishment_state: ESTABLISHED)
```

### Step 2: Question Intent
"When service_auth is retracted from database_db1, does platform_edge dependency fail?"
Gold answer: "NO" (Platform edge should NOT fail because database_db1 can use service_oauth instead)

### Step 3: C1 Processing Q4-04
```
_answer_q4(Q4-04, "2024-09-15"):
  event_ids = ["E010", "E011", "E012", "E013"]
  primary_event = ct_store.get("E010")
  return _evaluate_establishment("E010", "2024-09-15")
```

### Step 4: _evaluate_establishment("E010", "2024-09-15")
```
event = ct_store["E010"]  # database_db1 depends_on service_auth
# Event type: ASSERT
# Has condition_ref? NO (condition_ref is None)
# So return establishment_state: "ESTABLISHED"

return "ESTABLISHED"
```

### Step 5: Back to _answer_q4
```
returns "ESTABLISHED"
```

### Step 6: Evaluator
```
predicted = "ESTABLISHED"
gold = "NO"
is_correct("ESTABLISHED", "NO"): "ESTABLISHED" != "NO" → FALSE
```

**ISSUE:** C1 returns fact state, not answer to "does dependency fail?"

The question asks "does platform_edge dependency **fail**?"
- Gold answer: "NO" (it does not fail)
- C1 answer: "ESTABLISHED" (the fact is established)

**FUNDAMENTAL PROBLEM:** 
1. C1 doesn't understand question semantics ("fail" = NOT_ESTABLISHED or UNKNOWN)
2. C1 doesn't evaluate E013 (platform_edge) - only checked E010
3. Answer format mismatch again: "ESTABLISHED" vs "NO"

**FAILURE POINT:** Multiple issues
- Question interpretation (semantic mismatch)
- Event selection (checked wrong event)
- Answer format (ESTABLISHED vs YES/NO)

---

## TRACE 3: Q5-01 Multi-hop

### Step 1: Events
```
E010: database_db1 depends_on service_auth (condition_ref: null)
E013: platform_edge depends_on database_db1 (condition_ref: E010)
E014: endpoint_api depends_on platform_edge (condition_ref: E013)
```

### Step 2: Question
"Is endpoint_api established at 2024-09-15 given the full dependency chain?"
Gold answer: "YES"

### Step 3: C1 Processing
```
_answer_q5(Q5-01):
  event_ids = ["E010", "E013", "E014"]
  return _check_multi_hop_dependency(["E010", "E013", "E014"], "2024-09-15")
```

### Step 4: _check_multi_hop_dependency()
```
for event_id in ["E010", "E013", "E014"]:
  event = ct_store.get(event_id)
  state = _evaluate_establishment(event_id, "2024-09-15")
  
  # For E010:
  event.condition_ref = None
  return "ESTABLISHED"
  
  # For E013:
  event.condition_ref = "E010"
  visiting.add("E013")
  premise_state = _evaluate_establishment("E010", ...)  # ESTABLISHED
  visiting.remove("E013")
  return "ESTABLISHED"
  
  # For E014:
  event.condition_ref = "E013"
  visiting.add("E014")
  premise_state = _evaluate_establishment("E013", ...)  # ESTABLISHED
  visiting.remove("E014")
  return "ESTABLISHED"
  
  # All returned "ESTABLISHED"
return "ESTABLISHED"
```

### Step 5: Evaluator
```
predicted = "ESTABLISHED"
gold = "YES"
is_correct("ESTABLISHED", "YES"): "ESTABLISHED" != "YES" → FALSE
```

**FAILURE POINT:** Answer format mismatch (ESTABLISHED vs YES)

---

## TRACE 4: Q9-01 Current State

### Step 1: Event
```
E009: alice CORRECT company_beta (valid_from: 2024-07-01, valid_to: null)
      establishment_state: ESTABLISHED, condition_ref: null
```

### Step 2: Question
"At current time (2024-09-15), is alice working for company_beta?"
Gold answer: "YES"

### Step 3: C1 Processing
```
_answer_q9(Q9-01):
  event_ids = ["E009"]
  evt = ct_store.get("E009")
  result = _get_fact_state_at_time("alice", "works_for", "company_beta", "2024-09-15")
```

### Step 4: _get_fact_state_at_time()
```
key = ("alice", "works_for", "company_beta")
# current_facts was indexed during init
# Does this key exist?

# During _build_construction_store():
# E009 has subject="alice", relation="works_for", object="company_beta"
# key = ("alice", "works_for", "company_beta") 
# current_facts[key].append("E009")

# Yes, it exists

for event_id in current_facts[key]:  # ["E009"]
  event = ct_store["E009"]
  if event.event_type == 'RETRACT': # NO
  if event.event_type in ('ASSERT', 'CORRECT'): # YES (CORRECT)
    if _is_valid_at_time(event, "2024-09-15"): # 2024-07-01 <= 2024-09-15 <= null? YES
      latest_assert = event
      latest_assert_state = _evaluate_establishment("E009", "2024-09-15")
      # E009.condition_ref = None, return "ESTABLISHED"
      latest_assert_state = "ESTABLISHED"

return "ESTABLISHED"
```

### Step 5: Evaluator
```
predicted = "ESTABLISHED"
gold = "YES"
is_correct("ESTABLISHED", "YES"): FALSE
```

**FAILURE POINT:** Answer format mismatch (ESTABLISHED vs YES)

---

## Failure Table

| Question | Category | Event ID | Event Loaded | Representation Built | Establishment Evaluated | Condition Propagation | Query Resolved | Answer Format | Gold Match | First Error |
|----------|----------|----------|--------------|----------------------|------------------------|-----------------------|----------------|---------------|-----------|------------|
| Q1-01 | Q1 | E001 | ✓ | ✓ | ✓ ("ESTABLISHED") | ✓ (none) | ✓ | ❌ "ESTABLISHED" vs "YES" | FAIL | Answer Format |
| Q4-04 | Q4 | E010 | ✓ | ✓ | ✓ ("ESTABLISHED") | ✓ (none) | ⚠️ Wrong event | ❌ "ESTABLISHED" vs "NO" | FAIL | Answer Format + Semantic |
| Q5-01 | Q5 | E010,E013,E014 | ✓ | ✓ | ✓ ("ESTABLISHED") | ✓ (chains) | ✓ | ❌ "ESTABLISHED" vs "YES" | FAIL | Answer Format |
| Q9-01 | Q9 | E009 | ✓ | ✓ | ✓ ("ESTABLISHED") | ✓ (none) | ✓ | ❌ "ESTABLISHED" vs "YES" | FAIL | Answer Format |

---

## Root Cause Analysis

### Primary Failure: Answer Format Mismatch

**The core issue across ALL selected questions:**

C1 returns establishment state values: `"ESTABLISHED"`, `"NOT_ESTABLISHED"`, `"UNKNOWN"`
Gold answers and evaluation expect: `"YES"`, `"NO"`, `"UNKNOWN"`, or semantic values

**Mapping Gap:**
- C1: establishment_state enum → direct output
- Expected: semantic answer to question → YES/NO/UNKNOWN

### Answer Normalization Bug

In `stage1_evaluator.py`, `normalize_answer()`:
```python
def normalize_answer(self, answer: Any) -> str:
    if answer is None:
        return "UNKNOWN"
    if isinstance(answer, bool):
        return "YES" if answer else "NO"
    return str(answer).upper().strip()
```

**Problem:**
- Input: "ESTABLISHED" → normalized to "ESTABLISHED" (no conversion)
- Expected: "YES"
- Comparison: "ESTABLISHED" != "YES" → FAIL

### Secondary Issue: Answer Interpretation

Questions ask semantic queries:
- "Does X work for Y?" → Expected: YES/NO
- "Does X fail?" → Expected: YES/NO
- "Is X established?" → Expected: YES/NO/UNKNOWN

But C1 directly returns establishment state enum without translating to question semantics.

---

## Root Cause Summary

**PRIMARY:** Answer format mismatch in C1 output
- C1 outputs: establishment_state enum values
- Evaluator expects: semantic YES/NO/UNKNOWN/special values
- Gap between system output format and expected gold answer format

**SECONDARY:** Semantic mapping missing
- C1 doesn't interpret question intent
- No translation from establishment_state to answer semantics
- Multiple Q4/Q5/Q9 methods return raw state instead of answering the question

**NOT A DATA BUG:** events.json, questions.json, gold_answers.json are correct
**NOT A SPECIFICATION BUG:** stage1_schema.md is clear
**IS AN IMPLEMENTATION BUG:** construction_representation.py and answer formatting logic

---

## Gold Answer Integrity Check

✓ `gold_answers.json` is sealed and does NOT contain:
- Any reference to C1 or D outputs
- Any dynamic computation
- Any system-generated answers

✓ Gold answers directly match question_id entries in questions.json
✓ No leakage from evaluator or test systems

---

## Files Prohibited from Modification

Per research boundaries:
- `events.json` - ✗ Don't modify
- `questions.json` - ✗ Don't modify
- `gold_answers.json` - ✗ Don't modify
- `stage1_schema.md` - ✗ Don't modify
- `stage1_question_matrix.md` - ✗ Don't modify
- All scoring rules - ✗ Don't modify

---

## Files Requiring Correction

1. **RESULTS.md**
   - Remove self-added success criteria
   - Restore specification-only interpretation
   - Record only: Overall Accuracy, Q4 Accuracy, UCR, Contradiction Rate, CPU ms

2. **RUN_LOG.md**
   - Add note: "Self-added gates were not in specification"
   - Clarify: Results show implementation bug, not research failure

---

## Repair Locations (Not to be executed now)

1. **construction_representation.py**
   - Modify all `_answer_q*` methods to return semantic YES/NO/UNKNOWN
   - OR add answer mapping layer before return

2. **stage1_evaluator.py**
   - Add proper normalization for establishment_state → YES/NO
   - OR add mapping in answer collection

**MUST NOT FIX UNTIL DEBUG REPORT APPROVED**

---

## Next Steps After Debug Approval

1. Fix answer format mapping
2. Verify Q1 returns YES/NO
3. Verify Q4 interprets question semantics
4. Verify Q5 traverses chain correctly
5. Verify Q9 returns appropriate answer
6. Re-run complete Stage 1 test
7. Compare new C1 vs D results
8. Report findings without misrepresentation

---

**END OF DEBUG TRACE**

Status: DIAGNOSTIC COMPLETE - AWAITING REVIEW
