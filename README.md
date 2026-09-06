# CEGS: Constrained Event Generation Space

結構化 Token 之作用、最低使用條件、形式化基礎與工程路線

---

## 👥 Who Should Care

### You work on:
- **LLM Systems** → RAG, multi-turn dialogue, tool authorization
- **AI Governance** → Policy, compliance, audit trails  
- **Enterprise AI** → Permission systems, content moderation, qualification logic

### Your pain point is:
> "AI systems make decisions about what qualifies to enter a rule space, but we can't see or audit how."

### CEGS helps by:
Making those decisions **explicit, traceable, and human-revisable**.

---

## 🎯 What This Is

**CEGS** is a framework for understanding how **Qualification** — the problem of "what has the right to enter a particular rule space" — works in AI systems and human institutions.

Rather than proposing to *solve* qualification, CEGS provides infrastructure to make qualification decisions:
- **Explicit** (not hidden in black boxes)
- **Auditable** (traceable to source)
- **Revisable** (modifiable by humans)

---

## 💡 Where CEGS Actually Helps

CEGS is most useful **between** AI computation and human decision-making:

```
Input
  ↓
【Qualification Check】← Does this have the right to proceed?
  ↓
[AI Processing]
  ↓
【Qualification Check】← Does this output have the right to be used?
  ↓
Human Review / Decision
```

### Real-World Use Cases

**1. Retrieval-Augmented Generation (RAG)**
- Explicitly mark: "Does this source document qualify for the context window?"
- Let humans set the qualification rules
- Audit which documents were included/excluded and why

**2. Multi-Turn Dialogue State Management**
- Track: "Does this previous turn's answer qualify to be treated as 'established'?"
- Condition: depends on whether safety checks passed, facts verified, etc.
- If a premise fails, propagate the failure forward
- Let humans review the state at each turn

**3. Tool Execution Authorization**
- LLM outputs: "Call delete_user_account()"
- CEGS checks: Does this action have qualification?
  - Does AI have permission?
  - Are prerequisites satisfied?
  - Do dependent conditions hold?
- System executes or refuses based on human-defined rules

---

## ⚠️ Critical Design Principle

> Construction is not meant to automate qualification decisions.  
> It exists to make qualification decisions transparent, traceable, and controllable by humans.

### What CEGS Can Do

✅ **Mechanism Layer**
- Explicitly represent "a qualification judgment has been made"
- Track how qualification dependencies propagate
- Record who made the judgment and when
- Verify whether conditions for qualification are actually satisfied

### What CEGS Cannot Do (and should not)

❌ **Value Layer**
- Decide what *should* become a qualification condition
- Decide *who* has the right to set conditions
- Resolve conflicts between competing qualification standards
- Determine whether a qualification change is "fair"

---

## 📋 Qualification Layers & Responsibility

| Layer | Content | Who Decides |
|-------|---------|-------------|
| **Mechanism** | How qualification is computed, tracked, propagated | System architecture (technical) |
| **Standard** | What conditions grant qualification | **Humans** |
| **Authority** | Who has the right to set those conditions | **Humans** |
| **Conflict** | When standards conflict, which wins | **Humans** |
| **Change** | Whether standards should change | **Humans** |
| **Responsibility** | Who is accountable if qualification causes harm | **Humans / Institutions** |

CEGS operates only in the **Mechanism** layer. Everything else is human territory.

---

## 🚨 The Core Governance Problem

### Self-Qualification Risk

If a qualification-rule-maker uses rules *they created* to grant themselves qualification:

```
C → R → Qualify(C)

"The rule creator can declare themselves qualified via their own rules"
```

This is not automatically illegal. But it **must be visible and controllable by humans**.

#### Example: Content Moderation AI

```
AI creates moderation rule: "word X → delete post"
AI applies rule to its own internal logs: "passes moderation"
AI therefore qualifies to moderate user content

CEGS can expose: ✓ Who made the rule? Who benefits? What changed?
CEGS cannot decide: ✗ Should this be allowed? Is it fair?
```

**Only humans can answer that.**

---

## 🔬 Research Status

This repository contains:

- **Theoretical Framework** (`construction-framework.md`) — core concepts of invariants, alignment, narrative chains
- **Formalization** (`構築計算空間規格.md`) — mathematical definitions with Python implementation
- **Experiment Lab** (`construction_lab/`) — Stage 0 (token efficiency) and Stage 1 (semantic correctness) benchmarks

### Current Findings

- ✅ Correspondence → Symmetry → Alignment → Qualification chain is conceptually sound
- ✅ Qualification can be separated from Application Context
- ✅ AI systems already execute qualification-like behaviors (implicitly)
- ⚠️ **Whether this reduces token consumption, improves correctness, or scales to real systems still requires external verification**

---

## 📌 The One-Sentence Summary

> **Qualification decisions exist in all systems (human and AI). CEGS makes them visible so humans can review, audit, and change them. It doesn't replace human judgment — it enables it.**

---

## 🚫 What CEGS Is NOT

- ❌ A replacement for human decision-making
- ❌ A guarantee of fairness or objectivity
- ❌ An automation tool for values
- ❌ A theory of consciousness or agency
- ❌ A claim that AI has or should have independent authority

---

## ✅ What CEGS IS

- ✓ A way to structure how qualification decisions are made
- ✓ A transparency layer between AI computation and human authority
- ✓ An auditing and revision infrastructure
- ✓ A framework for understanding governance of AI systems

---

## 📚 Documentation

- `construction-framework.md` — Theoretical foundations
- `構築計算空間規格.md` — Formalization + Python implementation  
- `構築單位呈現條件與形式化研究.md` — Motivation for Construction Tokens
- `construction_lab/` — Runnable experiments
- `資格論.md` — Philosophical grounding in qualification theory

---

## 🧪 Try It Out

The `construction_lab/` directory contains working implementations of both theoretical and experimental approaches:

```bash
# View Stage 0 token efficiency experiments
python construction_lab/stage0_token_count.py

# Run Stage 1 semantic correctness evaluation
python construction_lab/stage1_evaluator.py

# Inspect baseline vs construction representations
python construction_lab/baseline_representation.py
python construction_lab/construction_representation.py
```

See `construction_lab/START_HERE.txt` and `construction_lab/START_HERE_STAGE1.txt` for guided walks through experiments.

---

## ⚖️ License & Attribution

This research is a collaborative investigation into qualification structures in AI systems.

**Important**: Do not deploy any CEGS-based system that treats its outputs as "objective" or "bias-free". All qualification decisions must be human-reviewable and human-revisable.

---

## 📧 Questions?

For questions about the framework, experimental results, or potential applications, please open an issue or start a discussion.

For Chinese-language questions: 本研究使用中文撰寫，歡迎提出中文議題或討論。
