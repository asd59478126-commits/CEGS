# CEGS AI Ingestion Guide

> This file defines how an AI system should read CEGS without flattening historical versions, current theory, active research, and experimental evidence into one undifferentiated knowledge state.

## 1. First rule

Treat the repository as a layered research record, not as a single document.

```text
Repository
├─ Index / metadata
├─ Current theory
├─ Historical versions
├─ Active research
├─ Date-bound raw evidence
└─ Historical experiments
```

A later document may supersede an earlier formulation without making the earlier document false as a historical record.

## 2. Source priority

When answering "what is the current theory?":

1. `10_CURRENT_THEORY/`
2. `構築研究 MOC.md`
3. `00_INDEX/`

When answering "how did this concept develop?":

1. `20_VERSIONED/`
2. `2026.9.10/`
3. `2026.9.12/`
4. `10_CURRENT_THEORY/`

When answering "what is still unresolved?":

1. `30_ACTIVE_RESEARCH/`
2. open-problem sections in current theory documents
3. `00_INDEX/RESEARCH_STATUS.md`

When answering "what was actually implemented or tested?":

1. `construction_lab/`
2. experiment and audit records
3. historical result files

## 3. Never flatten these distinctions

```text
Historical version ≠ Current theory
Current theory ≠ Proven theory
Candidate ≠ Established
Experiment reproducibility ≠ Theory validation
Stored information ≠ Usable memory
Representation ≠ Reality
Observation ≠ Reality
Interpretation ≠ Observation
```

## 4. Construction interpretation baseline

Current Construction research should be read as a theory of adaptive structural organization for multidimensional information and concepts.

Core current direction:

```text
Purpose + Goal + Conditions
            ↓
      Construction
            ↓
Adaptive form
            ↓
Thematic continuity
```

The current theory explicitly allows multiple valid constructions and does not require one universal minimal structure.

## 5. Mapping layer

The 2026-09-12 supplement introduces a current theoretical direction:

```text
Internal State
      ↓
External Representation
      ↓
Interpretation
```

Interpretation rules:

- do not treat representation as transparent transmission;
- do not treat interpretation as direct retrieval of internal state;
- do not infer the original internal state directly from an interpretation;
- investigate what thematic structure can remain continuous across these mappings.

This is a theoretical supplement, not a final ontology of mind or consciousness.

## 6. How to quote or summarize

When summarizing a claim, attach its status mentally before stating it:

- **Established:** explicitly stated as currently established or structurally adopted.
- **Candidate:** proposed for cross-topic or formalization work.
- **Active research:** currently being tested, compared, or developed.
- **Historical:** valid as evidence of an earlier formulation, not automatically current.
- **Unresolved:** intentionally left open.
- **Not claimed:** explicitly disclaimed by the research.

Do not silently convert one status into another.

## 7. Human vs AI reading behavior

For a human reader, prioritize conceptual orientation and lineage.

For an AI reader, preserve structured metadata and source boundaries before semantic synthesis.

Recommended internal record for every document:

```yaml
path: <repository path>
date: <known date or null>
version: <version or null>
status: current | historical | active | unresolved | evidence
role: theory | formalization | appendix | research | archive | experiment | index
parent_concept: <optional>
supersedes: <optional>
superseded_by: <optional>
claims: []
open_questions: []
```

## 8. Safe synthesis rule

Synthesis may connect documents, but must preserve provenance.

Example:

```text
2026-08-28 computational-space model
        ↓ historical lineage
2026-09-07 Construction framework
        ↓ conceptual consolidation
2026-09-10 adaptive construction / thematic invariance
        ↓ new theoretical supplement
2026-09-12 state-representation-interpretation mapping
```

The synthesis is an interpretation of the lineage; it is not a replacement for any source document.
