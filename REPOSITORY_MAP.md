# CEGS Repository Map

> 目的：把 CEGS 的「研究理論、歷史實驗、實驗審計、可執行程式與封裝副本」分開，使 repository 可以被正確閱讀，而不把不同研究階段混成同一套結論。

## 1. Repository 定位

CEGS（Constrained Event Generation Space）目前應視為 Construction 研究歷程中的公開工程／實驗節點，而不是 Construction 理論本身。

目前閱讀時採以下層次：

```text
Construction theory
        ↓
MCS / minimum necessary structure
        ↓
Current formalization
        ↓
Historical CEGS / Qualification work
        ↓
Stage 1 experiment + methodological audit
```

README 與 EXECUTIVE_SUMMARY 已明確區分 Construction、MCS、CEGS，以及歷史 Stage 1 的研究地位。

## 2. 建議閱讀順序

### A. 先看 repository 全貌

1. `README.md` — 專案定位、研究狀態、Stage 1 限制。
2. `EXECUTIVE_SUMMARY.md` — 給研究者快速確認目前結論與不主張事項。
3. `GETTING_STARTED.md` — 執行與進入點。

### B. 再看目前 Construction 理論

4. `construction-framework.md` — 目前較完整的 Construction 概念鏈：TOKN、Direction、Invariant、Alignment、Order、Narrative Chain、Trace、Current Reality。
5. `構築 — 形式化草稿 型別優先.md` — 目前型別優先的形式化草稿；明確標出 T/C/K/P 等型別缺口，不應視為已完成定義。
6. `構築單位呈現條件與形式化研究.md` — Construction 單位與表示條件的研究背景。
7. `構築 — 形式化草稿 型別優先.md` 與其他形式化文件有衝突時，先保留差異，不自行合併成單一答案。

### C. 歷史／實驗層

`construction_lab/` 是實驗區，不是 Construction 理論的唯一權威來源。

核心內容：

- `events.json` — 固定事件資料。
- `questions.json` — 固定問題資料。
- `gold_answers.json` — 評估答案資料。
- `stage1_evaluator.py` — Stage 1 評估器。
- `baseline_representation.py` — baseline 表示。
- `construction_representation.py` — Construction 表示。
- `stage1_results.json` — 歷史結果。
- `stage1_question_matrix.md` — 題型矩陣。
- `RUN_LOG.md` — 執行紀錄。

### D. 審計層

以下文件應被視為「Stage 1 方法學審計」群組，不與原始結果混讀：

- `STAGE1_DEBUG_REPORT.md`
- `STAGE1_DEBUG_TRACE.md`
- `STAGE1_REPAIR_REPORT.md`
- `RESULTS.md`

目前 repository 的正式敘述是：Stage 1 結果可重現，但原始 Construction-specific inference 因 source-level / methodological 問題不能直接作為 Construction 理論驗證。

### E. 可攜式實驗封裝

`construction_lab/construction_stage1_package/` 是供本機／Claude Code 執行的封裝版本。它包含：

- `CLAUDE_TASK.md`
- `README.md`
- `START_HERE.txt`
- `stage0_token_count.py`
- `cpu_ct_benchmark.py`

這個目錄應理解為「可攜式實驗包」，不是另一套獨立理論。

### F. 研究紀錄

`construction_lab/研究紀錄/` 保存 Construction Lab 的研究紀錄；與程式、原始資料及審計文件分開閱讀。

## 3. 根目錄目前應保持的文件角色

| 文件 | 角色 | 狀態 |
|---|---|---|
| `README.md` | 對外總入口 | 主入口 |
| `EXECUTIVE_SUMMARY.md` | 研究執行摘要 | 主摘要 |
| `GETTING_STARTED.md` | 執行入口 | 操作文件 |
| `construction-framework.md` | Construction 理論框架 | 理論工作文件 |
| `構築 — 形式化草稿 型別優先.md` | 型別優先形式化 | 草稿 |
| `構築單位呈現條件與形式化研究.md` | 表示條件研究 | 研究文件 |
| `構築_附錄C_展開的相對性與錨點必要性_20260907.md` | 附錄／局部推導 | 研究附錄 |
| `構築_20260908_檔案庫完整閱讀紀錄.pdf` | 2026-09-08 研究閱讀紀錄 | 歷史／證據紀錄 |
| `資格論.md` | Qualification 理論 | 歷史／相關理論 |
| `construction_lab/` | 實驗與研究材料 | 實驗區 |

## 4. 研究狀態分層

不要把以下四種狀態混在一起：

**Established / 可確認**
- repository 中的歷史程式、資料與文件確實存在。
- Stage 1 的歷史結果具有可重現性。
- Stage 1 已接受 source-level / methodological audit。

**Research candidate / 理論候選**
- Invariant、Logic Chain、Narrative Chain。
- Correspondence、Symmetry、Alignment 的部分關係。
- MCS 的形式化方向。

**Unresolved / 尚待決定**
- Q 的二值／三值語義。
- T、C、K、P 的正式型別與相互關係。
- MCS 最小性採 M1、M2 或其他定義。
- Narrative Chain 的停止條件與動力學。

**Not claimed / 明確不主張**
- Stage 1 已證明 Construction。
- Construction 必然提高模型正確率。
- Construction 必然節省 Token。
- MCS 已完成正式證明。
- CEGS 能自行決定公平、正當或治理結果。

## 5. 目前最重要的結構性整理

目前 repository 已經不是「單一實驗專案」的形態，而是三個不同時間層的集合：

```text
[Current Theory]
Construction / MCS / formalization

[Historical Experiment]
Qualification / Stage 1 / benchmark

[Evidence & Audit]
run logs / debug / repair / research records
```

因此後續新增文件時，優先標明它屬於哪一層，不要直接把新理論塞入歷史 Stage 1 目錄，也不要把 Stage 1 的歷史數值當成目前 Construction 的證據。

## 6. 一個重要的 repository hygiene 規則

Python 產生的 `__pycache__/` 與 `*.pyc` 不屬於研究證據，也不應進入版本控制。它們應由 `.gitignore` 排除。

研究證據應保存：

- 原始輸入資料；
- 明確版本的程式；
- evaluator；
- 結果 JSON／表格；
- run log；
- audit；
- 能解釋結果的研究紀錄。

不要用編譯快取代替上述任何一項。
