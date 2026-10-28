# CAD tools / 可选工具

Read this when selecting a tool, deriving sketches from PCB files or handling unit/export issues. For source screening and task tables use [research workflow](research.md); do not load this file for ordinary source searches. The Skill has no required CAD/EDA app or connector.
在选择工具、依据 PCB 文件画草图、处理单位或导出问题时读取；本 Skill 不绑定 CAD/EDA 软件或连接器。

## PCB to sketches / PCB 到草图

- Follow the core order: matching 3D source first; otherwise native PCB layout, then Gerber/drill with available BOM and placement data; other drawings only for reconstruction or remaining gaps. Read-only parsing or an available viewer is sufficient for research; do not force an EDA installation.
  遵守先 3D、再 PCB、最后其他资料；查资料可只读解析或用现有查看器，不强制安装 EDA。
- Check native file units, outline/cutout layers, drill origin, placement origin, rotations and bottom-side mirror conventions. Convert them into one stated CAD frame before deriving board, hole and placement sketches; group compatible coplanar profiles. A footprint courtyard or page border is not the PCB edge.
  核对单位、板框/开槽层、钻孔与贴片原点、角度及底面镜像，转成共同 CAD 基准再画板框、孔位与定位草图；同平面兼容轮廓共草图，不把占位框或页边框当板边。
- Gerbers/drills support only their actual planar information. Use the BOM/layout and photos to identify fitted parts; schematic-only sources give nets/parts, not physical placement. Find PCB thickness, body length/width/height and connector/contact extents from verified models, package drawings or other stated evidence. Do not extrude a pad/courtyard to an invented height.
  Gerber/钻孔只支持实际含有的平面信息；原理图不能证明位置，BOM/布局与照片用于确认实装件。板厚、元件本体长宽高及接口接点范围另找可靠依据，不能把焊盘或占位框随意拉高。
- Reuse verified linked component models without rebuilding them. Share package dimensions across identical fitted parts while keeping every reference, side, coordinate and rotation; leave unsupported components unresolved and mark partial work incomplete.
  已核实的关联元件模型直接复用；相同实装封装共享尺寸，每个元件保留位号、板面、坐标和角度。资料不足的元件不猜建，部分成果标为未完成。

## Pick a working route / 选择可运行路线

1. Use the user's selected tool when it can do the job. Otherwise inspect available CAD apps, existing plugins/connections, and import/export support. Detect locally; do not scan a user's whole drive or assume an app from a previous machine exists.
   用户选择优先；否则查看现有 CAD、已连接工具及导入导出能力。按当前环境确认，不全盘扫描，也不把其他电脑的配置当成本机事实。
2. Prefer a working native API, existing integration, or official local connector. Check capabilities needed here: union into one valid solid, grouped sketches/extrusions, a separate pin-text sketch, equivalent face offset as the final geometry step, measurement, native/STEP saving and views. Import/export or scaling alone cannot fulfill this workflow.
   优先现有 API、集成或官方本地连接；确认可合并为单实体、分组草图与拉伸、创建独立引脚文字草图、以等效偏移面完成最后几何步骤，以及测量、保存和视图能力。只有导入导出或缩放功能不够。
3. If nothing can execute, agree on the target for any generated script and mark it unexecuted. A script-only route is not verified CAD delivery. Do not turn a missing tool into a forced download.
   无法执行时先确定脚本目标工具，并标为未运行；缺工具不等于必须下载指定软件。

## Optional app routes / 可选软件路线

| Tool / 工具 | Route / 用法 | Check / 核对点 |
| --- | --- | --- |
| Fusion | Existing API/script access or an official local MCP if available / 使用已有 API 或可用的官方本地 MCP | Confirm internal length units and mm conversion; preserve the active user's design / 确认内部长度单位，保护当前工程 |
| FreeCAD | Available Python API or macro environment / 使用现有 Python API 或宏环境 | Confirm actual unit handling, valid solids, offset results and STEP support / 确认单位、有效实体、偏移结果与 STEP 能力 |
| Another CAD tool / 其他 CAD | Use its supported equivalent / 使用软件支持的等效操作 | Check units, solid import/export and measurable geometry / 检查单位、实体导入导出及几何测量 |

For a Fusion local connection, consult the current [Autodesk official overview](https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW). It describes a local server for live modeling and a separate cloud Data server for managing project data. Do not assume the Data connection can run desktop modeling commands. Read current setup instructions rather than hard-coding a port or configuration path.
Fusion 的本地建模连接与云端项目数据连接用途不同；查当前官方文档，不把数据连接当作建模接口，也不写死端口或本机配置路径。

No mandatory MCP dependency is declared in the Skill metadata. Install or enable optional tools only within the user's authorization; keep any setup changes separate from model output.
Skill 元数据不声明强制 MCP 依赖；可选工具的安装启用遵循用户授权，与模型交付文件分开。

## Geometry and export checks / 几何与导出检查

- Use one stated coordinate frame for all exports. Check at least one known size after import; display units alone do not prove correct scale.
  所有导出共享明确坐标基准；导入后测一个已知尺寸，界面显示毫米不等于比例一定正确。
- Preserve the downloaded original. Reuse imported geometry, add missing components and join bodies; do not accept a multi-solid compound as one solid. Save one-solid nominal and clearance documents separately, each with its dedicated `PinMap` sketch.
  保留下载原件；复用导入几何，补齐元件后合并，不能把多实体复合对象算作一个实体。真实与避让文档分开保存，每份单实体并带独立 `PinMap` 草图。
- Mesh-only sources can be reference evidence. Do not claim they are exact B-rep solids or simply rename them to STEP. If conversion is needed, disclose approximation and verify critical dimensions.
  网格可作参考，不能冒充精确实体或只改 STEP 后缀；需要转换时说明近似与尺寸验证情况。
- Build nominal geometry with Join and batch compatible profiles/operations; retain different heights as separate extrusions. Extend non-critical component bases into the PCB if needed for connectivity, without blocking holes or connector openings or moving pin positions.
  真实几何使用 Join，兼容轮廓与操作分组；不同高度分开拉伸。必要时延伸非关键元件底部与 PCB 连接，不堵安装孔或接口，不改变引脚位置。
- Use the chosen tool's actual face-offset operation last on the saved nominal copy, not a whole-body scaling or bounding-envelope substitute. Check a valid connected solid, outward 0.2 mm per side, unchanged hole references and nominal pin-map coordinates. Failed offsets require face/geometry repair and retry; absent capability or unresolved failures remain incomplete.
  另存真实模型后，最后使用工具实际的面偏移操作，不用整体缩放或外包体替代。核对有效连通实体、每侧向外 0.2 mm、未改变的孔位及真实引脚坐标；失败应修复表面或几何后重试，能力缺失或失败未解决时如实标记未完成。
- Keep all pin labels in the independent sketch; never engrave/extrude them. Native sketch text may be absent from STEP, so include native files and pin notes and verify each format's actual contents.
  引脚标注集中在独立草图，不雕刻、不拉伸；STEP 可能不含草图文字，因此保留原生文件与引脚说明，并按格式核对实际内容。
- Reopen the native file and STEP exports and measure them. State unsupported formats or missing checks instead of claiming a full delivery.
  重新打开并测量原生文件与 STEP；不支持的格式或未完成检查如实列出。
