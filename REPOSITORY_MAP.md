# CEGS Repository Map

> 目的：把 CEGS 的「現行理論、歷史版本、持續研究、歷史實驗」分開。日期負責保存形成歷史；研究狀態負責表示目前地位。兩者不可互相取代。

## 1. Repository 定位

CEGS（Constrained Event Generation Space）是 Construction 研究歷程中的公開工程／實驗節點，不等於完整 Construction 理論。

目前 repository 同時保存不同時期的文件，因此不能用「檔案在同一 repository」推定它們屬於同一版本。

## 2. 現在的資料夾結構

```text
CEGS/
│
├─ 00_INDEX/
│  └─ RESEARCH_STATUS.md
│
├─ 10_CURRENT_THEORY/
│  ├─ README.md
│  ├─ foundation/
│  │  └─ construction-framework.md
│  ├─ formalization/
│  │  └─ 構築 — 形式化草稿 型別優先.md
│  └─ appendices/
│     └─ 構築_附錄C_展開的相對性與錨點必要性_20260907.md
│
├─ 20_VERSIONED/
│  ├─ README.md
│  ├─ 20260828/
│  │  ├─ 構築成立條件規格Construction Unit Presentation Conditions & Formalization.md
│  │  ├─ 構築計算空間規格Construction Computational Space Specification.md
│  │  └─ 構築單位呈現條件與形式化研究.md
│  └─ 20260906/
│     ├─ 資格論.md
│     └─ 解釋報告資料總篇.md
│
├─ 30_ACTIVE_RESEARCH/
│  ├─ README.md
│  └─ 20260908/
│     └─ 構築_20260908_檔案庫完整閱讀紀錄.pdf
│
├─ 90_UNDATED_OR_UNRESOLVED/
│  └─ 通用舒適ux版.md
│
└─ construction_lab/
   ├─ Stage 1 實驗與程式
   ├─ 歷史結果
   ├─ audit / debug / repair
   ├─ 研究紀錄/
   └─ construction_stage1_package/
```

## 3. 四種狀態的判讀

### Current Theory / 現行理論

表示目前仍作為 Construction 研究基準使用的文件。

位於此區不代表所有內容都已證明；型別、MCS、必要性等仍可能是開放問題。

### Versioned / 歷史版本

保存某一時期形成的版本。即使後來被修改、替代或抽象化，也不刪除。

用途是：

- 追蹤概念如何演化；
- 比較不同版本的定義；
- 確認某個推論在什麼時間形成；
- 防止把後來的結論倒灌回早期文件。

### Active Research / 持續研究

保存目前還在推導、比較、驗證或等待決定的內容。

這裡不是「最新版資料夾」，而是「尚未結束的研究狀態」。

### Historical Experiment / 歷史實驗

`construction_lab/` 保存 Stage 0 / Stage 1 等實驗、資料、程式、結果與方法學審計。

它的研究價值來自可追溯性，而不是因為它是目前 Construction 理論的唯一實作。

## 4. 目前已確認的時間分界

### 2026-08-28 ～ 2026-08-29

早期 Construction 規格與研究母稿形成期，包括 Construction Framework v1.1、Construction Unit Presentation Conditions、Computational Space Specification 等。

目前定位：**歷史版本**。

### 2026-09-06

Qualification 理論與相關聊天室收斂文件形成期。

目前定位：**歷史／相關理論版本**。

這些文件很重要，因為它們保存 Construction 如何從 Qualification 問題中抽離出來的形成歷史；但不應直接當作目前 Construction 的最終定義。

### 2026-09-07

現行 Construction Framework、型別優先形式化草稿、附錄 C 等形成期。

目前定位：**現行理論 + 持續研究**。

### 2026-09-08

檔案庫完整閱讀紀錄。

目前定位：**研究紀錄／證據**，不是理論定稿。

## 5. 目前持續研究問題

- Q 的二值／三值語義。
- T、C、K、P 的正式型別。
- K 的多重語義用途是否需要拆分。
- MCS 的最小性條件（M1 / M2）。
- 不變詞、邏輯鏈、敘事鏈的必要性與相互關係。
- Narrative Chain 的停止條件與動力學。
- Correspondence / Symmetry / Alignment 是否構成 Qualification 的共同底層結構。
- Construction 是否能在實際 AI 系統中產生可驗證的工程收益。

## 6. 不可混讀的幾組文件

`20_VERSIONED/20260828/` 的規格文件 ≠ `10_CURRENT_THEORY/` 的現行定義。

`20_VERSIONED/20260906/` 的 Qualification 理論 ≠ Construction 完整定義。

`construction_lab/` 的 Stage 1 結果 ≠ Construction 已被驗證。

`30_ACTIVE_RESEARCH/` 的研究紀錄 ≠ 已完成證明。

## 7. 文件新增規則

新增文件時先回答兩個問題：

1. **它是哪個時間／版本的產物？**
2. **它目前是定稿、歷史、還是仍在研究？**

若答案只是「日期不同」，放入 `20_VERSIONED/YYYYMMDD/`。

若答案是「目前仍在推導」，放入 `30_ACTIVE_RESEARCH/`，必要時按日期再分資料夾。

若答案是「目前採用的理論基準」，放入 `10_CURRENT_THEORY/`。

若文件時間與研究地位都暫時無法判定，不要猜，先放 `90_UNDATED_OR_UNRESOLVED/`。

## 8. 研究狀態聲明

**Established / 可確認**

- repository 中的歷史程式、資料與文件確實存在。
- Stage 1 的歷史結果可重現。
- Stage 1 已接受 source-level / methodological audit。
- Construction 與 Qualification 已開始明確分離。

**Research candidate / 理論候選**

- Invariant、Logic Chain、Narrative Chain。
- Correspondence、Symmetry、Alignment 的部分關係。
- MCS 的形式化方向。

**Unresolved / 尚待決定**

- Q 的二值／三值語義。
- T、C、K、P 的型別與關係。
- MCS 最小性的正式條件。
- Narrative Chain 的停止條件與動力學。
- Construction 的實際工程收益。

**Not claimed / 明確不主張**

- Stage 1 已證明 Construction。
- Construction 必然提高模型正確率。
- Construction 必然節省 Token。
- MCS 已完成正式證明。
- CEGS 能自行決定公平、正當或治理結果。

## 9. Repository hygiene

Python `__pycache__/` 與 `*.pyc` 不屬於研究證據，應由 `.gitignore` 排除。

研究證據應優先保存：原始輸入、明確版本的程式、evaluator、結果、run log、audit 與研究紀錄。
