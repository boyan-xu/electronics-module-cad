# Lean research / 标准查证

Read for research tasks and resume. Read CAD guidance only when that phase is needed. Use task-local files; no database, required plugin or fixed CAD app. 查证只加载本参考，按缺项续查。

## Screen, inspect, fill / 筛选、解析、补缺

1. Start `research.md` with clean product URL/ID, maker, selected option, revision evidence (unknown is allowed), scope and units. Record source dimensions when found. On resume read this summary and only relevant table rows; keep earlier reports/downloads in place.
2. Search matching 3D sources first: attachments/seller, maker downloads/official repositories, then reliable public model sources. Read source description and previews before downloading large files. Compare chip, USB type, buttons/crystals, header direction, outline and layout. Reject clear mismatches with a one-line reason. Uncertain matches remain unverified; do not adopt by appearance alone.
3. Inspect promising files twice. First: signature/type, revision evidence, units, outline, side distribution and component count. Only then: detailed body/lead sizes, placements, connector pin positions and coverage. Counts of solids/faces are not counts of electronic components. A preview can reject a mismatch, but cannot prove all hidden geometry.
4. If no matching usable 3D source, repeat screening for same-version native PCB, then Gerber/drill plus BOM/placement. Verify board outline layers, origins, units, rotations and bottom transforms. Footprint anchor is not always body center; record the transform. A schematic supplies parts/signals, not placement. Gerbers alone lack fitted identities and heights.
5. Fill only remaining facts using official mechanical/package drawings, datasheets, same-version distributor files or user measurements. Look inside relevant diagram/PDF pages, not only extracted text. Supplied dimensions stay adopted unless a documented conflict requires resolution; never average versions. Package tolerances/ranges stay ranges, separate from assembly clearance.

先看版本与预览，明显不同立即排除；有希望的文件先概览，再提取全部数据。尺寸冲突保留来源，不拼成“通用同款”。缺元件型号、背面清单或高度时，明确对应缺项。

## Reuse and limits / 复用与边界

- Group package research by exact maker part + package variant + relevant size/lead evidence. Share verified dimensions and model geometry, but keep every component's ref/side/position/rotation. A common label such as 0603 does not prove equal height across different parts.
- Save downloaded originals unchanged. Hash file bytes with SHA-256; identical bytes from different URLs reuse the extraction, with each source URL retained. Extraction reuse also depends on parser/version and options/units/transforms: changed parsing invalidates affected results even if bytes match. Changed bytes invalidate derived data; keep old evidence as historical. A hash proves identical bytes, not the correct product.
- Cache only within the task by default. Do not scan personal files or create a global database. Do not automatically migrate old prose reports: link them and extract needed rows when continuing.
- Each query must target a named gap and record whether it resolved that gap. Batch independent searches; keep dependent screening/inspection sequential. Prefer primary sources; follow hits to files rather than trusting snippets or README claims.
- Use available parsers to extract once. Return compact facts/counts/conflicts and file locations; keep raw STEP/PCB/PDF/page bodies out of chat. Inspect relevant drawings visually. Never print embedded account/session metadata from source files.

同文件不重复解析；封装只查一次，实例不合并丢失。缓存由内容和解析条件共同决定，不因网址相同就信任旧结果。

## Task files / 任务文件

Use UTF-8 CSV with these exact headers; quote fields containing commas. Units are mm/degrees. Blank is unknown, never zero by default. One source ID per row; where evidence comes from several sources, use separate source rows with a reason pointing to the supporting IDs. `research.md` records field-specific evidence when a row combines them.

| File | Header |
| --- | --- |
| `sources.csv` | `id,url,revision,path,sha256,status,reason` |
| `packages.csv` | `id,part,variant,length_mm,width_mm,height_mm,lead_extents,source,status` |
| `components.csv` | `ref,side,x_mm,y_mm,rotation_deg,package,source,status` |
| `pins.csv` | `connector,number,signal,x_mm,y_mm,z_mm,view,source,status` |

Sources: status `adopted`, `reference`, `rejected`, `blocked` or `unverified`; `path` and hash are blank for web-only sources, revision may be unknown. Local/user measurements can use an evidence note path in `url`; record datum/endpoints in `reason`. A downloaded file needs a recorded SHA-256. Hash computation and source-match verification are done by the researcher, not the checker.

Other tables: status `verified`, `missing`, `unverified` or `conflict`. `components.side` is `top` or `bottom`. Use photo IDs if no designator is known; one row per mounted part, including header assemblies/shunts. Pin contacts get separate connector/number rows. An empty pins table is allowed only when no external contacts exist, explained in `research.md`; otherwise it is incomplete. Unknown signals are written `unknown`, distinct from missing physical numbering or positions.

Record original units/coordinates, conversion, datum, viewing direction and mirror/rotation conventions in `research.md`, alongside board outline/cutouts, thickness, hole data and their sources. CSV coordinates use the stated common nominal frame; preserve raw source data separately. Package dimension ranges may be written `min..max` with the selected modeling value recorded in notes; the optional checker requires numeric chosen dimensions, so leave unresolved ranges marked unverified until a documented choice is made. Do not silently select nominal or worst case.

每件有独立位号与坐标；来源、封装共享。表格不能替代板框图、原始坐标和转换说明，尺寸范围的选择必须记录。

Example: R1 and R2 both reference package P1 only when their exact fitted package is confirmed. Keep two component rows with separate positions/rotations; a third different-maker 0603 with unknown height gets another package row, not P1 by default.

## Small read-only check / 可选检查器

From the Skill folder run:

```sh
python scripts/check_research.py /path/to/task
python scripts/check_research.py /path/to/task --details
```

Python 3 standard library only; optional, no CAD installation. Checks exact headers, row shape, duplicate IDs/refs/pin keys, references, numeric chosen sizes/coordinates, source hash syntax, status counts and package resolution. Exit 0 means table checks passed; exit 1 means errors or unresolved entries; usage errors exit 2. Default output is a short summary. It does not download, hash files, test URLs, validate PCB transforms, compare photos, certify all fitted parts or run CAD. 缺项时可继续保存表格，检查失败不代表应删掉缺项。

## Stop and resume / 停止与恢复

Stop when required evidence is sufficient. Otherwise record each meaningful search round: targeted gaps, sources checked, new evidence, resolved gaps, remaining leads. After **two consecutive rounds with no new valid evidence and no concrete unchecked lead**, stop repeating the search. A specific new lead overrides the no-progress stop; rejected generic boards do not count as new matching evidence. Do not stop after an arbitrary number of hits while clear useful leads remain.

For blocked links with known identity, search independent reachable sources; do not bypass sign-in or safety blocks or claim blocked content was read. If identity is unknown, ask for the selected option or accessible evidence. After reasonable research, batch only actionable missing measurements with datum/endpoints. If the user already said no download exists, do not ask that again. Report incomplete, the exact evidence needed and the resume condition. Do not contact sellers, buy files or publish downloads without authorization.

Before CAD, audit: exact-target evidence; board outline/thickness/holes; both-side fitted inventory; per-part dimensions/lead extents/placement; physical pin IDs/contact positions/view. Only then call research complete. Partial authorized modeling stays marked incomplete. Link an older blocked report without converting its unknowns into passes.

End each round with a brief delta: **new facts; exclusions; gaps; next step**. Detailed evidence stays in tables. On resume recheck changed sources and continue gaps, not the whole search. 无增量就停止重复；新证据到来再续查，不能把“没找到”写成“全网不存在”。
