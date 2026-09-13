# Construction Theory Framework
> Derivation record | Centered on Invariants, Alignment, Sub-symmetry, and Continuable Invariants

---

## I. TOKN Extension

Original TOKN structure:

```text
TOKN = Collection + Weight
```

This can describe association strength but cannot describe relation direction.

Proposed extension:

```text
TOKN = Collection + Relation + Direction + Weight
```

Here **Direction is a fundamental dimension that was originally missing**, not a later decoration.

### Symbol conventions

| Symbol | Meaning |
|------|------|
| `→` | Directed |
| `←` | Reverse-directed |
| `↔` | Bidirectional |
| `↛` | Relation does not hold |

**Reverse direction ≠ negation** and must be strictly distinguished.

### Direction vs. Role

```text
Direction = how a relation is directed
Role      = whether a node serves as Source or Target in the relation
```

They are different levels and cannot be interchanged.

---

## II. Basic Structure

### Invariant

An Invariant is a **semantic anchor that cannot be removed from the topic within this segment of discussion**, providing a stable reference domain.

> Note: An Invariant is a constraint and localization condition, not the parent node of the content.

### Construction Structure

```text
Invariant {
  Subset1 ( Subsymmetry1 | Subsymmetry2 )
  Subset2 ( Subsymmetry1 )
}
→
InvariantB {
  Subset1 ( Subsymmetry1 )
}
```

Directional arrows between topics represent relations.

### Substitution Conditions

```text
Valid substitution = positional alignment (subsymmetries fully match)
                  + traceable logical chain
                  + preservation of Role / Anchor / Order / Constraint
```

- Fully matching → substitutable (`A ↔ C`)
- Partially matching → locally substitutable (`A ≈ C`)
- No match → not substitutable (`A ≁ C`)

**Traceable ≠ valid.**

---

## III. Order

Order is the **priority structural condition** that Construction uses to preserve identity continuity and narrative traceability; it is not a fifth parallel element.

### Three Levels of Order

| Level | Content |
|------|------|
| Representation | Symbol arrangement (`A → B → C`) |
| Relational | Why the sequence holds in this order |
| Historical | How the Construction became what it is now |

### Narrative Chain Definition

```text
NarrativeChain ≠ OptimalPath
NarrativeChain ≠ CorrectPath
Revision ⊂ NarrativeChain
```

The Narrative Chain preserves the **historical structure of how the Construction became what it is now**.

Aligned logical-chain combinations → form the Order of the Narrative Chain (accumulated from alignment results, rather than given in advance).

The anchor of identity continuity is not the Invariant itself, but the **accumulated record of alignment events (Alignment Trace)**.

---

## IV. Construction Minimum Closure

The bridge by which one alignment becomes a Construction is the **continuable Invariant**.

### Four-Layer Structure

```text
① Alignment
  A sub-item forms local consistency with an existing reference

② Subsymmetry
  A recognizable relational structure is formed from the alignment

③ Stage-wise Invariant
  A stable portion capable of crossing into the next stage is retained from the subsymmetry

④ Continuous Expansion
  The next subset aligns again with reference to that Invariant
```

### Minimum Closure Process

```text
Invariant / Existing Stable Reference
    ↓
Subset localization
    ↓
Alignment established
    ↓
New structure / subsymmetry formed
    ↓
Extract continuable Invariant
    ↓
【 Construction Closed 】
    ↓
Become the basis of the next Construction
```

### Important Distinction

```text
Construction closure ≠ Narrative Chain continuation
```

- **Construction** only needs to be completed once.
- **Narrative Chain** is what repeatedly occurs across stages.

> Each establishment leaves the conditions for the next establishment — that is Construction.

An Invariant can recursively continue by stage:

```text
Global Invariant
    ↓
Local alignment → Local invariant
    ↓
Next-stage invariant
    ↓
New alignment → New local invariant
    ↓
……
```

---

## V. Memory Mechanism

### Core Principle

```text
Memory preservation ≠ memory use
Past Data × Current Reality → Usable Memory
```

The present is the judge of memory.

```text
Exists ≠ retrievable ≠ should be retrieved ≠ should affect judgment
```

### Qualification Definition

```text
Data ≠ Qualification
AI   ≠ Qualification
Judgment Result = Qualification
```

Qualification = the current Construction's judgment of an establishment relation concerning a piece of historical data.

Qualification itself is temporal:

```text
Qualification( Trace, t | Construction_t )
```

The same Trace may receive different qualification results at different times.

### Trace Definition

```text
Trace ≠ recording of the entire process
Trace = continuable evidence of a completed Construction
Full History ≫ Identity Certificate
```

Only a Minimal Sufficient Trace is required; the entire history need not be preserved.

### Memory Recall Process

```text
Invariant Set
    ↓
Subset
    ↓
Sub-item
    ↓
Alignment formed
    ↓
Alignment Trace
    ↓
Current Reality re-check
    ↓
Memory re-entry
```

Current Reality does not directly judge old memory; an existing unit that can be aligned must first be found.

**Ordinary Retrieval:** this data resembles the present, so retrieve it.

**This architecture:** the item once aligned at a recognizable structural position, the same position is found again, and the current reality permits renewed qualification; only then is it restored for use.

---

## VI. Irreversibility and Historical Establishment

Construction theory **does not require** LLM internal computation to be irreversible in a physical or information-theoretic sense.

What is actually required is:

> Once an Alignment Trace has formed, the way in which it **previously became established** cannot be fabricated after the fact.

### Three Layers Kept Separate

| Layer | Property |
|----|------|
| Formation | Cannot be arbitrarily rewritten backward |
| Qualification | Can be recomputed over time |
| Usage | Can change |

After Trace₁ becomes false in qualification, this does not mean it "never held":

```text
Historically established ≠ currently valid ≠ should currently be used
```

### Architectural Layers

```text
LLM
(candidate computational results)
    ↓
Construction Layer
(determine which alignments hold and which Traces form)
    ↓
Memory Layer
(store continuable Invariants and Traces)
    ↓
Current Reality
(re-determine whether they are currently usable)
```

Construction does not parasitize the history of internal LLM neurons; it is a **structural layer built above the LLM**.

### Core Proposition

> Construction establishment does not depend on whether underlying LLM computation is reversible. It only requires that the history of a formed Construction not be arbitrarily tampered with, while its current qualification for use may be re-determined by Current Reality.

---

## VII. Research Positioning

This is neither vLLM nor LLVM. The closest existing description is:

```text
Knowledge Representation + Graph-based Prompting
```

However, no existing framework currently covers the whole structure.

### Components Already Present in Existing Research

| Component | Status |
|------|------|
| Alignment | ✓ |
| Relation Path | ✓ |
| Traceability | ✓ |
| Temporal Order | ✓ |
| Incremental Update | ✓ |

**What is missing:** the complete causal chain of "accumulation of alignment events → why the Construction remains the same Construction."

### Current Research Boundary

```text
Construction
└─ Topic
   └─ Topic Identity
      └─ Narrativity
         └─ Narrative Chain   ← current boundary
```

Stop at Narrative Chain. Do not continue toward a complete memory system or Identity Certificate.
