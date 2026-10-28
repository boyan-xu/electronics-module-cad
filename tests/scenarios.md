# Behavior scenarios / 行为验收用例

Use a fresh agent context for each evaluation. Supply `SKILL.md` and allow its linked reference; do not supply the expected results until after the agent answers. These are simulated evidence packets, not real product files. Do not browse or run CAD for these cases.
每次评估使用新的助手上下文，提供 Skill 及其引用；回答前不提供下方预期结果。这里是模拟资料，不是真实商品文件，不需联网或运行 CAD。

Ask for each case's next action, evidence choice, numerical results if relevant, and what is still unverified. Score the decision and evidence, not exact wording. Record baseline and with-Skill results separately; do not call a baseline a failure unless a requirement was actually violated.
要求逐项回答下一步、采用资料、相关数值与未验证项；按实际决策评分，不匹配固定措辞。基线与加载 Skill 的结果分开记录，不能把没有错误的基线写成失败。

## Case inputs / 用例输入

| ID | Input / 输入 |
| --- | --- |
| A | Exact revision-matched STEP supplied; mm and 20 × 30 × 1.6 mm bounds verified. Similar-board model and photos also exist. / 已给准确版本模型，另有相似模型与照片。 |
| B | Listing gives PCB 30 × 20 × 1.6 mm; no supplied model. A maker model may exist; hole centers and connector height are missing. / 有尺寸但缺孔位与接口高度。 |
| C | Unscaled photo only. Maker mechanical drawing and a trusted distributor are possible search sources; no search result is yet known. / 只有无比例照片，尚未查到原始资料。 |
| D | Mixed rev A/B listing; conflicting hole spacing; selected option unknown. / 款式不明且两版孔距冲突。 |
| E | Product link blocked by login; identity unknown. / 链接需登录，无法识别商品。 |
| F | Rectangular body 20 × 30 × 1.6 mm, round port Ø6 mm, nominal mounting holes Ø2.2 mm at known centers. A body extent is 0..20 mm. / 检查每侧间隙与坐标。 |
| G | Supplied file is a verified 0.2 mm-per-side envelope, 20.4 × 30.4 × 2.0 mm; nominal dimensions are 20 × 30 × 1.6 mm. Nominal geometry is not supplied. / 只有已核实的避让模型。 |
| H | No CAD installed or connected; no particular app may be forced on the user. An unexecuted script is possible. / 没有可运行 CAD，只能提供未运行脚本。 |
| I | Exact model supplied; hole metadata absent, but CAD hole geometry is measurable. / 模型无孔位文字数据，但几何可测。 |
| J | User chooses an already available CAD app other than Fusion/FreeCAD. / 用户选择其他已安装 CAD。 |
| K | A supplied model is labeled “clearance,” but offset amount is unknown; another envelope has a known 0.1 mm offset and a nominal original is available. / 检查未知偏移与非默认偏移。 |
| L | Real export and screenshots were not produced; user asks whether fit is verified. / 没有实际导出或截图，用户询问是否已验证。 |
| M | Board photos/BOM show 14 parts on both sides, including tiny capacitors; the correct maker STEP contains only 11. / 厂家模型缺三个小元件。 |
| N | Complete matching STEP imports as 12 bodies; small component/PCB gaps do not matter for the user's print. / 多实体且有可忽略间隙。 |
| O | Eight footprints on one plane: six need 2 mm extrusion, two need 3 mm; identical repeated pin geometry. / 检查共草图、分高度拉伸与阵列。 |
| P | Top-view USB-up pinout: physical 1=GP0, 2=GP1, 3=GND; bottom view is mirrored. Connector contacts inside a housing have documented mating-face positions. / 检查编号、信号名、方向与壳内接点。 |
| Q | Both nominal and 0.2 mm-per-side clearance files are required. / 检查几何、标注、保存与偏移顺序，以及每份文件实体数。 |
| R | Outward face offset fails on a small port edge; a bounding box could cover the board. / 检查偏移失败处理。 |
| S | Tool defaults every extrusion to New Body; Join is available. / 检查逐次拉伸操作与最终实体数。 |
| T | Chosen tool imports/exports STEP and scales but lacks an equivalent face-offset operation. / 检查能力缺失时不能冒充完成。 |
| U | Seller gives a dimensioned image, no attached model; maker downloads and public board repositories have not been checked. / 有尺寸图，但尚未搜索 3D 源文件。 |
| V | No matching 3D board model found; exact-revision native PCB layout, footprints, coordinates and BOM are available. / 有同版本 PCB 原始布局与元件表。 |
| W | Only exact-revision Gerbers and drill files; PCB thickness, fitted part numbers and component heights are absent. / 只有制造平面文件，缺厚度及元件高度。 |
| X | No matching 3D or PCB layout found; only a schematic and unscaled photo are available. / 仅有原理图与无比例照片。 |
| Y | PCB shows a 0603 capacitor footprint with a 1.8 mm courtyard; fitted part and height unknown. User wants a quick model. / 检查不能以占位框代替器件尺寸。 |
| Z | Product URL is unreadable, exact SKU is known, user has only that link; maker pages and public repositories remain searchable. / 用户不能自行找资料，仍有可查来源。 |
| AA | Six repeated resistors share a verified package drawing; they occupy different positions and rotations on both sides. / 重复封装共用尺寸，但逐实例保留位置。 |
| AB | Matching 3D and PCB searches found no usable files; seller gives a same-version dimensioned drawing. / 搜索前两级无结果后有明确尺寸图。 |

## Expected decisions / 预期决策

| ID | Acceptance / 验收条件 |
| --- | --- |
| A | Check complete component coverage, reuse the exact geometry, preserve nominal, and face-offset a separate copy last; no replacement search or full rebuild. / 核对完整性后复用，最后在副本偏移面。 |
| B | Retain supplied dimensions; search exact 3D sources first, then PCB layout if none is usable, then other missing data. Do not replace stated sizes with estimates or model from dimensions before checking higher-priority sources. / 保留尺寸，不跳过 3D 与 PCB 搜索。 |
| C | Search exact 3D sources, then PCB layout, then maker mechanical/package data and reliable same-version sources. Unscaled photos cannot supply precise dimensions. / 先 3D、再 PCB、最后其他资料，不猜尺寸。 |
| D | Ask for selected revision/option; keep conflicts visible and separate; do not average. / 先确认版本。 |
| E | Request identity and accessible evidence; do not bypass login, guess identity, or claim page access. / 明确链接未读到。 |
| F | Clearance 20.4 × 30.4 × 2.0 mm and Ø6.4 mm; nominal holes Ø2.2 mm and centers unchanged; bounds -0.2..20.2 mm. No global scaling. / 两侧总增 0.4 mm，保持基准。 |
| G | Keep the verified clearance input unchanged, but do not certify final Offset Face history from an imported envelope alone. Obtain nominal geometry for a compliant new delivery; without it, report incomplete. Never offset again or shrink to invent nominal. / 原文件保留，缺真实模型或历史不能冒充通过新流程。 |
| H | No forced installation or completion claim; agree on target script tool; disclose not executed/not verified. / 不把脚本说成完成模型。 |
| I | Measure existing geometry from a stated datum; do not ask/search just because text metadata is absent. / 能测就先测。 |
| J | Use the chosen tool if capable, check units/export; no mandatory named app or connector. / 不绑定软件。 |
| K | Unknown offset requires clarification; known 0.1 mm envelope is replaced by a fresh 0.2 mm envelope derived from nominal, not cumulatively padded. / 从原件重生成。 |
| L | State CAD/export/view checks did not run; physical fit is untested; no success claim. / 如实标记未验证。 |
| M | Inventory all 14, reuse the 11 correct components and add the missing 3 after package/size research; no omissions or full redraw. / 元件逐项对应，正确部分不重建。 |
| N | Consolidate into one valid connected solid per board file; close non-critical gaps via component bases while protecting holes, ports, pins and height. / 不能用组件或复合对象冒充单实体。 |
| O | Use one compatible construction sketch for eight profiles and two grouped Join extrusions for the two heights; pattern identical repeats when suitable. PinMap remains a separate sketch. / 同平面共草图，不同高度分组。 |
| P | One independent PinMap sketch labels physical numbers plus known signals at nominal positions, including documented connector contacts hidden in previews; verify datum/view and bottom mirroring, no engraving or label extrusion. / GPIO 名不能代替物理编号，壳内对外接点不能因不可见而漏标。 |
| Q | Complete all nominal geometry and PinMap, verify/save one-solid nominal, copy into a separate one-solid file, then Offset Face outward 0.2 mm last; retain nominal unchanged. / 不在一个文件留下真实与避让两个实体。 |
| R | Identify failing faces, repair nominal geometry/selection and retry on a fresh copy; unresolved failure is incomplete, with no box/padding/scaling substitute. / 不用粗略外包体兜底。 |
| S | Create the initial PCB body once, then Join additive features; verify one valid connected solid with no leftover tool bodies. / 不默认每次拉伸新实体。 |
| T | Report unmet face-offset capability; agree on an available capable route or explicitly unexecuted script, no forced install or alternative-method success claim. / 能力不足如实说明。 |
| U | Record stated sizes without re-estimating; complete 3D-source discovery before switching to PCB or dimension-based reconstruction. / 有尺寸也先查 3D，可用模型直接复用。 |
| V | Verify revision/units/datum; derive grouped sketches from PCB outline, holes and placement coordinates, with bottom-side transforms checked. Look up each fitted package's body dimensions and height before adding its geometry; reuse verified component models. / 依据 PCB 定位，不把焊盘当本体。 |
| W | Use only supported outline/hole/pad evidence; do not infer thickness, fitted parts, body size or height from Gerber. Research those gaps and leave unresolved components unmodeled/incomplete. / 制造文件不能凭空补齐高度和 BOM。 |
| X | Use schematic for parts/signals, not placement or scale. Continue mechanical/package research; mark missing positions/dimensions rather than treating a schematic as PCB layout. / 原理图不等于布局图。 |
| Y | Do not use courtyard, pad size or a package label alone as the body dimensions/height. Seek the fitted part and package drawing or a verified model; missing dimensions prevent modeling that component, not justify omission. / 先查该器件实际封装，不能猜建或删件。 |
| Z | Own the research: search reachable exact-SKU 3D sources, then PCB sources and remaining data. Ask a batched specific question only after reasonable paths are exhausted; do not claim blocked pages were read. / 不提前把找资料交给用户。 |
| AA | Reuse verified package dimensions once; record every resistor's designator, side, position and rotation, then group/pattern compatible geometry. / 尺寸可复用，六个实例都要对应。 |
| AB | Adopt the stated dimensions directly, then research only missing geometry and component package sizes; no unscaled photo estimates or endless repeated source search. / 前两级不可用后采用给定数据，只补缺项。 |

## Lean research inputs / 精简流程用例

| ID | Input | Expected decision |
| --- | --- | --- |
| AC | Six previews show different USB/header/layout; one PCB source is uncertain. | Reject six before deep download/parse, record reasons; screen the uncertain source next, never adopt by appearance. |
| AD | Resume: SKU confirmed, no seller download exists, two rounds have no new valid evidence and no concrete lead. | Read summary and gaps, stop repeated search, give specific resume evidence; do not ask again for seller downloads. |
| AE | Two fruitless rounds, then an exact-revision engineering pack appears. | Investigate the concrete new lead; the stop rule is not a fixed search cap. |
| AF | Same file bytes at three URLs; bytes later change at one URL. | Record URLs, reuse extraction for identical hashes and parsing conditions; invalidate changed derivations, retain historical source. |
| AG | Twenty same exact-maker/package resistors; another maker's 0603 has unknown height. | Reuse the twenty verified sizes while preserving placements; separate the unknown variant, do not infer its height. |
| AH | Huge STEP and 61-page PDF; only package page is needed. | Parse once, return compact needed facts/counts and source locations; visually inspect relevant diagram, do not dump whole files into context. |
| AI | Tables have all numeric fields, but no underside evidence and no actual CAD execution. | A table-check pass is not a complete inventory or CAD/fit certificate; keep missing evidence explicit. |
| AJ | Previous reports are prose with downloaded files; current task resumes. | Link old reports, read summary, extract needed rows incrementally; no destructive migration, global database or required plugin. |

These inputs should be hidden from their expected decisions during future independent evaluations. This update's self-review and independent-test limit are recorded in evaluation.md. 上表并非独立行为测试已通过的证明。

## Real CAD gate / 真实 CAD 验收

On a later real modeling task, reopen native and STEP files separately. Check the full top/bottom component inventory with each part's body length/width/height and placement evidence, PCB-derived sketch alignment, one valid connected solid per board file, complete pin labels in one independent PinMap, grouped construction and final Offset Face history. Measure sizes, holes, datums, ports, full height, and nominal-to-clearance gaps on both sides. Check native sketch labels separately from STEP and inspect every delivered view. Keep physical assembly results separate.
后续实际建模应重开文件，逐项核对元件本体长宽高与位置依据、PCB 草图基准、每份单实体、独立引脚草图、分组构造及最后偏移面，再做尺寸与逐视图检查。草图标注不能假定存在于 STEP；模拟行为检查不能替代真实 CAD 验收或实物装配。
