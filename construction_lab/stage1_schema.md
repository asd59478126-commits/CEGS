# Construction Stage 1 — 實驗 Schema 定稿

版本：Stage 1 Schema v1.0  
狀態：待封版後執行  
目的：在不引入 LLM 抽取誤差的前提下，直接測試 Construction 核心機制是否比 baseline 提供額外功能價值。

## 1. 實驗原則

Stage 1 全部由人工建立 CT。不得在本階段使用 LLM 從自然語言抽取 CT。

唯一核心比較：
- Baseline：時間性／事實性結構，不使用 Construction 的條件式成立狀態。
- Construction：在相同事件資料上，加入 establishment_state、condition_ref 與依賴傳播所需結構。

不得把「模型會不會抽取 CT」混入本階段。

## 2. 基本單位

Event：一筆人工建立的事件。  
CT：事件的結構化表示。  
Question：針對事件集合提出的一個可判定問題。  
Gold Answer：由人工依實驗規則預先封存的正確答案。

建議最小欄位：

```text
event_id
event_type
subject
relation
object
valid_from
valid_to
condition_ref
establishment_state
```

Baseline 可忽略或不暴露：
- condition_ref
- establishment_state

Construction 保留並計算：
- condition_ref
- establishment_state

## 3. 75 Events

正式實驗使用 75 筆人工 CT。

事件應覆蓋：
1. Direct fact
2. Temporal change
3. Retraction
4. Correction
5. Dependency
6. Multi-hop dependency
7. Unknown premise
8. Contradiction
9. Current-state change
10. Historical persistence

事件設計不可讓 Construction 題型全部偏容易。

## 4. 96 Questions

96 題必須由事件集合派生，且答案可由明確規則判定。

建議分類與題數：

Q1 Direct Fact：10  
Q2 Temporal：10  
Q3 Retraction：12  
Q4 Dependency / Premise Failure Propagation：16  
Q5 Multi-hop：12  
Q6 Unknown：8  
Q7 Contradiction：8  
Q8 Correction：8  
Q9 Current State：8  
Q10 Historical State：4  

合計：96

Q4 為主檢驗類別，因為 Construction 核心命題集中於條件式成立與前提失效傳播。

## 5. 重要控制

必須包含對 Construction 不利的題目：
- 歷史成立，但現在仍成立。
- 發生撤回，但不應擴散到無依賴的 CT。
- 新事實出現，但不能自動推導為 SUPERSEDE。
- 前提 UNKNOWN 時，不可自行提升為 ESTABLISHED 或 NOT_ESTABLISHED。
- 多個依賴中只有部分失效時，依規則決定結果，不得一律 false。
- 同一事件不同時間點的資格可以不同。

## 6. C1 ↔ D 核心比較

C1：有符號層 + establishment_state + condition propagation。  
D：有符號層，但沒有 establishment_state 的 Construction 機制。

兩者必須：
- 使用完全相同的 75 Events。
- 接受完全相同的 96 Questions。
- 使用相同的輸出格式。
- 由同一套 evaluator 計分。

若 C1 > D，才有資格進一步討論 Construction-specific effect。

A ↔ B 類比較只能說明符號／規則層是否有幫助，不能單獨證明 Construction。

## 7. 評估指標

至少記錄：
- Overall Accuracy
- Q4 Accuracy
- UCR（若規格已有正式定義，沿用原定義）
- Contradiction Rate
- cpu_ms
- e2e_ms（若有模型/API）
- context_tokens（若本階段存在上下文輸入）

cpu_ms 與 e2e_ms 是伴隨成本指標，不是成立判定。

## 8. 答案封存

Gold answer 必須在測試前封存。

測試程式不得根據參與評估的輸出動態修改 gold answer。

輸出至少分成：
- gold_answers.json
- baseline_answers.json
- construction_answers.json
- evaluation.json

## 9. Randomization / 重現性

如果題目或事件順序需要 randomization，固定 seed 並記錄。
同一次實驗兩組必須看到等價題序或由同一固定 seed 派生。

## 10. 不得擅自修改

不得修改以下既定研究條件：
- 96 題總數
- 75 事件總數
- Q4 作為核心類別
- C1 ↔ D 作為 Construction-specific 核心比較
- LLM extraction 不進 Stage 1
- 門檻與既有規格若另有封版文件，以封版文件為最高優先級

任何必要修改先記錄，不得靜默改動。
