# CEGS 入門指南

CEGS 是一個用於表示、檢查與追蹤結構化資格／決策資訊的研究型專案。

本指南描述的是目前公開 repository 所包含的 **CEGS Stage 1**。
它不代表目前 Construction 研究的全部內容。

## 1. 先理解 CEGS 與 Construction 的關係

目前研究需要區分三個層次：

```text
Construction
    ↓
MCS（Minimal Constructive Structure）
    ↓
Construction System
```

其中：

* **Construction**：目前研究中的結構層原理
* **MCS**：Construction 的正式研究對象
* **Construction System**：未來可能形成的實作系統

公開的 CEGS repository 則對應較早的 **Stage 1 implementation**。

因此：

```text
公開 CEGS Stage 1
≠
目前完整 Construction 理論
```

公開版的主要用途是提供一個穩定、可重現的研究階段與 implementation，而不是承載目前所有後續理論。

---

# 2. 如果你是第一次接觸 CEGS

建議先看：

1. `README.md`
2. `construction-framework.md`
3. `construction_lab/stage1_schema.md`

接著查看：

```text
construction_lab/
```

這個目錄包含 Stage 1 的資料、implementation、問題集與實驗紀錄。

公開 Stage 1 的核心比較是：

```text
C1 ↔ D
```

其中 C1 是 Construction representation，D 是 baseline representation。

---

# 3. 如果你是工程師

### 你可以先看

```text
construction_lab/baseline_representation.py
construction_lab/construction_representation.py
construction_lab/stage1_evaluator.py
```

它們分別對應：

* baseline 表示
* C1 表示
* Stage 1 評估流程

Stage 1 的重點不是建立完整 Construction 系統，而是檢查一個較窄的表示命題：

> 在相同事件與問題條件下，加入 `establishment_state`、`condition_ref` 與依賴傳播後，是否產生可觀測的差異？

公開 implementation 不包含目前後期研究所形成的全部 MCS、Anchor、Invariant 等概念。

---

# 4. 如果你是 AI／治理研究者

CEGS 的公開 Stage 1 可以作為一個具體的結構表示案例。

可以先閱讀：

```text
construction-framework.md
資格論.md
construction_lab/stage1_schema.md
```

需要注意：

公開 Stage 1 的研究範圍比目前 Construction 研究狹窄。

Stage 1 主要處理：

* qualification / establishment 類型的結構表示
* condition reference
* dependency propagation
* event history
* structured decision representation

它**不直接證明**：

* Construction Framework 整體成立
* MCS 已被證明存在
* 不變詞已被證明是必要結構
* 邏輯鏈與敘事鏈的完整理論
* 起點可追索已被實驗驗證

這些屬於後續 Construction 研究。

---

# 5. 如果你是企業 AI 團隊

CEGS 可以作為一個研究型結構表示範例，用於思考：

> 一個 AI 系統做出的判定，是否能保留足夠的結構，使後續仍可以檢查、比較與重新判定？

公開 Stage 1 提供的是較早期的實作與資料。

它可以用於：

* 閱讀結構化事件表示
* 檢查條件與依賴
* 觀察狀態變化
* 研究決策追蹤
* 研究結構化記錄

但不要把公開 Stage 1 直接理解成完整的企業治理產品。

目前 repository 的定位仍然是研究與實驗性質。

---

# 6. 如果你是研究生或獨立研究者

建議閱讀順序：

```text
README.md
    ↓
construction-framework.md
    ↓
construction_lab/stage1_schema.md
    ↓
construction_lab/
    ↓
目前研究狀態文件
```

研究時請注意時間順序。

公開 Stage 1 是一個已封版的研究階段。
後續 Construction 研究則進一步提出：

* 多維事件
* 歷史切片
* 主題與結構定位
* 不變詞
* 邏輯鏈
* 敘事鏈
* MCS
* 起點可定位／可追索

這些後續概念不應回溯要求公開 Stage 1 implementation 已經具備。

---

# 7. Stage 1 研究目前應如何理解

Stage 1 使用：

* 75 個事件
* 96 個問題
* C1 / D 兩個主要表示

其目標是檢查特定結構表示是否產生可觀測差異。

需要特別注意：

**公開 Stage 1 的原始結果可以重現，但重現結果不等於研究結論有效。**

後續 source-level audit 發現公開版本的 baseline 與部分題目設計存在問題，因此原先的 Construction-specific 結論不能直接作為有效證據。

目前較準確的說法是：

> Stage 1 的資料與原始結果具有可重現性，但原先的 Construction-specific 推論需要重新建立有效 baseline 與實驗條件後再評估。

這代表的是：

```text
實驗證據目前不足
```

而不是：

```text
Construction 假說已被否證
```

兩者必須分開。

---

# 8. 目前 Construction 研究的方向

目前更一般化的研究問題是：

> **事件被切片並形成歷史記錄、作為後續理解的載體時，為維持理解過程可回看、可比較、可對齊、可重新判定，最低需要保留什麼結構？**

目前的核心區分是：

```text
Construction
    = 尋找與保留最低必要結構的原理

MCS
    = 最低必要結構的正式研究對象
```

目前 MCS 的形式化候選為：

$$
Q(T,S,C,K)=1
$$

並要求：

$$
\not\exists S' \subsetneq S:
Q(T,S',C,K)=1
$$

因此「最小」不是：

* 最少文字
* 最少 token
* 最少欄位
* 最少資料

而是：

> 在目前情境與成立判準下，再移除就無法維持目標結構成立的最低必要結構。

這一部分仍屬研究中的形式化工作，不能把「已形式化」直接等同於「已證明」。

---

# 9. 目前正在研究的結構方向

目前有三個重要的結構方向正在研究：

```text
不變詞
    → 主題／主體的持續對應

邏輯鏈
    → 成立與依賴關係

敘事鏈
    → 形成與歷史關係
```

目前傾向認為，在多維事件中這三種關係都可能同時存在。

但：

```text
必然存在
≠
必然完整保留
```

Construction 要研究的是：

> 每種結構在特定情境下到底需要保留多少，才能維持後續理解所需的能力。

這一部分仍然是理論候選，不應被讀成已完成的形式證明。

---

# 10. 研究狀態

目前研究內容應區分：

### 已正式定義

* Construction / MCS / Construction System 的層級區分
* `Q(T,S,C,K)`
* MCS 的極小性形式
* 「最小」的研究意義
* TOKEN 多解性與結構解釋固定的區分
* 資訊治理與交換治理的區分

### 理論候選

* 對比 + 對齊 + 對稱
* 不變詞、邏輯鏈、敘事鏈的結構關係
* 起點可定位／可追索
* 歷史切片與最小必要結構之間的關係

### 尚待研究

* `K` 的完整刻畫
* MCS 的存在條件
* MCS 是否具有共同必要部分
* 非單調條件下的極小性
* 不變詞的正式型別
* 邏輯鏈與敘事鏈的完整操作化
* 母問題與實驗之間的可檢驗連結

因此，目前不應宣稱 Construction 已經被實驗證明。

---

# 11. 如何閱讀這個 repository

如果你的目的只是理解公開 CEGS：

```text
README.md
→ construction-framework.md
→ construction_lab/stage1_schema.md
→ construction_lab/construction_representation.py
```

如果你的目的是理解目前 Construction 研究：

請另外閱讀專案中的最新研究狀態文件，而不要只依賴公開 Stage 1 文件。

研究狀態文件應作為：

```text
目前研究上下文入口
```

公開 Stage 1 文件則作為：

```text
歷史實驗階段記錄
```

兩者用途不同。

---

# 12. 最後的定位

CEGS 公開版可以被理解為：

> 一個已封版、可重現的 Stage 1 結構表示實驗。

而目前 Construction 研究正在問的是更一般的問題：

> **當事件與資訊持續形成歷史記錄時，什麼結構是後續理解不可失去的最低必要結構？**

因此，CEGS 是目前研究歷程中的一個具體實作與實驗階段，而不是 Construction 全部內容的同義詞。

---

*文件性質：公開版入門指南*
*最後更新：2026-09-07*
