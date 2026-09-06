# 系統化分層應用方法論 v1.0 定義書初稿

**（Systematic Layered Application Methodology - Definition Specification v1.0）**

## 摘要與定位

「系統化分層應用方法論 v1.0」是一套專為大型語言模型（LLM）應用、Prompt 工程及複雜資訊系統所設計的 **「架構治理框架（Architecture Governance Framework）」**。

本方法論的核心目的不在於提供單一程式語言的寫法或工具操作手冊，而是透過 **五層遞進結構（Layer 1 ~ Layer 5）** 建立「責任分離」、「運行環境隔離」與「演化控制機制」，解決 LLM 系統在長期維護與複雜化過程中常見的 **「架構污染（Architecture Dilution）」** 與 **「結構熵增（Architectural Entropy）」** 危機。

## 第一章 核心概念與治理哲學

### 1.1 五層遞進架構與遞進關係

本方法論採用五層遞進結構，各層級具備不可替代且不可跨越的邏輯順序：

$$\text{Layer 1 (Why)} \rightarrow \text{Layer 2 (Rules)} \rightarrow \text{Layer 3 (Specs)} \rightarrow \text{Layer 4 (Verification)} \rightarrow \text{Layer 5 (Governance)}$$

```
Layer 1：存在合理性與需求來源 (Why does it exist?)
   │
   ▼
Layer 2：運作邏輯與限制條件治理 (How does it operate?)
   │
   ▼
Layer 3：可執行規格轉譯 (How is it built?)
   │
   ▼
Layer 4：案例驗證與結果分類 (Does it work?)
   │
   ▼
Layer 5：層級診斷與演化治理 (How does it evolve?)
```

- **Layer 1**：回答「為什麼此系統需要這些核心結構？」
    
- **Layer 2**：回答「這些結構如何互相作用以及系統允許與禁止什麼？」
    
- **Layer 3**：回答「如何將抽象架構轉換為可實作的強型別規格？」
    
- **Layer 4**：回答「此架構在實際情境中是否能產生預期結果？」
    
- **Layer 5**：回答「當面對異常與新需求時，如何判定歸因並控制演化？」
    

### 1.2 雙向建模模式與資訊可信度

本方法論支援正向開發與反向解析兩種運作模式，並針對資訊透明度建立標記原則：

1. **正向開發模式（Forward Engineering）**：從 Layer 1 到 Layer 5 完整的自上而下建構流程。
    
2. **反向架構建模模式（Reverse Architectural Modeling）**：基於公開文件與行為觀察，向上逆向推導系統模型。在反向模式下，**Layer 3 強制降級為「架構假設規格（Hypothetical Implementation Specification）」**，不得偽裝為真實內部工程數據。
    

|**系統層級**|**正向模式狀態**|**反向架構建模模式狀態**|**信心標記 MD**|
|---|---|---|---|
|**Layer 1 (Rationale)**|需求推導完成|依據公開功能推導|`[Derived - High]`|
|**Layer 2 (Rules)**|運作邏輯定義|行為觀察模型|`[Observed - Medium]`|
|**Layer 3 (Specification)**|可執行技術規格|架構假設規格|`[Hypothesis - Low]`|
|**Layer 4 (Verification)**|實機測試閉環|形式驗證與一致性沙盤推演|`[Simulated]`|
|**Layer 5 (Governance)**|演化控制機制|治理模擬與邊界防守|`[Governed]`|

## 第二章 層級責任與規範

### 2.1 Layer 1：存在合理性與需求來源 (Rationality & Basis)

#### 2.1.1 任務目標

確立系統核心架構元素存在的必要性與理論基礎，證明各實體不可替代。

#### 2.1.2 演化治理之必要性（Layer 5 存在的 L1 理由）

複雜系統在長期運行中必然面臨環境與需求變化。缺乏 Layer 5 時，系統異常將引發對 Layer 3（規格）或 Layer 1（架構）的盲目修改。因此，**演化治理（Layer 5）的存在是確保系統能在邊界內自我修正、維持結構一致性的必要防線**。

#### 2.1.3 責任邊界（不包含）

不包含流程設計、工程實作規格、資料庫 Schema、API 定義及實際案例驗證。

### 2.2 Layer 2：運作邏輯與限制條件治理 (Operational Rules & Scope)

#### 2.2.1 任務目標

定義系統內部資訊流轉、狀態變化規則，以及外部環境進入系統時的限制邊界。

#### 2.2.2 Runtime 邊界治理 (Runtime Boundary Governance)

將「系統內部規則」與「外部執行環境限制」進行責任分離：

- **系統內部責任**：包含狀態轉換規則、資料純化邏輯、結構定義。
    
- **外部 Runtime 責任**：包含 Context Window 限制、Token 預算上限、UI 檔案載入順序及外部介面限制。
    
- **原則**：**外部 Runtime 物理限制不得被誤判為 Layer 3 解析邏輯失效**。超長數據流轉必須採用「狀態帶入機制（Chunking & State Carry Forward）」而非原始數據疊加：
    

$$\text{Chunk}_n + \text{State Snapshot}_{n-1} \xrightarrow{\text{Parser}} \text{State Snapshot}_n$$

#### 2.2.3 輸入治理 (Input Governance) 與資料源/接口分離

1. **控制與資料分離（Envelope Separation）**：
    
    - **控制層（Control Layer）**：系統指令、轉譯規則（如 Master Prompt），擁有最高控制權。
        
    - **資料層（Data Layer）**：被分析之原始對象，嚴禁夾帶系統級控制指令。
        
2. **輸入資訊分類**：劃分為控制資訊、任務資訊、資料資訊與外部參考資訊。
    
3. **資料來源與輸入接口分離原則**：資料保存位置（Data Source）不等於外部執行單元取得資料的入口（Input Interface）。輸入接口代表受控的「授權與任務暴露範圍」，而非完整資料位置。
    

### 2.3 Layer 3：可執行規格轉譯 (Implementation Specification)

#### 2.3.1 任務目標

將抽象架構與運作邏輯轉譯為具體可執行的強型別 Schema 與數據結構規範。

#### 2.3.2 核心五表模型結構（維持原規格）

1. **Event_Table**：經純化萃取之獨立事件單元。
    
2. **State_Table**：系統與環境當前之實質狀態與矛盾。
    
3. **Task_Table**：基於當前狀態衍生之待辦任務與標準。
    
4. **Feedback_Table**：任務執行後之反饋與結案狀態。
    
5. **Evolution_Candidate_Table**：可供下游演化引擎判讀之模式鏈結。
    

#### 2.3.3 規格轉譯驗證報告 (Validation Report)

Layer 3 輸出必須包含結構化 Validation Report，記載當次轉譯之資料完整度、邊界狀態與診斷報告。

### 2.4 Layer 4：案例驗證與結果分類 (Run-Through Verification)

#### 2.4.1 任務目標與禁令

透過具體情境（Run-Through）驗證 Layer 3 規格是否符合 Layer 2 邏輯。 **禁令**：本層級僅記錄「驗證發現（Verification Findings）」，**嚴禁將本層級建立為案例資料庫，亦嚴禁根據單次測試結果修改 Layer 1/2 核心架構**。

#### 2.4.2 驗證結果狀態分類

驗證結果嚴禁簡化為二元成功/失敗，必須依照下表進行分類判定：

|**分類**|**意義**|**處置方向**|
|---|---|---|
|**Valid**|完全符合預期|驗證通過。|
|**Partial**|受限於外部 Runtime 限制未完整完成|歸因至 Layer 2 Runtime 邊界補強，不修改 Layer 3 Schema。|
|**Invalid**|違反系統規格或邏輯|觸發 Layer 5 問題診斷矩陣。|
|**Unknown**|資料或上下文不足無法判定|補充資料或回退檢視。|

## 第三章 Layer 5：層級診斷與演化治理邏輯

### 3.1 核心任務

建立系統變更、異常處理與長遠演化之診斷控制機制。Layer 5 不負責編寫程式碼或產出內容，其核心功能為 **「診斷 (Diagnosis)」** 與 **「變更控制 (Governance)」**。

### 3.2 系統觀察歸因矩陣 (Issue Attribution Matrix)

當系統出現異常現象或新變更需求（**系統觀察 System Issue**）時，禁止直接修改系統，必須依序通過以下矩陣診斷：

```
問題發生 (System Issue) ──► 影響範圍分析 ──► 責任層級歸因 ──► 演化決策產出 (Change Request) ──► 保留紀錄
```

|**診斷歸因層級**|**系統觀察特徵 (System Issue)**|**診斷條件與方向**|**許可修改範圍**|**嚴格禁止事項**|
|---|---|---|---|---|
|Layer 1<br><br>  <br><br>(存在合理性)|核心概念無法解釋需求來源；資料實體缺乏不可替代性。|重新檢視理論基礎與存在必要性。|修正架構存在宣告與理論依據。|禁止直接增加欄位或修改流程。|
|Layer 2<br><br>  <br><br>(運作邏輯)|資料流向不明；角色權限被污染；撞上外部 Runtime 物理限制。|調整資訊流轉規則、輸入治理 SOP 或 Runtime 邊界條件。|修正規則、邊界與流程定義。|禁止直接修改 Layer 3 資料結構 Schema。|
|Layer 3<br><br>  <br><br>(可執行規格)|理論與邏輯均正確，但輸出 Schema 欄位無法容納轉譯數據。|修正 Schema 定義、驗證規則或格式約束。|調整 Schema 欄位與驗證條件。|禁止破壞 Layer 2 之運作邊界。|
|Layer 4<br><br>  <br><br>(案例驗證)|架構與規格完整，但測試情境邊界覆蓋不足。|增加測試情境驗證與邊界極限測試。|補強 Run-Through 驗證流程。|禁止修改核心架構或變更 Schema。|
|Layer 5<br><br>  <br><br>(演化治理)|發現新需求，但無法確定修改會影響何處。|執行變更衝擊分析，產出變更決策紀錄。|產出 Change Request / ADR 規範。|禁止無視歸因直接盲目擴張系統。|

### 3.3 演化決策規範 (Change Request Standard)

任何架構變更必須填寫演化決策紀錄，保持追溯性：

Markdown

```
Change_Request_ID: EVO-CR-XXX

1. 系統觀察現象 (System Issue):
2. 主要歸因層級 (Attributed Layer): [Layer 1 / Layer 2 / Layer 3 / Layer 4 / Layer 5]
3. 受影響層級 (Impacted Layers):
4. 是否需要修改核心架構 (Core Architecture Altered): [YES / NO]
5. 修改位置與理由 (Modification Scope & Rationale):
6. 允許修改範圍 (Allowed Boundary):
7. 禁止修改範圍 (Prohibited Scope):
8. 需重新驗證之 Layer (Re-validation Required):
```

## 第四章 適用範圍與明確排除事項

### 4.1 適用範圍

1. **複雜 Prompt / LLM Agent 系統架構設計**：防止大型提示詞隨需求增加而崩潰。
    
2. **多源資料驅動應用之輸入與權限治理**：處理高風險資料流入與角色隔離。
    
3. **長期維護型軟體與 AI 應用的架構演化控制**[cite: 1, 2, 4]。
    

### 4.2 明確排除事項 (Explicit Exclusions)

為維持本方法論作為「架構治理框架」的通用性與純粹性，**以下內容明確禁止納入本方法論定義書主體**：

- ❌ **具體案例資料庫**：案例屬於 Layer 4 驗證過程資料，方法論僅定義驗證分類與診斷流程，不保存具體案例。
    
- ❌ **特定工具實作細節**：不綁定特定的工程框架（如 LangGraph, Ollama, API Controller）。
    
- ❌ **Prompt 語法細節**：不收錄特定提示詞字句，僅定義 Layer 3 規格產出標準。
    
- ❌ **特定 LLM 模型行為筆記**：模型硬體與廠商限制統一透過 Layer 2 Runtime Governance 抽象化處理，不綁定特定模型版本。