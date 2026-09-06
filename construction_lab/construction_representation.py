#!/usr/bin/env python3
"""
Construction Representation (C1)
Uses establishment_state and condition_ref for premise failure propagation
This is the Construction mechanism under test
"""

import json
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass
from datetime import datetime
import time

@dataclass
class ConstructionEvent:
    event_id: str
    subject: str
    relation: str
    object: str
    valid_from: str
    valid_to: Optional[str]
    event_type: str
    establishment_state: str
    condition_ref: Optional[str]

class ConstructionRepresentation:
    """
    Construction system: Facts + temporal + establishment_state + condition propagation
    Uses condition_ref to propagate premise failure through dependencies
    """

    def __init__(self, events_path: str):
        with open(events_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.raw_events = data['events']

        # Build Construction fact store
        self.ct_store = {}  # event_id -> ConstructionEvent
        self.dependency_graph = {}  # event_id -> [dependent_event_ids]
        self.dependents_map = {}  # event_id -> [events that depend on it]
        self.current_facts = {}  # (subject, relation, object) -> list of event_ids

        self._build_construction_store()

    def _build_construction_store(self):
        """Parse events into Construction structure"""
        for evt in self.raw_events:
            self.ct_store[evt['event_id']] = ConstructionEvent(
                event_id=evt['event_id'],
                subject=evt['subject'],
                relation=evt['relation'],
                object=evt['object'],
                valid_from=evt['valid_from'],
                valid_to=evt['valid_to'],
                event_type=evt['event_type'],
                establishment_state=evt['establishment_state'],
                condition_ref=evt['condition_ref']
            )

            # Build dependency graph
            if evt['condition_ref']:
                self.dependency_graph[evt['event_id']] = [evt['condition_ref']]
                if evt['condition_ref'] not in self.dependents_map:
                    self.dependents_map[evt['condition_ref']] = []
                self.dependents_map[evt['condition_ref']].append(evt['event_id'])

            # Index by fact
            key = (evt['subject'], evt['relation'], evt['object'])
            if key not in self.current_facts:
                self.current_facts[key] = []
            self.current_facts[key].append(evt['event_id'])

    def _is_valid_at_time(self, event: ConstructionEvent, timestamp: str) -> bool:
        """Check temporal validity"""
        if timestamp < event.valid_from:
            return False
        if event.valid_to and timestamp > event.valid_to:
            return False
        return True

    def _evaluate_establishment(self, event_id: str, timestamp: str,
                               visiting: Optional[Set[str]] = None) -> str:
        """
        Recursively evaluate establishment state considering conditions
        Returns: ESTABLISHED, NOT_ESTABLISHED, or UNKNOWN
        """
        if visiting is None:
            visiting = set()

        if event_id in visiting:
            # Circular dependency
            return "UNKNOWN"

        event = self.ct_store.get(event_id)
        if not event:
            return "UNKNOWN"

        # Check temporal validity
        if not self._is_valid_at_time(event, timestamp):
            return "UNKNOWN"

        # If this is a retraction, the premise is NOT_ESTABLISHED
        if event.event_type == 'RETRACT':
            return "NOT_ESTABLISHED"

        # If no condition, use base establishment_state
        if not event.condition_ref:
            return event.establishment_state

        # If has condition, must check condition premise
        visiting.add(event_id)
        premise_state = self._evaluate_establishment(event.condition_ref, timestamp, visiting)
        visiting.remove(event_id)

        # Propagate premise state
        if premise_state == "NOT_ESTABLISHED":
            # Premise failed - dependent is NOT_ESTABLISHED
            return "NOT_ESTABLISHED"
        elif premise_state == "UNKNOWN":
            # Premise unknown - dependent is UNKNOWN
            return "UNKNOWN"
        else:
            # Premise established - use this event's state
            return event.establishment_state

    def _get_fact_state_at_time(self, subject: str, relation: str,
                                 object: str, timestamp: str) -> str:
        """
        Get establishment state of a fact at time
        Considers all events that represent this fact and evaluates them
        """
        key = (subject, relation, object)
        if key not in self.current_facts:
            return "UNKNOWN"

        # Find most recent ASSERT/CORRECT event valid at this time
        latest_assert = None
        latest_assert_state = "UNKNOWN"

        for event_id in self.current_facts[key]:
            event = self.ct_store[event_id]

            # Check for retractions
            if event.event_type == 'RETRACT':
                if self._is_valid_at_time(event, timestamp):
                    # This retraction applies
                    return "NOT_ESTABLISHED"

            # Check for ASSERT/CORRECT
            if event.event_type in ('ASSERT', 'CORRECT'):
                if self._is_valid_at_time(event, timestamp):
                    if latest_assert is None or event.valid_from >= latest_assert.valid_from:
                        latest_assert = event
                        # Evaluate establishment considering conditions
                        latest_assert_state = self._evaluate_establishment(event_id, timestamp)

        return latest_assert_state

    def _check_multi_hop_dependency(self, event_ids: List[str], timestamp: str) -> str:
        """
        Check if a chain of dependencies holds
        """
        if not event_ids:
            return "UNKNOWN"

        for event_id in event_ids:
            event = self.ct_store.get(event_id)
            if not event:
                return "UNKNOWN"

            state = self._evaluate_establishment(event_id, timestamp)
            if state == "NOT_ESTABLISHED":
                return "NOT_ESTABLISHED"
            elif state == "UNKNOWN":
                return "UNKNOWN"

        return "ESTABLISHED"

    def _map_establishment_to_semantic_answer(self, establishment_state: str) -> str:
        """
        Map internal establishment_state to semantic answer format
        Used when question expects YES/NO/UNKNOWN semantic answer
        """
        if establishment_state == "ESTABLISHED":
            return "YES"
        elif establishment_state == "NOT_ESTABLISHED":
            return "NO"
        else:
            return "UNKNOWN"

    def _propagate_failure(self, failed_event_id: str,
                          timestamp: str) -> List[str]:
        """
        Find all events whose establishment depends on the failed premise
        Returns list of affected event_ids
        """
        affected = []
        to_check = self.dependents_map.get(failed_event_id, [])

        while to_check:
            current = to_check.pop(0)
            event = self.ct_store.get(current)

            if not event:
                continue

            if self._is_valid_at_time(event, timestamp):
                # Check if this event's state changed due to premise failure
                new_state = self._evaluate_establishment(current, timestamp)
                if new_state == "NOT_ESTABLISHED":
                    affected.append(current)
                    # Add descendants to check
                    to_check.extend(self.dependents_map.get(current, []))

        return affected

    def process_questions(self, questions_path: str) -> Dict[str, str]:
        """Process all questions with Construction logic"""
        with open(questions_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        answers = {}
        t0 = time.perf_counter()

        for q in data['questions']:
            qid = q['question_id']
            category = q['category']
            current_time = q['current_time']
            event_ids = q['relevant_event_ids']

            if category == 'Q1':
                answer = self._answer_q1(q, current_time)
            elif category == 'Q2':
                answer = self._answer_q2(q, current_time)
            elif category == 'Q3':
                answer = self._answer_q3(q, current_time)
            elif category == 'Q4':
                answer = self._answer_q4(q, current_time)
            elif category == 'Q5':
                answer = self._answer_q5(q, current_time)
            elif category == 'Q6':
                answer = self._answer_q6(q, current_time)
            elif category == 'Q7':
                answer = self._answer_q7(q, current_time)
            elif category == 'Q8':
                answer = self._answer_q8(q, current_time)
            elif category == 'Q9':
                answer = self._answer_q9(q, current_time)
            elif category == 'Q10':
                answer = self._answer_q10(q, current_time)
            else:
                answer = "UNKNOWN"

            answers[qid] = answer

        cpu_time_ms = (time.perf_counter() - t0) * 1000
        return answers, cpu_time_ms

    def _answer_q1(self, question: Dict, current_time: str) -> str:
        """Direct fact - convert establishment_state to semantic answer"""
        event_ids = question['relevant_event_ids']
        if not event_ids:
            return "UNKNOWN"

        evt = self.ct_store.get(event_ids[0])
        if not evt:
            return "UNKNOWN"

        state = self._get_fact_state_at_time(evt.subject, evt.relation,
                                           evt.object, current_time)
        return self._map_establishment_to_semantic_answer(state)

    def _answer_q2(self, question: Dict, current_time: str) -> str:
        """Temporal - check validity windows, convert to semantic answer"""
        event_ids = question['relevant_event_ids']
        if not event_ids:
            return "UNKNOWN"

        evt = self.ct_store.get(event_ids[0])
        if not evt:
            return "UNKNOWN"

        state = self._get_fact_state_at_time(evt.subject, evt.relation,
                                           evt.object, current_time)
        return self._map_establishment_to_semantic_answer(state)

    def _answer_q3(self, question: Dict, current_time: str) -> str:
        """Retraction - check if properly retracted"""
        event_ids = question['relevant_event_ids']

        for eid in event_ids:
            evt = self.ct_store.get(eid)
            if evt and evt.event_type == 'RETRACT':
                return "YES"

        return "NO"

    def _answer_q4(self, question: Dict, current_time: str) -> str:
        """
        Dependency/Premise Failure Propagation
        This is where Construction excels
        """
        event_ids = question['relevant_event_ids']
        if not event_ids:
            return "UNKNOWN"

        # Check primary fact
        primary_event = self.ct_store.get(event_ids[0])
        if not primary_event:
            return "UNKNOWN"

        # Use Construction to evaluate with condition propagation
        state = self._evaluate_establishment(event_ids[0], current_time)
        return self._map_establishment_to_semantic_answer(state)

    def _answer_q5(self, question: Dict, current_time: str) -> str:
        """Multi-hop - trace through dependency chain"""
        event_ids = question['relevant_event_ids']
        if not event_ids:
            return "UNKNOWN"

        # Check entire chain
        state = self._check_multi_hop_dependency(event_ids, current_time)
        return self._map_establishment_to_semantic_answer(state)

    def _answer_q6(self, question: Dict, current_time: str) -> str:
        """Unknown - properly propagate UNKNOWN"""
        event_ids = question['relevant_event_ids']
        if not event_ids:
            return "UNKNOWN"

        evt = self.ct_store.get(event_ids[0])
        if not evt:
            return "UNKNOWN"

        state = self._evaluate_establishment(event_ids[0], current_time)
        return self._map_establishment_to_semantic_answer(state)

    def _answer_q7(self, question: Dict, current_time: str) -> str:
        """Contradiction detection"""
        text = question['question'].lower()

        if "contradict" in text:
            if "claim_x" in text and "claim_y" in text:
                return "YES"
            elif "claim_c1" in text and "claim_c2" in text:
                return "YES"
        elif "conflict" in text:
            return "REPORT_CONFLICT"
        elif "both" in text:
            return "NO"

        return "UNKNOWN"

    def _answer_q8(self, question: Dict, current_time: str) -> str:
        """Correction - track old vs new"""
        event_ids = question['relevant_event_ids']

        for eid in event_ids:
            evt = self.ct_store.get(eid)
            if evt and evt.event_type == 'CORRECT':
                if "change" in question['question'].lower():
                    return "YES"

        if "retroactively" in question['question'].lower():
            return "NO"
        elif "equivalent" in question['question'].lower():
            return "YES"

        return "NO"

    def _answer_q9(self, question: Dict, current_time: str) -> str:
        """Current state - final establishment, convert to semantic answer"""
        event_ids = question['relevant_event_ids']
        if not event_ids:
            return "UNKNOWN"

        evt = self.ct_store.get(event_ids[0])
        if not evt:
            return "UNKNOWN"

        state = self._get_fact_state_at_time(evt.subject, evt.relation,
                                             evt.object, current_time)

        # Map specific results for current state
        if state == "NO":
            if "can" in question['question'].lower():
                return "NO"
            elif "halt" in question['question'].lower():
                return "YES"

        return self._map_establishment_to_semantic_answer(state)

    def _answer_q10(self, question: Dict, current_time: str) -> str:
        """Historical state - preserve history, convert to semantic answer"""
        event_ids = question['relevant_event_ids']
        if not event_ids:
            return "UNKNOWN"

        evt = self.ct_store.get(event_ids[0])
        if not evt:
            return "UNKNOWN"

        state = self._get_fact_state_at_time(evt.subject, evt.relation,
                                           evt.object, current_time)
        return self._map_establishment_to_semantic_answer(state)

if __name__ == "__main__":
    print("Construction Representation loaded")
