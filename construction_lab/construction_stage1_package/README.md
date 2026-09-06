# Construction Lab

用途：把目前 Construction 實驗整理成一個可由 Claude Code 在本機執行的資料夾。

目前範圍：
1. Stage 0 Token：L2-a / L2-b / L2-c token 成本。
2. Qwen tokenizer 補測。
3. English rendering 補測。
4. 最小 CPU ct_eval benchmark。
5. 不建立新的 A/B/C benchmark。
6. 不提前進入 LLM extraction。

固定研究狀態：
- L2-b vs L2-a：o200k + 中文，n=20，28.4%，已通過 25% 門檻，但帶中文 rendering 偏誤。
- L3：8.8% < 10%，目前 Pending，不定案。
- L2-c：+3 token；token 指標不適用，不作失敗結論。

下一個正式研究階段：Stage 1 L1，人工 CT；不是 LLM 抽取。
