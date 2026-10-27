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

## Expected decisions / 预期决策

| ID | Acceptance / 验收条件 |
| --- | --- |
| A | Adopt the exact model, preserve nominal, generate separate clearance; no replacement search or rebuild. / 直接复用，不重复建模。 |
| B | Retain supplied dimensions first; seek exact maker model, then only missing dimensions; ask for unresolved measurements. / 不用照片覆盖已有尺寸。 |
| C | Search maker mechanical drawing/datasheet first, distributor second; no invented dimensions or claimed search results. / 按来源顺序补查。 |
| D | Ask for selected revision/option; keep conflicts visible and separate; do not average. / 先确认版本。 |
| E | Request identity and accessible evidence; do not bypass login, guess identity, or claim page access. / 明确链接未读到。 |
| F | Clearance 20.4 × 30.4 × 2.0 mm and Ø6.4 mm; nominal holes Ø2.2 mm and centers unchanged; bounds -0.2..20.2 mm. No global scaling. / 两侧总增 0.4 mm，保持基准。 |
| G | Reuse clearance as-is; do not offset again or shrink it to invent nominal; request nominal geometry if needed. / 不重复加间隙，不反推原模型。 |
| H | No forced installation or completion claim; agree on target script tool; disclose not executed/not verified. / 不把脚本说成完成模型。 |
| I | Measure existing geometry from a stated datum; do not ask/search just because text metadata is absent. / 能测就先测。 |
| J | Use the chosen tool if capable, check units/export; no mandatory named app or connector. / 不绑定软件。 |
| K | Unknown offset requires clarification; known 0.1 mm envelope is replaced by a fresh 0.2 mm envelope derived from nominal, not cumulatively padded. / 从原件重生成。 |
| L | State CAD/export/view checks did not run; physical fit is untested; no success claim. / 如实标记未验证。 |

## Real CAD gate / 真实 CAD 验收

On a later real modeling task, open the saved native document and exported STEP in separate documents. Measure known sizes, holes, datums, ports, and full height. Measure the nominal-to-clearance gap on both sides of each relevant feature, inspect all delivered views, and note unsupported exports. Keep physical assembly results separate.
后续实际建模任务需要重开文件、测量与逐视图检查；这份模拟行为检查不能替代真实 CAD 验收或实物装配。
