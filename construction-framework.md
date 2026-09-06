# Construction 理論框架
> 推導紀錄｜以不變詞、對齊、子對稱、可延續不變量為核心

---

## 一、TOKN 擴展

原始 TOKN 結構：

```
TOKN = Collection + Weight
```

只能說明相關強度，無法說明關係方向。

擴展方向：

```
TOKN = Collection + Relation + Direction + Weight
```

其中 **Direction 是原本就缺失的基本維度**，不是後加的裝飾。

### 符號規範

| 符號 | 意義 |
|------|------|
| `→` | 定向 |
| `←` | 反向定向 |
| `↔` | 雙向 |
| `↛` | 關係不成立 |

**反向 ≠ 否定**（需嚴格區分）

### Direction 與 Role 的區別

```
Direction = 關係如何定向
Role      = 節點在關係中是 Source 還是 Target
```

兩者是不同層級，不能混用。

---

## 二、基本結構

### 不變詞

不變詞 = 主題在這段討論中**無法被移除的語意錨點**，提供穩定參照域。

> 注意：不變詞是限制與定位條件，不是內容的父節點。

### 構築結構

```
不變詞 {
  子集合1 ( 子對稱1 | 子對稱2 )
  子集合2 ( 子對稱1 )
}
→
不變詞B {
  子集合1 ( 子對稱1 )
}
```

主題之間用方向箭頭表示關係。

### 置換條件

```
置換合法 = 位置對齊（子對稱完全吻合）
         + 邏輯鏈可追蹤
         + Role / Anchor / Order / Constraint 保持
```

- 完全吻合 → 可置換（`A ↔ C`）
- 部分吻合 → 可局部置換（`A ≈ C`）
- 完全不吻合 → 不可置換（`A ≁ C`）

**可追蹤 ≠ 合法**

---

## 三、Order

Order 是 Construction 維持身份連續性與敘事可追蹤性的**優先結構條件**，不是並列的第五個元素。

### Order 的三層

| 層級 | 內容 |
|------|------|
| 表示層 | 符號排列（`A → B → C`） |
| 關係層 | 為什麼在這個順序成立 |
| 歷史層 | 構築如何成為現在這個樣子 |

### 敘事鏈定義

```
NarrativeChain ≠ OptimalPath
NarrativeChain ≠ CorrectPath
Revision ⊂ NarrativeChain
```

敘事鏈保存的是**構築如何成為現在這個樣子的歷史結構**。

對齊邏輯鏈組合 → 形成敘事鏈的 Order（從對齊結果累積而來，不是被給定的）

身份連續性的錨點不是不變詞本身，而是**對齊事件的累積記錄（Alignment Trace）**。

---

## 四、Construction 最小閉環

一次對齊變成 Construction 的橋樑：**可繼承的不變量**。

### 四層結構

```
① 對齊
  某一子項目與既有參照形成局部一致

② 子對稱
  由對齊形成可辨識的關係結構

③ 階段性不變量
  從子對稱中留下能跨越下一階段的穩定部分

④ 連續展開
  下一子集合以該不變量為參照再次對齊
```

### 最小閉環流程

```
不變詞／既有穩定參照
    ↓
子集合定位
    ↓
對齊成立
    ↓
新結構／子對稱形成
    ↓
提取可延續不變量
    ↓
【 Construction Closed 】
    ↓
成為下一次構築的基底
```

### 重要區分

```
Construction 閉環  ≠  Narrative Chain 延續
```

- **Construction** 只需完成一次
- **Narrative Chain** 才是跨階段反覆發生的

> 每次成立之後，留下下一次成立的條件——這才是 Construction。

不變詞可以階段性遞歸：

```
Global Invariant
    ↓
Local alignment → Local invariant
    ↓
Next-stage invariant
    ↓
New alignment → New local invariant
    ↓
……
```

---

## 五、記憶機制

### 核心原則

```
記憶保存 ≠ 記憶使用
Past Data × Current Reality → Usable Memory
```

現在是記憶的裁判。

```
存在 ≠ 可取用 ≠ 應取用 ≠ 應影響判斷
```

### 資格定義

```
資料 ≠ 資格
AI   ≠ 資格
判定結果 = 資格
```

資格 = 當前構築對一段歷史資料所作出的成立關係判定。

資格本身是時間性的：

```
Qualification( Trace, t | Construction_t )
```

同一 Trace 在不同時間點可能得到不同資格結果。

### Trace 的定義

```
Trace ≠ 整個過程的錄影檔
Trace = 已完成構築的可延續憑據
Full History ≫ Identity Certificate
```

只需要 Minimal Sufficient Trace，不需要保存全部歷史。

### 記憶召回流程

```
Invariant Set
    ↓
Sub-set
    ↓
Sub-item
    ↓
Alignment formed
    ↓
Alignment Trace
    ↓
Current Reality 重驗
    ↓
Memory re-entry
```

Current Reality 不直接裁判舊記憶——中間需要先找到可對齊的既有單位。

**普通 Retrieval：** 這筆資料跟現在相似，所以拿出來。

**這個架構：** 曾在可辨識的結構位置完成對齊，現在又找到相同位置，且當前現實允許重新取得資格，才恢復使用。

---

## 六、不可逆性與歷史成立

Construction 理論**不要求** LLM 內部計算是物理或資訊論意義上的不可逆。

真正需要的是：

> 已形成的 Alignment Trace，其「曾經如何成立」**不能被事後偽造**。

### 三層分開

| 層 | 性質 |
|----|------|
| Formation | 不可任意逆寫 |
| Qualification | 可隨時間重算 |
| Usage | 可改變 |

Trace₁ 資格變 false 之後，不代表它「從未成立」：

```
歷史成立 ≠ 現在有效 ≠ 現在應該使用
```

### 架構層次

```
LLM
（產生候選計算結果）
    ↓
Construction Layer
（判定哪些對齊成立、哪些 Trace 形成）
    ↓
Memory Layer
（保存可延續不變量與 Trace）
    ↓
Current Reality
（重新判定現在是否可用）
```

Construction 不寄生在 LLM 內部神經元歷史上，而是**建立在 LLM 上方的結構層**。

### 核心命題

> Construction 的成立不依賴底層 LLM 計算是否可逆；只要求「構築形成的歷史」具有不可任意竄改性，而其「當前使用資格」可由 Current Reality 重新判定。

---

## 七、研究定位

這套東西不是 VLLM 也不是 LLVM。最接近：

```
Knowledge Representation + Graph-based Prompting
```

但目前沒有現有框架完整覆蓋。

### 現有研究已有的零件

| 零件 | 狀態 |
|------|------|
| Alignment | ✓ |
| Relation Path | ✓ |
| Traceability | ✓ |
| Temporal Order | ✓ |
| Incremental Update | ✓ |

**缺的是：** 「對齊事件累積 → 為什麼構築仍是同一個構築」的完整因果鏈。

### 目前研究邊界

```
Construction
└─ Topic
   └─ Topic Identity
      └─ Narrativity
         └─ Narrative Chain   ← 目前邊界
```

到 Narrative Chain 為止。不繼續推向完整記憶或 Identity Certificate。
