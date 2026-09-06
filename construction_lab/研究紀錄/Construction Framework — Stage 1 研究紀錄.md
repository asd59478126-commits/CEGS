# Construction Framework — Stage 1 研究紀錄

**紀錄日期：2026-09-06**  
**階段：Stage 1 — L1 Representation Layer**  
**研究狀態：正式執行完成，進入研究解釋階段**

---

## 1. 本階段研究目的

Stage 1 的目的，是比較 Baseline（D）與 Construction（C1）在相同事件、相同問題、相同 evaluator 下的表現差異。

本階段不是測試 LLM 抽取能力，也不是測試 token 壓縮，而是測試：

> 當資訊需要透過顯式的 establishment、condition 與 relation 結構維持其成立狀態時，Construction representation 是否能在特定結構性任務中提供 Baseline 不具備的能力。

因此，本階段的核心比較為：

`Construction (C1) ↔ Baseline (D)`

尤其觀察：

`Dependency / Premise Failure Propagation`
以及
`Multi-hop Dependency`

---

## 2. 固定研究資料

### Events

共建立：

**75 筆人工設計事件**

事件由人工建立，不使用 LLM 進行抽取。

涵蓋：

- ASSERT
- RETRACT
- CORRECT
- Direct Fact
- Temporal
- Retraction
- Correction
- Dependency
- Multi-hop
- Unknown
- Contradiction
- Current State
- Historical State

### Questions

共：

**96 題**

固定分布：

| 類別 | 題數 |
|---|---:|
| Q1 Direct Fact | 10 |
| Q2 Temporal | 10 |
| Q3 Retraction | 12 |
| Q4 Dependency / Premise Failure Propagation | 16 |
| Q5 Multi-hop | 12 |
| Q6 Unknown | 8 |
| Q7 Contradiction | 8 |
| Q8 Correction | 8 |
| Q9 Current State | 8 |
| Q10 Historical State | 4 |
| **合計** | **96** |

Gold Answer 在正式測試前封存。

---

## 3. 實驗系統

### Baseline D

使用一般時間／事實結構處理事件與查詢。

### Construction C1

額外加入：

- `establishment_state`
- `condition_ref`
- condition propagation
- dependency relation handling

C1 的目的不是增加一般語義，而是明確表示：

> 某個構造是否成立、其成立依據為何，以及依據失效時構造如何受到影響。

---

# 4. 第一輪 Stage 1 執行

第一輪執行：

- 75 Events：通過
- 96 Questions：通過
- Schema Validation：通過
- Gold Answer Integrity：通過

初始結果：

| 指標 | D | C1 |
|---|---:|---:|
| Overall Accuracy | 46.88% | 19.79% |
| Q1 | 60% | 0% |
| Q4 | 31.25% | 0% |
| Q5 | 16.67% | 0% |
| Q9 | 75% | 0% |

第一眼看起來像是 C1 全面失敗。

但此結論沒有成立。

---

# 5. 第一輪 Debug

對以下四題進行 end-to-end trace：

- Q1-01
- Q4-04
- Q5-01
- Q9-01

追蹤：

`event`
→ `representation`
→ `establishment_state`
→ `condition_ref`
→ `propagation`
→ `query resolution`
→ `answer`
→ `evaluator`

結果：

4 / 4 題都不是在 Construction representation 或 condition propagation 階段首先失敗。

共同的第一個錯誤位置為：

**Answer Format**

C1 內部使用：

- `ESTABLISHED`
- `NOT_ESTABLISHED`
- `UNKNOWN`

但 evaluator / gold-answer 所要求的是依問題語義表達的答案，例如：

- YES
- NO
- UNKNOWN
- 或相應的語義答案

因此 C1 的內部狀態雖然已正確計算，卻沒有正確轉換為問題要求的答案表示。

---

# 6. 規格違反與修正

第一輪報告曾自行加入兩條不存在於研究規格中的條件：

1. C1 overall accuracy > 50%
2. C1 Q4 accuracy > D Q4 accuracy

重新讀取封版規格 `stage1_schema.md` 後確認：

**上述兩條並非正式研究 gate。**

原始規格要求的是：

- 記錄 Overall Accuracy
- 記錄 Q4 Accuracy
- 記錄 UCR
- 記錄 Contradiction Rate
- 記錄 CPU / e2e 等伴隨指標
- 比較 C1 與 D
- 若 C1 > D，才有資格進一步討論 Construction-specific effect

因此已完成以下修正：

- 移除自行增加的 success criteria
- 不修改 benchmark
- 不修改 gold answers
- 不修改 scoring rules
- 不修改 threshold
- 在 `RUN_LOG.md` 與 `RESULTS.md` 留下規格修正紀錄

這次規格錯誤本身也保留為 research provenance。

---

# 7. Implementation Bug

確認主要問題：

**`construction_representation.py` 中的 answer mapping 缺失。**

問題表現為：

所有相關 `_answer_q*()` 方法直接返回內部：

`establishment_state`

而沒有將其轉換為問題要求的 semantic answer。

因此：

> C1 的結構計算並沒有首先失敗，失敗的是「內部狀態 → 最終語義答案」的介面層。

因此第一輪：

`C1 = 19.79%`

不能當作 Construction 的研究結果。

第一輪正式狀態改為：

**Implementation Invalid / Pending Repair**

而不是：

**Construction Fail**

---

# 8. 最小修復

修復目標：

只修復必要的 answer semantic mapping。

修改：

`construction_representation.py`

具體內容：

- 新增 `_map_establishment_to_semantic_answer()`
- 更新 7 個 `_answer_q*()` 方法
- 約 30 行程式碼

沒有修改：

- `events.json`
- `questions.json`
- `gold_answers.json`
- `stage1_schema.md`
- `stage1_question_matrix.md`
- scoring rules
- benchmark 數量
- 題目分布

修復完成後重新執行完整：

**75 Events × 96 Questions**

---

# 9. 修復後 Stage 1 結果

## C1 Overall

修復前：

**19.79%**

修復後：

**54.17%**

提升：

**+34.38 percentage points**

---

## 各核心類別

| 類別 | 修復前 | 修復後 | 變化 |
|---|---:|---:|---:|
| Q1 Direct Fact | 0% | 80% | +80pp |
| Q4 Dependency | 0% | 31.25% | +31.25pp |
| Q5 Multi-hop | 0% | 58.33% | +58.33pp |
| Q9 Current State | 0% | 62.50% | +62.50pp |

這證明第一輪的 C1 低分主要確實來自 answer-format implementation bug，而非單純的 Construction reasoning failure。

---

# 10. C1 vs D 最終比較

| 類別 | Baseline D | Construction C1 | 差異 |
|---|---:|---:|---:|
| Q1 Direct Fact | 60% | **80%** | **+20pp** |
| Q4 Dependency | 31.25% | 31.25% | 0pp |
| Q5 Multi-hop | 16.67% | **58.33%** | **+41.66pp** |
| Q8 Correction | 62.50% | **75%** | **+12.50pp** |
| Q9 Current State | **75%** | 62.50% | **-12.50pp** |

---

# 11. 最重要的正向結果：Q5 Multi-hop

Q5：

Baseline D：

**16.67%**

Construction C1：

**58.33%**

差異：

**+41.66pp**

這是目前 Stage 1 最明確的 Construction-specific 訊號。

其研究意義是：

> 在本測試集的 Multi-hop dependency task 中，顯式 Construction representation 顯示出維持跨事件依賴關係的能力優勢。

換言之：

Baseline 可以處理部分單點資訊，但當問題需要：

`A → B → C → ...`

這種多跳結構時，C1 表現明顯較高。

這支持一個暫定研究假說：

> **Construction 的價值可能不是普遍地提高所有問答準確率，而是在需要維持跨事件結構關係的任務中產生比較明顯的優勢。**

這仍然是初步證據，而不是一般性定理。

---

# 12. Q4：Dependency / Premise Failure Propagation

Q4：

D：

**31.25%**

C1：

**31.25%**

差異：

**0pp**

因此目前不能宣稱：

> Construction 在所有 premise-failure propagation 任務中都優於 Baseline。

可能原因包括：

1. 本次 Q4 題目中，有些問題並不需要比 D 更複雜的條件傳播。
2. 題目設計尚未充分拉開兩種表示方式的能力差距。
3. Construction 的優勢可能依賴特定 dependency depth 或 conditional structure。

目前以上均只是研究假說，尚未確認。

因此：

**Q4 是限制性證據，而不是 Construction failure。**

---

# 13. Q9：Current State

Q9：

D：

**75%**

C1：

**62.50%**

差異：

**-12.50pp**

這證明 Construction 並非全面優於 Baseline。

這個結果值得保留，不能刪除，也不能用 Q5 的提升抵銷。

可能的後續研究問題：

> 顯式 establishment / condition 結構是否在保留依賴資訊的同時，引入了某些 current-state query 的額外解析成本？

目前尚不能確定。

因此 Q9 應保留為：

**Construction 的負向／限制性結果。**

---

# 14. CPU

CPU 測試結果顯示：

Baseline D：

**0.150 ms**

Construction C1：

**0.077 ms**

C1 約較快。

但 CPU 不作為 Construction 是否成立的判定標準。

原因是：

> 一個更快但答案錯誤的系統，沒有研究價值上的優勢。

因此 CPU 只作為：

**伴隨成本指標**

而非：

**Construction success criterion**

---

# 15. 目前研究結論

目前不能宣稱：

- Construction 已全面成功
- Construction 已被完全證明
- Construction 對所有 reasoning task 都有優勢
- Construction 已經一般化

目前可以提出的最嚴謹結論是：

> **Stage 1 提供初步實證支持：在本測試集的 Multi-hop dependency task（Q5）中，Construction C1 相較 Baseline D 出現 +41.66 個百分點的準確度優勢。**
>
> **然而，該優勢尚未在 Dependency / Premise Failure Propagation（Q4）中重現，且 Current State（Q9）出現 12.50 個百分點退步。因此目前證據支持的是「條件性的 Construction-specific advantage」，而非全面性優勢。**

目前研究狀態：

`Stage 1 Execution = COMPLETE`

`Implementation Correctness = ACCEPTED`

`Research Signal = PRELIMINARY POSITIVE`

`Generalization = NOT ESTABLISHED`

---

# 16. 方法學上的重要紀錄

本階段出現過一次研究規格偏移：

執行器自行加入不存在的：

- C1 overall > 50%
- C1 Q4 > D Q4

後續已透過重新讀取封版規格發現並移除。

因此本階段形成了一條完整的研究 provenance：

`Initial Run`
→ `Unexpected C1 Failure`
→ `Debug Trace`
→ `Implementation Bug Identified`
→ `Specification Deviation Identified`
→ `Specification Corrected`
→ `Minimal Repair`
→ `Full Rerun`
→ `Research Interpretation`

這一過程本身應保留。

---

# 17. 已建立的 Stage 1 文件

目前資料庫中應保留：

- `events.json`
- `questions.json`
- `gold_answers.json`
- `stage1_evaluator.py`
- `baseline_representation.py`
- `construction_representation.py`
- `stage1_test_runner.py`
- `stage1_results.json`
- `STAGE1_DEBUG_TRACE.md`
- `STAGE1_DEBUG_REPORT.md`
- `STAGE1_REPAIR_REPORT.md`
- `RUN_LOG.md`
- `RESULTS.md`

---

# 18. 下一研究節點

下一步不應立即將 Q5 結果擴張為 Construction 的一般性理論。

應優先研究三個不對稱結果：

### Q5
**+41.66pp**

為什麼 Multi-hop 出現明顯 Construction 優勢？

### Q4
**0pp**

為什麼 Dependency / Premise Failure Propagation 沒有產生差異？

### Q9
**-12.50pp**

為什麼 Current State 反而出現 Construction 退步？

這三個結果可能共同揭露 Construction 真正的適用邊界。

---

# 19. 核心研究命題的目前位置

目前 Construction 最值得繼續驗證的命題，不是：

> 「Construction 會讓 AI 變得更準。」

而是：

> **當資訊需要跨事件、跨條件、跨依賴鏈維持其成立關係時，顯式 Construction representation 是否能提供 Baseline 不具備的結構穩定性？**

Stage 1 的 Q5 結果對這個問題提供了第一個明確的正向訊號。

Q4 與 Q9 則提供了邊界條件與反例。

因此目前最合適的研究方向不是證明 Construction「全面有效」，而是找出：

**Construction 在什麼條件下開始產生不可忽略的優勢。**

---

## Stage 1 最終狀態

**完成。**

**目前證據：局部支持。**

**核心訊號：Q5 Multi-hop +41.66pp。**

**尚未成立：一般化 Construction advantage。**

**下一步：研究 Construction advantage 的成立條件與邊界。**

---

**紀錄版本：Construction Stage 1 Research Record v1.0**