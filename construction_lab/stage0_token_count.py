#!/usr/bin/env python3
import argparse
import sys

CTS = [
    ("a1f3", "ASSERT",    "proj_atlas",   "assigned_to", "kobayashi",    "ESTABLISHED",     "2024-03-01", "2024-07-15", None),
    ("b2c9", "ASSERT",    "proj_atlas",   "depends_on",  "module_auth",  "ESTABLISHED",     "2024-03-01", None,         None),
    ("c7d1", "ASSERT",    "module_auth",  "part_of",     "platform_core","ESTABLISHED",     "2024-02-10", None,         None),
    ("d4e8", "ASSERT",    "kobayashi",    "located_in",  "office_osaka", "ESTABLISHED",     "2024-01-05", "2024-07-15", None),
    ("e9f2", "ASSERT",    "src_hr01",     "states",      "ct_a1f3",      "ESTABLISHED",     "2024-03-01", "2024-06-20", None),
    ("f5a7", "RETRACT",   "src_hr01",     "states",      "ct_a1f3",      "NOT_ESTABLISHED", "2024-06-20", None,         None),
    ("a8b3", "ASSERT",    "proj_atlas",   "assigned_to", "tanaka",       "UNKNOWN",         "2024-06-20", None,         "f5a7"),
    ("b1c4", "SUPERSEDE", "proj_atlas",   "assigned_to", "watanabe",     "ESTABLISHED",     "2024-07-15", None,         None),
    ("c6d2", "ASSERT",    "watanabe",     "located_in",  "office_tokyo", "ESTABLISHED",     "2024-07-15", None,         None),
    ("d3e5", "ASSERT",    "module_auth",  "depends_on",  "lib_crypto",   "ESTABLISHED",     "2024-02-10", None,         None),
    ("e7f9", "ASSERT",    "lib_crypto",   "supersedes",  "lib_legacy",   "ESTABLISHED",     "2024-01-20", None,         None),
    ("f2a1", "CORRECT",   "proj_atlas",   "part_of",     "platform_edge","NOT_ESTABLISHED", "2024-04-02", "2024-04-02", None),
    ("a5b8", "ASSERT",    "proj_atlas",   "part_of",     "platform_core","ESTABLISHED",     "2024-04-02", None,         None),
    ("b9c3", "ASSERT",    "src_pm02",     "states",      "ct_b1c4",      "ESTABLISHED",     "2024-07-15", None,         None),
    ("c4d7", "ASSERT",    "proj_atlas",   "depends_on",  "vendor_nexus", "UNKNOWN",         "2024-05-11", None,         "d3e5"),
    ("d8e1", "ASSERT",    "vendor_nexus", "located_in",  "region_apac",  "ESTABLISHED",     "2024-05-11", None,         None),
    ("e2f6", "RETRACT",   "module_auth",  "depends_on",  "lib_crypto",   "NOT_ESTABLISHED", "2024-08-03", None,         None),
    ("f7a4", "ASSERT",    "proj_atlas",   "assigned_to", "team_infra",   "UNKNOWN",         "2024-08-03", None,         "e2f6"),
    ("a3b6", "ASSERT",    "team_infra",   "part_of",     "org_platform", "ESTABLISHED",     "2024-01-01", None,         None),
    ("b6c8", "ASSERT",    "src_audit",    "states",      "ct_e2f6",      "ESTABLISHED",     "2024-08-03", None,         None),
]

STATE_ZH = {"ESTABLISHED":"目前成立", "UNKNOWN":"目前無法確認", "NOT_ESTABLISHED":"目前不成立"}
REL_ZH = {"assigned_to":"指派給", "depends_on":"依賴於", "part_of":"隸屬於", "located_in":"位於", "supersedes":"取代", "states":"宣稱"}
EVENT_ZH = {"ASSERT":"建立", "RETRACT":"依據失效撤回", "CORRECT":"記錄錯誤更正", "SUPERSEDE":"被取代"}

def render_a(ct, lang="zh"):
    cid, ev, s, r, o, st, vf, vt, cond = ct
    if lang == "en":
        text = f"{s} {r.replace('_',' ')} {o}, effective {vf}. Event type: {ev}; relation state: {st}."
        if vt: text += f" Ended {vt}."
        if cond: text += f" Its qualification depends on whether record {cond} is established."
        return text
    parts = [f"{s} {REL_ZH[r]} {o}，此關係於 {vf} 生效"]
    if vt: parts.append(f"，並於 {vt} 結束")
    parts.append(f"。此紀錄的事件類型為{EVENT_ZH[ev]}，該關係{STATE_ZH[st]}")
    if cond: parts.append(f"，其成立條件取決於編號 {cond} 的紀錄是否成立")
    parts.append("。")
    return "".join(parts)

def render_b(ct):
    cid, ev, s, r, o, st, vf, vt, cond = ct
    return f"CT|{cid}|{ev}|{s}|{r}|{o}|{st}|{vf}|{vt or '-'}|{cond or '-'}"

def render_c(ct, ref_map):
    cid, ev, s, r, o, st, vf, vt, cond = ct
    ref = ref_map.get(cond, "-") if cond else "-"
    return f"CT|{cid}|{ev}|{s}|{r}|{o}|{st}|{vf}|{vt or '-'}|{ref}"

def get_tokenizer(args):
    if args.hf:
        try:
            from transformers import AutoTokenizer
        except ImportError as e:
            raise RuntimeError("缺少 transformers，請先 pip install transformers") from e
        tok = AutoTokenizer.from_pretrained(args.hf)
        return f"HF:{args.hf}", lambda t: len(tok.encode(t, add_special_tokens=False))
    try:
        import tiktoken
    except ImportError as e:
        raise RuntimeError("缺少 tiktoken，請先 pip install tiktoken") from e
    enc = tiktoken.get_encoding(args.encoding)
    return f"tiktoken:{args.encoding}", lambda t: len(enc.encode(t))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--encoding", default="o200k_base")
    p.add_argument("--hf", default=None)
    p.add_argument("--lang", choices=("zh","en"), default="zh")
    args = p.parse_args()
    name, count = get_tokenizer(args)
    ref_map = {}
    for i, ct in enumerate(CTS):
        if ct[8]: ref_map[ct[8]] = f"<REF-{min(i, 16)}>"
    texts_a = [render_a(c, args.lang) for c in CTS]
    texts_b = [render_b(c) for c in CTS]
    texts_c = [render_c(c, ref_map) for c in CTS]
    tot_a = sum(count(t) for t in texts_a)
    tot_b = sum(count(t) for t in texts_b)
    tot_c = sum(count(t) for t in texts_c)
    frame_now = 0
    frame_ideal = 0
    for ct in CTS:
        cid, ev, s, r, o, st, vf, vt, cond = ct
        for elem in (ev, r, st):
            frame_now += count(elem)
            frame_ideal += 1
        frame_now += count("CT") + 9 * count("|")
        frame_ideal += 1 + 9
    saving = frame_now - frame_ideal
    reduction = (tot_a - tot_b) / tot_a
    frame_ratio = frame_now / tot_b
    l3_ceiling = saving / tot_b
    print(f"tokenizer            : {name}")
    print(f"render language       : {args.lang}")
    print(f"CT 筆數              : {len(CTS)}")
    print()
    print(f"L2-a 總 token        : {tot_a:6d}")
    print(f"L2-b 總 token        : {tot_b:6d}")
    print(f"L2-c 總 token        : {tot_c:6d}")
    print()
    print(f"L2-b 相對 L2-a 縮減   : {reduction:6.1%}   [門檻 25%]")
    print(f"框目前佔 L2-b 比例    : {frame_ratio:6.1%}")
    print(f"L3 理論上限（可省）   : {l3_ceiling:6.1%}   [門檻 10% / 25%]")
    print()
    if reduction < 0.25:
        print(">> L2 判定：序列化無效益 → 未通過")
    else:
        print(">> L2 判定：token 門檻通過（正確率另測）")
    if l3_ceiling < 0.10:
        print(">> L3 判定：目前僅作單次量測結果，不在此直接定案")
    elif l3_ceiling < 0.25:
        print(">> L3 判定：待跨 tokenizer / language 補測")
    else:
        print(">> L3 判定：待跨 tokenizer / language 補測")
    print()
    print("--- sample ---")
    print("L2-a:", texts_a[6])
    print("L2-b:", texts_b[6])
    print("L2-c:", texts_c[6])

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
