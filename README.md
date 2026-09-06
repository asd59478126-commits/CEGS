# CEGS: Constrained Event Generation Space

結構化事件表示、Qualification 機制與 Construction 研究的公開實驗專案。

---

## 本專案是什麼

CEGS 是一個用於研究「事件如何被表示、判定與進入特定規則空間」的研究與實作專案。

公開 repository 主要保存的是 **CEGS Stage 1 的歷史實作、實驗資料與相關文件**。
它不是目前全部 Construction 理論的完整實作，也不應被視為 Construction 研究的最終形式。

目前的研究方向已進一步從早期的 Qualification / 結構化事件表示，轉向一個更基礎的問題：

> 當事件被切片並形成歷史記錄，作為後續理解的載體時，為維持理解過程可回看、可比較、可對齊、可重新判定，最低需要保留什麼結構？

目前研究以：

```text
Construction
    ↓
Minimum Construction Structure (MCS)
    ↓
Construction System
```

作為主要研究路線。

CEGS 是這條研究歷程中的公開工程與實驗節點，而不是整個研究的同義詞。

---

## CEGS 早期處理的問題

早期 CEGS 主要探索：

> 一個事件或資訊單位，在進入特定 Qualification / rule space 之前，需要具備哪些可表示、可判定與可追蹤的條件？

因此，CEGS 曾將研究重心放在 Qualification：

```text
Input
  ↓
Qualification Check
  ↓
AI Processing / Rule Application
  ↓
Qualification Check
  ↓
Human Review / Decision
```

這條路線關注的是：

* qualification judgment 是否被明確表示
* qualification dependency 是否能被追蹤
* 判定是否能被重新檢查
* 人類是否能介入與修正

這些內容仍具有研究與工程價值，但不應與目前的 Construction 理論直接等同。

---

## CEGS 與 Construction 的關係

目前應區分三個層次：

| 層次               | 內容                                          |
| ---------------- | ------------------------------------------- |
| **Construction** | 研究多維事件在被保留為理解載體時，最低需要什麼結構                   |
| **MCS**          | Construction 的形式化研究對象：維持目標結構成立所需的最小必要結構     |
| **CEGS**         | 研究歷程中的公開工程與實驗專案，包含早期 Qualification / 事件表示工作 |

因此：

```text
Construction ≠ CEGS
MCS ≠ Stage 1
Qualification ≠ Construction 本身
```

公開 CEGS repository 應以其實際完成的工程與實驗內容為準，不代表目前全部研究成果。

---

## 公開 Stage 1

本 repository 的主要公開實驗是 **Stage 1**。

Stage 1 使用固定的事件、問題與答案資料，對比較表示進行評估。

公開資料包含：

* 75 個事件
* 96 個問題
* C1 與 D 兩種表示／處理條件
* 固定的 evaluation pipeline
* 可重現的歷史實驗資料

Stage 1 的設計目的，是探索結構化事件表示是否可能影響特定條件下的判定結果。

### 重要：可重現不等於已證明

Stage 1 的原始數值結果可以重現。

但後續的 source-level audit 發現，部分題型的評分並未真正反映 Construction representation 的差異。例如：

* 部分 baseline 題型直接使用固定輸出；
* 部分題型主要依賴問題文字或 keyword；
* 部分 gold label 不在實作允許的輸出集合中；
* 公開資料與部分歷史時間資訊存在不一致。

因此：

> **Stage 1 的結果具有可重現性，但原始的 Construction-specific 結論不能直接視為有效的理論驗證。**

這應理解為 **experiment validity 問題，而不是 Construction hypothesis 已被否證**。

Stage 1 因而主要保留為一個公開、可追溯的歷史實驗節點。

---

## 目前 Construction 研究

目前的研究問題已從早期的 Qualification 表示進一步抽象化。

核心問題不是：

> 如何把更多資訊塞進更短的 Token？

也不是：

> 如何讓模型固定遵守一套規則？

而是：

> 在資訊被切片、壓縮或部分保存之後，什麼結構仍然必須存在，才能讓後續理解保持可追溯性？

目前使用的形式化方向是：

```text
Q(T, S, C, K) ∈ {0,1}
```

其中：

* `T`：目標理解對象
* `S`：候選結構
* `C`：上下文
* `K`：使判定成立所需的結構性條件

候選的 Minimum Construction Structure 可表示為：

```text
S = MCS(T | I, C, K)
```

並要求：

```text
Q(T, S, C, K) = 1
```

且不存在更小的 `S' ⊊ S` 仍滿足成立條件。

這裡的「最小」不是最少字元、最少 Token 或最少欄位。

它指的是：

> **為維持目標結構成立所不可再刪除的必要結構。**

---

## 多維事件中的三個研究方向

目前 Construction 研究正在檢查多維事件中的三種基本結構方向：

### 不變詞

維持主題、對象或區域性主題的持續性。

它回答的是：

> 「這段記錄仍然在談什麼？」

### 邏輯鏈

維持成立、依賴與條件關係。

它回答的是：

> 「這個判定為什麼能成立？」

### 敘事鏈

維持事件由過去狀態形成目前狀態的關係。

它回答的是：

> 「這個狀態是怎麼形成的？」

目前研究傾向認為，多維事件中這三個方向可能具有基本地位，但其正式定義、必要性、相互關係與最小保留條件仍屬研究中的問題。

因此，本 repository 不把以下命題視為已完成證明：

```text
MCS = Invariant + Logic Chain + Narrative Chain
```

它目前仍是待形式化與驗證的研究候選。

同樣地：

```text
Existence
    ≠
Full Retention
```

某種結構在事件中存在，不代表它必須完整保留在最終表示中。

---

## Qualification 在這個研究中的位置

Qualification 仍然是 CEGS 的重要歷史研究主題，但目前不再把它當作 Construction 的完整定義。

可以區分：

```text
Construction
    ↓
What structure must remain?

Qualification
    ↓
Does this represented object satisfy a given rule space?

Application
    ↓
What should be done with the qualified object?
```

因此，CEGS 可以研究 qualification mechanism，例如：

* 條件是否成立
* 依賴是否成立
* 狀態是否需要重新判定
* qualification judgment 是否可追蹤

但 CEGS 不應直接宣稱自己能決定：

* 哪些條件「應該」存在
* 哪個標準「應該」優先
* 哪個價值判斷是公平的
* 哪個治理結果具有正當性

這些屬於標準、權限、價值與治理責任層次。

---

## 研究狀態

目前內容應區分為四種狀態。

### 已完成或可確認

* 公開 Stage 1 實作存在
* Stage 1 歷史資料可以取得
* 歷史結果可以重現
* 部分 source-level behavior 已完成審計
* Construction 與 Qualification 已開始進行概念分離
* MCS 已形成初步形式化方向

### 理論候選

* 不變詞、邏輯鏈、敘事鏈作為基本結構方向
* Correspondence / Alignment / Symmetry 的部分關係
* `K` 與上述結構的關係
* Construction 與歷史可追索性的形式連結

### 尚待證明

* MCS 是否能由目前形式化完整定義
* `K` 的正式性質
* 多維事件中三種結構方向的必要性
* 最小性條件在不同 Q 性質下是否保持一致
* Construction 是否能穩定改善實際理解、回看、比較或重新判定
* 是否能在真實 AI 系統中形成可驗證的工程收益

### 明確不主張

本 repository 不宣稱：

* 已證明 Construction 是完整的 AI 架構
* 已證明 Construction 必然節省 Token
* 已證明 Construction 必然提高模型正確率
* 已證明 Qualification chain 已經完成理論證明
* 已證明 CEGS 能自動產生公平或客觀的治理結果
* 已證明 AI 因此具有獨立的治理權限

---

## Repository 結構

主要研究文件包括：

```text
construction-framework.md
```

Construction 早期理論框架與相關概念。

```text
構築計算空間規格.md
```

形式化與計算方向的研究文件。

```text
構築單位呈現條件與形式化研究.md
```

Construction Token 與表示條件的研究背景。

```text
construction_lab/
```

歷史實驗與相關研究資料。

```text
資格論.md
```

Qualification 相關的哲學與理論研究。

---

## Stage 1 工程入口

主要程式包括：

```text
construction_lab/stage1_evaluator.py
construction_lab/baseline_representation.py
construction_lab/construction_representation.py
```

可用於檢查公開 Stage 1 的歷史實作與評估流程。

例如：

```bash
python construction_lab/stage1_evaluator.py
```

以及：

```bash
python construction_lab/baseline_representation.py
python construction_lab/construction_representation.py
```

實際可執行項目應以 repository 當前版本為準。

---

## 如何閱讀這個 Repository

第一次閱讀時，建議先理解：

```text
1. README
       ↓
2. Construction / Qualification 的區分
       ↓
3. Stage 1 歷史實作
       ↓
4. Stage 1 審計結果
       ↓
5. 目前 Construction / MCS 研究
```

最重要的閱讀原則是：

> **不要把歷史 Stage 1 的實作內容，直接當成目前 Construction 理論的完整定義。**

本 repository 保留研究歷程，包含早期假設、實作、實驗與後續發現。

這些內容不需要被重新寫成一條「從一開始就已經正確」的故事。

---

## 研究哲學

本專案採取一個簡單的原則：

> 能重現的結果，才進入可檢驗範圍；
> 能證明的命題，才進入理論結論；
> 尚未證明的內容，保持為研究問題。

因此，研究中的「失敗」與「錯誤」不會被視為需要從歷史中刪除的內容。

一個實驗可能：

```text
可重現
    ↓
但方法無法支持原本結論
```

這種情況的正確處理不是修改資料去配合理論，而是保留實驗、指出失效原因，並降低結論強度。

---

## 一句話定位

> **CEGS 是 Construction 研究歷程中的公開工程與實驗專案，用來探索結構化事件、Qualification 與可追溯表示；目前更核心的研究問題，則是找出多維事件在被保存為理解載體時所需的最低必要結構。**

---

## License & Research Notice

本 repository 是研究性專案。

其中不同文件可能代表不同研究階段，因此：

* 歷史實作不等於目前理論
* 實驗結果不自動等於理論證明
* 理論候選不應被視為已完成結論
* qualification output 不應被視為客觀、無偏或不可修改的最終決策

任何將 CEGS 應用於實際治理、授權、審核或高風險決策的系統，都應保留適當的人類覆核、責任歸屬與修正機制。

---

## Questions & Discussion

如果對研究框架、公開實驗、形式化方法或歷史結果有疑問，歡迎透過 GitHub Issues 或 Discussions 提出。

本研究主要使用中文撰寫，歡迎使用中文討論。
