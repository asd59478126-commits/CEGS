# GLOBAL CODE CONSTRUCTION STATE

### Technical Specification — Normative Framework

**Version 1.0**

---

## Part 1 — Scope

### 1.1 Subject Matter

This specification defines the normative rules governing all code construction operations performed within a system, regardless of which Agent, tool, interface, or project executes the operation.

### 1.2 Applicability

This specification applies to any operation that places the system in one or more of the following states:

- construction
- inspection
- modification
- movement
- testing
- building
- isolation
- deletion

### 1.3 Binding Parties

This specification is binding upon:

- all Agents performing code operations
- all tools invoked during code operations
- all execution units participating in a construction process

### 1.4 Precedence

Where a conflict exists between a local optimization and a requirement of this specification, this specification takes precedence.

---

## Part 2 — Definitions

For the purposes of this specification, the following terms apply.

**2.1 Construction Unit**

The smallest system object that has an explicit Definition, can be located, can be acted upon, and has its own Condition of Validity.

**2.2 Explanation Unit**

The basis provided for locating, understanding, classifying, or evaluating a Construction Unit. An Explanation Unit may be shared across multiple Construction Units.

**2.3 Definition**

The explicit statement of the state that an operation is intended to establish.

**2.4 Action**

The actual operation performed on a specified Construction Unit.

**2.5 Condition of Validity**

The condition that must hold after an Action for the operation to be considered established.

**2.6 Baseline**

A comparable record of the system state prior to modification, against which post-modification state can be evaluated.

**2.7 Impact Scope**

The set of Construction Units, dependencies, runtime paths, and Conditions of Validity that an Action may affect.

**2.8 Functional Evidence**

A reproducible and verifiable record of actual system state. Functional Evidence must be obtained from runtime behavior, reachable dependencies, integration results, end-to-end results, actual data flow, actual invocation, or reproducible build or execution results.

**2.9 State**

The determination assigned to a Construction Unit or operation following inspection or verification. Valid states are defined in Part 7.

**2.10 Execution Unit**

A bounded operation consisting of one or more Construction Units that share a single coherent Construction objective.

**2.11 Indexability**

The property of a Construction Unit whereby the system can locate its existence, confirm its identity, trace its relationships, reference it again, and restore or re-activate it when required.

---

## Part 3 — Construction Unit

### 3.1 Formation

A Construction Unit shall be formed by the following structure:

**Definition → Explanation Unit → Action → Condition of Validity**

Each element shall be explicitly stated. No element shall substitute for another.

### 3.2 Distinctness

A Construction Unit shall remain distinguishable from all other Construction Units. Two objects must not be merged into a single Construction Unit solely because they:

- exist in the same file
- share the same name
- use the same Explanation Unit
- serve the same function

### 3.3 Merging Condition

Two operations may be merged into a single Execution Unit only when their Definition, target object, Action, and Conditions of Validity are equivalent.

### 3.4 Explanation Unit Reuse

An Explanation Unit may be reused across multiple Construction Units. Reuse of an Explanation Unit does not imply identity of Construction Unit, identity of Action, or identity of Condition of Validity. The Action and Condition of Validity of each Construction Unit shall be determined independently.

### 3.5 Indexability Requirement

Any Construction Unit that must be located, referenced, restored, or understood by the system, an Agent, a tool, or a future maintainer shall satisfy the Indexability condition. A Construction Unit that exists but cannot be reliably located or traced shall not be considered fully established.

---

## Part 4 — Baseline

### 4.1 Establishment Requirement

Prior to any operation that may affect existing functionality, dependencies, data, or runtime state, a Baseline shall be established.

### 4.2 Minimum Baseline Content

A Baseline shall enable the system to determine:

- which Construction Units existed prior to modification
- which necessary dependencies existed prior to modification
- whether principal functions were valid prior to modification
- whether important data existed prior to modification
- whether important runtime paths existed prior to modification

### 4.3 Post-Modification Comparison

The post-modification state shall be compared against the Baseline. A modification shall not be treated as established without this comparison where functional conditions are at stake.

### 4.4 Absence of Baseline

If a reasonable Baseline cannot be established, the operation shall not be treated as low-impact by default. The Impact Scope determination required under Part 6 shall proceed on the assumption of potentially high impact.

---

## Part 5 — Operation Rules

### 5.1 Inspection

**5.1.1** Inspection is an independent Execution Unit. It shall not be treated as a preliminary step of modification.

**5.1.2** An Inspection operation shall conform to the following structure:

- **Definition:** obtain a specified state
- **Explanation Unit:** the concrete object being inspected
- **Action:** search, read, compare, trace, or verify
- **Condition of Validity:** obtain an actual result sufficient to support the current determination

**5.1.3** Inspection results shall be classified as one of the following:

- CONFIRMED
- CONFLICT
- UNKNOWN / UNVERIFIED

**5.1.4** Interpretation, naming, inference, and speculation obtained during Inspection shall not be promoted to Functional Evidence.

### 5.2 Modification

**5.2.1** A Modification operation shall conform to the following structure:

- **Definition:** establish a specified new state
- **Explanation Unit:** the Construction Unit being modified
- **Action:** add, rewrite, refactor, or adjust
- **Condition of Validity:** the new state is established without unverified destruction of necessary relationships

**5.2.2** Completion of a Modification Action establishes only ACTION COMPLETED. It shall not be treated as establishing FUNCTION CONFIRMED.

**5.2.3** A Modification shall not be considered established solely on the basis that the Action succeeded without error.

### 5.3 Movement

**5.3.1** A Movement operation shall conform to the following structure:

- **Definition:** change location or active status
- **Explanation Unit:** the Construction Unit being moved and its necessary relationships
- **Action:** move, relocate, or isolate
- **Condition of Validity:** the new location is identifiable, indexable, traceable, and necessary dependencies remain available

**5.3.2** Movement shall not be treated as implying any of the following unless separately established:

- deletion
- invalidation
- disappearance of dependency
- loss of function
- preservation of function

**5.3.3** Each of the states listed in 5.3.2 shall be established by independent inspection or verification.

### 5.4 Deletion

**5.4.1** A Deletion operation shall conform to the following structure:

- **Definition:** permanently remove a specified Construction Unit
- **Explanation Unit:** the object to be deleted and its necessary relationships
- **Action:** delete
- **Condition of Validity:** sufficient evidence confirms that the Construction Unit is no longer a necessary state and that its removal does not violate overall validity

**5.4.2** The following shall not independently justify a Deletion determination:

- failure to locate the object
- absence of a direct reference
- a name that appears to indicate legacy status
- prior movement or isolation
- absence of tests
- an Agent's determination that the object is no longer needed

**5.4.3** A Deletion determination shall be supported by affirmative evidence that the object is no longer necessary and that removal does not break established Conditions of Validity elsewhere in the system.

---

## Part 6 — Impact Scope and Verification

### 6.1 Verification Trigger

Verification strength shall not be chosen arbitrarily by the Agent. The standard process is:

1. Define the Action
2. Establish or confirm the Baseline
3. Inspect the Impact Scope
4. Identify affected Construction Units and Conditions of Validity
5. Determine the Verification Level
6. Perform the corresponding verification
7. Obtain Evidence
8. Update State

### 6.2 Impact Scope Determination

An Inspection shall determine at minimum:

- whether only structure or location is being changed
- whether local behavior may change
- whether cross-module or runtime relationships may change
- whether a principal system path or overall behavior may change

If the Impact Scope cannot be determined, the operation shall not be assigned a lower Verification Level on that basis alone.

When Impact Scope is unknown:

**UNKNOWN / UNVERIFIED → further Inspection → determine Verification Level**

### 6.3 Verification Levels

**Level 0 — Structural Operation**

The operation changes only location, ordering, or another state verified not to affect functional Conditions of Validity. Established primarily through structural, index, and dependency inspection.

**Level 1 — Local Behavioral Operation**

The operation may affect a single module, function, schema, command, or local dependency. Direct Functional Evidence corresponding to the affected Construction Unit is required.

**Level 2 — Integrated Behavioral Operation**

The operation may affect multiple modules, runtime dependencies, databases, filesystems, external binaries, or cross-module relationships. Integration-level evidence is required.

**Level 3 — Global Behavioral Operation**

The operation may change core state, principal runtime paths, the core dependency graph, or major end-to-end paths. End-to-end evidence, or equivalent complete Functional Evidence, is required.

The following assignments are not automatic:

- Movement is not automatically Level 0
- Modification is not automatically Level 1
- A successful build does not automatically satisfy all verification requirements

Verification Level shall be determined by the question:

> **Which Conditions of Validity may actually be affected by this Action?**

### 6.4 Evidence Coverage

A verification result establishes only the Conditions of Validity it actually covers.

Successful compilation supports the build condition. It does not establish runtime validity, integration validity, or end-to-end validity.

A file satisfying Indexability supports the indexing condition. It does not establish functional correctness, runtime invocation validity, or overall system validity.

Evidence coverage shall not be expanded automatically beyond what the verification actually demonstrates.

### 6.5 Return and Redefinition

The process defined in 6.1 is not an irreversible linear sequence.

If Inspection reveals any of the following, the system shall return to an earlier stage:

- an insufficient original Definition
- an incorrect identification of the target object
- an Impact Scope exceeding the original Definition
- a previously unknown necessary dependency
- a previously unknown Condition of Validity
- a previously unrecognized conflict

The return path is:

**Inspection → redefine → reconfirm Construction Unit → establish or revise Baseline → redetermine Impact Scope → proceed to Action and Verification**

**6.5.1** A return to an earlier stage shall not be treated as an implicit modification of the original Definition.

**6.5.2** If the Definition, target object, Action, or Condition of Validity changes materially, a new Construction Unit or Execution Unit shall be established.

**6.5.3** A new objective shall not be represented as the original objective. The state difference shall be preserved.

---

## Part 7 — State Management

### 7.1 Valid States

The following states are valid within this specification:

| State | Meaning |
|---|---|
| CONFIRMED | A specific Condition of Validity has been established by corresponding evidence |
| PARTIALLY CONFIRMED | Some but not all required Conditions of Validity have been established |
| ACTION COMPLETED | The Action has been performed; functional verification has not yet been obtained |
| FUNCTION UNVERIFIED | Required functional evidence has not yet been obtained |
| CONFLICT | Verification has produced mutually incompatible results |
| UNKNOWN / UNVERIFIED | Sufficient evidence cannot be obtained to determine the state |

### 7.2 State Binding

Every CONFIRMED determination shall correspond to a specific Condition of Validity and evidence capable of covering that condition. A local verification result shall not be used to mark multiple uncovered conditions as CONFIRMED.

### 7.3 State Substitution

The states defined in 7.1 shall not substitute for one another. In particular:

- ACTION COMPLETED shall not be written as CONFIRMED
- UNKNOWN / UNVERIFIED shall not be treated as nonexistence
- PARTIALLY CONFIRMED shall not be treated as CONFIRMED

### 7.4 UNKNOWN / UNVERIFIED Handling

UNKNOWN / UNVERIFIED does not require the entire system to stop.

While a Construction Unit is in UNKNOWN / UNVERIFIED state:

- non-destructive work that does not depend on the unknown condition may continue
- irreversible Actions shall not be performed solely on the basis of the unknown condition
- an unverified function shall not be represented as confirmed

### 7.5 CONFLICT Handling

When Conditions of Validity belonging to different Construction Units conflict, the Agent shall not select one arbitrarily.

The required process is:

1. Stop destructive Actions that may enlarge the conflict
2. Locate the conflicting Construction Units
3. Locate the conflicting relationships
4. Inspect the higher-level Definition
5. Let the explicit Definition determine the next Action

Overall explicit Definition takes precedence over local optimization.

---

## Part 8 — Concurrent Operations

### 8.1 Independence Condition

Different Construction Units may be processed concurrently. Operations shall not automatically be treated as independent when they:

- act on the same Construction Unit
- modify the same relationship
- share potentially conflicting Conditions of Validity
- may overwrite the same state
- are based on different versions or different Baselines

### 8.2 Pre-Concurrency Inspection

Before concurrent operations proceed, the following shall be inspected:

- the Construction Units involved
- their Baselines
- their dependencies
- their Conditions of Validity
- their state differences

If interaction between concurrent operations cannot be determined, Inspection takes priority over proceeding.

### 8.3 Change Boundary

A single Execution Unit shall, as far as practicable, establish one coherent Construction objective. If one operation simultaneously combines functional modification, refactoring, cleanup, movement, dependency adjustment, or data migration, the operation shall be decomposed into separate Execution Units unless an explicit Definition establishes that they must succeed together.

If Inspection materially changes the original Definition, target object, Action, or Condition of Validity, the original Execution Unit shall not continue carrying the new objective. A new Construction or Execution Unit shall be established.

### 8.4 Independent Verification

The Agent that produces a modification may perform verification. However, its self-assessment shall not automatically constitute independent evidence.

For Level 2 and Level 3 operations, and for any operation assessed as high-risk, verification shall preferentially use:

- reproducible scripts
- deterministic checks
- independent tests
- rules-based analysis
- verification by a separate Execution Unit
- human review

This requirement exists to reduce the risk that generation and verification rely on the same incorrect assumption.

---

## Part 9 — Global Prohibitions

The following substitutions are prohibited under this specification:

| Prohibited Substitution |
|---|
| Naming in place of function |
| Explanation in place of evidence |
| Dependency relationship in place of functional utility |
| Local testing in place of uncovered global functionality |
| Movement in place of a Deletion determination |
| ACTION COMPLETED in place of FUNCTION CONFIRMED |
| Agent self-assessment in place of required independent verification |
| UNKNOWN / UNVERIFIED in place of nonexistence |
| Local optimization in place of overall validity |
| A new objective represented as the original objective |
| Unconfirmed Impact Scope treated as Level 0 |
| Uncovered verification treated as an established Condition |
| Local evidence treated as establishing overall validity |
| A materially changed Definition treated as a valid continuation of the original Execution Unit |

---

## Final Requirement

The governing question for any code construction operation is not:

> *"Does the code run?"*

The governing question is:

> *"Has the state required by this Action been established by evidence that corresponds to its Impact Scope and actually covers the relevant Condition of Validity?"*