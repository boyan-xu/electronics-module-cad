# Evaluation / 验证记录

## Lean research update / 精简研究更新 — 2026-10-28

The entrypoint now routes research and CAD detail separately. Source screening precedes deep parsing; task-local CSVs, exact-package reuse, hash/parser-aware extraction reuse and two-round no-progress stopping are documented. All original geometry/pin/clearance acceptance conditions remain required. 新流程采用先筛后解析、按需加载和增量续查。

`python -m unittest discover -s tests -p 'test_*.py'`: **8 tests passed**, including nonfinite/missing sizes, duplicate refs, invalid source/package/status/side, malformed/missing tables, hash syntax, unresolved counts, bounded default output and read-only behavior. The first six tests were observed failing before the checker existed, then passed; two further boundary checks passed after implementation. No CAD or source-authenticity claim follows from a passing checker.

Fresh baseline evaluation was attempted but the test agent failed due to account usage limits before answering. No fresh independent baseline, with-Skill behavioral run, wording micro-test or final independent review completed for this revision. The author reviewed A–AB for retained decisions and AC–AJ for the new workflow; this is self-review, not independent behavioral evidence. 不能把静态自查写成独立验收，旧结果继续保留为历史。

Self-review findings: A/I reuse existing geometry and measure missing metadata; B/C/U/V/W/X/Y/Z/AB retain the research hierarchy and missing-data boundaries; D/E keep identity/conflict/access limits; F/G/K/Q/R/T retain per-side final face-offset and nominal requirements; H/J/L preserve tool choice and verification limits; M/N/O/P/S/AA retain all parts, one solid, grouped features and correctly oriented PinMap. AC rejects mismatches before parsing; AD stops only without useful leads; AE resumes on concrete new evidence; AF invalidates changed extraction; AG separates unknown variants; AH restricts returned raw text; AI does not certify truth from tables; AJ leaves historical reports intact.

Controlled reading comparison uses the same simulated source packets, excluding answers from both input sizes. At baseline `cd8e0bd`, SKILL.md is 24,889 UTF-8 bytes; the revised entrypoint is 8,203 bytes, and research reference is 8,901 bytes (17,104 total for the default research route). The old research entrypoint alone was 24,889 bytes. This is a text-volume proxy, not tokenizer billing or a measured agent speedup. CAD reference remains conditional; README/test history are not runtime inputs. 新研究路线读取量减少约 31%，仅入口减少约 67%；不能说真实 Token 节省相同比例。

Controlled local fixture checks: twenty component rows may reference one verified package, preserving all twenty placements; different-maker 0603 remains separate. Duplicate source bytes need no repeated extraction under identical parsing conditions; changed bytes invalidate the derived evidence. These are prescribed workflow decisions, not measured network download counts. Live before/after search calls, downloads, elapsed research time and billed Token counts were **not measured**; no speed or success-rate improvement is claimed. Checker test runtime is not research runtime.

No CAD/EDA install, model, PinMap geometry, face offset, STEP export or physical fit test ran. Existing Tmall research and all original downloads were left unchanged; the exact-product data gap remains unresolved. 未重新搜索商品，也未将通用板作为商品替代。

Package checks: UTF-8, ten relative links, portable paths, UI invocation/policy and official Skill validator passed. The validator initially used Windows GBK defaults and failed to read UTF-8; rerunning with Python `-X utf8` passed, without changing its code or global settings. Git whitespace checks passed; Git reported its existing LF/CRLF conversion warnings. No new third-party runtime dependency was installed.

Historical evaluation / 历史评估日期: 2026-10-26

The results below apply to the original Skill contract only. They do not certify the component-completeness, single-solid, PinMap or final Offset Face requirements added on 2026-10-27. Current checks are recorded separately below.
以下结果仅适用于最初版本，不能证明 2026-10-27 新增的全部元件、单实体、独立引脚草图与最后偏移面要求；本次检查另行记录。

## Method / 方法

A fresh baseline agent answered nine simulated cases before the Skill was written. No material failure was observed; there is no measured improvement claim over that baseline.
编写前，一个独立基线助手回答了九个模拟场景，未观察到实质错误；不能据此宣称 Skill 相比基线提高了成功率。

After creation, a different fresh-context agent read only `SKILL.md` and its optional CAD reference. It answered twelve scenario inputs without reading the expected-result table. The author compared each answer with the acceptance conditions in [scenarios.md](scenarios.md).
编写后，另一个新上下文助手只读 Skill 与可选 CAD 参考，不读预期答案；作者逐项对照用例验收条件检查。

## Observed decisions / 实际判断

| Case | Observed result / 观察结果 | Verdict / 结论 |
| --- | --- | --- |
| A: supplied model | Adopt exact STEP, preserve original, stop replacement research / 直接复用对应模型 | Pass / 通过 |
| B: supplied sizes | Keep 30 × 20 × 1.6 mm; seek maker model, then only missing hole/height evidence / 保留已有尺寸 | Pass / 通过 |
| C: missing dimensions | Seek maker CAD/drawings before distributor evidence; no sizes invented / 不从无比例图猜尺寸 | Pass / 通过 |
| D: conflicting revisions | Ask for selected revision; keep A/B conflicts separate / 版本未定则先确认 | Pass / 通过 |
| E: blocked link | Request identity and accessible evidence; no claimed page access / 不虚报读到页面 | Pass / 通过 |
| F: clearance | 20.4 × 30.4 × 2.0 mm, Ø6.4 mm, hole Ø2.2 unchanged, X −0.2..20.2 mm / 间隙与基准正确 | Pass / 通过 |
| G: already offset | Reuse envelope once; request nominal source if needed; no shrink-to-recover / 不重复添加 | Pass / 通过 |
| H: no CAD | Agree script target; disclose not executed/not verified; no forced install / 不强制下载 | Pass / 通过 |
| I: absent metadata | Measure existing hole geometry before searching or asking / 先测已有几何 | Pass / 通过 |
| J: other CAD app | Use chosen capable app; check units and export support / 工具不绑定 | Pass / 通过 |
| K: uncertain/other offset | Clarify unknown offset; rebuild 0.2 mm from nominal for known 0.1 mm case / 不累加偏移 | Pass / 通过 |
| L: unchecked output | State fit is unverified and separate software from physical checks / 不虚报验证 | Pass / 通过 |

The independent evaluator found no instruction gap in those twelve cases. This is one observed evaluation, not a guarantee for all models or agents.
评估助手未在这十二例中发现说明缺口；这是一次实际观察，不是对所有模型与助手的保证。

## Package checks / 包检查

- The Skill Creator `quick_validate.py` returned `Skill is valid!` with exit code 0.
  Skill Creator 格式检查通过，退出码为 0。
- UI YAML parsed; invocation name and automatic discovery policy checked; no required MCP dependency.
  UI 元数据解析通过，调用名称与自动发现规则正确，没有强制 MCP 依赖。
- Relative documentation links resolve; text is UTF-8; no host-specific user path or unfinished scaffold was found.
  相对文档链接可解析，文本为 UTF-8，未发现本机用户绝对路径或未完成模板。

The validator used a temporary, isolated PyYAML dependency. It is not a runtime dependency of this Skill.
验证器使用临时隔离的 PyYAML，不是 Skill 的运行依赖。

## Not run / 未执行

No actual product page research, CAD connection, model creation, STEP export/reimport, preview inspection, or physical assembly was performed. No product link or real model was provided for this implementation task. GitHub publication is separate from these local checks.
本次没有真实商品链接或模型，因此未执行商品资料查找、CAD 连接、建模、STEP 导出重开、预览检查及实物装配；GitHub 发布也不属于这些本地检查。

## Historical single-solid update / 单实体更新历史 — 2026-10-27

The update requires every board component, one connected solid per board file, grouped construction operations, one dedicated PinMap sketch, and final Offset Face clearance. Only Skill/docs/tests were changed; no CAD task was executed.
本次要求全部元件、每份板卡文件单一连通实体、分组合并构造步骤、独立引脚草图及最后偏移面；只改 Skill、文档和测试，没有执行建模。

### Baseline gaps / 旧规则基线缺口

A fresh read-only agent applied the pre-update Skill to cases M–T before edits. Its decisions exposed the missing requirements below; these are contract gaps, not claims about a failed CAD execution.
修改前，独立只读助手按旧 Skill 处理 M–T；以下为实际观察到的规则缺口，不是 CAD 运行失败记录。

| Case | Old decision / 旧判断 | Updated decision checked / 已核对的新判断 |
| --- | --- | --- |
| M | Add only fit-critical missing parts / 只补影响装配的缺件 | Inventory all 14, reuse 11 correct parts, add all 3 missing parts / 全部元件逐项覆盖 |
| N | Keep 12 imported bodies / 保留 12 实体 | Close non-critical gaps and union to one valid connected solid / 简化连接并合成单实体 |
| O | Separate sketches by height were allowed / 可按高度另建草图 | One compatible construction sketch, two grouped Join extrusions for 2/3 mm / 共草图、分高度拉伸 |
| P | Labels and CAD mechanism unspecified / 未要求引脚标注方式 | Dedicated PinMap, physical IDs plus known signals, correct view and documented connector contacts / 独立草图及完整对应 |
| Q | File body count and exact operation order unspecified / 实体数与操作顺序未定 | Complete nominal + PinMap, save, copy, Offset Face last, one solid per file / 顺序与文件约束明确 |
| R | Conservative bounding envelope permitted / 可用粗略外包体 | Repair nominal/selection, retry final face offset, or report incomplete / 不以外包体兜底 |
| S | New Body accepted for each extrusion / 每次可新建实体 | Initial PCB body once, then Join, no leftover tool bodies / 后续合并 |
| T | Alternate envelope route permitted / 可改用外包方法 | Missing face-offset capability means incomplete clearance; no scaling substitute / 不冒充完成 |

### Independent evaluation and refinement / 独立复测与修订

A different fresh-context agent read only the updated Skill/reference and applied cases A–T, without reading the expected-result table. The author checked its decisions against the scenarios. Existing research, identity, units, hole preservation and no-CAD boundaries remained covered, alongside the eight new cases.
另一个新上下文助手只读修改后的 Skill 与工具参考，不读预期答案，处理 A–T 共 20 个场景；作者逐项核对，覆盖原有资料流程与新增八例。

That review found an ambiguity for pre-offset imports with no feature history. The instructions now preserve such inputs unchanged, but do not certify the final Offset Face operation; a compliant new pair requires nominal geometry. Connector contact scope was also clarified to include documented mating contacts even when hidden in previews.
复测发现已有避让文件无历史时的歧义，已明确原件不重复偏移，但不能宣称最后偏移面已验证，合规新交付仍需真实几何；同时明确连接器壳内有文档的配合接点也要标注。

A third fresh-context agent reran G, P, Q, R and T against the final text, including a four-contact hidden connector. All five decisions matched the revised acceptance conditions, and it found no material contradiction in those cases. This gives 20-case coverage with five targeted final rechecks; it is not a statistical reliability or CAD-success claim.
第三个新上下文助手按最终文本重测 G、P、Q、R、T，包含四接点连接器，五项均符合修订条件，未发现实质冲突。结果是 20 例覆盖、其中五例最终复测，不是统计可靠性或真实 CAD 成功率证明。

### Package and scope checks / 包与范围检查

Skill Creator format validation, UI YAML/invocation policy, relative links, UTF-8, portable paths and Git whitespace checks passed. No required CAD app, connector or runtime dependency was added. The original 2026-10-26 evaluation remains above as historical evidence.
Skill Creator 格式、UI 元数据与调用策略、相对链接、UTF-8、路径可移植性及 Git 空白检查通过；没有新增强制软件、连接器或运行依赖，旧评估保留为历史。

No CAD app was opened, no Pico geometry was imported or changed, and no model, clearance body, export or physical fit test was created by this update. Future real modeling must still check the complete component inventory, body count, pin positions, history order and measured clearance in CAD.
本次没有打开 CAD、导入或修改 Pico 几何，也没有创建模型、避让体、导出或试装；后续真实建模仍需实际核对元件清单、实体数、引脚位置、操作顺序与间隙。

## Research-order update / 资料顺序更新 — 2026-10-27

This update changes discovery to **3D source → PCB layout → other data**, with body dimensions established before modeling each component. The earlier evaluations above remain historical; they do not certify this new routing.
本次改为先 3D 源文件、再 PCB 布局、最后其他资料，并要求每个元件先查本体尺寸；上方评估保留为历史，不能当作本次新顺序的验证。

### Baseline observations / 基线观察

A fresh read-only agent applied the pre-update Skill/reference to seven raw cases before the core edit. It recorded seller dimensions before maker-model discovery, treated PCB/Gerber files under general gap research, and reported no explicit PCB-source hierarchy or PCB-to-sketch method. It correctly avoided invented heights/courtyard sizes and continued searching when a known-SKU link was blocked. These correct decisions are not labeled failures.
核心修改前，新上下文助手按旧规则处理七例；旧文先记录给定尺寸再查厂家模型，PCB/Gerber 归入一般补缺，未明确 PCB 优先级与草图来源。它已正确拒绝猜高度或占位尺寸，也会继续查已知 SKU 的受阻链接；这些正确行为不算失败。

The gaps were explicit research priority, distinguishing layout from manufacturing/schematic data, required per-part dimension/placement fields, and the boundary for partial modeling. The new text adds those contracts while preserving reuse and the existing geometry rules.
本次补齐的是明确顺序、布局与制造/原理图的区别、逐件尺寸位置字段及部分成果边界；保留原有复用与几何约束。

### Independent application / 独立应用检查

A different fresh-context agent read only the revised Skill and CAD reference, without the expected-result table, and answered the eight new cases U–AB plus regression cases A, M, N, O, P, Q, R and T. The author checked all 16 decisions against the acceptance conditions.
另一新上下文助手仅读修改后的 Skill 与工具参考，不看预期表，处理 U–AB 八个新场景及 A、M、N、O、P、Q、R、T 八个回归场景，作者逐项核对共 16 项判断。

| Case / 用例 | Observed decision / 实际判断 | Result / 结果 |
| --- | --- | --- |
| U | Keep stated sizes but search 3D before PCB/reconstruction / 有尺寸也不跳过前两级 | Pass / 通过 |
| V | Use PCB outline/holes/placement for sketches, verify frames and fitted-package dimensions / 依据 PCB 定位，另核对本体尺寸 | Pass / 通过 |
| W | Keep supported Gerber/drill facts; research thickness, fitted parts and heights / 不凭制造平面信息猜高度 | Pass / 通过 |
| X | Schematic/photo do not prove layout or scale; research remaining evidence / 原理图不冒充 PCB 布局 | Pass / 通过 |
| Y | Do not extrude the courtyard or infer height from a package label / 缺尺寸先查，部分板卡未完成 | Pass / 通过 |
| Z | Own known-SKU research through reachable sources before a user handoff / 不让用户先找文件 | Pass / 通过 |
| AA | Share verified package dimensions, retain six individual placements/rotations / 封装尺寸复用，实例逐项对应 | Pass / 通过 |
| AB | After 3D/PCB sources are unusable, use explicit drawing sizes and fill gaps / 正确进入其他资料分支 | Pass / 通过 |

The eight regression decisions retained exact-model reuse, missing-part supplementation, one connected solid, grouped heights, a separate correctly oriented PinMap, saved nominal plus separate clearance copy, final face offset and honest failure/capability limits. The review noted that the opening phrase “nominal copy” could be clearer; it was clarified throughout the overview/invocation text to “clearance copy of saved nominal,” consistent with section 4. No workflow exception was added.
八个回归判断保留模型复用、补缺件、单实体、分高度构造、独立正确引脚图、原件与避让副本、最后偏移及失败边界。复查提示开头“nominal copy”表述可更清楚，已在概述与调用文案统一为“已保存真实模型的避让副本”，与第四节一致，未新增例外。

The scenario document now contains 28 input/acceptance pairs A–AB; only the 16 listed cases were independently applied in this update. No claim is made that all 28 were rerun, or that a statistical improvement was measured.
用例库现有 A–AB 共 28 对输入与验收；本轮独立应用的是上述 16 例，不能宣称全部 28 例已重跑，也无统计提升结论。

### Package and execution boundary / 包检查与执行边界

Skill Creator validation returned `Skill is valid!` with exit 0. UI YAML/invocation/policy, UTF-8, six relative links, portable paths, input/acceptance pairing and Git whitespace checks passed. A local counting check initially included the table's `ID` header as a case; excluding that header corrected the check to 28, without changing the scenarios.
格式验证、UI 元数据、UTF-8、六个相对链接、路径可移植性、用例成对性与 Git 空白检查通过。临时计数检查最初把表头 ID 算成用例，排除表头后确认 28 对，用例本身未因此改变。

No CAD/EDA tool was installed or opened; no PCB sketch, component model, offset, export or physical assembly was executed. These are simulated instruction decisions and package checks only. Repository publication must be verified separately against remote contents.
未安装或打开 CAD/EDA，未画 PCB 草图、元件、偏移、导出或试装；仅验证指令决策与文件包，远程发布需另核对实际内容。
