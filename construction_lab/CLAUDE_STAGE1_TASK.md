# 給 Claude Code 的執行任務：Construction Stage 1

你現在位於 Construction Lab 本機研究資料夾。

## 研究邊界

Stage 0 已完成：
- L3 不再作為後續核心投入。
- L2 token 效益具有 tokenizer / language dependence，不能泛化成固定 25%。
- CPU 計算只作伴隨成本指標。

現在進入 Stage 1。Stage 1 的唯一核心目標是測試 Construction 的核心功能命題。

## 絕對限制

1. 不使用 LLM 做 CT extraction。
2. 不建立新的 A/B/C benchmark。
3. 不修改 75 Events / 96 Questions 的總量。
4. 不修改既有門檻。
5. 不把 CPU 成本變成成立判定。
6. 不把「有符號層」的收益誤稱為 Construction-specific effect。
7. Construction-specific 核心比較必須保留 C1 ↔ D。
8. 如發現規格矛盾，先記錄問題，不自行改規格。

## 你的任務

### Step 1
讀取：
- README.md
- CLAUDE_TASK.md
- stage1_schema.md
- stage1_question_matrix.md
- 現有 Stage 0 結果

### Step 2
建立 Stage 1 測試資料結構：
- events.json
- questions.json
- gold_answers.json

要求：
- 75 events
- 96 questions
- question category totals 必須完全符合 matrix
- 所有 gold answer 可由人工規則推導
- 題目不可洩漏 Construction 正確答案

### Step 3
建立兩個被測表示：

Baseline（D）
- 不使用 establishment_state 作為顯式 Construction 機制
- 保留一般時間／事實結構

Construction（C1）
- 使用 establishment_state
- 使用 condition_ref
- 使用既定條件傳播規則

兩者使用完全相同的原始事件與問題。

### Step 4
建立 evaluator：
- overall accuracy
- Q4 accuracy
- UCR
- contradiction rate
- cpu_ms
- e2e_ms（若本階段沒有 API，標記 N/A）
- context_tokens（若沒有模型上下文，標記 N/A）

### Step 5
建立 test runner。
在正式跑之前先做 schema validation：
- event count = 75
- question count = 96
- category count = matrix
- gold answer 完整
- C1 / D 使用相同輸入資料

### Step 6
生成實驗報告，但不要自己宣稱 Construction 成立。
報告只能：
- 呈現數據
- 呈現組間差異
- 檢查既定判定條件
- 清楚區分「觀察結果」與「研究結論」

### Step 7
記錄 CPU timing。
`cpu_ms` 必須明確說明測的是：`ct_eval + ct_query`，不是單一 CT 的時間，並記錄測量範圍與 iteration。

## 執行原則

先建立資料與 evaluator，再執行正式測試。不要把 LLM 接進 Stage 1。

所有產生的檔案要放在目前資料夾中。

完成後更新：
- RESULTS.md
- RUN_LOG.md

並在最後回報：
1. 哪些檔案建立／修改
2. 75/96 是否通過 schema validation
3. C1 vs D 的結果
4. Q4 結果
5. CPU timing
6. 是否觸發任何既定判定條件
7. 是否有任何未解決問題
