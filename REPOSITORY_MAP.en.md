# CEGS Repository Map

> Purpose: separate CEGS into "index, current theory, historical versions, ongoing research, date evidence, and historical experiments." Dates preserve formation history; research status represents current standing. Neither replaces the other.
>
> From 2026-09-12 onward, `00_INDEX/CONTENT_CATALOG.md` and `00_INDEX/AI_INGESTION_GUIDE.md` were added as shared human / AI reading entry points and layered-reading rules.

## 1. Repository Position

CEGS (Constrained Event Generation Space) is a public engineering / experimental node in the history of Construction research; it is not equivalent to the complete Construction theory.

The repository preserves documents from different periods at the same time. Therefore, their coexistence in the same repository must not be used to infer that they belong to the same version.

## 2. Current Directory Structure

```text
CEGS/
│
├─ 00_INDEX/
│  ├─ RESEARCH_STATUS.md
│  ├─ CONTENT_CATALOG.md
│  └─ AI_INGESTION_GUIDE.md
│
├─ 10_CURRENT_THEORY/
│  ├─ README.md
│  ├─ foundation/
│  ├─ formalization/
│  └─ appendices/
│
├─ 20_VERSIONED/
│  ├─ README.md
│  ├─ 20260828/
│  └─ 20260906/
│
├─ 30_ACTIVE_RESEARCH/
│  ├─ README.md
│  └─ construction/
│     ├─ memory/
│     └─ exchange/
│
├─ 90_UNDATED_OR_UNRESOLVED/
│
├─ 2026.9.10/
│  └─ Original dated research / version evidence
│
├─ 2026.9.12/
│  └─ New research supplements / dated evidence from that day
│
└─ construction_lab/
   └─ Historical engineering and experimental evidence
```

## 3. Seven Reading States

### Index

`00_INDEX/` does not carry new theoretical conclusions. It tells humans and AI where documents are, what state they are in, and how they should be read.

### Current Theory

`10_CURRENT_THEORY/` represents content currently adopted and maintained as the basis of Construction theory.

Being located here does not mean being proven; types, MCS, necessity, and some cross-layer relations remain open questions.

### Versioned

`20_VERSIONED/` preserves documents with explicit versions or historical stages. Its purpose is to trace evolution, not to provide the one currently correct answer.

### Active Research

`30_ACTIVE_RESEARCH/` preserves research still undergoing derivation, comparison, reduction, validation, or decision.

### Date Evidence

`2026.9.10/` and `2026.9.12/` preserve original materials formed on specific dates. A dated directory can contain multiple research topics and therefore does not directly correspond to a single theoretical layer.

### Historical Experiment

`construction_lab/` preserves early engineering, code, results, run logs, debugging, repair, audit, and related materials. These are experimental evidence and are not automatically equivalent to theoretical validation.

### Unresolved

`90_UNDATED_OR_UNRESOLVED/` preserves materials whose dates or research positions cannot currently be determined reliably. Do not guess a classification merely for tidiness.

## 4. Current Construction Main Line

```text
Early Event Representation / Qualification
                ↓
Construction emergence
                ↓
Alignment / Invariant / Trace / Narrative Continuity
                ↓
Core candidate baseline
                ↓
Adaptive Construction + Thematic Invariance
                ↓
State → Representation → Interpretation
                ↓
Memory / Emotion / Exchange research branches
```

## 5. Important Non-Merging Relationships

`20_VERSIONED/20260828/` ≠ `10_CURRENT_THEORY/`.

`20_VERSIONED/20260906/` Qualification theory ≠ complete Construction definition.

Stage 1 results in `construction_lab/` ≠ Construction has been validated.

`30_ACTIVE_RESEARCH/` ≠ completed proof.

`2026.9.10/` and `2026.9.12/` ≠ a single current-theory layer.

## 6. New-Document Rules

When adding a document, first determine:

1. **Time / version:** When was it formed?
2. **Research status:** Is it current, historical, ongoing, evidence, or unresolved?
3. **Document role:** Is it theory, formalization, appendix, research, index, experiment, or original data?

If it only differs by historical date, do not overwrite the current theory.

If it is still being derived, place it in `30_ACTIVE_RESEARCH/`.

If it is a currently adopted theoretical baseline, place it in `10_CURRENT_THEORY/`.

If the data has irreplaceable historical-evidence value, preserve the dated original even when a current reading location also exists.

## 7. Current Index Entry Point

For first reading:

```text
README
 ↓
00_INDEX/RESEARCH_STATUS
 ↓
00_INDEX/CONTENT_CATALOG
 ↓
00_INDEX/AI_INGESTION_GUIDE
 ↓
Construction Research MOC
 ↓
10_CURRENT_THEORY
 ↓
30_ACTIVE_RESEARCH
 ↓
20_VERSIONED / Date Evidence / construction_lab (trace back as needed)
```

## 8. Current Research Status Summary

**Established / Traceable**

- Historical repository, engineering, and experimental materials.
- Conceptual separation between Construction and Qualification.
- Current main Construction theory.
- Fourteen core candidate baseline.
- Research direction in which multiple minimal structures may establish the same target.
- Layered preservation of version, date, and research status.
- State / Representation / Interpretation mapping supplement added 2026-09-12.

**Theoretical Candidates / Ongoing Research**

- Formal MCS minimality.
- Invariant / Logic Chain / Narrative Chain.
- Correspondence / Symmetry / Alignment.
- Memory Equivalent / Current Judgment Quantity.
- Emotion → Memory Equivalent.
- First layer of Exchange: Difference → Need → Exchange.
- Thematic continuity in State → Representation → Interpretation.

**Explicitly Not Claimed**

- Construction has been completely proven.
- Stage 1 has proven Construction.
- A single MCS is universally valid.
- Emotion, exchange, or cross-layer mapping has become an indispensable core.
- CEGS can independently determine value, fairness, or governance legitimacy.

## 9. Principles

> A historical version is not an erroneous version.
>
> A research candidate is not a proven proposition.
>
> Experimental success is not theoretical establishment.
>
> A date is not a status.
>
> An index is not a theory.
