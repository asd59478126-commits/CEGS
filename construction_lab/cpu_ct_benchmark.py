#!/usr/bin/env python3
from dataclasses import dataclass
from time import perf_counter

@dataclass(frozen=True)
class CT:
    cid: str
    state: str
    condition_ref: str | None = None

CTS = {
    "1": CT("1", "ESTABLISHED"),
    "2": CT("2", "NOT_ESTABLISHED", "1"),
    "3": CT("3", "ESTABLISHED"),
    "4": CT("4", "ESTABLISHED"),
    "5": CT("5", "UNKNOWN", "6"),
    "6": CT("6", "ESTABLISHED"),
}

def ct_eval(cid, cts, visiting=None):
    if visiting is None:
        visiting = set()
    if cid in visiting:
        return "UNKNOWN"
    ct = cts[cid]
    if ct.condition_ref is None:
        return ct.state
    visiting.add(cid)
    ref_state = ct_eval(ct.condition_ref, cts, visiting)
    visiting.remove(cid)
    if ref_state == "NOT_ESTABLISHED":
        return "NOT_ESTABLISHED"
    if ref_state == "UNKNOWN":
        return "UNKNOWN"
    return ct.state

def main():
    rounds = 100_000
    t0 = perf_counter()
    for _ in range(rounds):
        results = {cid: ct_eval(cid, CTS) for cid in CTS}
    total_ms = (perf_counter() - t0) * 1000
    avg_us = total_ms * 1000 / rounds
    print("=== Construction CPU micro-benchmark ===")
    print(f"CT count                : {len(CTS)}")
    print(f"evaluation rounds       : {rounds:,}")
    print(f"total CPU time          : {total_ms:.3f} ms")
    print(f"average per round      : {avg_us:.3f} us")
    print("final states            :", results)
    print()
    print("This measures deterministic CPU rule evaluation only.")
    print("It is not an LLM/API latency measurement.")

if __name__ == "__main__":
    main()
