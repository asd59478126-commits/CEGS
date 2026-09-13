---
title: "Construction — Formalization Draft, Type-First"
aliases:
  - "Formalization Draft"
  - "Type-First Version"
tags:
  - Construction/Formalization
  - Status/Draft
created: 2026-09-07
version: v0.1
supersedes: none
frozen_exception: true
---

> [!info] Sequence
> ← [[Construction — Appendix C: The Relativity of Expansion and the Necessity of Anchors]]
> Parent document: [[CONSTRUCTION_RESEARCH_STATUS]]

# Construction — Formalization Draft (Type-First Version)

**Creation date**: 2026-09-07  
**Document version**: Draft v0.1  
**Document nature**: New draft. **Does not replace, overwrite, or delete 《Mathematical Representation of Construction Establishment Criteria and Minimum Establishment Structure》 or any existing document.**

**Writing principle**: Only write the parts whose **types are determined**. Leave type-uncertain parts blank and explicitly state what is missing.  
**No numerical values are involved.** All content in this document concerns structure and types; there is no quantification.

---

## 0. Notation Conventions

| Notation | Meaning |
|---|---|
| `X : T` | X has type T |
| `𝒫(X)` | Power set of X |
| `X ⇀ Y` | Partial function from X to Y |
| `⟨…⟩` | Ordered tuple |
| **［Missing］** | Type is undetermined; this draft does not write it |

---

## 1. Underlying Sets

```text
I  : Set                      currently accessible information set
S  : Set,  S ⊆ I              retained information structure
Θ  : Set                      set of topics
```

**Type determined.** `S ⊆ I` is consistent across all existing documents, with no divergence.

**Note**: This draft does not assume that I is finite. When I is infinite, the existence conditions for an MCS remain an item to be proved under STATUS §2.3.

---

## 2. Establishment Judgment Q

### 2.1 Codomain

```text
Q : ⟨T, S, C, K⟩ → 𝔹        𝔹 = {established, not established}
```

**Basis**: The proposer explicitly stated in this round that “K has only two values for the topic invariant: established and not established.”

**Conflict already marked (STATUS §4.5)**: the implementation, §4 of 《AI Structured Understanding》, and T1.1 of the test plan all use a three-valued Kleene table (ESTABLISHED / NOT_ESTABLISHED / UNKNOWN).

**Treatment in this draft**: The codomain is written as 𝔹, with a note that the computational upper-bound argument in Appendix B §11.1 requires “I did not check everything” to be expressible, which requires a third value. **The binary-versus-ternary choice has not been decided; this draft does not force a choice.**

### 2.2 Parameter Types

```text
T : ［Missing］                  target structure
S : Set                         ✓ determined
C : ［Missing］                  Context
K : ［Missing］                  see §3
```

**Of the four parameters, only S has a determined type.** This is the largest gap in the current formalization; this is not an exaggeration.

---

## 3. K — The Main Gap

### 3.1 Three Existing Uses with Incompatible Types

| Source | Role of K | Implied type |
|---|---|---|
| 《Mathematical Representation》, second equation | parameter of Q, parallel to T, S, C | a **value** |
| This round: “the anchor point of the multidimensional unit called Topic” | localization | a **point** |
| This round: returns established / not established | judgment | a **function** `I ⇀ 𝔹` |

**Value, point, and function have different types.** Until the type is determined, Q cannot be written as a definition and can only be written as notation.

### 3.2 What Can Be Written in This Round

The proposer supplied one computable component in this round:

```text
exists_theme : Θ ⇀ 𝔹          “whether the theme described by the K currently in use exists”
```

**Type determined; it can be written.**

Its scope must nevertheless be stated explicitly:

```text
exists_theme(θ) = not established  ⟹  Q(T,S,C,K) = not established
exists_theme(θ) = established      ⟹  ［value of Q undetermined］
```

That is: **topic existence is a necessary condition for establishment, not a sufficient condition.** It is a threshold, not the complete criterion.

### 3.3 Excluded Candidates (Listed Only for Type Reasons)

| Candidate | Type problem |
|---|---|
| K = [[Invariant]] | Invariant is a unit; K is required to be a judgment; a unit does not judge |
| K ⊆ S | Q treats S and K as independent parameters; if K ⊆ S, `∄S′ ⊊ S` may remove K itself |
| K = task purpose | collapses back into T; Q becomes minimization of T relative to T |
| K = [[Anchor Ontology]] | Anchor Ontology was determined in this round to be methodology, not a unit (see §5) |

---

## 4. [[Minimality]]

### 4.1 Two Non-Equivalent Definitions (STATUS §4.6, Preserved Verbatim)

```text
(M1)  Q(T,S,C,K)=established  ∧  ∄ S′ ⊊ S : Q(T,S′,C,K)=established
(M2)  Q(T,S,C,K)=established  ∧  ∀ x ∈ S  : Q(T, S∖{x}, C, K)=not established
```

**M1 ⟺ M2 only when Q is monotonic.** The existence of the Q7 Contradiction category indicates that Q is non-monotonic (adding information can break establishment), so the two definitions diverge in practice.

**New criterion introduced this round**: Appendix B §4.3 records [[Explicit Value-Add]] as a **marginal quantity** whose result depends on order. Marginality naturally falls on the M2 side.

**If M2 is adopted**: MCS non-uniqueness has three sources — (1) multiple minimal solutions under the same K (《Necessity》 v3 §7.7); (2) changing K changes the MCS (this round); (3) different selection orders produce different results (this round).

### 4.2 MCS Notation

```text
MCS : ⟨T, I, C, K⟩ → 𝒫(I)
S = MCS(T | I, C, K)
```

**The type can be written** (codomain is the power set of I because the solution is non-unique; if uniqueness were assumed it would be a subset-valued mapping with a unique result, but uniqueness has already been rejected).

**However, it depends on the three gaps in §2.2.** The notation is valid; the definition is not.

---

## 5. Current Status of the First Equation

### 5.1 Original Equation

```text
A  --θ-->  I(θ)  --P-->  S
A = Anchor Ontology,  θ = Topic,  I(θ) = Invariant corresponding to the current Topic,  P = Anchor Point
```

### 5.2 Parts Rejected in This Round

| Item | Status |
|---|---|
| `A` in the equation | **Invalid.** Anchor Ontology was determined this round to be **methodology**, not a unit. It cannot be an item in the equation. The methodology generates this equation; it is not inside it. |
| `I(θ) ↔ θ` | **Withdrawn.** The Invariant is now defined as a multidimensional domain unit that “neither corresponds nor judges.” |
| `I(θ₁) → I(θ₂)` (the Invariant changes when the Topic changes) | **Direction reversed.** The Invariant itself does not change; what changes is which subset is selected. |
| `P` = [[Anchor Point]] | Retained |

### 5.3 What Remains

```text
θ  ∈ Θ                        Topic                                  ✓
Inv : Set                     Invariant (unchanging multidimensional domain unit)  ✓ type determined
sub : Θ → 𝒫(Inv)             subset selection (what changes with Topic)            ✓ type writable
P : ［Missing］                Anchor Point                            type undetermined
```

**`sub` is the only type-determined element rescued from the remains of the first equation this round.**

### 5.4 Symbol Conflict Between P and K 【Unresolved】

If K = the Anchor Point of the Topic (this round), while P = [[Anchor Point]] in the first equation, then **K and P are the same thing**.

However, P in the first equation has the role of “the Topic locating into structure,” while K in the second equation has the role of “the criterion.” **The same symbol would be doing different things in the two equations.**

This draft does not resolve the conflict; it is listed as a gap.

---

## 6. The Two Chains — The Clearest Part at the Type Level This Round

### 6.1 [[Narrative Chain]]

```text
Narr : sequential dependency relation
Narr ⊆ U × U                  U is the set of information units
```

Properties (determined this round):

- **Does not judge right or wrong.** It expresses only “this comes after that, relying on that.”
- It has **order only**, not temporal order — the index is `n ∈ ℕ`, not a timestamp.
- **Linear cost**: fixed cost per step; chain length is the cost.

**Writable.** Dependency is a standard binary relation, so there is no type dispute.

**Undetermined**: stopping condition. This round it was initially set to “value-add goes to zero,” then became invalid after the criterion changed to “dependency.” The proposer later supplied “according to the relationship between the Narrative Chain and Logic Chain,” which must be written as **dynamics** (alternation) rather than a definition (mutual definition), otherwise it becomes circular. **The dynamics have not been formalized in this draft.**

### 6.2 [[Logic Chain]]

```text
Align : U × Θ × Θ ⇀ 𝔹
Align(x, θ₁, θ₂) = established  ⟺  x exposes the same substructure under θ₁ and θ₂
```

**Basis**: The proposer stated this round: “For each piece of information, under different Topics, whether the same substructure can be found for alignment.”

**Type determined; writable.** This is the most formalized item among the additions in this round.

The definition of the **“reasonable observation node”** can therefore also be written:

```text
reasonable(θ) ⟺ ∃ x ∈ U, ∃ θ' ≠ θ : Align(x, θ, θ') = established
```

**Cost**: pairwise cross-topic comparison; with m Topics, O(m²). **This follows from the definition; it is not an implementation limitation.**

### 6.3 Asymmetry of the Two Chains (Type Level)

| | Type | Cost | Quantity |
|---|---|---|---|
| Narr | `⊆ U × U`, binary relation | Linear | Single |
| Align | `U × Θ × Θ ⇀ 𝔹`, ternary partial function | Quadratic | Multiple when there are multiple Topics |

**The asymmetry comes from the types themselves, not from an additional setting.** This is the substantive result of this round.

---

## 7. [[Drift]]

### 7.1 Definition (Final Version This Round)

```text
drift ⟺ Narr cannot be continued when the Topic shifts (Construction cannot be completed)
```

**Withdrawn**: using “whether the party declares a change” as the antecedent (Appendix A §4.3). The criterion was changed to observing Narr without asking the person.

**Withdrawn**: “all Logic Chains fail ⟹ [[Drift]].” Reason: subsets and subnodes are observed entities and are not lost; a broken Logic Chain only means that this comparison failed.

### 7.2 Type

```text
drift : 𝔹                     binary; judges “this moment”
```

Restoration does not affect binary typing — restoration happens later and is a judgment at another moment.

### 7.3 Unresolved Exhaustiveness Problem

If, when continuation fails, the construction can **switch Invariants and become established again** (Appendix B §11.6), then the strict definition of Drift should be:

```text
drift ⟺ ∀ v ∈ Inv_array : Narr cannot be continued under v
```

**This requires exhaustively enumerating `Inv_array`.** The exhaustiveness problem has not disappeared; it has merely moved from the Logic Chain to the Invariant array.

**A protection clause is also required**: failure to find something ≠ non-existence (Unknown ≠ Unexplained, 《Complete Interpretation Report》§22). Without this clause, verification of `∀` would treat “not finished checking” as “none are established.”

---

## 8. Missing Materials — Checklist

Sorted by blocking severity. **Without the first three items, Q and MCS cannot move from notation to definition.**

### 8.1 Blocking Level

| # | Missing item | Why it blocks | Minimum requirement to complete |
|---|---|---|---|
| **1** | **Type of K**: value / point / function, choose one | Q’s parameter position requires a definite type. All three have appeared and are mutually incompatible. | Choose one. If function, specify domain and codomain; if point, explain how the point participates in judgment. |
| **2** | **Type of T**: what is the target structure? | Q’s first parameter. “Structure” has no type anywhere in the full document set. | Is T a subset of I? A relation on U? A proposition? All are possible; one must be selected. |
| **3** | **Type of C**: what is Context? | Q’s third parameter. All documents only use the name. | Is it a parameter set? Another subset of I? An index? |

### 8.2 Structural Level

| # | Missing item | Impact |
|---|---|---|
| 4 | **Codomain of Q**: binary or ternary | §2.1. Three values are needed to express “not finished checking,” while §7.3 relies on that. |
| 5 | **Whether P and K are the same** | §5.4. If they are, the first and second equations must be merged and rewritten; if not, their relationship must be specified. |
| 6 | **Whether a “descriptive unit” can occupy a parameter position** | The proposer stated this round that “these are all descriptive units, not fixed units.” A description cannot occupy a parameter position. If this stance is adopted, all formalization must be downgraded to **illustrative notation**, not definition. |
| 7 | **Whether minimality uses M1 or M2** | §4.1. This round’s marginality argument leans toward M2. |
| 8 | **Dynamics of the two chains** | §6.1. The stopping condition must be written as alternation; otherwise the system is circular. No formalization currently exists. |

### 8.3 Deferrable Level

| # | Missing item | Why it can be deferred |
|---|---|---|
| 9 | Forms of relation (echo / composability / contrast / antithesis) | Types cannot be compared on a single scale, so they should not enter one unified metric. They can be labels of `U × U → Type` and do not block Q. |
| 10 | “Degree measures” (how much established, how much drift, how much value-add) | This round encountered three blocking cases. The time-point distinction in §7.2 makes binary judgment provisionally sufficient. |
| 11 | Relationship between the Qualification layer and Establishment layer | Unresolved in STATUS §4.7. It does not block this draft, but determines the semantic ownership of Q. |
| 12 | Enumeration method for Inv_array | §7.3. This is a usability issue for the criterion, not a type issue. |

---

## 9. Current Summary

**Expressions whose types can be determined:** `S ⊆ I`, `sub : Θ → 𝒫(Inv)`, `Narr ⊆ U × U`, `Align : U × Θ × Θ ⇀ 𝔹`, `reasonable(θ)`, `exists_theme : Θ ⇀ 𝔹`, `drift : 𝔹`.

**Expressions that are notation only, without definitions:** `Q`, `MCS`. The reason is that three of the four parameter types remain undetermined (§8.1).

**Removed from the first equation:** `A` (methodology does not enter the equation), `I(θ) ↔ θ` (correspondence withdrawn).

**Honest assessment:** The formalization level of the two chains produced this round is **higher than** that of the core Q/MCS. The core equations are currently empty shells — exactly the condition referred to by STATUS §4.1 as “content parasitism.” This draft has not changed that state; it has only marked the gaps.

**Implication for publication:** The current material is insufficient to support the core chapter of a formalization paper. What it can support is an article on **problem definition and type analysis** — that is honest and valuable, but it is not “the mathematical representation of Construction.”

---

**Document version**: Draft v0.1  
**Nature**: New draft; does not replace any existing document  
**Next step**: Complete the three items in §8.1. Once all three are supplied, Q can move from notation to definition.
