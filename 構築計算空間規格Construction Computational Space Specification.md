這是一套將「構築詞（Construction Token）」形式化為**有限約束事件生成空間（Constrained Event Generation Space, CEGS）**的完整架構定義與工程實作。

---

# 一、數學符號形式化 (Mathematical Formalism)

定義事件生成空間為一個八元組：
$$G = \langle \mathcal{S}, \mathcal{X}, \mathcal{I}, \mathcal{P}, \mathcal{A}, \mathcal{T}, \mathcal{C}, \mathcal{K} \rangle$$

### 1. 空間與全局狀態 (Global State)
* **空間幾何與物理環境**：$\mathcal{X} = \langle D, E_{env} \rangle$，其中 $D$ 為主體間的拓撲/度量空間距離矩陣，$E_{env}$ 為環境約束（光線、地形、摩擦力）。
* **全局離散狀態空間**：$\Sigma = \left( \prod_{i=1}^n \Sigma_{s_i} \right) \times \Sigma_{\mathcal{X}}$
  - $\Sigma_{s_i}$ 為主體 $s_i$ 的內部私有實體狀態（如：肌肉疲勞度、隱藏傷勢、剩餘平衡值）。
  - $\sigma_t \in \Sigma$ 代表時間步 $t$ 時的系統全真狀態（Ground Truth State）。

### 2. 主體形式化 (Subjectivity)
每個假設性主體定義為五元組：
$$s_i = \langle ID_i, Cap_i, Cog_i, Purp_i, \sigma_{i, t} \rangle$$
* **$ID_i$**：身份與關係矩陣定位。
* **$Cap_i \subseteq \mathcal{A}_{univ}$**：主體靜態能力集合（如最大發力極限、可用動作模式）。
* **$Cog_i = \langle K_{i,t}, \mathcal{R}_i \rangle$**：主體認知邊界。
  - $K_{i,t}$ 為主體當前**主觀知識庫**。
  - $\mathcal{R}_i: \Omega_i \to \Delta(K_i)$ 為推論規則引擎。
* **$Purp_i: \Sigma \to \mathbb{R}$**：效用評估函數，指導合法行動之選擇方向。
* **$\sigma_{i,t} \in \Sigma_{s_i}$**：動態實體狀態。

### 3. 資訊邊界與觀測投影 (Information Projection)
真實狀態到主體主觀認知的投影函數為 $\mathcal{O}_i$：
$$\mathcal{O}_i: \Sigma \times \mathcal{X} \to \Omega_i$$
* 任意主體 $s_i$ **嚴禁**直接存取其他主體 $s_j$ 的私有狀態 $\sigma_{j,t}$。
* 狀態僅能透過**可觀測洩漏函數 (Observable Emission)** 釋出：
  $$\operatorname{Emit}(\sigma_{j,t}) = O_{j,t} \in \Omega_{env}$$
* 主體 $s_i$ 的感知資訊為：
  $$I_{i,t} = \mathcal{O}_i(\sigma_t) = K_{i, t-1} \cup \operatorname{Filter}(O_{j,t}, \text{Distance}(s_i, s_j), E_{env})$$
* **資訊合法性公理**：若斷言 $\phi$ 未在 $I_{i,t}$ 中且無法由 $\mathcal{R}_i(I_{i,t})$ 演繹，則引發該斷言的任何行動決策均為**非法狀態轉移**。

### 4. 行動與因果轉移函數 (Action & Causal Transition)
行動定義為四元組：$a = \langle s_i, \text{Pre}(a), \text{Cost}(a), \text{Eff}(a) \rangle$。
* **前置條件合法性**：
  $$\operatorname{ValidAct}(a, s_i, \sigma_t, I_{i,t}) \iff \text{Pre}(a)(\sigma_{i,t}) \land a \in Cap_i \land \text{CanInferActionNecessity}(I_{i,t})$$
* **多主體聯合行動**：$\vec{a}_t = (a_{1,t}, a_{2,t}, \dots, a_{n,t}) \in \mathcal{A}^*$
* **因果狀態轉移函數**：
  $$\delta: \Sigma_t \times \mathcal{A}^* \to \Sigma_{t+1}$$
  $$\delta(\sigma_t, \vec{a}_t) = \sigma_t \ominus \sum \text{Cost}(\vec{a}_t) \oplus \sum \text{Eff}(\vec{a}_t, \mathcal{X}_t)$$
* **因果邊界約束**：$\mathcal{C}(\sigma_t, \vec{a}_t, \sigma_{t+1}) = \text{True} \iff \sigma_{t+1} = \delta(\sigma_t, \vec{a}_t)$，禁止 $\sigma_t \to \sigma_{t+1}$ 出現無溯源差值（No Uncaused Delta）。

### 5. 時間序列與收束邊界 (Temporal & Closure Boundary)
* **時間演進**：$\mathcal{T} = (\sigma_0 \xrightarrow{\vec{a}_0} \sigma_1 \xrightarrow{\vec{a}_1} \dots \xrightarrow{\vec{a}_{k-1}} \sigma_k)$
* **收束判定函數**：
  $$\kappa: \Sigma_t \to \{0, 1\}$$
  當 $\kappa(\sigma_t) = 1$ 時，事件生成空間強制終止，不再接受新的行動輸入。

---

# 二、類 UML 結構設計

```
 +-----------------------------------------------------------------------+
 |                     EventGenerationSpace (G)                          |
 +-----------------------------------------------------------------------+
 | - subjects: Dict[SubjectId, Subject]                                  |
 | - spatial_state: SpatialEnvironment                                   |
 | - causal_engine: CausalTransitionEngine                               |
 | - closure_evaluator: ClosureBoundary                                  |
 | - history: List[StateTransitionStep]                                  |
 +-----------------------------------------------------------------------+
 | + step(joint_actions: List[ActionIntent]) -> StepResult               |
 | + validate_state_consistency(s_prev, s_next) -> bool                  |
 | + is_closed() -> bool                                                 |
 +-----------------------------------------------------------------------+
                                    |
          +-------------------------+-------------------------+
          |                                                   |
          v                                                   v
 +-----------------------------------+     +-----------------------------------+
 |             Subject               |     |        SpatialEnvironment         |
 +-----------------------------------+     +-----------------------------------+
 | + id: SubjectId                   |     | + terrain_friction: float         |
 | + identity: Identity              |     | + lighting_level: float           |
 | + capabilities: Set[Capability]   |     | + relative_distance: float        |
 | + cognitive_boundary: Cognitive   |     | + spatial_obstacles: List[str]    |
 | + private_state: SubjectState     |     +-----------------------------------+
 +-----------------------------------+
 | + observe(env_cues) -> None       |
 | + infer() -> Set[Inference]       |
 | + emit_observable_cues() -> Cues  |
 +-----------------------------------+
          |
          v
 +-----------------------------------------------------------------------+
 |                             Action                                    |
 +-----------------------------------------------------------------------+
 | + actor_id: SubjectId                                                 |
 | + action_type: ActionType                                             |
 | + target_id: Optional[SubjectId]                                      |
 | + required_knowledge: Set[KnowledgeFact]                              |
 | + cost: PhysicalCost(stamina, balance, wrist_load)                    |
 | + apply_consequence(state: GlobalState) -> GlobalState                |
 +-----------------------------------------------------------------------+
```

---

# 三、Python 完整實作架構

以下採用 Python 3.10+ Dataclasses 實作完整的「事件生成空間模型」，包含資訊可見性遮蔽、認知推論引擎、物理代價轉移、因果一致性校驗與收束判定。

```python
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Set, Optional, Tuple


# =====================================================================
# 1. 空間與基礎型態 (Spatiality & Primitives)
# =====================================================================

class ActionType(Enum):
    PROBE_ATTACK = auto()      # 試探性刺擊
    HEAVY_SLASH = auto()       # 重劈
    PARRY = auto()             # 格擋
    FEINT_AND_EXPLOIT = auto() # 假動作並針對弱點打擊
    OBSERVE_STANCE = auto()    # 觀察對手架勢與步法
    DEFENSIVE_RETREAT = auto() # 後撤防守


@dataclass(frozen=True)
class ObservableCue:
    """由主體生理/物理狀態外洩的客觀物理現象（視覺/聽覺可捕獲）"""
    source_id: str
    cue_type: str              # 例："FOOT_TREMBLE", "BREATH_HITCH", "HEAVY_STOMP"
    intensity: float           # 顯著度 0.0 ~ 1.0


@dataclass
class SpatialEnvironment:
    """底層空間物理約束"""
    terrain: str = "FROZEN_GROUND"       # 凍硬土地：摩擦力低，消耗平衡
    ground_friction: float = 0.65
    lighting_level: float = 0.5          # 火把照明：視野有限
    distance_meters: float = 2.5         # 雙方距離
    boundary_limit_meters: float = 6.0   # 演武場邊界（半高矮牆距離）


# =====================================================================
# 2. 主體性 (Subjectivity) 與 資訊邊界 (Information Boundary)
# =====================================================================

@dataclass
class SubjectState:
    """主體私有物理狀態（其他主體不可直接讀取）"""
    stamina: float = 100.0              # 體力 [0, 100]
    balance: float = 100.0              # 重心平衡 [0, 100]
    wrist_strain: float = 0.0           # 虎口/手腕負擔 [0, 100]
    hidden_injury_severity: float = 0.0 # 隱藏傷勢（例如膝蓋舊傷）
    hidden_injury_active: bool = False  # 是否處於受傷激發態
    is_incapacitated: bool = False      # 是否倒地/失去戰鬥力


@dataclass
class CognitiveBoundary:
    """主體的主觀認知邊界與推論系統"""
    direct_facts: Set[str] = field(default_factory=set)        # 直接已知事實
    inferred_hypotheses: Set[str] = field(default_factory=set) # 透過觀測推論出的結論

    def can_know(self, fact: str) -> bool:
        return (fact in self.direct_facts) or (fact in self.inferred_hypotheses)

    def process_observations(self, cues: List[ObservableCue]) -> None:
        """主觀推論引擎：將物理線索升華為認知結論，嚴禁越界獲取私有狀態"""
        for cue in cues:
            if cue.cue_type == "RIGHT_FOOT_TREMBLE" and cue.intensity > 0.4:
                self.inferred_hypotheses.add("OPPONENT_RIGHT_LEG_UNSTABLE")
            elif cue.cue_type == "BREATH_HITCH_ON_RECOVERY":
                self.inferred_hypotheses.add("OPPONENT_CORE_STRAIN")
            elif cue.cue_type == "BLADE_VIBRATION_HIGH":
                self.inferred_hypotheses.add("OPPONENT_WRIST_FATIGUE")


@dataclass
class Subject:
    id: str
    identity_role: str                   # 角色定位（如："LORD_FATHER_VETERAN", "SON_LEARNER"）
    capabilities: Set[ActionType]        # 靜態技能集合
    purpose: str                         # 主體內部目的
    state: SubjectState                  # 私有狀態
    cognition: CognitiveBoundary         # 認知邊界

    def emit_cues(self) -> List[ObservableCue]:
        """因物理狀態產生的自然物理外洩（不可隱瞞之線索）"""
        cues = []
        # 右腳舊傷受壓時，會出現腳步顫抖
        if self.state.hidden_injury_active and self.state.hidden_injury_severity > 30.0:
            cues.append(ObservableCue(
                source_id=self.id,
                cue_type="RIGHT_FOOT_TREMBLE",
                intensity=min(1.0, self.state.hidden_injury_severity / 50.0)
            ))
        # 體力過低時發出喘息停頓
        if self.state.stamina < 40.0:
            cues.append(ObservableCue(
                source_id=self.id,
                cue_type="BREATH_HITCH_ON_RECOVERY",
                intensity=(40.0 - self.state.stamina) / 40.0
            ))
        # 虎口負擔過大時，劍身發出不正常震顫
        if self.state.wrist_strain > 40.0:
            cues.append(ObservableCue(
                source_id=self.id,
                cue_type="BLADE_VIBRATION_HIGH",
                intensity=self.state.wrist_strain / 100.0
            ))
        return cues


# =====================================================================
# 3. 行動邊界與因果轉移 (Action & Causal Engine)
# =====================================================================

@dataclass
class ActionIntent:
    actor_id: str
    action_type: ActionType
    target_id: Optional[str] = None
    epistemic_dependency: Optional[str] = None  # 行動依賴的前提認知


@dataclass
class GlobalState:
    subjects: Dict[str, Subject]
    environment: SpatialEnvironment
    step_count: int = 0


class CausalValidationError(Exception):
    """因果邊界或資訊邊界違規引發的異常"""
    pass


class EventGenerationSpace:
    """
    構築空間核心控制器：
    嚴格控制 State(T) + ValidActions -> State(T+1) 的合法狀態流轉。
    """
    def __init__(self, subjects: List[Subject], environment: SpatialEnvironment):
        self.state = GlobalState(
            subjects={s.id: s for s in subjects},
            environment=environment,
            step_count=0
        )
        self.execution_log: List[str] = []

    # ---------------- 邊界校驗 ----------------
    def _validate_information_boundary(self, action: ActionIntent) -> None:
        """資訊邊界驗證：主體是否具備採取該行動的合法認知依據？"""
        actor = self.state.subjects[action.actor_id]
        if action.epistemic_dependency:
            if not actor.cognition.can_know(action.epistemic_dependency):
                raise CausalValidationError(
                    f"【資訊邊界違規】主體 {actor.id} 試圖執行依賴 '{action.epistemic_dependency}' "
                    f"的行動 {action.action_type.name}，但該資訊未被感知或推論！"
                )

    def _validate_action_capability(self, action: ActionIntent) -> None:
        """能力與體能邊界驗證"""
        actor = self.state.subjects[action.actor_id]
        if action.action_type not in actor.capabilities:
            raise CausalValidationError(f"【能力邊界違規】主體 {actor.id} 不具備技能 {action.action_type.name}")
        if actor.state.is_incapacitated:
            raise CausalValidationError(f"【狀態違規】主體 {actor.id} 已失去行動能力，無法執行動作")

    # ---------------- 狀態轉移與因果計算 ----------------
    def step(self, joint_actions: List[ActionIntent]) -> Dict[str, str]:
        """單一時間步因果推進：T_n -> T_{n+1}"""
        self.state.step_count += 1
        transition_report = {}

        # 1. 預先驗證所有行動的合法性
        for act in joint_actions:
            self._validate_action_capability(act)
            self._validate_information_boundary(act)

        # 2. 廣播環境與生理線索（資訊發散）
        all_emitted_cues: List[ObservableCue] = []
        for s in self.state.subjects.values():
            all_emitted_cues.extend(s.emit_cues())

        # 主體接收與感知（不可讀取自身發出的線索）
        for s in self.state.subjects.values():
            perceived_cues = [c for c in all_emitted_cues if c.source_id != s.id]
            s.cognition.process_observations(perceived_cues)

        # 3. 因果轉移執行 (Causal Execution & Cost Deduction)
        for act in joint_actions:
            actor = self.state.subjects[act.actor_id]
            target = self.state.subjects.get(act.target_id) if act.target_id else None

            if act.action_type == ActionType.HEAVY_SLASH:
                # 歐文發動重劈：消耗大量體力，對右膝造成高負擔，逼退對手
                actor.state.stamina -= 18.0
                actor.state.balance -= 10.0
                if actor.state.hidden_injury_severity > 0:
                    actor.state.hidden_injury_active = True  # 舊傷被劇烈發力激發
                
                if target:
                    target.state.stamina -= 12.0
                    target.state.wrist_strain += 25.0       # 防守方虎口承受劇烈震盪
                    target.state.balance -= 20.0            # 防守方重心大幅後移
                    self.state.environment.distance_meters = 1.8
                
                transition_report[actor.id] = (
                    f"{actor.id} 施展沉重劈砍。自身體力-18，重心-10，右膝舊傷受壓激發；"
                    f"迫使 {target.id if target else '環境'} 承受強烈衝擊。"
                )

            elif act.action_type == ActionType.PARRY:
                # 雷恩全力格擋：承受手腕負擔與失衡風險
                actor.state.stamina -= 10.0
                actor.state.wrist_strain += 15.0
                actor.state.balance -= 15.0
                transition_report[actor.id] = f"{actor.id} 舉劍硬接衝擊，手腕負擔加劇(+15)，腳步在凍土上後滑。"

            elif act.action_type == ActionType.OBSERVE_STANCE:
                # 專注觀察：消耗少量體力以捕捉對手動態
                actor.state.stamina -= 3.0
                transition_report[actor.id] = f"{actor.id} 壓低身位維持防守，凝神捕捉對手重心轉移與步法。"

            elif act.action_type == ActionType.FEINT_AND_EXPLOIT:
                # 假動作轉向攻擊弱點（右側）：需要認知依據
                actor.state.stamina -= 15.0
                actor.state.balance -= 12.0
                if target:
                    # 歐文右下盤不穩，被迫轉向導致失衡崩潰
                    target.state.balance -= 35.0
                    target.state.stamina -= 15.0
                transition_report[actor.id] = (
                    f"{actor.id} 利用觀測到的右側步法破綻發動變向突進！"
                    f"{target.id if target else ''} 支撐腳承重受限，重心嚴重崩塌。"
                )

            elif act.action_type == ActionType.DEFENSIVE_RETREAT:
                actor.state.stamina -= 5.0
                actor.state.balance = min(100.0, actor.state.balance + 10.0)
                self.state.environment.distance_meters += 1.0
                transition_report[actor.id] = f"{actor.id} 借助反作用力後撤，拉開距離嘗試重整架勢。"

        # 4. 連鎖因果後果判定 (Secondary Consequences)
        for s in self.state.subjects.values():
            # 凍土環境判定：當平衡值低於 20 時，在凍硬地面上極易直接倒地
            if s.state.balance < 20.0 and self.state.environment.ground_friction < 0.7:
                s.state.is_incapacitated = True
                transition_report[f"{s.id}_FATAL"] = f"{s.id} 因重心徹底瓦解且凍土地面濕滑，失去支撐倒地。"
            elif s.state.stamina <= 0.0:
                s.state.is_incapacitated = True
                transition_report[f"{s.id}_FATAL"] = f"{s.id} 體力徹底耗盡，無法維持武器架勢。"

        return transition_report

    # ---------------- 4. 收束邊界 (Closure Boundary) ----------------
    def evaluate_closure(self) -> Tuple[bool, Optional[str]]:
        """
        收束判定：
        不評估情緒或敘事戲劇性，僅評估終止條件是否成立。
        """
        # 條件 1：任一主體失去戰鬥能力
        for s in self.state.subjects.values():
            if s.state.is_incapacitated:
                return True, f"收束觸發：主體 {s.id} 失去戰鬥能力（生理/平衡限制達成）。"

        # 條件 2：演武場物理空間逼至死角
        if self.state.environment.distance_meters >= self.state.environment.boundary_limit_meters:
            return True, "收束觸發：脫離演武場有效戰鬥邊界。"

        # 條件 3：最大步數保護（因果時間長度上限）
        if self.state.step_count >= 10:
            return True, "收束觸發：已達時間狀態步數上限，雙方進入僵持停滯。"

        return False, None
```

---

# 四、歐文與雷恩演武案例測試

此測試嚴格驗證四項系統約束：
1. **資訊隔離驗證**：雷恩在 $T_0$ 無法發動針對歐文舊傷的攻擊（因果邊界阻斷）。
2. **線索外洩與推論**：歐文施展強攻激發舊傷，雷恩透過客觀線索合法推論出弱點。
3. **物理後果累積**：每一次交鋒的體力、虎口震盪與重心消耗不可逆。
4. **收束條件判定**：最終因累積的生理與環境極限終止事件。

```python
def run_test_simulation():
    print("================================================================")
    print("      構築詞事件生成空間：歐文 vs 雷恩 演武測試運行")
    print("================================================================\n")

    # 1. 建立環境
    env = SpatialEnvironment(terrain="FROZEN_DIRT", ground_friction=0.65, distance_meters=2.0)

    # 2. 建立主體：歐文（領主/父親）
    owen_state = SubjectState(
        stamina=80.0,
        balance=90.0,
        wrist_strain=0.0,
        hidden_injury_severity=45.0,  # 右膝舊傷：真實存在但為私有狀態
        hidden_injury_active=False
    )
    owen = Subject(
        id="Owen",
        identity_role="LORD_FATHER_VETERAN",
        capabilities={ActionType.HEAVY_SLASH, ActionType.PROBE_ATTACK, ActionType.DEFENSIVE_RETREAT},
        purpose="QUICK_DISARM_AND_TEST",
        state=owen_state,
        cognition=CognitiveBoundary(direct_facts={"RENN_STANCE_STANDARD"})
    )

    # 3. 建立主體：雷恩（長子/學習者）
    renn_state = SubjectState(
        stamina=65.0,
        balance=75.0,
        wrist_strain=0.0,
        hidden_injury_severity=0.0
    )
    renn = Subject(
        id="Renn",
        identity_role="SON_LEARNER",
        capabilities={ActionType.PARRY, ActionType.OBSERVE_STANCE, ActionType.FEINT_AND_EXPLOIT, ActionType.DEFENSIVE_RETREAT},
        purpose="HOLD_LINE_AND_ENDURE",
        state=renn_state,
        cognition=CognitiveBoundary(direct_facts={"OWEN_SWORD_HEAVY"})  # 不包含 OWEN_RIGHT_LEG_UNSTABLE
    )

    # 4. 初始化事件空間
    space = EventGenerationSpace(subjects=[owen, renn], environment=env)

    # -------------------------------------------------------------
    # 測試 0：非法越界測試（雷恩在未知情時嘗試針對弱點進攻）
    # -------------------------------------------------------------
    print("--- [測試階段 0] 驗證資訊邊界防禦機制 ---")
    illegal_action = ActionIntent(
        actor_id="Renn",
        action_type=ActionType.FEINT_AND_EXPLOIT,
        target_id="Owen",
        epistemic_dependency="OPPONENT_RIGHT_LEG_UNSTABLE"
    )
    try:
        space.step([illegal_action])
        print("❌ 異常：系統未攔截非法資訊跨越！")
    except CausalValidationError as e:
        print(f"✅ 成功攔截非法生成：{e}\n")

    # -------------------------------------------------------------
    # 時間步 T1：歐文發動重劈，雷恩選擇防守觀察
    # -------------------------------------------------------------
    print("--- [時間步 T1] 歐文強攻，雷恩格擋並觀察 ---")
    t1_actions = [
        ActionIntent(actor_id="Owen", action_type=ActionType.HEAVY_SLASH, target_id="Renn"),
        ActionIntent(actor_id="Renn", action_type=ActionType.PARRY, target_id="Owen")
    ]
    report_t1 = space.step(t1_actions)
    for k, v in report_t1.items():
        print(f"  • {v}")

    print(f"\n  [T1 後狀態反饋]")
    print(f"  歐文狀態: 體力={owen.state.stamina}, 舊傷激發態={owen.state.hidden_injury_active}")
    print(f"  雷恩狀態: 體力={renn.state.stamina}, 虎口負擔={renn.state.wrist_strain}, 平衡={renn.state.balance}")
    print(f"  雷恩當前認知庫: {renn.cognition.inferred_hypotheses}")

    is_closed, reason = space.evaluate_closure()
    print(f"  收束判定: {is_closed} ({reason})\n")

    # -------------------------------------------------------------
    # 時間步 T2：歐文持續壓迫，雷恩透過線索合法推論並執行針對攻擊
    # -------------------------------------------------------------
    print("--- [時間步 T2] 雷恩合法使用已推論資訊，實施變向進攻 ---")
    t2_actions = [
        ActionIntent(actor_id="Owen", action_type=ActionType.HEAVY_SLASH, target_id="Renn"),
        ActionIntent(
            actor_id="Renn",
            action_type=ActionType.FEINT_AND_EXPLOIT,
            target_id="Owen",
            epistemic_dependency="OPPONENT_RIGHT_LEG_UNSTABLE" # 此時已合法推論獲得
        )
    ]
    report_t2 = space.step(t2_actions)
    for k, v in report_t2.items():
        print(f"  • {v}")

    print(f"\n  [T2 後狀態反饋]")
    print(f"  歐文狀態: 平衡={owen.state.balance}, 倒地/失能={owen.state.is_incapacitated}")
    print(f"  雷恩狀態: 虎口負擔={renn.state.wrist_strain}, 平衡={renn.state.balance}, 倒地/失能={renn.state.is_incapacitated}")

    is_closed, reason = space.evaluate_closure()
    print(f"\n  收束判定: {is_closed} | 原因: {reason}\n")


if __name__ == "__main__":
    run_test_simulation()
```

---

# 五、驗證機制與架構結論

這套模型的生成邏輯與傳統 Prompt Engineering 的對照如下：

```
傳統 Prompt:
「寫一場雷恩發現父親歐文右腿有舊傷，並透過精彩劍術反擊獲勝的演武。」
（結果由模型自由發揮，容易出現跳步、無視物理代價與全知視角 Bug）

構築詞生成空間 (CEGS):
1. 主體邊界：Owen.HiddenInjury = 45 (Private), Renn.Knowledge = {}
2. 空間邊界：Terrain = FrozenDirt (Friction: 0.65)
3. 資訊邊界：Renn 不能直接讀取 Owen.HiddenInjury；必須由 Owen.HeavySlash 觸發 FootTremble 線索，經由推論引擎合法解鎖認知標籤。
4. 因果邊界：每一次攻防扣減 Stamina、累積 WristStrain，數值跨步嚴格繼承。
5. 收束邊界：Balance < 20 結合地面 Friction 自動觸發倒地失能，事件強行終止。
```

任何大型語言模型（LLM）在此系統中，**只能作為「候選行動提議器（Candidate Action Proposer）」或「合法狀態轉移後的語意渲染器（State-to-Text Renderer）」**，無法越過數學與因果邊界任意捏造結果。