# Getting Started with CEGS

This guide helps you understand CEGS based on what you do.

---

## 🎯 I'm an LLM/AI Engineer

### The Problem You Already Have
Your RAG system picks documents by vector similarity. Your tool authorization just checks "is this in the allowed list?" Your dialogue state management has implicit assumptions that break silently.

**All of these are qualification decisions — but you can't see them or audit them.**

### Quick Start

1. **Understand the concept** (15 min)
   - Read the "Real-World Use Cases" section in `README.md`
   - Look at `construction_lab/stage1_question_matrix.md` for concrete examples

2. **See it in code** (30 min)
   - `construction_lab/baseline_representation.py` — how systems do it implicitly now
   - `construction_lab/construction_representation.py` — how CEGS makes it explicit

3. **Measure the difference** (20 min)
   - `construction_lab/stage0_token_count.py` — token efficiency impact
   - `construction_lab/stage1_evaluator.py` — semantic correctness gains

### Next Steps
- Check `construction_lab/RESULTS.md` for Stage 0 & Stage 1 findings
- Examine `construction_lab/gold_answers.json` to see what "correct qualification" looks like
- Open an issue if you see how to apply this to your system

---

## 🛡️ I'm an AI Safety / Governance Researcher

### The Problem You're Studying
AI governance frameworks talk about "transparency" and "auditability" in the abstract. But qualification decisions — who decides what can do what — are concrete and already happening in production systems.

**You need a way to make those decisions visible and traceable.**

### Quick Start

1. **Understand the theoretical foundation** (45 min)
   - `construction-framework.md` — core concepts of alignment, invariants, narrative chains
   - `資格論.md` — philosophical grounding: why qualification is more fundamental than "consciousness"

2. **See the formal definition** (30 min)
   - `構築計算空間規格.md` — mathematical formalization
   - Look at the Python implementation in `construction_lab/construction_representation.py` for how these map to code

3. **Understand the research status** (20 min)
   - `construction_lab/RESULTS.md` — what we've verified so far, what's still open
   - `construction_lab/STAGE1_DEBUG_REPORT.md` — what we're still debugging

### Key Insights
- **Qualification ≠ Subjectivity** — You don't need to solve "is AI conscious?" to ask "what qualification does this AI have?"
- **Mechanism ≠ Values** — CEGS only handles the mechanism layer (how decisions are recorded). Humans decide the values (what conditions should matter).
- **Separation from Application Context** — Whether something qualifies doesn't depend on where it's used, but on what structural conditions it meets.

### Next Steps
- Review the Qualification Layers table in `README.md` — this is directly usable in AI governance policy
- Examine `construction_lab/stage1_schema.md` to see the formal structure of a qualification decision
- See if you can map existing AI governance frameworks onto the layers defined in the README

---

## 🏢 I'm an Enterprise AI Team

### The Problem You Have
You deploy content moderation, recommendation systems, or authorization engines. You need to:
- **Audit** why a decision was made (compliance)
- **Override** decisions when they're wrong (human control)
- **Change rules** without retraining (agility)

**CEGS gives you the infrastructure to do this.**

### Quick Start

1. **Understand what CEGS does for you** (10 min)
   - Read the "Where CEGS Actually Helps" section in `README.md`
   - Scan the qualification layers table — this is your responsibility map

2. **See a working example** (20 min)
   - `construction_lab/construction_representation.py` — concrete implementation
   - Pay attention to the logging/tracing parts — that's your audit trail

3. **Check feasibility** (15 min)
   - `construction_lab/cpu_ct_benchmark.py` — computational overhead
   - `construction_lab/RESULTS.md` — token cost impact on LLM systems

### Implementation Path
- Start with one system (e.g., RAG document filtering)
- Use CEGS to represent qualification decisions
- Log every decision with `who`, `what`, `when`, `why`
- Let humans review before applying at scale

### Next Steps
- Estimate which of your systems could benefit most (start with high-stakes ones)
- Check if token cost is acceptable for your use case (see Stage 0 results)
- Open an issue if you want to discuss real-world deployment challenges

---

## 🎓 I'm a Student / Researcher Exploring AI

### The Problem CEGS Solves
Most AI research treats decision-making as a black box. CEGS says: "No, let's make the structure visible."

It's relevant if you're interested in:
- AI transparency and interpretability
- AI governance and policy
- Formal verification of AI systems
- Alignment and safety

### Quick Start

1. **Get the big picture** (20 min)
   - `README.md` — the full overview
   - `construction-framework.md` — theoretical foundations

2. **See the mathematics** (45 min)
   - `構築計算空間規格.md` — formal definitions
   - `construction_lab/stage1_schema.md` — concrete structure

3. **Understand the open questions** (30 min)
   - `construction_lab/RESULTS.md` — "Current Findings" section
   - `資格論.md` — the deepest reflection on what's been discovered

### Key Concepts to Grasp
- **Correspondence, Symmetry, Alignment** — three operations that form qualification
- **Qualification Chain** — how individual decisions connect into traceable sequences
- **Establishment Domain** — what makes something "qualified" independent of context

### Next Steps
- Try running the experiments in `construction_lab/` — understand the code
- Read `資格論.md` deeply — this is the research frontier
- Consider how to extend this to your own research area

---

## 🌍 General Orientation

### File Map

| File | Purpose | Read Time |
|------|---------|-----------|
| `README.md` | Overview for all audiences | 10-20 min |
| `construction-framework.md` | Theory and core concepts | 30-45 min |
| `構築計算空間規格.md` | Mathematical formalization | 45-60 min |
| `資格論.md` | Philosophical grounding | 30-40 min |
| `construction_lab/` | Working code and experiments | 30-120 min depending on depth |

### Research Status

**✅ Established:**
- Correspondence → Symmetry → Alignment → Qualification conceptual chain
- Qualification can be separated from application context
- AI systems already do qualification implicitly

**⚠️ Still Verifying:**
- Token efficiency gains (Stage 0: showing 28.4% improvement over 25% threshold, but with rendering issues)
- Semantic correctness improvements (Stage 1: in progress)
- Real-world system scalability

**🔴 Still Unknown:**
- Whether this scales to large production systems
- Best practices for enterprise deployment
- How to handle qualification conflicts

---

## 📞 Next Steps

1. **Identify your role** in the table above
2. **Follow the Quick Start** for that role (should take 1-2 hours)
3. **Read the relevant sections** based on your interest depth
4. **Open an issue** if you have questions or want to contribute
5. **Share your use case** if you see how CEGS applies to your work

---

## 🌐 Resources

- **Theory-first:** Start with `construction-framework.md` then `資格論.md`
- **Code-first:** Start with `construction_lab/construction_representation.py` then work backwards to theory
- **Problem-first:** Identify your use case in the README, then find the relevant code/docs

---

*Last updated: 2026-09-06*  
*Language: English (中文版本請見各文件)*
