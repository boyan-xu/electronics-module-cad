# CAD tools / 可选工具

Read this only when selecting a tool or handling unit/export issues. The Skill has no required CAD app or connector.
仅在选择工具、处理单位或导出问题时读取；本 Skill 不绑定软件或连接器。

## Pick a working route / 选择可运行路线

1. Use the user's selected tool when it can do the job. Otherwise inspect available CAD apps, existing plugins/connections, and import/export support. Detect locally; do not scan a user's whole drive or assume an app from a previous machine exists.
   用户选择优先；否则查看现有 CAD、已连接工具及导入导出能力。按当前环境确认，不全盘扫描，也不把其他电脑的配置当成本机事实。
2. Prefer a working native API, existing integration, or official local connector. Check capabilities before choosing one: reading files is not proof it can create solids, offset geometry, measure, export, or capture views.
   优先现有 API、集成或官方本地连接；读取文件不代表具备建实体、偏移、测量、导出与截图能力，逐项确认实际所需能力。
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
- Preserve the downloaded original. Import to a new document; derive a separate clearance body, component, or document without transforming nominal geometry.
  保留下载原件，导入新文档；避让体单独创建，不改真实模型。
- Mesh-only sources can be reference evidence. Do not claim they are exact B-rep solids or simply rename them to STEP. If conversion is needed, disclose approximation and verify critical dimensions.
  网格可作参考，不能冒充精确实体或只改 STEP 后缀；需要转换时说明近似与尺寸验证情况。
- A successful offset command is not enough: check that the result is valid, outward, and contains the required occupied space. Keep verified hole references distinct from any conservative filled envelope.
  偏移命令成功仍需检查有效性、方向和空间包含关系；真实孔位与保守外包体分开。
- Reopen the native file and STEP exports and measure them. State unsupported formats or missing checks instead of claiming a full delivery.
  重新打开并测量原生文件与 STEP；不支持的格式或未完成检查如实列出。
