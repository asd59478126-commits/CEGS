# CEGS

**Constrained Event Generation Space**

CEGS 是一個公開研究與實驗 repository，保存「結構化事件表示 → Qualification → Construction」這條研究歷程中的工程實作、歷史資料、理論文件與目前研究紀錄。

> **CEGS 是研究載體，不等同於 Construction 本身。**

## 目前研究定位

研究的核心已不再只是「如何表示一個事件」，而是：

> **當多維事件不能被完整保留時，為維持後續理解、比較、對齊、追索與重新判定，最低需要保留什麼結構？**

目前「構築（Construction）」的工作性定義為：

> **多維事件的最短結構展開與起點可追索性。**

這裡的「最短」不是最少字元、最少 Token 或最少欄位，而是在特定目的、目標、條件與邊界下，仍足以使目標結構成立並可被後續重新理解、定位、比較或追索的必要結構。

目前研究已從「唯一最小結構」進一步檢查：**同一主題可能存在多個不同但均成立的最小結構形式。** 因此，目前重點包含適應性結構與主題性不變，而不是固定唯一的最小表示。

## Construction、MCS 與 CEGS

| 名稱 | 定位 |
|---|---|
| **Construction** | 原理：研究多維事件如何以必要結構成立、保留與追索 |
| **MCS／最小成立結構** | 形式化研究層：描述特定條件下不可再刪除的必要結構 |
| **CEGS** | 公開研究與工程載體：保存實驗、歷史版本、研究文件與可執行內容 |

```text
Construction ≠ CEGS
MCS ≠ CEGS Stage 1
Qualification ≠ Construction 本身
```

## 早期研究：Qualification 與事件表示

CEGS 的早期階段主要研究一個事件或資訊單位，在進入特定規則空間前需要具備哪些可表示、可判定與可追蹤的條件。

```text
Input
  ↓
Qualification
  ↓
Rule / Processing
  ↓
Qualification
  ↓
Human Review / Decision
```

這些內容仍保留在 repository 中，因為它們是目前研究形成的歷史依據，而不是需要被新理論覆蓋掉的材料。

## Stage 1：公開歷史實驗

CEGS 的公開 Stage 1 是早期結構化事件表示實驗，包含固定事件、問題、答案與評估流程，用於比較不同表示方式在特定條件下的表現。

後續 source-level audit 發現，部分評分路徑沒有真正隔離表示方式的影響，例如固定輸出、問題文字／關鍵詞依賴，以及部分標籤與允許輸出集合之間的不一致。

因此：

> **Stage 1 可以作為可追溯、可重現的歷史實驗，但不能直接把原始結果當成 Construction 已被驗證。**

這是實驗有效性問題，不等於 Construction 假說已被否證。

## 目前 Construction 研究

目前重要的概念鏈包括：

```text
Presence
  ↓
Localization
  ↓
Establishment
  ↓
Construction
  ↓
Difference
  ↓
Meaning
```

重要區分：

- **Presence ≠ Establishment**：存在不代表已建立為可用結構。
- **Establishment ≠ Truth / Endorsement**：成立於某一結構空間，不等於真實或被認可。
- **Unknown ≠ False**：未知不可直接當作否定。

Construction 是在條件與邊界下，使結構能成立、保留、追索與重新判定的原理，而不是固定格式。

### 2026-09-12 新增的跨層映射補充

目前新增一個重要但尚未完成形式化的方向：

```text
Internal State
      ↓
External Representation
      ↓
Interpretation
```

這裡區分：

- 內在狀態不等於外化表示。
- 外化表示不等於接收者理解。
- 表示不是透明傳輸。
- 理解不是對原始內在狀態的直接取回。
- 即使形式改變，仍可能維持可追索的主題性連續。

此方向目前視為構築理論的跨層結構補充，不暫定為第十五個核心基元，也不宣稱完整心智或意識本體論。

## 目前研究延伸

### 記憶當量

研究不只問「過去保存了多少」，而是：

> **過去有多少結構實際能在現在的理解、判斷與構築中重新參與？**

目前區分：

```text
Stored Information
      ≠
Usable Memory
      ≠
Memory Continuity
```

並延伸研究 Memory Invariant、當下判斷量，以及記憶重新進入當前結構的條件。

### 情緒與記憶當量

情緒目前是可能影響「回憶優先級 → 記憶當量 → 當下判斷」的候選模組，而不是 Construction 必須模擬人類情緒的既定結論。

```text
Emotion State
    ↓
Recall Priority
    ↓
Memory Equivalent
    ↓
Current Judgment
```

同時區分代理自身的情緒峰值參照與特定使用者的情緒參照；兩者均屬研究中的比較基準，不等於讀心或生物情緒模擬。

### 交換

目前從最基礎的差異與需求形成開始：

```text
Physical / Cognitive Difference
        ↓
Communication Need
        ↓
Exchange Need
        ↓
Demand Boundary / Peak
        ↓
Exchange
```

目前僅保存第一層原理與假設，尚未把第三方、權限、衝突、多方遞迴等高階問題當成已完成模型。

## 研究狀態

### 已建立／可追溯

- CEGS Stage 1 歷史實作與資料
- 歷史實驗結果及其來源記錄
- Stage 1 的部分 source-level 審計
- Construction 與 Qualification 的概念區分
- Construction 的目前核心工作定義
- 多個最小結構可以成立的研究方向
- 研究資料的版本、日期與現行分類架構
- 2026-09-12 狀態／表示／理解跨層映射補充

### 目前理論／研究中

- 適應性構築與主題性不變
- 記憶當量與記憶連續性
- 當下判斷量
- 情緒對記憶當量的影響
- 交換形成的第一層原理
- Construction 的形式化與實驗化
- 跨主體狀態 → 表示 → 理解映射

### 尚未宣稱完成證明

本 repository 不宣稱：

- Construction 已經成為完整 AI 架構
- Construction 必然降低 Token 或計算成本
- Construction 必然提高模型正確率
- 任何單一 MCS 形式已經普遍成立
- 所有相關結構的必要性都已完成形式證明
- 跨主體映射已完成完整形式化
- CEGS 可以自行決定公平、價值或治理正當性
- AI 因此取得獨立治理權限

## Repository 結構

目前 repository 使用「索引 → 現行理論 → 歷史版本 → 持續研究 → 日期證據 → 歷史實驗」的分層方式：

```text
00_INDEX/
    導航、研究狀態、內容目錄、AI 讀取規範

10_CURRENT_THEORY/
    目前採用的理論與正式研究基礎

20_VERSIONED/
    歷史版本與版本化文件

30_ACTIVE_RESEARCH/
    尚在推進的研究問題與延伸模組

90_UNDATED_OR_UNRESOLVED/
    尚未能可靠歸入日期或版本的材料

2026.9.10/
    2026-09-10 原始研究材料與日期證據層

2026.9.12/
    2026-09-12 新增研究補充與日期證據層

construction_lab/
    歷史工程與實驗程式、結果、審計與修復紀錄
```

**日期資料與現行分類可以同時存在。** 日期資料保存研究發生時的原始狀態；現行分類提供現在閱讀與研究時的結構入口。兩者不是互相覆蓋的關係。

## 統一閱讀入口

完整分類與檔案角色：

- [CONTENT_CATALOG.md](./00_INDEX/CONTENT_CATALOG.md)
- [AI_INGESTION_GUIDE.md](./00_INDEX/AI_INGESTION_GUIDE.md)
- [RESEARCH_STATUS.md](./00_INDEX/RESEARCH_STATUS.md)
- [REPOSITORY_MAP.md](./REPOSITORY_MAP.md)
- [構築研究 MOC.md](./構築研究%20MOC.md)

第一次閱讀建議：

```text
README
  ↓
00_INDEX/RESEARCH_STATUS
  ↓
00_INDEX/CONTENT_CATALOG
  ↓
00_INDEX/AI_INGESTION_GUIDE
  ↓
構築研究 MOC
  ↓
10_CURRENT_THEORY
  ↓
30_ACTIVE_RESEARCH
  ↓
20_VERSIONED / Date Evidence / construction_lab
```

## 工程與實驗

`construction_lab/` 保留早期 CEGS 工程與實驗資料，用於：

1. 提供歷史實作的可追溯來源。
2. 檢查早期 Qualification／事件表示的實際行為。
3. 作為後續實驗有效性與方法修正的比較基線。

新的研究結論不應在沒有對應實驗或形式化依據的情況下，直接從歷史 Stage 1 程式碼推導。

## 閱讀原則

CEGS 的文件會同時存在「當時怎麼做」與「現在怎麼理解」兩種資訊。這不是資料不乾淨，而是研究歷史本身的一部分。

```text
歷史版本
    ≠
目前理論

研究候選
    ≠
已證明命題

實驗可重現
    ≠
理論有效

日期
    ≠
研究地位

索引
    ≠
理論
```

CEGS 的目標不是清掉過去的研究痕跡，而是讓不同時間形成的材料能被定位、比較、追溯，並在新的研究結構下重新理解。

## 狀態說明

本 README 是 repository 的**現行入口頁**。具體理論內容、研究問題與版本歷史，以對應目錄中的文件為準；README 的功能是更新「目前應如何理解與進入 repository」，而不是取代歷史文件。

最後更新：2026-09-12
