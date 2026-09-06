# Construction Stage 1 — 96 題分類表定稿

版本：Stage 1 Question Matrix v1.0  
狀態：待生成題目內容後封版  
總題數：96  
總事件數：75

## 題型配置

| 類別 | 題數 | 核心問題 |
|---|---:|---|
| Q1 Direct Fact | 10 | 直接查詢既有事件 |
| Q2 Temporal | 10 | 時間前後與有效區間 |
| Q3 Retraction | 12 | 撤回是否正確生效 |
| Q4 Dependency / Premise Failure Propagation | 16 | 前提失效是否沿條件關係正確傳播 |
| Q5 Multi-hop | 12 | 深度 2–3 的依賴鏈 |
| Q6 Unknown | 8 | 前提未知時是否保留 UNKNOWN |
| Q7 Contradiction | 8 | 衝突狀態與矛盾處理 |
| Q8 Correction | 8 | CORRECT 與舊紀錄的關係 |
| Q9 Current State | 8 | 問「現在」成立什麼 |
| Q10 Historical State | 4 | 問「過去某時點」成立什麼 |
| **合計** | **96** | |

## Q1 Direct Fact（10）

用來建立 baseline 能正常處理的低難度控制題。不得全部涉及 Construction 特有條件。

## Q2 Temporal（10）

測：
- valid_from
- valid_to
- 同一關係不同時段
- 時間邊界
- 目前時間與歷史時間區分

## Q3 Retraction（12）

至少包含：
- 直接撤回
- 撤回後仍有其他獨立成立紀錄
- 撤回來源紀錄
- 撤回不應擴散的案例
- 撤回後新紀錄成立

## Q4 Dependency / Premise Failure Propagation（16）

Stage 1 主測類別。

必須至少包含：
- 單層依賴
- 前提失效
- 前提 UNKNOWN
- 多個前提
- 一個前提失效、其他仍成立
- 依賴恢復
- 條件只影響局部 CT
- 不存在依賴時不得傳播

Q4 的答案必須能由既定規則獨立推導。

## Q5 Multi-hop（12）

深度以 2–3 hop 為主。禁止使用 Construction 規則以外的隱性常識作為答案依據。

## Q6 Unknown（8）

刻意設計證據不足的情境。禁止把「未證明」當成 false，也禁止把「可能」升級為 true。

## Q7 Contradiction（8）

包含：
- 同一關係衝突
- 不同來源衝突
- 時間區間衝突
- 撤回與仍有效紀錄並存

要區分：
- contradiction
- NOT_ESTABLISHED
- UNKNOWN

三者不得混用。

## Q8 Correction（8）

測：
- 更正事件
- 舊值與新值
- correction 是否等於 retraction
- correction 是否自動生成 supersede

沒有明示的 SUPERSEDE 不得當成 gold answer。

## Q9 Current State（8）

問題必須明確指定「現在」。這是 Construction / Qualification 的重要終點。

要求 evaluator 使用指定 current_time。

## Q10 Historical State（4）

問題指定過去時間點。用來確認 Construction 不會因現在失效，就抹掉歷史成立。

## 題目平衡要求

96 題中應有足量「Construction 不能作弊」的題目：
- 直接問題
- 不受依賴影響的事件
- UNKNOWN
- 歷史成立
- 不應推導 SUPERSEDE
- 局部失效而非全局失效

## 題目資料格式

建議每題：

```json
{
  "question_id": "Q4-01",
  "category": "Q4",
  "question": "...",
  "current_time": "2024-...",
  "relevant_event_ids": ["..."],
  "gold_answer": {
    "state": "..."
  },
  "difficulty": "..."
}
```

注意：gold_answer 僅在封存檔中保存；實際盲測輸入不得把答案一起提供給被測系統。

## 封版條件

在 96 題真正生成前，必須確認：
1. 題數 = 96
2. 類別總和 = 96
3. 每題可判定
4. 每題至少對應一組事件
5. 金標答案可由人工獨立重算
6. 題目不存在只有 Construction 才能理解的語言提示
7. 題型不把 Construction 預設成正確答案
