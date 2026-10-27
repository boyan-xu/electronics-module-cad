# Electronics Module CAD / 电子模块建模

A reusable agent Skill for making true-size electronics module models from product links. Built for enclosure and assembly work, with **research and reuse first**.
通过商品链接还原电子模块、单片机开发板或芯片封装，服务外壳与装配设计；核心是先查资料、优先复用。

## What it does / 核心功能

1. **Use a supplied model:** check the part, revision, units, and known size, then adopt it.
   **有模型直接用：**核对对应型号、版本、单位与尺寸，匹配后不重复建模。
2. **Use stated dimensions:** read the listing, drawings, and attachments before estimating or searching.
   **有尺寸直接用：**先采用商品页、图纸和附件中的数据，不用照片估算覆盖。
3. **Search only for gaps:** look for an exact maker model, then missing dimensions in official drawings, datasheets, and reliable same-version sources.
   **只补查缺项：**按准确型号查厂家模型，再查缺失的机械尺寸；资料来源与版本要记录。
4. **Ask for key measurements:** if needed geometry is still unknown or conflicting, request specific measurements with clear endpoints.
   **缺关键尺寸再问：**说明测量位置与两端，不编造孔距或接口高度。

## Clearance / 装配间隙

The real-size model stays unchanged. A separate keep-out model adds **0.2 mm on each side** of the outer fit surfaces. It is assembly clearance, not `±0.2 mm` manufacturing tolerance.
保留真实尺寸，另建每侧 **0.2 mm** 避让体；这不是制造公差。已添加过的间隙不能重复叠加。

| Feature / 特征 | Real size / 真实尺寸 | Clearance / 避让尺寸 |
| --- | --- | --- |
| Rectangular body / 长方体 | 20 × 30 × 1.6 mm | 20.4 × 30.4 × 2.0 mm |
| Round port / 圆柱接口 | Ø6 mm | Ø6.4 mm |
| Mounting hole in nominal model / 真实模型安装孔 | Ø2.2 mm | Nominal hole stays Ø2.2 mm / 原孔径不变 |

Do not scale the whole model. Hole centers stay fixed; screw and mounting-boss fit is a separate interface. The whole module envelope includes components and protruding pins, not just PCB thickness.
不能整体缩放；孔中心不变，螺钉与安装柱配合单独处理。整板避让要包括元件和突出针脚，不能只计算 PCB 厚度。

## Use and install / 使用与安装

Use an agent that supports `SKILL.md`. Put this repository folder in that agent's skill directory, named `electronics-module-cad`, or use its skill installer with this repository URL. In Codex, the usual user location is `~/.codex/skills/electronics-module-cad/`; a custom configuration may use another location.
使用支持 `SKILL.md` 的助手，把本仓库目录放进它的 Skill 目录，或用安装器读取本仓库链接；目录名称保留 `electronics-module-cad`。不需要本作者电脑上的路径。

Invoke it with a product link, for example:
调用时提供商品链接即可，例如：

```text
Use $electronics-module-cad to model the board at this product link for a case:
[product link]
请优先采用页面模型与尺寸，并另建每侧 0.2 mm 的装配避让体。
```

No particular CAD app is required by the Skill. It uses the user's chosen or available capable tool. Official connections are optional; the Skill does not install apps or connectors on its own. Actual verified model delivery still requires an executable CAD tool.
不绑定 Fusion、FreeCAD 或其他特定软件；优先用户选择或现有可用工具，官方连接可选，不自行安装。真正生成并验证 CAD 模型仍需要可运行的工具。

If no CAD tool can execute, the agent may offer an agreed-tool script or measurement notes, clearly marked **not executed / not verified**.
没有可执行 CAD 时，可提供已确定目标工具的脚本或测量说明，必须明确“未执行 / 未验证”，不能声称模型已完成。

## Delivery / 交付内容

- Adopted original or editable native model, plus a separate clearance model.
  采用的原模型或可编辑工程，以及独立避让模型。
- Separate nominal and clearance STEP exports where the tool supports them.
  软件支持时，分别导出真实模型与避让模型 STEP。
- Source/dimension notes and top, bottom, side, and isometric previews.
  资料尺寸说明，以及顶、底、侧、轴测预览。

The agent must reopen exports, measure geometry, and inspect previews before reporting those checks as passed. Physical fit remains a separate test. Commercial product files are not bundled or automatically published with this Skill.
导出要重开测量，预览要实际查看；软件验证不能代替实物试装。商品模型与图片不随本 Skill 自动上传或再发布。

## Files and checks / 文件与检查

- [SKILL.md](SKILL.md): the research, modeling, clearance, and delivery workflow / 核心流程。
- [CAD tools](references/cad-tools.md): optional tool and export guidance / 可选工具参考。
- [Behavior scenarios](tests/scenarios.md): repeatable acceptance cases / 行为验收用例。
- [Evaluation](tests/evaluation.md): observed instruction checks and limits / 实际检查结果与边界。

The repository has no required runtime package or fixed CAD connection. Behavior scenarios test the instructions; they do not prove any CAD file or physical part fits.
仓库没有强制运行依赖或固定 CAD 连接；行为用例验证的是流程说明，不代表已完成某款商品的 CAD 或实物验证。
