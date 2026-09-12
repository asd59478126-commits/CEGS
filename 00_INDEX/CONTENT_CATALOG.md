# CEGS Content Catalog

> Purpose: provide a stable, human-readable and AI-readable catalog of the repository without replacing any research document.
>
> **Authority rule:** this catalog is an index, not a theory source. When it conflicts with a source document, read the source document and preserve the conflict for review.
>
> **Preservation rule:** historical files are not deleted, overwritten, or silently reclassified. A file may have both a historical location and a current reading role.

## 1. Repository-level classification

| Class | Path | Meaning | Reading priority |
|---|---|---|---|
| Index | `00_INDEX/` | Navigation, status, catalog, cross-file interpretation | First |
| Current Theory | `10_CURRENT_THEORY/` | Current Construction theory baseline and formalization work | Second |
| Versioned History | `20_VERSIONED/` | Explicit historical versions and superseded formulations | As needed for lineage |
| Active Research | `30_ACTIVE_RESEARCH/` | Unresolved, comparative, experimental, or still-forming research | Third |
| Undated / Unresolved | `90_UNDATED_OR_UNRESOLVED/` | Material whose date/status cannot yet be assigned reliably | Last / quarantine |
| Date Evidence | `2026.9.10/`, `2026.9.12/` | Raw date-bound research evidence; preserves formation history | Historical evidence |
| Historical Experiment | `construction_lab/` | Executable and audit material for earlier CEGS / Stage 1 work | Evidence / validation |

## 2. Current theory

### 2.1 Primary theory

`10_CURRENT_THEORY/foundation/構築（Construction）：多維資訊概念中的適應性結構與主題性不變.md`

Role: current main Construction theory document.

Current themes:
- adaptive construction;
- thematic invariance;
- multiple valid constructions;
- task purpose / task goal / conditions;
- fourteen core candidate structures;
- state / representation / interpretation mapping;
- explicit non-claims about uniqueness and final ontology.

### 2.2 Core candidate baseline

`10_CURRENT_THEORY/foundation/目前研究核心第一版：內容資料正式紀錄.md`

Role: first stable cross-topic core set.

Core candidates:
`Topic`, `Invariant`, `Relation`, `Condition`, `Validity`, `Observation`, `Interpretation`, `Necessary Structure`, `Sufficiency`, `Expansion`, `Anticipation`, `Continuation`, `State`, `Boundary`.

Important rule: the fourteen items are a working candidate basis, not a final set of irreducible primitives.

### 2.3 Earlier Construction framework

`10_CURRENT_THEORY/foundation/construction-framework.md`

Role: earlier/current-supporting framework containing TOKN, direction, invariant words, alignment, order, narrative chain, traceability, memory re-entry, qualification, and the historical distinction between formation, qualification, and usage.

Important lineage: this file is especially useful for understanding how Construction evolved from earlier Qualification / representation work.

### 2.4 Formalization

`10_CURRENT_THEORY/formalization/構築 — 形式化草稿 型別優先.md`

Role: type-first formalization work; not automatically proof of the theory.

### 2.5 Appendix

`10_CURRENT_THEORY/appendices/構築_附錄C_展開的相對性與錨點必要性_20260907.md`

Role: supporting local derivation on expansion relativity and anchor necessity.

## 3. Current research branches

### 3.1 Memory / emotion

Path: `30_ACTIVE_RESEARCH/construction/memory/`

Focus:
- Memory Equivalent;
- memory continuity;
- current judgment quantity;
- memory invariant;
- emotion as a candidate influence on recall / current judgment;
- agent emotional peak vs user-specific emotional reference.

Status: research branch, not established Construction core.

### 3.2 Exchange

Path: `30_ACTIVE_RESEARCH/construction/exchange/`

Focus:
- difference;
- communication need;
- exchange need;
- demand boundary / peak;
- first-layer Exchange Governance assumptions.

Status: research branch; not a completed governance model.

### 3.3 Mapping research

Current source:
`2026.9.12/構築_狀態表示理解映射補充.md`

Current direction:
`State → Representation → Interpretation`

Working interpretation:
- external representation is a constructed form, not transparent transmission;
- interpretation is reconstructed understanding, not direct retrieval;
- thematic continuity may be preserved despite representational change.

Status: important current theoretical supplement; formalization still unresolved.

## 4. Historical version line

### 2026-08-28

`20_VERSIONED/20260828/`

Contains earlier Construction Unit presentation conditions, computational-space specification, and related formalization.

Use for historical lineage only. Do not treat as the sole current definition.

### 2026-09-06

`20_VERSIONED/20260906/`

Contains Qualification-related theory and explanatory report material.

Use to trace the separation of Qualification from Construction.

### 2026-09-10 raw evidence

`2026.9.10/`

Contains the raw date-bound set for that research session, including Construction, core records, memory/emotion, exchange, planetary program, and PDF evidence.

This directory is intentionally heterogeneous. **Do not treat the entire date directory as one theory layer.**

### 2026-09-12 raw evidence

`2026.9.12/`

Contains the dated record for the state–representation–interpretation mapping supplement.

## 5. Historical experiment

`construction_lab/`

Role: historical engineering / experiment evidence.

Contains Stage 1 instructions, baseline and Construction representation implementations, results, run logs, debug traces, repair reports, and the Stage 1 package.

Rule: experimental execution history is evidence about an experiment, not automatic proof of Construction.

## 6. Undated / unresolved

`90_UNDATED_OR_UNRESOLVED/通用舒適ux版.md`

Status: intentionally unresolved classification. Do not promote it merely because it is useful or old.

## 7. Cross-file conceptual map

```text
Early event representation / Qualification
              ↓
Construction emergence
              ↓
Alignment / invariant / trace / narrative continuity
              ↓
Core candidate set
              ↓
Adaptive construction + thematic invariance
              ↓
State → Representation → Interpretation
              ↓
Current research branches
        ┌───────────────┐
        ↓               ↓
   Memory / Emotion   Exchange
```

## 8. Human reading order

1. `README.md`
2. `00_INDEX/RESEARCH_STATUS.md`
3. `00_INDEX/CONTENT_CATALOG.md`
4. `構築研究 MOC.md`
5. `10_CURRENT_THEORY/foundation/構築（Construction）：多維資訊概念中的適應性結構與主題性不變.md`
6. `10_CURRENT_THEORY/foundation/目前研究核心第一版：內容資料正式紀錄.md`
7. `10_CURRENT_THEORY/foundation/construction-framework.md`
8. `10_CURRENT_THEORY/formalization/`
9. `30_ACTIVE_RESEARCH/construction/`
10. `20_VERSIONED/` and date-bound records only when lineage is required
11. `construction_lab/` when validating engineering history

## 9. AI reading protocol

When ingesting CEGS, do not flatten all files into one undifferentiated context.

First extract metadata:
- path;
- date/version;
- research status;
- document role;
- whether it is source evidence, current theory, candidate, or unresolved material.

Then read in layers:

```text
INDEX
  ↓
CURRENT THEORY
  ↓
CORE BASELINE
  ↓
ACTIVE RESEARCH
  ↓
HISTORICAL LINEAGE
  ↓
EXPERIMENTAL EVIDENCE
```

Never infer theory status from date alone.
Never infer truth from repository location alone.
Never replace a historical formulation with a later formulation without recording the transition.
Never merge a candidate definition into an established definition merely because they use similar language.

## 10. Change rules

- Add a new file without deleting the source it came from.
- Record date and status explicitly when known.
- Use `10_CURRENT_THEORY` only for material currently serving as a theory baseline.
- Use `30_ACTIVE_RESEARCH` for unresolved or still-changing work.
- Use `20_VERSIONED` for explicit historical versions.
- Preserve date-bound raw records as evidence.
- If status is genuinely uncertain, keep the file unresolved rather than guessing.
