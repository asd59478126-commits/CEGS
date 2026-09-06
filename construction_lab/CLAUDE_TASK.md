# Claude Code 任務：Construction Lab 本機執行

你現在位於 Construction Lab 根目錄。
請直接在本機執行工作，不要只給建議；先檢查檔案，再執行可執行項目，最後回報實際輸出。

## 研究邊界（不可自行修改）

1. 不修改既定門檻：L2 25%；L3 10%/25%。
2. 不新增 A/B/C benchmark。
3. Stage 0 只處理 token 成本與補測。
4. Stage 1 必須是人工建立 CT，不得先改成 LLM extraction。
5. L2-c 的 token 差異不作為 REF 成敗判準；REF 的判準是 Q4 前提失效傳播正確率提升 8 個百分點。
6. CPU 時間與端到端延遲只是伴隨指標，不是主要判定指標。
7. 不把 tokenizer 差異、CPU 微秒級成本或格式正確直接解讀為 Construction 成立證據。

## 立即執行

### Step 1：環境檢查
確認 Python 版本、tiktoken 是否可用、transformers 是否可用。
不要為了完成測試擅自安裝大型依賴；若 Qwen tokenizer 缺套件，只明確回報缺少什麼。

### Step 2：Stage 0-o200k baseline
執行現有/整理後的 token counter，保留：
- tokenizer
- rendering language
- n
- L2-a total
- L2-b total
- L2-c total
- reduction
- frame ratio
- L3 theoretical ceiling

### Step 3：Qwen tokenizer
執行：
python stage0_token_count.py --hf Qwen/Qwen2.5-7B

把結果視為單獨量測，不覆寫 o200k baseline。

### Step 4：English rendering
用與中文完全相同的 20 筆 CT，只把 L2-a rendering 改成英文，再用同一 tokenizer 跑一次。
記錄 rendering language。

### Step 5：CPU micro-benchmark
執行 cpu_ct_benchmark.py。
只測 ct_eval/ct_query 類型的 deterministic computation。
輸出：
- CT count
- rounds
- total CPU ms
- average CPU us/ms per evaluation
不要宣稱這代表真正的 LLM/API latency。

### Step 6：結果判定
最後建立 RESULTS.md，內容必須區分：
- Already supported
- Pending
- Metric not applicable
- Next required experiment

不得把 pending 寫成 failed，也不得把 CPU benchmark 改寫成新的主 benchmark。

## 結束條件

完成後直接回報：
1. 實際執行了哪些命令。
2. 每個命令的實際結果。
3. Stage 0 最終狀態。
4. 哪些項目仍 Pending。
5. 是否可以進入 Stage 1 L1。

不要自行進入 Stage 1，除非上面的 Stage 0 補測全部完成並回報。
