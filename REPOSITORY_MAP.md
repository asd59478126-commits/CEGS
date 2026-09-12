# CEGS Repository Map

> 目的：把 CEGS 的「索引、現行理論、歷史版本、持續研究、日期證據、歷史實驗」分開。日期負責保存形成歷史；研究狀態負責表示目前地位。兩者不可互相取代。
>
> 2026-09-12 起增加 `00_INDEX/CONTENT_CATALOG.md` 與 `00_INDEX/AI_INGESTION_GUIDE.md`，作為人類／AI 共用的閱讀入口與分層規則。

## 1. Repository 定位

CEGS（Constrained Event Generation Space）是 Construction 研究歷程中的公開工程／實驗節點，不等於完整 Construction 理論。

目前 repository 同時保存不同時期的文件，因此不能用「檔案在同一 repository」推定它們屬於同一版本。

## 2. 現在的資料夾結構

```text
CEGS/
│
├─ 00_INDEX/
│  ├─ RESEARCH_STATUS.md
│  ├─ CONTENT_CATALOG.md
│  └─ AI_INGESTION_GUIDE.md
│
├─ 10_CURRENT_THEORY/
│  ├─ README.md
│  ├─ foundation/
│  ├─ formalization/
│  └─ appendices/
│
├─ 20_VERSIONED/
│  ├─ README.md
│  ├─ 20260828/
│  └─ 20260906/
│
├─ 30_ACTIVE_RESEARCH/
│  ├─ README.md
│  └─ construction/
│     ├─ memory/
│     └─ exchange/
│
├─ 90_UNDATED_OR_UNRESOLVED/
│
├─ 2026.9.10/
│  └─ 原始日期研究／版本證據
│
├─ 2026.9.12/
│  └─ 當日新增研究補充／日期證據
│
└─ construction_lab/
   └─ 歷史工程與實驗證據
```

## 3. 七種閱讀狀態

### Index / 索引

`00_INDEX/` 不承載新的理論結論，負責告訴人與 AI：文件在哪裡、目前是什麼狀態、應怎麼讀。

### Current Theory / 現行理論

`10_CURRENT_THEORY/` 表示目前被採用、持續作為 Construction 理論基準使用的內容。

位於此區不代表已證明；型別、MCS、必要性與部分跨層關係仍可能是開放問題。

### Versioned / 歷史版本

`20_VERSIONED/` 保存具有明確版本或歷史階段的文件。用途是追蹤演化，不是提供目前唯一正確答案。

### Active Research / 持續研究

`30_ACTIVE_RESEARCH/` 保存仍在推導、比較、化約、驗證或等待決定的研究。

### Date Evidence / 日期證據

`2026.9.10/` 與 `2026.9.12/` 保存特定日期形成時的原始材料。日期目錄可以包含多個不同研究主題，因此不直接等同於理論層。

### Historical Experiment / 歷史實驗

`construction_lab/` 保存早期工程、程式、結果、run log、debug、repair、audit 等材料。這些是實驗證據，不自動等同於理論驗證。

### Unresolved / 未定類

`90_UNDATED_OR_UNRESOLVED/` 保存目前無法可靠判定日期或研究地位的材料。不要為了整齊而猜分類。

## 4. 目前 Construction 主線

```text
Early Event Representation / Qualification
                ↓
Construction emergence
                ↓
Alignment / Invariant / Trace / Narrative Continuity
                ↓
Core candidate baseline
                ↓
Adaptive Construction + Thematic Invariance
                ↓
State → Representation → Interpretation
                ↓
Memory / Emotion / Exchange research branches
```

## 5. 重要不可混讀關係

`20_VERSIONED/20260828/` ≠ `10_CURRENT_THEORY/`。

`20_VERSIONED/20260906/` Qualification 理論 ≠ Construction 完整定義。

`construction_lab/` 的 Stage 1 結果 ≠ Construction 已被驗證。

`30_ACTIVE_RESEARCH/` ≠ 已完成證明。

`2026.9.10/` 與 `2026.9.12/` ≠ 單一現行理論層。

## 6. 新增文件規則

新增文件時先判定：

1. 時間／版本：它何時形成？
2. 研究狀態：它目前是現行、歷史、研究中、證據，還是未定？
3. 文件角色：理論、形式化、附錄、研究、索引、實驗或原始資料？

若只是歷史日期不同，不應覆蓋現行理論。

若仍在推導，放入 `30_ACTIVE_RESEARCH/`。

若是目前採用的理論基準，放入 `10_CURRENT_THEORY/`。

若資料具有不可替代的歷史證據價值，保留日期原檔，即使另有現行閱讀位置。

## 7. 目前索引入口

第一次閱讀：

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
20_VERSIONED / Date Evidence / construction_lab（按需要回溯）
```

## 8. 目前研究狀態總結

**已建立／可追溯**

- 歷史 repository、工程與實驗材料。
- Construction 與 Qualification 的概念分離。
- 現行 Construction 理論主體。
- 十四項核心候選基線。
- 多個最小結構可以成立的研究方向。
- 版本、日期、研究狀態分層保存方式。
- 2026-09-12 新增狀態／表示／理解映射補充。

**理論候選／持續研究**

- MCS 正式最小性。
- Invariant / Logic Chain / Narrative Chain。
- Correspondence / Symmetry / Alignment。
- Memory Equivalent / Current Judgment Quantity。
- Emotion → Memory Equivalent。
- Exchange 第一層 Difference → Need → Exchange。
- State → Representation → Interpretation 的主題性連續。

**明確未宣稱**

- Construction 已完全證明。
- Stage 1 已證明 Construction。
- 單一 MCS 已普遍成立。
- 情緒、交換或跨層映射已經成為不可替代核心。
- CEGS 可以自行決定價值、公平或治理正當性。

## 9. 原則

> 歷史版本不是錯誤版本。
>
> 研究候選不是已證明命題。
>
> 實驗成功不是理論成立。
>
> 日期不是地位。
>
> 索引不是理論。
