# Electronics Module CAD / 电子模块建模

A portable agent Skill for product-link research and board CAD for enclosure design. It searches **3D source → PCB layout → other dimensions**, reuses verified work and records only gaps on resume. 商品链接即可开始，先复用，后补缺。

All mounted parts on both sides must be covered, each with size and placement evidence. Models keep one connected solid per board file and one independent `PinMap` sketch. Save nominal first; apply **0.2 mm per side with Offset Face last** in a separate clearance copy. 全部元件、单实体、引脚编号与最后偏移面要求不因节省时间而降低。

## Use / 使用

Put this folder in your agent's supported Skill location, for example `~/.codex/skills/electronics-module-cad`, or use the host's GitHub Skill installer with this repository. Keep `SKILL.md`, `agents`, `references` and `scripts` together. No required CAD app, MCP connection, database or Python package. Python 3 is needed only for the optional checker.
将仓库作为一个 Skill 文件夹使用；不强制下载任何 CAD，也不自动安装工具。

```text
Use $electronics-module-cad with [product link]. Research only for now.
先查完整建模资料，保留来源和缺项，暂不建模。
```

For modeling, state the chosen tool if any. The Skill uses an available capable tool; if none can run, any agreed-tool script is explicitly unexecuted. Actual delivery includes native nominal/clearance files, STEP where supported, component/pin/source notes and multi-view previews; checks require reopening and measuring real files. STEP may not retain sketch text. 实物试装需另行验证。

## Faster research / 更快查证

- Screen identity and previews before large downloads; inspect promising files in two passes. 先筛版本，再深度解析。
- Read saved `research.md` on resume; search missing facts rather than repeating answered questions. 续查只读摘要与相关表格。
- Reuse identical file extraction by hash and parsing conditions; share exact package dimensions while retaining each placement. 同封装复用尺寸，每个实例独立。
- Stop after two rounds with no new valid evidence and no concrete unchecked lead. New useful evidence resumes the search. 不无限换通用板查找。
- Load research/CAD references only when needed; keep raw files local and tool replies short. 按需加载，报告只讲增量。

Task data uses `research.md`, `sources.csv`, `packages.csv`, `components.csv` and `pins.csv`. Headers, statuses and evidence rules are in [research workflow](references/research.md). Existing reports stay in place; no automatic migration or global cache.

```sh
python scripts/check_research.py /path/to/task
python scripts/check_research.py /path/to/task --details
python -m unittest discover -s tests -p 'test_*.py'
```

The checker is read-only and uses the Python standard library. A clean result means table checks passed, **not complete product evidence or CAD verification**. Unknown values remain recorded; they must not be removed just to pass. 检查器不能证明没有漏件、来源匹配或模型能装配。

## Files and limits / 文件与边界

- [SKILL.md](SKILL.md): core decisions and modeling contract / 核心流程。
- [Research](references/research.md): screening, tables, reuse and stop rules / 查证细则。
- [CAD tools](references/cad-tools.md): optional tools, transforms and export checks / 建模阶段参考。
- [Scenarios](tests/scenarios.md) and [evaluation](tests/evaluation.md): behavioral cases, dated results and limits / 验收与历史。

No measured live Token or speed gain is promised. Instruction text and controlled local checks can be compared; real research depends on accessible sources. Commercial models, screenshots and local project records are not bundled or automatically published. 不足的资料仍须标记不足，不用相似商品代替。
