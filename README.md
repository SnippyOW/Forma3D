# Forma

An original, cross-platform 3D modeling and animation app. Its workflow is modeled on classic DCC tools:
marking menus, a spacebar hotbox, a channel box, an outliner, shelves, a manipulator per tool and
remappable hotkeys. It contains no third-party DCC code, icons or assets.

Python + Qt (PySide6) + OpenGL 3.3 core. It runs natively on **Windows**, **Linux** and **macOS on Apple
Silicon (arm64)**.

## Run from source

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate     macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run_forma.py
```

## Build a standalone app

| Platform | Command | Output |
|---|---|---|
| Windows | `powershell -ExecutionPolicy Bypass -File scripts\build_windows.ps1` | `dist\Forma\Forma.exe` |
| macOS (Apple Silicon) | `./scripts/build_macos.sh` (run on the Mac) | `dist/Forma.app` |
| Both, in CI | push to GitHub; `.github/workflows/build.yml` builds on `windows-latest` and `macos-14` (arm64) | downloadable artifacts |

PyInstaller can't cross-compile, so the Mac build must run on a Mac or on the `macos-14` CI runner.
The Mac app is ad-hoc signed. The first time you open a downloaded copy, right-click → **Open**, or run
`xattr -dr com.apple.quarantine Forma.app`.

## Controls

| Action | Input |
|---|---|
| Tumble / Track / Dolly | Alt + LMB / MMB / RMB (Option on Mac). Trackpad: Alt+Cmd+LMB to track, scroll or pinch to dolly |
| Select / Move / Rotate / Scale | Q / W / E / R. Double-click a toolbox icon for Tool Settings |
| Toggle / Deselect / Add selection | Shift / Ctrl / Ctrl+Shift + click or drag a marquee |
| Component marking menu | RMB in the viewport (Ctrl-click on a Mac) |
| Poly tools marking menu | Shift + RMB |
| Convert-selection marking menu | Ctrl + RMB |
| Tool option marking menus | Hold W / E / R + LMB |
| Hotbox / maximize panel | Hold Space / tap Space |
| Object / vertex / edge / face | F8 / F9 / F10 / F11, or the RMB marking menu |
| Edge loop | Double-click an edge |
| Snap to grid / curves / points, relative steps, edit pivot | Hold X / C / V, hold J, hold D or Insert (see Snapping) |
| Soft selection | B; hold B + MMB-drag to set the radius |
| Virtual slider | Click channel names in the Channel Box, then MMB-drag in the viewport. Hold Ctrl for finer steps or Shift for coarser ones. Speed (Slow / Medium / Fast) and Hyperbolic are under Channel Box RMB → Settings |
| Scrub a numeric field | Ctrl + drag left/right on the field: MMB = step, LMB = step × 0.1, RMB = step × 10 (plain MMB-drag also works). Or type a value |
| Frame selection / all | F / A (Shift for all views) |
| Wireframe / shaded | 4 / 5 |
| Smooth preview | 1 / 2 / 3 |
| Keys | S (all), Shift+W/E/R (translate/rotate/scale); `,` / `.` previous/next key; Alt+V play |
| Repeat last / undo / redo | G / Z or Ctrl+Z / Shift+Z or Ctrl+Y |
| Add a menu item to the shelf | Ctrl+Shift+click the item |
| Primitive options | Click the □ option box next to a Create → Polygon Primitives item |

**More Maya default hotkeys:**

| Key | Action |
|---|---|
| Ctrl+F9 / F10 / F11 / F12 | Convert the selection to vertices / edges / faces / UVs (UVs open in the UV Editor) |
| F12 | UV selection (opens the UV Editor) |
| Ctrl+1 | Isolate Select in the view under the mouse |
| Ctrl+X / Ctrl+C / Ctrl+V | Cut / copy / paste objects, with children, skeletons and materials. Also via the system clipboard, so they paste into another Forma window |
| [ / ] | Undo / redo a view change |
| Alt+B | Cycle the background (gradient, grey, black, light grey) |
| Page Up / Page Down | Smooth mesh preview one step up / down |
| Ctrl+M / Shift+M / Ctrl+Shift+M | Main menu bar / panel menus / panel tool bar |
| Ctrl+Space | Hide / show the UI around the views |
| Hold K + drag | Scrub time in the viewport |
| Shift+S | Keyframe menu at the mouse |
| Shift+G | Recent commands at the mouse |
| F1 | Hotkey cheat sheet |
| Ctrl+Q | Quit |

Not mapped: Maya's T (Show Manipulator Tool) and 0 (default quality display), since Forma has no equivalent tool.

**Blender hotkeys inside the Blender-style modes.** **Sculpt Mode**, **Grease Pencil** (Draw / Edit / Sculpt / Vertex Paint), **Geometry Nodes Mode** and **Shading Mode** switch the keyboard to Blender's keymap while they are on, and the Maya hotkeys come back when you leave. Your remapped Maya keys are kept.
- **In every one of these modes:**
  - Ctrl+Z / Ctrl+Shift+Z undo / redo, Shift+R repeat, Ctrl+S save, F12 render, F1 hotkeys, Ctrl+Space maximize.
  - Space plays, Left / Right step frames, Up / Down jump keys, Shift+Left / Right go to start / end.
  - Numpad 1 / 3 / 7 front / right / top (Ctrl for the opposite side), Numpad 5 perspective, Numpad 0 scene camera.
  - Home frames all, Numpad . frames the selection, Shift+Z toggles wireframe, Alt+Z X-ray.
  - N toggles the sidebar, T the tool bar, Ctrl+Tab opens the mode menu.
  - Middle mouse orbits, Shift+MMB pans, Ctrl+MMB zooms. Alt navigation still works.
- **Sculpt Mode:** the brush keys (X, C, I, G, S, L, P, K, M, Shift+C, Shift+T), F / Shift+F / Ctrl+F, Ctrl+D, Ctrl+R, PgUp / PgDn, Shift+S, plus:
  - A: mask menu.
  - W: face-set menu.
  - E: stroke-method menu.
  - R: voxel size.
  - Shift+Space: brush menu.
- **Grease Pencil:** Blender's Draw / Edit / Sculpt keys, plus I (insert-keyframe menu) and X (delete-keyframe menu) in Draw.
- **Geometry Nodes Mode / Shading Mode** (Windows → Modes, or Ctrl+Tab): Blender's Geometry Nodes / Shading workspaces.
  - Layout: the node editor is docked under the 3D view. Shading also switches the view to Material Preview.
  - Keys go to the area under the mouse.
  - **Node editor:** Shift+A add, G grab, Shift+D duplicate, X / Delete delete, Ctrl+X dissolve with reconnect, Ctrl+C / V copy / paste, A / Alt+A / Ctrl+I select, L / Shift+L select linked, F make links, M mute, H collapse, Ctrl+H hide unlinked sockets, F2 rename, F3 / Ctrl+F search / find, Home / Numpad . view, Ctrl+Shift+click preview / viewer, Ctrl+right-drag cut links, N sidebar.
    - Geometry Nodes only: Ctrl+G / Ctrl+Alt+G / Tab / Ctrl+Tab for groups.
    - Shading only: Ctrl+J / Alt+P for frames.
  - **3D view:** Blender's object keys: G / R / S, X, Shift+D, Alt+D, A / Alt+A / Ctrl+I, H / Alt+H / Shift+H, Tab, I / Alt+I keys, Ctrl+P / Alt+P, Shift+A add menu.
  - Leave with **Exit**, **Object Mode** in the header's mode menu, or Ctrl+Tab.

**G (Edit → Repeat)** repeats the last command as a whole, like Maya: the menu item, its option settings and its interactive part. For example, Extrude repeats with its drag and tools start again. Navigation, selection, display, file, window and tool-switch commands are not repeated. The menu item shows what will repeat (*Repeat "Extrude"*), and **Edit → Recent Commands** lists the last 15 commands. You can remap the key in the Hotkey Editor.

### Duplicate, Duplicate Special, Instance (Edit menu)

- **Duplicate** (Ctrl+D) copies the selected objects and what is under them.
- **Duplicate Special** (Ctrl+Shift+D; option box) makes **several copies**, each offset from the previous one:
  - **Offsets:** translate / rotate are added, scale is multiplied. Use it for stairs, spirals, rows of fence posts.
  - **Geometry type:** **copy**, or **instance** (the copies share one mesh: move or sculpt the points of any of them and all change).
  - **Group under:** parent, world, or a new group.
  - **Duplicate input graph:** also copies the animation.
  - **Duplicate input connections:** keeps the constraints, driven keys, skin and deformers that drive the original.
- **Duplicate with Transform** (Shift+D): duplicate, move / rotate / scale the copy, then press Shift+D to repeat the same step again and again.
- **Instance** shares the mesh with the original.
- Instances stay instances through save / load and undo. Edits that rebuild a mesh's topology make the edited one unique.

```python
cmds.duplicateSpecial('step', copies=12, translate=(0, 0.2, 0), rotate=(0, 15, 0), instance=True, group='new')
cmds.duplicate('post', instance=True); cmds.duplicateWithTransform()
```

### Modeling tools

| Tool | How |
|---|---|
| Extrude (Ctrl+E) | Faces: move the mouse to set thickness along the normals. Edges: extrude into quads. Vertices: Blender-style; a lone vertex grows a new edge, then the new verts follow the mouse (X/Y/Z constrain). Click to confirm, Esc to cancel |
| Bevel (Ctrl+B) | Works on selected edges (faces/verts are converted; objects bevel every edge, or only hard edges). Drag left/right to set the width, +/- to scale, **[ / ]** (or Page Up / Down) for fewer / more segments, click to confirm. See **Rounded bevel** below |
| Multi-Cut (Ctrl+Shift+X) | Click edges to cut across faces. Ctrl+click inserts an edge loop; Shift snaps to 10%. Enter or right-click starts a new cut, Backspace undoes, Esc exits |
| Insert Edge Loop | Mesh Tools menu; click an edge |
| Target Weld | Drag from one vertex onto another vertex of the same mesh |
| Merge / Merge to Center | Edit Mesh menu; the option box sets the distance threshold |
| Fill Hole / Create Face (Ctrl+Shift+F) | Builds a face from the selected vertices or the hole bounded by selected edges |
| Combine / Separate / Extract | Mesh menu. Extract splits the selected faces off into a new object |
| Mirror | Mesh menu; the option box sets axis, object pivot or world origin, and merge threshold. Border vertices are welded |
| Grab | Mesh Tools menu; move the selection with the mouse (X/Y/Z constrain) |

In component mode, Shift + RMB opens a modeling-tools marking menu with these tools.

#### Rounded bevel (Edit Mesh → Bevel ❏, like Maya's Bevel / Blender's Bevel)

The option box (also used by the interactive tool and the Modeling Toolkit's **Bevel segs / Profile / Chamfer** row):

- **Width type:** absolute (drag sets the distance) or fraction (a fraction of the shortest edge at the bevelled vertices; 0.5 meets in the middle).
- **Segments:** 1 is the classic chamfer (unchanged from earlier versions); more segments round the bevel. Segment edges are marked soft, so the result shades smooth.
- **Profile:** 0.5 is a circular arc (exact on right angles), 0.25 flat, 1 square, below 0.25 concave. **Chamfer** forces a flat profile with the segments kept.
- **Mitering:** where three or more bevelled edges meet (box corners), **auto / patch** fills the corner with a quad grid (a sphere octant on a box), **radial** with a triangle fan, **none** with a single n-gon. Mixed corners get an n-gon.
- **Affect:** edges, or vertices (vertex bevel: each vertex is cut off; rounded with segments > 1).
- **Objects: only hard edges** / **Hard edge angle:** in object mode, bevel only edges marked hard or sharper than the angle.

The result is always a valid mesh (closed meshes stay closed), UVs are interpolated from the original faces, and per-face normals follow their faces.

```python
cmds.polyBevel(offset=0.1, segments=3)                       # rounded, profile 0.5
cmds.polyBevel(fraction=0.25, segments=4, profile=0.7)       # fraction of the shortest edge, fuller profile
cmds.polyBevel(offset=0.05, segments=2, hardEdgesOnly=True, angle=40)
cmds.polyBevel(offset=0.2, affect='vertices', segments=3)    # vertex bevel
cmds.polyBevel(offset=0.1, segments=3, chamfer=True, mitering='radial')
```

### NURBS curves and surfaces (Create, and the Curves / Surfaces menus of the Modeling menu set)

Curves and surfaces are true NURBS: any degree, open or periodic, with non-uniform knots and rational
weights. Circles from Three Point Arc and partial revolves are exact.

**Creating curves**

| Tool | How |
| --- | --- |
| CV Curve Tool | Click to place control vertices. |
| EP Curve Tool | Click points the curve passes through. |
| Bezier Curve Tool | Click to add anchors; click-drag to pull mirrored tangent handles. |
| Three Point Circular Arc | Click the start, a point on the arc, and the end. |
| NURBS Circle / Square | Create → NURBS Primitives. |

- All curve tools snap with X, C and V.
- In every curve tool, Enter creates the curve, Backspace removes the last point and Esc finishes.

**Primitives** (Create → NURBS Primitives; the option boxes set sizes, sections, spans, degree and caps)
- Sphere, Cube, Cylinder, Cone, Plane and Torus.
- Each keeps construction history (`makeNurbSphere1`, …): edit radius, spans and the rest in the Channel Box or
  Attribute Editor.
- The cube is a group of six patches; cylinder and cone caps are child surfaces.

**Editing curves** (Curves menu)
- **Open/Close** and **Rebuild** (spans, degree).
- **Reverse Direction**.
- **Insert Knot** and **Detach**: pick a point on the curve.
- **Attach**: joins the nearest ends.
- **Offset Curve**.
- **Duplicate Surface Curves**: pick an isoparm to extract an exact curve.

**Building surfaces** (Surfaces menu)
- **Loft**: through curves, in selection order.
- **Planar**: closed planar curves; inner curves become holes.
- **Revolve**: around an axis through the curve's pivot, with start/end sweep. Cubic gives Maya's periodic
  surface, linear a faceted one, exact rational arcs are available.
- **Extrude**: tube or flat along a path (select the profile, then the path), with scale and twist; or
  distance.
- **Birail** (Birail 1 / 2 / 3+): select one or more profile curves, then the two rails. Each profile is moved,
  turned and scaled so its ends ride the rails (proportional: its height scales with the rail gap too); between
  profiles the shapes blend (linear or smooth). The surface passes through the profiles and the rails.
- **Boundary**: 3 or 4 edge curves.
- **Bevel Plus**: closed planar outlines become a bevelled solid with caps (straight or round bevel).

Loft, Planar, Revolve, Extrude and Boundary keep construction history: move or reshape the input curves and the
surface follows. Their option boxes can also output polygons.

**Editing surfaces**
- **CVs:** right-click a surface → Control Vertex, then use the move / rotate / scale tools (soft selection
  works). Scripts address CVs as `surface.cv[u][v]`.
- **Insert Isoparms, Detach, Duplicate Surface Curves:** pick on the surface. A dashed isoparm previews the
  pick; Shift switches between u and v.
- **Attach** (nearest edges), **Rebuild** (spans, degree), **Reverse Direction** (u, v, swap) and
  **Open/Close**.
- **Trimming:** **Project Curve on Surface** (along the active view or to the closest points), then the
  **Trim Tool** — click the region to keep or discard. Seams and poles are handled.
  Closed curves cut out regions (nested ones make holes); open curves that cross the surface from edge to edge
  split it (ends that stop just short of an edge are extended to it), and several cuts combine: the clicked piece
  is exactly the region they bound. **Untrim Surfaces** removes the trims.
- **Fillets:** **Circular Fillet** (two surfaces; radius, reverse either normal, optional contact curves on
  surface for the Trim Tool) rolls a ball along both surfaces: the fillet is tangent to each and keeps the radius.
  **Freeform Fillet** (two surfaces) blends their nearest edges, or any isoparms, with a cubic surface leaving each
  tangentially (depth, bias). **Curves → Curve Fillet** joins two coplanar curves with a circular arc (radius;
  trim cuts the curves back to it, join attaches everything).
- **Stitch:** **Stitch Edges** makes the closest edges of two surfaces coincide exactly (the CV rows are made to
  match by knot insertion; weighting 0 keeps the first edge, 1 the second, 0.5 meets halfway; match tangents
  lines up the next rows so the seam is tangent continuous). **Stitch Surface Points** moves the selected CVs of
  several surfaces to their average. **Global Stitch** stitches every pair of edges of the selected surfaces that
  are closer than the max separation, and pulls shared corners together.
- **Sculpt Geometry Tool:** drag over a surface to push, pull, smooth, relax (smooth along the surface only) or
  erase (back to the CVs before the tool started) its CVs. Each CV is moved through the surface point it controls
  most (its Greville point), with the sculpt brush falloffs. Ctrl swaps push / pull, Shift smooths; radius,
  strength, falloff and operation are in the option box. Every stroke is one undo step.
- **Deformers:** Bind Skin, clusters, lattices and blend shapes deform a surface's CVs - it stays NURBS and
  re-tessellates (targets of a NURBS blend shape are surfaces with the same CVs). Skin weights live on the CVs.
- **Display smoothness:** keys **1 / 2 / 3** set rough, medium or fine (Surfaces → Display Smoothness).
  Cycles always renders the fine tessellation.
- **Convert NURBS to Polygons:**
  - tessellation: display, fine, general (u × v over the whole surface) or per span;
  - output: quads or triangles.

  A polygon tool used on a surface converts it to polygons, as Maya's tools ask you to.
- **Rendering and FBX:** surfaces render in Cycles, have UVs, and export to FBX and OBJ as their
  tessellation (a skinned surface exports as a skinned mesh, its CV weights carried to the tessellation). Blender's
  FBX exporter cannot write NURBS surfaces or curves, so use IGES to exchange NURBS.
- **IGES** (File → Import / Export, `.igs` / `.iges`): exports surfaces (entity 128; trimmed surfaces as 144 with
  142 curves on surface), curves (126) and colours (314) in world space, centimetres; periodic shapes come back
  closed. Import also reads lines (110), arcs (100), composite curves (102), copious data (106) and
  transformation matrices (124), scales from the file's units, and rebuilds trims from parameter-space curves
  (or projects model-space boundaries when those are missing) as best it can.

**Scripting**

```python
cmds.nurbsSphere(radius=2, sections=8, spans=4, degree=3)
c1, c2 = cmds.circle(radius=1), cmds.circle(radius=2); cmds.move(0, 3, 0, c2)
s = cmds.loft(c1, c2, degree=3)                    # history: moving c2 reshapes s
cmds.revolve('profile', startSweep=0, endSweep=270, sections=8, degree=3)
cmds.extrude('ring', 'path', style='tube', scale=0.5)
cmds.planarSrf('outline', 'hole'); cmds.boundary('a', 'b', 'c', 'd')
cmds.projectCurve('cutter', surface='ball', direction=(0, 0, -1)); cmds.trimSurface('ball', 2.0, 4.0, keep=False)
cmds.insertKnotSurface('ball', 1.5, 'u'); cmds.detachSurface('ball', 2.0, 'v'); cmds.rebuildSurface('ball', spansU=6)
cmds.epCurve(points); cmds.bezierCurve(anchors); cmds.circularArc(p1, p2, p3); cmds.rebuildCurve('c', spans=8)
cmds.nurbsToPoly('ball', method='general', uNumber=16, vNumber=32)
cmds.birail('profile1', 'profile2', 'rail1', 'rail2', transform='proportional', blend='smooth')  # rails last
cmds.circularFillet('floor', 'wall', radius=0.25, curveOnSurface=True)
cmds.freeformFillet('a', 'b', curveA='u1', curveB=('v', 0.5), depth=0.5, bias=0.0)
cmds.curveFillet('line1', 'line2', radius=0.5, trim=True)
cmds.stitchSurfaceEdges('a', 'b', weight=0.5, tangent=True); cmds.globalStitch('p1', 'p2', 'p3', maxSeparation=0.1)
cmds.stitchSurfacePoints('a.cv[3][3]', 'b.cv[0][0]', ('c', 0.5, 0.5))      # CVs and surface points meet
cmds.sculptGeometry('ball', center=(0, 1, 0), radius=0.5, operation='pull', strength=0.5)
cmds.exportFile('model.igs'); cmds.importFile('part.iges')                  # or cmds.igesExport / igesImport
```

### Graph Editor

Open it from **Windows → Animation Editors → Graph Editor**, the Key menu, or the Animation shelf. It shows
the curves of the selected objects. Pick attributes in the left list to show only those curves.

| Action | Input |
|---|---|
| Select keys | Click; drag a marquee; Shift toggles, Ctrl deselects, Ctrl+Shift adds. Clicking a curve selects all its keys |
| Move keys | Drag a selected key, or MMB-drag anywhere. Shift constrains to time or value. Snaps to whole frames unless "Snap to frames" is off |
| Edit tangents | Drag the orange handles of selected keys. **Break** / **Unify** split or join the in/out handles |
| Tangent types | Toolbar or Tangents menu: Auto (no overshoot), Spline, Linear, Flat, Stepped; in and out sides separately |
| Infinity | Curves menu or right-click: Constant, Linear, Cycle, Cycle with Offset, Oscillate (shown dashed) |
| Exact values | Frame / Value fields; they accept `+=2`-style relative edits |
| Navigate | Alt+MMB or Alt+LMB pans, Alt+RMB zooms, the wheel zooms (Shift = values only, Ctrl = time only). F frames the selection, A frames all |
| Time | Click or drag in the frame ruler, or hold K and drag |
| Keys | I inserts a key at the current time; Delete removes keys; Z / Ctrl+Z undo |

Scripting: `cmds.keyTangent(obj, attribute='tx', inTangentType='linear', outTangentType='linear')`,
`cmds.setInfinity(obj, postInfinite='cycle')`, `cmds.keyframe(obj, 'translateX', 12, value=3)`,
`cmds.keyframeQuery(obj, 'tx')`.

### Locators (Create → Locator)

A locator marks a point in space. It draws as a small X/Y/Z cross, never renders, and is selectable and snappable like any object. Use it:
- as a parent: move the locator, and what is under it follows;
- as a constraint target (point, aim, parent, pole vector ...);
- as a simple animation control.

**Local Scale** (`localScaleX/Y/Z` in the Channel Box) resizes the cross without scaling its children. `cmds.wireColor(loc, side='Left')` (or `color=(r, g, b)`) colours it.

```python
loc = cmds.spaceLocator(name='aim_target', position=(0, 5, 3), localScale=0.5)
cmds.aimConstraint(loc, 'hero_L_eye')
```

### Rigging (menu set F3)

| Menu | Items |
|---|---|
| **Skeleton** | **Create Joints**: click to place joints; each joint parents to the previous one. Click an existing joint to branch from it; Backspace removes the last joint; Enter finishes and orients the chain. Also: **Orient Joint** (X down the bone, Y up), **Mirror Joint** (option box: axis, `L_`→`R_` renaming), **Create IK Handle**, **Create IK/FK Chain**, **Create FK Controls**, **Snap FK to IK** / **Snap IK to FK** |
| **Skin** | **Bind Skin**: select the root joint and the mesh; the option box sets max influences and dropoff. Weights are automatic, from distance to the bones. Also: **Unbind**, **Go to Bind Pose**, **Paint Skin Weights** (replace / add / subtract / smooth, opacity, radius, flood; heat-map display) |
| **Constrain** | Parent, Point, Orient, Scale (option box: maintain offset), Aim, Pole Vector, Delete Constraints. Select the target(s) first, then the object to constrain |
| **Control** | Circle, Square, Cube, Diamond, Cross and Sphere control curves (option box: size) |

#### Auto Rig (Skeleton → Auto Rig...)

Rigs a character's body and face and builds the controls for you, like Maya's Quick Rig. The character should stand on the ground at the origin, Y up, facing +Z, in a T or A pose. Select the mesh, plus separate eyeball meshes if it has them.

- **One-Click Rig** does everything below in one step.
- **Step-By-Step:**
  1. **Create Guides** fits guide spheres to the mesh. Move them onto the joints. Only the blue (left) side matters: the right side mirrors it when the skeleton is built.
  2. **Build Skeleton** creates oriented, labelled joints.
  3. **Create Controls** builds the control rig.
  4. **Bind Skin** binds the mesh.

  Building the skeleton again keeps your guides, so you can adjust them and rebuild.
- **Options:** spine joints (1–6), fingers per hand (0–5, thumb first), the face parts (jaw, eyes, eyelids, brows, lips, cheeks, nose), and max influences.

**The controls** are coloured by side: left blue, right red, centre yellow.

| Part | Controls |
|---|---|
| Body | Main (circle with arrows), COG, hips, FK spine, chest, neck, head, clavicles |
| Arms | IK/FK with pole vector and switch. They start in FK |
| Legs | IK/FK with a foot-shaped IK control. They start in IK |
| Reverse foot | Heel, toe-tip and ball pivots: rotate them to roll the foot. The toes stay planted on a ball roll |
| Fingers and toes | FK. They follow the hand and foot in both modes |
| Face | Jaw; eye aim (one control for both eyes, plus one per eye); eyelids (move up and down to blink); brows, cheeks, nose and lips. Lip corners follow the jaw halfway |

The hand and foot follow the IK control in IK. **Skeleton → Match** switches FK ↔ IK without popping, including the hand's rotation.

**Skin weights** are distance-to-bone for the body. Each face joint adds a local falloff, so a brow control moves the brow and not the forehead. Upper and lower lips and eyelids are kept apart, and eyeball meshes bind rigidly to their eyes. Refine with **Paint Skin Weights** / **Skin Tools**.

**Posing buttons:**
- **Select All Controls** (to key them)
- **Reset Controls**
- **Show / Hide Joints**
- **Show / Hide Guides**
- **Delete Rig**: unbinds and removes the skeleton and controls, keeping the guides
- **Delete Rig + Guides**

Names are `<name>_<side>_<part>`, e.g. `hero_L_elbow`, `hero_L_arm_ik_ctrl`, `hero_L_arm_ikfk_switch`. Everything lives under `<name>_rig`.

```python
cmds.autoRig('body', 'eyeL', 'eyeR', name='hero')             # one click
cmds.autoRig('head', name='face', body=False)                 # face only (the mesh is a head)
cmds.autoRigGuides('body', name='hero', fingers=4, spineJoints=2, faceParts=['jaw', 'eyes', 'brows'])
cmds.autoRigMirrorGuides(name='hero')                         # left -> right
cmds.autoRigSkeleton(name='hero'); cmds.autoRigControls(name='hero'); cmds.autoRigBind(name='hero')
cmds.setAttr('hero_L_arm_ikfk_switch.ikBlend', 1)             # left arm to IK
cmds.autoRigResetControls(name='hero'); cmds.autoRigShowJoints(name='hero', show=False)
cmds.wireColor('myCtrl', side='Left')                         # or color=(r, g, b); Maya drawing override
```

#### Control Picker (Skeleton → Control Picker..., or Windows → Animation Editors → Control Picker)

A separate window of buttons that select a rig's controls, like the pickers animators use in Maya. **New → From Auto Rig** builds one for an auto-rigged character, laid out from the rest pose (your current pose is kept):

- **Body tab:** a front-view silhouette of the character, with a button on every control. Buttons are coloured like the controls: the character's left (blue) is on the right of the picker, as in a front view. GLOBAL sits under the feet.
- **Face tab:** a close-up of the head with the face controls.
- **Global buttons:**
  - **Select All**
  - **Reset Selection**: zero the selected controls
  - **Key Selection**
  - **Hide Controls**
  - **Flip Pose**: swap the sides; centre controls flip in place
  - **Mirror Pose**: copy the selection onto the other side
- **Beside each arm and leg:**
  - **Snap IK → FK** / **Snap FK → IK**: switch without popping
  - **FK Mode** / **IK Mode**
  - **IK Blend**: selects the switch
- **Hand poses:** 8 slots per hand. Click an empty slot (+) to store the current finger pose, and a stored slot (●) to apply it. Right-click a slot to name, overwrite or clear it.

**Using it:**
- Click a button to select its controls. Shift toggles, Ctrl removes, and dragging a box selects many.
- Right-click a button to key or reset its controls.
- Hover a button to see its controls.
- Mouse wheel zooms, the middle button pans, and F resets the view.
- **Character prefix:** points the same picker at another character built the same way, e.g. `hero2_...`.

**Edit Layout** (checkbox) to make your own picker:
- **Moving buttons:** drag to move them; drag the corner handle to resize. Arrow keys nudge (Shift for 10), Ctrl+D duplicates, Delete removes, and double-click edits the label.
- **Right-click a button:** Label, Assign Selected Controls, Color (left / right / centre / custom), Size, Align, **Mirror to Other Side** (copies the buttons across and points them at the `_L_` ↔ `_R_` controls), Duplicate, Delete.
- **Right-click empty space:**
  - add a button for the selected controls
  - add buttons for every selected control, placed where it appears from the front
  - add a label or a pose slot
  - add action buttons, including IK/FK snap and mode buttons for a selected switch
- **More menu:**
  - Background: snapshot of the character, load an image, or clear
  - Add / rename / delete tabs
  - Canvas size
  - Export / import the layout as `.json`, to reuse it in another scene
  - Delete the picker

**New → Empty** starts a blank picker for any rig. Pickers are stored in the scene (a hidden `<name>_picker` node), so they save with the file, and every edit can be undone.

```python
cmds.pickerCreate(name='hero')                       # from the auto rig 'hero'; fromRig=False for an empty one
layout = cmds.pickerLayout('hero_picker'); cmds.pickerSetLayout('hero_picker', layout)
cmds.mirrorPose('hero_L_shoulder_fk_ctrl')           # onto hero_R_...; flip=True swaps both sides
pose = cmds.poseValues('hero_L_index1_fk_ctrl'); cmds.applyPose(pose); cmds.resetTransforms('hero_L_arm_ik_ctrl')
```

**IK/FK chain.** Select the start and end joints and choose **Create IK/FK Chain**. This builds:
- FK circle controls in offset groups (rotate only);
- an IK handle under a cube IK control;
- a pole-vector control;
- an IK/FK switch control with an `ikBlend` attribute: 1 = IK, 0 = FK, and anything in between blends.

The controls of the inactive mode hide automatically. Snap FK to IK / Snap IK to FK switch modes without the pose popping, so animators can change modes mid-shot.

**How it evaluates:** animation → constraints → IK (blended with the FK pose) → skin, after every change. Constraint/IK-driven channels show in blue in the Channel Box. Your own FK values and keys are never overwritten.

**Channel Box.** Right-click to Lock, Unlock, or Lock and Hide channels, and to Add Attribute (custom keyable floats, e.g. for switches). The manipulators respect locked channels.

**Scripting:**
```python
cmds.joint(position=(0, 5, 0), parent='', name='L_shoulder')
cmds.orientJoint('L_shoulder')
cmds.skinCluster('L_shoulder', 'arm', maxInfluences=4)
cmds.skinPercent('arm', [10, 11], [('L_elbow', 1.0)])
cmds.ikHandle('L_shoulder', 'L_wrist')
rig = cmds.createIKFKChain('L_shoulder', 'L_wrist')
cmds.setAttr(rig['switch'] + '.ikBlend', 0)
cmds.ikFkMatch(rig['handle'], to='ik')
cmds.parentConstraint('ctrl', 'prop'); cmds.aimConstraint('target', 'eye')
```

**Not yet:** dual-quaternion skinning, IK spline / ribbon rigs, mirroring skin weights, and editing a mesh's components after it is bound (edit in the bind pose, then rebind).

### Rendering with Cycles (menu set F6)

Forma renders with **Cycles**, Blender's path tracer. It runs Blender in the background, so you need the
free [Blender](https://www.blender.org) 4.2 or newer installed. Forma finds it automatically in the usual
install locations (Program Files on Windows, /Applications on macOS, `blender` on PATH on Linux), or you can set the
path in Render Settings → System. GPU rendering is picked automatically: OptiX/CUDA (NVIDIA), HIP (AMD),
Metal (Apple Silicon) or oneAPI (Intel), with CPU as the fallback.

| Feature | Details |
|---|---|
| **Render** | Ctrl+Shift+R or Render → Render Current Frame. Render Sequence renders the playback range to numbered images; skinned and animated poses are evaluated per frame. The Render View shows progress (frame and sample), and has Save Image, Cancel and a Log |
| **Cameras** | Create → Cameras → Camera / Camera from View. Settings: focal length (mm) and sensor width (mm), as in Cycles; clipping; depth of field (focus distance, f-stop). Focal length, focus distance and f-stop are keyable. Use View → Camera or Look Through Selected Camera to look through one; navigating then moves the camera, and a resolution gate shows the render frame |
| **Lights** | Create → Lights: Point, Spot, Area (square / rectangle / disk / ellipse), Directional (Sun). Intensity is in watts (W/m² for the sun), exactly the same units as Cycles. Color, soft-shadow radius or angle, spot cone and blend, cast shadows. Intensity is keyable |
| **Viewport lighting** | Panel → Lighting → Use All Lights (7) shades the viewport with the scene lights, in the same units, so the light balance matches the render |
| **Materials** | Principled BSDF: base color, metallic, roughness, IOR, transmission, coat, subsurface, alpha, emission, plus a box-mapped color texture. Presets under Lighting/Shading → Assign New Material: plastic, metal, gold, glass, rubber, emissive, clay. Edit them in the Attribute Editor's *material* tab; the viewport shows base color, transparency and emission |
| **Render Settings** | Resolution and presets; samples; noise threshold; denoise (OptiX or OpenImageDenoise); bounces; device; view transform (AgX / Filmic / Standard); exposure; transparent film; PNG / JPEG / EXR; output folder; background color or HDRI environment with rotation; auto-smooth angle. Smooth Mesh Preview (keys 2/3) renders as subdivision surfaces |

Scripting:
```python
cmds.camera(name='shotCam', position=(0, 4, 11), aim=(0, 1, 0), focalLength=50)
cmds.light('area', name='key', position=(-5, 7, 5), intensity=900); cmds.setLight('key', size=3)
cmds.setMaterial('ball', preset='glass'); cmds.setMaterial('box', base_color=[0.9, 0.2, 0.1], roughness=0.3)
cmds.renderSettings(width=1920, height=1080, samples=256, camera='shotCam')
cmds.worldSettings(hdri='C:/hdris/studio.hdr', strength=1.2)
from forma import render; render.render_blocking(scene, 'C:/renders')      # from the script editor
```

#### Render layers and AOVs (Render → Render Setup (Layers / AOVs)..., or Windows → Rendering Editors)

Render layers work like Maya's Render Setup. Each layer becomes a Blender view layer.

- **Layer settings:** each layer has:
  - an on/off check;
  - members: *All objects*, or Add / Remove Selected;
  - overrides: a material override, holdout (matte: cut out with alpha 0), indirect only (seen only in
    reflections, shadows and GI) and shadow catcher (only receives shadows; this applies in every layer);
  - its own AOV passes: beauty, diffuse direct / indirect / color, glossy and transmission direct / indirect /
    color, emission, environment, AO, shadow catcher, normal, depth (Z), mist, position, UV, motion vector,
    object ID and material ID (the object index is the Forma node id), and Cryptomatte object / material.
- **What gets written:** with at least one enabled layer, each frame writes `<name>_<layer>_<pass>[.####].png`
  per pass and/or one multilayer `<name>_layers[.####].exr` with every layer and pass. Choose which under
  *Layered output*. A `<name>[.####].passes.json` manifest is written too.
- **Main image:** the first enabled layer's beauty. With no enabled layer, Forma renders one image as before.
- **Render View:** a pass selector next to the frame list shows each layer and pass of the current frame.
- **Script:**
  - `cmds.renderLayerCreate('fg', members=['ball'], passes=['diffuse_color', 'z', 'crypto_object'])`;
  - `cmds.renderLayerEdit('bg', holdout=['ball'], material='clay', addPasses=['ao'], enabled=True)`;
  - `cmds.renderLayers(full=True)`, `cmds.renderLayerDelete(name)`, `cmds.renderLayerOutput(exr=True, png=False)`.

#### Batch render and the Render Queue (Render → Batch Render / Render Queue...)

**Batch Render** renders the playback range of the current scene to files in the background. The UI stays
usable. It saves the scene to a temporary copy, then renders that copy as a Render Queue job with progress and
Cancel.

The **Render Queue** window lists jobs:

- **Add jobs:** *Add Current Scene...* (a snapshot) or *Add Scene File...* (a `.forma` file), each with a frame
  range, camera, render layers, output folder and file name.
- **Manage jobs:** reorder with Up / Down, Remove, Re-queue, Cancel (the selected job, or everything) and
  Clear Finished.
- **Run:** jobs run one at a time in a separate process (`python -m forma.render.batch`, or `forma.exe
  --batch-render` when frozen), which launches Blender.
- **Watch and open:** each job shows its status and progress, and a log for the selected job. *Open Output
  Folder* opens where the images went.
- **Script:**
  - `cmds.batchRender(start=1, end=24, wait=False)`;
  - `cmds.renderQueueAdd('C:/shots/sh010.forma', camera='shotCam', start=1, end=48, layers=['fg'],
    output='C:/renders/sh010')`;
  - `cmds.renderQueueStart()`, `cmds.renderQueue()`, `cmds.renderQueueCancel()`, `cmds.renderQueueWait()`.

### UVs (UV menu in the Modeling menu set, Windows → Modeling Editors → UV Editor)

UVs are stored per face corner with real seams, as in other DCCs.
- **Defaults:** every primitive comes with a clean layout: plane, sphere (lat-long), cylinder/cone (side band + cap discs), torus, and the cube in 6 islands.
- **Kept through modeling:** extrude, bevel, multi-cut / edge loops, mirror, merge/weld, smooth, triangulate, fill, delete, combine/separate/extract, and curve surfacing (revolve, loft and tube get grid UVs).
- **OBJ:** import and export carry UVs (`vt`).

| Tool | What it does |
|---|---|
| Planar X/Y/Z, Camera-based, Cylindrical, Spherical | Projections. They use the face selection if there is one, else the whole mesh |
| Automatic | Per-face best axis (6 directions) → shells → packed into 0–1 |
| Unfold | Least-squares conformal map (LSCM) of each shell; keeps the shell's place and orientation |
| Layout | Packs all shells into 0–1 at a uniform texel density, without overlaps |
| Cut / Move-and-Sew UV edges | Make or close seams along selected edges. Sew moves the smaller shell onto the other |
| Normalize, Flip U/V, Rotate ±90 | Basic UV transforms |

**UV Editor.** Shows the UVs over the material's texture, or a checker.
- **Tools:** Q/W/E/R select/move/rotate/scale; MMB drags the selection; Shift snaps to an axis (move) or to 15° (rotate). Double-click selects a shell.
- **Edge mode:** pick edges for cutting and sewing.
- **Navigation:** wheel zooms; Alt+drag or MMB on empty space pans; F/A frame. Every edit is undoable.

### Normals (Mesh Display menu in the Modeling menu set)

Shading uses per-corner normals, smoothed across edges whose faces meet within the mesh's **normal angle** (30° by default: cubes stay hard, spheres are smooth). Cycles gets exactly the same normals as custom split normals.

| Tool | What it does |
|---|---|
| **Conform** | Makes face winding consistent inside each connected shell; the majority direction wins. Reports how many faces were flipped |
| **Reverse** | Flips the selected faces, or whole meshes in object mode. User-locked normals flip with them |
| **Reverse and Propagate** | Flips the selected faces, then flips every connected face that disagrees, so the whole shell follows. Other shells are untouched |
| **Soften / Harden Edge, Set Normal Angle** | With edges (or faces) selected, only those edges change: Soften makes them smooth, Harden makes them hard, Set Normal Angle decides each edge by the angle between its faces. On whole objects it sets the mesh's smoothing angle (180 fully soft, 0 faceted) and clears per-edge settings. Shading splits only where hard edges actually separate the faces around a vertex, so a single hard edge inside a smooth area has no effect, as in Maya |
| **Harden UV Borders** | Hard edges exactly on the UV seams, soft everywhere else: the usual game-asset setup for clean normal-map bakes |
| **Select → Hard Edges / Display → Hard Edges** | Select or draw (pale yellow) every edge that currently shades hard |
| **Face / Vertex Normals display** | Display → Polygons, or Mesh Display. Per object: face normals in green, vertex normals in cyan, locked normals in orange. **Normals Size** sets their length |
| **Vertex Normal Edit Tool** | Click vertices to pick them (Shift / Ctrl add or remove); drag to rotate their normals around the view axes (Shift constrains). The panel has Lock, Unlock, Average, Set to Face, Flip, Point Up and typed X/Y/Z, plus normal display size |
| **Lock / Unlock / Average / Set to Face** | Also in the menu. Edited normals are locked and survive modeling, undo and saving. **Set to Face** works per vertex-face as in Maya: the selected faces shade flat while their neighbours stay smooth |
| **Per vertex-face normals** | **Alt+F9**, the right-click marking menu (Vertex Face), or Select → Convert Selection to Vertex Faces. Each face corner gets a small handle inside the face; selecting handles and editing (drag, Lock, Average, Set to Face, Flip, typed XYZ) gives each face its own normal at a shared vertex. The tool panel switches between **Per Vertex** and **Per Vertex-Face**. Vertex-face normals override everything else, follow their faces through extrude, delete, Multi-Cut and edge loops (new cut points blend the face's normals at the edge ends, so a flat face stays flat), Bevel (the bevelled corners of a face inherit its normals; the new bevel faces shade automatically), mirror (reflected), combine and triangulate, flip with Reverse, save with the scene and render in Cycles. Editing a whole vertex again replaces its per-face split; Unlock returns either kind to automatic |

Vertex faces are named like Maya's: `cmds.select('pCube1.vtxFace[3][0:2]')` (vertex 3, faces 0-2); `cmds.selectMode('vtxface')`.

Scripting: `cmds.polyNormal(normalMode=0/1/2)` (reverse / reverse and propagate / conform), `cmds.polyConformNormals()`, `cmds.polyReversePropagate()`, `cmds.polySoftEdge(angle=)`, `cmds.polyNormalDisplay(face=, vertex=)`, `cmds.polyNormalPerVertex(obj, verts, normal= | rotate=(axis, deg) | lock= | unlock=)` (add `corners=[(face, vertex), ...]` or select vertex faces for per-face normals), `cmds.polyAverageNormal`, `cmds.polySetToFaceNormal`.

### Edge flow (organic loops)

| Tool | What it does |
|---|---|
| **Insert Edge Loop** (option box, or Multi-Cut Ctrl+click) | With **Edge flow** on, the new loop's vertices sit on a smooth curve through the neighbouring vertices instead of the straight edges, so loops on rounded forms keep their volume. **Edge flow amount** blends between straight (0) and full curve (1). The Multi-Cut HUD shows `[edge flow]` while it's on |
| **Edit Mesh → Edit Edge Flow** | Moves the vertices of the selected edge loop(s) onto the curve of the surrounding surface. Useful after cutting a loop straight, or after pushing vertices around |
| **Edit Mesh → Offset Edge Loop** | Inserts a loop on each side of the selected loop at a distance (0–0.5 of the neighbouring edges), honouring the edge flow setting. Good for holding edges before a smooth |

Hard/soft settings stay on edges through extrude, splits, mirror, combine, extract and saving. A typical game-ready pass: insert or offset the loops (with edge flow), then **Mesh Display → Harden UV Borders** (or select edges and Soften/Harden), and check them with **Display → Polygons → Hard Edges**.

Scripting: `cmds.polyInsertEdgeLoop(obj, edge, t=0.5, flow=1.0)`, `cmds.polyEditEdgeFlow(obj=None, edges=None, amount=1.0)`, `cmds.polyOffsetEdgeLoop(obj=None, edges=None, distance=0.25, flow=0.0)`, `cmds.polySoftEdge(obj, angle=0|180, edges=[...])`, `cmds.polyHardenUVBorders()`, `cmds.selectHardEdges()`, `cmds.polyNormalDisplay(hard=True)`.

### UV sets, pins and UDIM

- **UV sets.** A mesh can hold any number of named sets (`map1`, `lightmap`, …).
  - Manage them from the UV Editor's **UV Sets** menu and toolbar selector, or with `cmds.polyUVSet(obj, create=, copy=, rename=, delete=, current=)`.
  - The current set is the one shown, edited, textured in the viewport, and used by default in Cycles.
  - Every set survives all modeling operations. All sets render as named UV maps, and a material can pick one with the **UV Map** node.
- **Pins.** UV Editor → Modify → Pin / Unpin (pins draw as red squares), or `cmds.polyPinUV`.
  - **Unfold** keeps pinned UVs exactly in place: with two or more pins it solves around them; with one, it relaxes and puts that pin back.
  - With a partial UV selection, Unfold only relaxes the selected UVs and keeps the rest of the island fixed.
- **UDIM.** UVs can extend into tiles 1001–1100.
  - **Layout into UDIM Tiles** spreads the islands over N tiles, balanced by area. **Move Shells to UDIM Tile** moves the selected islands into a tile.
  - Image textures use the standard `<UDIM>` token (`skin.<UDIM>.png`). Picking `skin.1001.png` in the Material Editor offers to switch to the whole tile set.
  - The viewport draws each tile with its own image, the UV Editor shows labelled tiles, and Cycles loads them as a tiled image.

### Texture painting (Lighting/Shading or UV → Texture Paint Tool)

The simple painter: it paints one image texture of the material at a time (any channel, below), through the current UV set. It handles UV seams and UDIM tiles, and doesn't paint hidden back faces or occluded surfaces.
- **Brush:** colour, radius (`[` `]`), strength, hardness; Paint or Blur mode.
- **Channel:** Base Color, Roughness, Metallic, Normal, Height / Bump, Emission, Alpha, Specular, Coat, Sheen or
  Transmission. The tool paints the image texture connected to that Principled input; when there is none it makes
  one, filled with the input's current value, and connects it (Non-Color for values, through a Normal Map node for
  normal, a Bump node for height). Greyscale channels paint the **Value**; normal paints a direction colour.
  Script: `cmds.texturePaintChannel(obj, 'roughness', resolution=2048)` returns the image it paints.
- **Picking and undo:** Ctrl+click picks a colour from the surface; Z undoes strokes (20 levels).
- **No texture yet?** The tool offers to create one: resolution, fill colour, and one file per UDIM tile when the UVs span tiles. It's wired into the material automatically.
- **Saving:** textures save when you close the tool, press **Save Textures**, save the scene, or render, so Cycles always sees the latest strokes.

For whole materials, layers and masks, use the Texture Painter below.

### Texture Painter (Lighting/Shading or UV → Texture Painter), like Substance Painter

Paints **materials** onto a mesh in **layers**. Every stroke can set colour, roughness, metallic, height, emission, normal, opacity, ambient occlusion, specular, coat, sheen and transmission at once. The first time, the tool asks for a texture resolution (512–4096) and creates a **paint set** on the object's material:
- The current Principled values become the bottom fill layer.
- The mesh maps are baked for smart masks.
- The output textures are wired into the material (Base Color, Roughness, Metallic, Normal Map, Emission), so the viewport (Material Preview, key 8) and Cycles show the result.

The paint set is part of the material, so it saves with the scene and layer edits undo.

- **Layers** (top first, like Substance):
  - **+ Paint** layers hold painted channels; **+ Fill** layers are a uniform material.
  - Per layer: **Smart Material** / **Fill Material** presets (Steel, Iron, Gold, Copper, Aluminium, Rust, painted colours, Plastic, Rubber, Leather, Wood, Dirt, Dust, Glow), visibility, opacity, blend mode (normal, multiply, screen, overlay, add, subtract), channel toggles, up/down, duplicate, delete.
  - **Image...** puts a picture (decal or scanned texture) into a paint layer's channel.
- **Masks:**
  - **Add White** / **Add Black** gives a paintable mask; tick **Paint on the mask** or press M to paint it, using the brush's mask value.
  - A **smart mask** is generated from the baked maps (curvature, cavity, position X/Y/Z, UV island, noise, AO) with low/high limits and invert. It multiplies with a painted mask.
  - Smart materials stack fill layers with smart masks: **Worn Painted Metal** (bare metal on the edges), **Rusty Iron**, **Dusty Surface** (dust on top), **Dirty Cavities**, **Gold Trim Edges**.
- **Brush:**
  - Settings: Paint / Erase / Blur (X switches paint/erase), size (`[` `]`), flow, hardness, spacing.
  - A material preset loads every channel at once. Tick the channels a stroke changes and set each one's value.
  - **Height** strokes raise or lower the surface and become normal-map detail (**Height strength** sets how much). **Normal** strokes paint a direction straight into the normal map (direction and tilt).
  - Ctrl+click picks the colour under the cursor, Z undoes a stroke, and Alt + mouse still navigates.
- **Extra channels:** Opacity (Alpha), Ambient Occlusion (multiplied into the base colour through a Mix node), Specular, Coat, Sheen and Transmission are wired into the material once a layer uses them, so unused ones change nothing (an unused opacity does not make the material transparent).
- **Displacement:** the brush panel's **Displacement** value also connects the height output to the Material Output's Displacement (true displacement in Cycles; `cmds.painterLayerEdit(m, None, displacement=0.05)`).
- **Viewport:** the Material dropdown solos one channel (any of the twelve).
- **Bake Maps:**
  - **Curvature** marks convex edges, including crisp hard edges on low-poly models. Also baked: **cavity**, **position**, **UV islands** and **noise**, all computed in Forma.
  - **Ambient occlusion** and **Normal from high poly** (a detailed mesh over the low-poly one, with a cage distance) are baked with Cycles. The baked normal becomes the base of the normal map.
- **Export Textures:**
  - **blender**: BaseColor / Roughness / Metallic / Normal (OpenGL) / Emissive / Height, plus Opacity / AmbientOcclusion / Specular / Coat / Sheen / Transmission when layers use them.
  - **unreal**: BaseColor / OcclusionRoughnessMetallic packed / Normal (DirectX).
  - **unity**: Albedo / MetallicSmoothness / Normal / Emission.

```python
m = cmds.painterCreate('crate', resolution=2048)
cmds.painterSmartMaterial(m, 'Worn Painted Metal')
lid = cmds.painterAddLayer(m, 'fill', material_preset='Rust')
cmds.painterSetMask(m, lid, generator={'map': 'cavity', 'low': 0.6, 'high': 0.95, 'invert': True})
cmds.painterBake(m, maps=['ao', 'normal'], highpoly='crate_sculpt', cage=0.02)
cmds.painterExport(m, 'C:/textures', preset='unreal')
```

### Material Editor (Windows → Rendering Editors → Material Editor), like Blender's Shader Editor

The node library is **Blender's own**: all 87 shader nodes of Blender 5.2, with their sockets, defaults and options, so any graph rebuilds 1:1 in Cycles.

| Category | Nodes |
|---|---|
| Shaders | Principled BSDF, Diffuse, Glossy, Metallic, Glass, Refraction, Translucent, Transparent, Sheen, Toon, Subsurface, Emission, Holdout, Mix / Add Shader, hair and volume shaders, Ray Portal |
| Textures | Image, Environment, Noise, Voronoi, Wave, Brick, Checker, Gradient, Magic, White Noise, Gabor, Sky, IES |
| Color | Mix (every blend mode), Hue/Saturation/Value, Invert, Brightness/Contrast, Gamma, RGB Curves, Light Falloff |
| Vector | Mapping, Bump, Normal Map, Normal, Displacement, Vector Displacement, Vector Rotate, Vector Transform, Vector Curves |
| Converter | Math, Vector Math (all operations), Map Range, Clamp, Color Ramp, Combine / Separate XYZ and Color, RGB to BW, Float Curve, Blackbody, Wavelength, Shader to RGB |
| Input | Texture Coordinate, UV Map, Geometry, Attribute, Color Attribute, Object Info, Layer Weight, Fresnel, Light Path, Ambient Occlusion, Bevel, Wireframe, Tangent, Camera Data, Value, RGB |
| Layout | Frame, Reroute |

**Editing**, as in Blender:
- **Adding and connecting:**
  - Shift+A / Tab / right-click adds a node; type to search.
  - Drag an output onto an input to connect; drag a connected input to unplug.
  - **Ctrl + right-drag** cuts links.
- **Values:** click a value or colour on a node to edit it in place. The right panel edits every input and option, including Color Ramps, RGB/Vector/Float **Curves**, the image file and the node **Label**.
- **Sockets follow the options:** e.g. Math set to Sine shows one input; Mix in Color mode shows the colour sockets.
- **Node shortcuts:**
  - **M** mutes a node (it passes its input through, in Cycles too).
  - **H** hides unused sockets.
  - **Ctrl+T** adds Texture Coordinate → Mapping to the selected textures (Node Wrangler).
  - **Ctrl+C / Ctrl+V** copy and paste, **Shift+D** duplicates, X deletes, F frames.
- **Frames:** drag a frame to move the nodes on it; drag its corner to resize it.
- **Previews:** texture and colour nodes show a **live thumbnail** of their output. The **preview sphere** updates instantly as you edit; **Render Preview** still renders a Cycles swatch.
- **Library** (left): New from preset, Duplicate, Rename, Delete, Assign to Selection, Select Objects with the material.
- **Settings** (right, like Blender's Material Properties): **Blend mode** — Auto (blended when Alpha / Transmission is below 1 or Alpha is connected), Opaque, Alpha Clip (with Clip threshold), Dithered (hashed), Blended; **Displacement** — Bump Only, Displacement Only, Displacement and Bump (Cycles moves the vertices, after **Displace subdiv** levels of subdivision); **Backface culling**. `cmds.materialSettings(m, blend_mode='clip', alpha_threshold=0.5)`.
- **Quick edits:** `cmds.setMaterial(obj, ...)` sets any Principled input by name (specular, specular_tint, anisotropic, coat_roughness, sheen, sheen_tint, subsurface_radius, thin_film_thickness, ...), a texture per channel (`roughness_texture=path`, `normal_texture=`, `bump_texture=`, `displacement_texture=` with `displacement_scale=`, ...; `''` removes it) and the settings above. The Attribute Editor's material panel shows the common inputs.

**In the viewport:**
- Materials that read only an image show it directly.
- Procedural textures, colour ramps, maths, Bump / Normal Map, the Displacement output, and maps on Roughness / Metallic / Normal / Emission / Alpha / Coat / Sheen / Transmission / Specular are evaluated over each mesh's UVs in the background. Material Preview (8) then shows the real colour, roughness, metallic, normal detail (displacement as bump), glow, alpha and the coat / sheen layers; Shaded / Textured (5, 6; OpenGL and GPU viewports) shows colour, normal detail, per-pixel roughness / metallic in the highlight, emission and alpha (clip / dithered / blended).

```python
m = cmds.createMaterial('rust', preset='metal')
n = cmds.shaderNode(m, 'noise'); cmds.connectShader(m, n, 'Fac', 'principled', 'Roughness')
cmds.setShaderProp(m, n, 'noise_type', 'RIDGED_MULTIFRACTAL')
cmds.shaderTextureSetup(m, n)                       # Ctrl+T
cmds.shaderNodeFlags(m, n, mute=True, label='Grime')
cmds.assignMaterial(m, 'crate')
```

Remap any hotkey in **Windows → Settings/Preferences → Hotkey Editor**. On macOS, Ctrl shortcuts are Cmd.

### Custom attributes (Modify → Add / Edit / Delete Attribute, or the Attribute Editor's Attributes menu)

**Add Attribute** adds to every selected node, with OK, Add (keeps the window open) and Cancel:

- **Long name:** letters, digits, `_` and `#`. The **nice name** is generated Maya-style (`fingerCurl` → "Finger Curl"), or typed with **Override nice name**.
- **Make attribute:**
  - **Keyable:** in the Channel Box and can be keyed.
  - **Displayable:** in the Channel Box (italic), not keyable.
  - **Hidden:** only reachable from script or Edit Attribute.
- **Data type:**
  - **Vector:** three floats `nameX/Y/Z`, edited as one.
  - **Float, Integer, Boolean.**
  - **String:** shown in the Attribute Editor; never keyable.
  - **Enum:** names one per line, or `A:B:C`.
- **Minimum / Maximum / Default** for numbers. Values, typed edits and keys are clamped to the range.
- **Attribute type:** only Scalar. Forma has no particles, so Per Particle is disabled.

The Channel Box shows booleans as on/off and enums by name (type a name to set it). Enum and boolean keys are stepped. The Attribute Editor's **Extra Attributes** section has a checkbox, drop-down, text field or number fields for each one.

**Edit Attribute** renames (animation, locks and vector children move along), changes the nice name, keyable/displayable/hidden, min/max (blank clears it) and enum names. **Delete Attributes** removes them with their animation; the Channel Box right-click menu also has Add / Edit / Delete Attributes for the selected channels. Built-in attributes can't be edited or deleted. Everything undoes, saves and duplicates.

Scripting:
- `cmds.addAttr(obj, longName=, attributeType='float'|'int'|'bool'|'enum'|'vector'|'string', niceName=, make='keyable'|'displayable'|'hidden', minValue=, maxValue=, defaultValue=, enumNames='A:B')`
  - Maya's `keyable=` / `hidden=` / `dataType='string'` flags also work.
- `cmds.editAttr(obj, attr, newName=, niceName=, make=, minValue=, maxValue=, enumNames=, defaultValue=)`
- `cmds.deleteAttr('obj.attr')`
- `cmds.listAttr(obj, userDefined=True)`
- `cmds.attributeQuery(obj, attr)`
- `cmds.getAttr('obj.mode', asString=True)`
- `cmds.setAttr('obj.mode', 'High')`, or a tuple for a vector.

### Building from a single vertex (Blender-style)

**Create → Polygon Primitives → Single Vertex**, or the **Single Vertex** button on the Poly Modeling shelf (`cmds.polySingleVertex(position=(x, y, z))`), makes a mesh with one vertex. It starts in vertex mode with that vertex selected, like Blender's edit mode. The shelf also has an **Extrude to Cursor** button.

| Step | How |
|---|---|
| **Extrude a vertex** | **Ctrl+E** (Edit Mesh → Extrude; Blender's E). A new vertex and edge follow the mouse in the view plane; X / Y / Z lock to an axis; click or Enter confirms; right-click or Esc leaves the new vertex on top of the old one. Repeat to draw a chain; select any vertex to branch from it |
| **Extrude to Cursor** (Mesh Tools → **Extrude to Cursor Tool**; Blender's Ctrl+right-click) | A left-click on empty space (or Ctrl+right-click, as in Blender) extrudes the selection so its centre lands on the clicked point, and the new part stays selected, so you can keep clicking to draw. With nothing selected, a click adds a loose vertex to the highlighted mesh. Works on vertices (new edges), edges (quads) and faces. Clicking a vertex selects it and dragging draws a marquee, so you can select several vertices and extrude them together. Shift+click toggles components, Ctrl+click deselects, Ctrl+Shift adds, X (grid snap) rounds to whole units, and Esc, Enter or right-click exits. The option box sets where points land: **view plane** through the selection (default), **ground plane** (Y = 0), or **surface** of another mesh under the cursor (for retopology). Script: `cmds.polyExtrudeToPoint((x, y, z))` |
| **Make a face** | Select the vertices and use Mesh → **Fill Hole / Create Face**. A chain of loose edges fills in chain order (closing the gap) and faces the camera |
| **Extrude edges into quads** | In edge mode, Ctrl+E on a loose edge or border edge makes a quad that follows the mouse; repeat for strips |
| **Delete** | Deleting a vertex removes it with its edges and faces; neighbours along loose edges stay as single vertices. Deleting a loose edge removes it and any end vertex left unused |

Loose vertices show as dots in object mode and can be clicked to select their object. Other single vertices in a mesh survive deletes, merges and bevels elsewhere in it. Meshes without faces are saved and undone like any other, and Cycles skips them.

### Mirroring, renaming and Skin Tools (Rigging menu set)

**Skeleton → Mirror Joint** (option box) duplicates the selected chain across the **YZ / XZ / XY** plane:

- **Behavior:** rotating the copy by the same values as the original gives mirrored motion.
- **Orientation:** the copy keeps the original's world orientation.

Names use **Search for / Replace with** plus extra pairs such as `lb_:rb_, l_:r_`; each pair is tried both ways. A joint with no match gets `_mirror`.

**Joint labels** work like Maya's. Each joint can have:
- a **Side**: Center, Left, Right or None;
- a **Type**: Root, Hip, Knee, Foot, Toe, Spine, Neck, Head, Collar, Shoulder, Elbow, Hand, Finger, Thumb, Index/Middle/Ring/Pinky Finger, toes, props…;
- **Other** with free text such as "Tail";
- **Draw Label**.

Set them in the Attribute Editor's **Joint Labelling** section or from **Skeleton → Joint Labelling**:
- **Label Based on Joint Names** reads `lb_forearm` → L Elbow, `RightUpLeg` → R Hip, `L_Tail3` → L Tail.
- **Show / Hide All Labels** and **Show Selected Labels**.
- **Add Left / Right Side**, **Add Center**, **No Side** and **Add Type**.

Labels are drawn next to the joints: blue for left, red for right, yellow for center. Mirror Joint gives the copies the opposite side. **Mirror Skin Weights** and Skin Tools' interactive mirror can match influences **by label** (Left Elbow ↔ Right Elbow, the closest one if several match), so names don't need to follow any pattern.

Script:
- `cmds.jointLabel(j, side='Left', type='Elbow', otherType=, drawLabel=True, hierarchy=)`
- `cmds.labelJointsFromNames()`
- `cmds.showJointLabels(all=True)`
- `cmds.jointLabelQuery(j)`
- Maya's `setAttr('j.side', 1)` / `getAttr('j.type', asString=True)`

**Modify → Search and Replace Names** (option box) renames a joint chain or anything else, e.g. `lb_arm` → `rb_arm`. It works in the selected **hierarchy**, the **selected** nodes only, or **all** nodes.

**Skin → Mirror Skin Weights** (option box) copies weights from one side to the other:

- **Plane:** YZ / XZ / XY.
- **Direction:** + to − or − to +.
- **Surface association:** **closest point** (interpolated on the surface) or **closest vertex**.
- **Influence association:** **name** (the pairs, e.g. `lb_:rb_`, with closest joint as a fallback) or **closest joint**.

Vertices on the plane are made symmetric. With Skin Tools layers, it mirrors the active layer and its mask.

**Skin → Transfer Influence Weights** (option box) "renames" weights. Every influence containing the *from* text hands its weights to the matching *to* influence (`lb_arm` → `rb_arm`): **move**, **swap** or **copy**.

#### Skin Tools (Skin → Skin Tools...)

**Initialize** turns the current weights into the **Base Weights** layer. Everything after that is non-destructive: the skin's final weights are the layers composited bottom to top.

- **Layers:** each layer holds weights for any influences. A partly painted vertex is partly transparent, so the layers below show through. Each layer has an **on/off** switch, an **opacity**, and a per-vertex **mask** (Clear / Invert / Empty, or paint it). Turning a layer off or deleting it restores what's underneath exactly. **Duplicate**, **Merge Down**, **Move Up/Down**, and rename by double-clicking.
- **Layer Groups** hold no weights. Their single mask and opacity control everything nested inside, e.g. one mask for a whole hand. Use **Into Group Above** / **Out of Group** to organise.
- **Brushes:**
  - **Replace**, **Add**.
  - **Scale:** reduces an influence without removing it.
  - **Smooth**; Shift+drag also smooths.
  - **Sharpen:** restores creases.
- **Brush targets:** the chosen influence or the layer/group mask.
- **Brush modes:**
  - **Surface:** visible vertices.
  - **Screen:** everything under the brush, both sides of the mesh.
  - **Volume:** a 3D sphere; smoothing crosses disconnected pieces.
- **Flood:** applies the brush to the selected vertices or the whole mesh.
- **Interactive mirror** repeats every dab on the other side, with the mirrored influence, as you paint. **Mirror Layer + to − / − to +** mirrors the layer in one go. **Remove Layers** keeps the final weights and drops the stack.
- Layers save with the scene and undo like everything else. The viewport shows the influence's final weights, or the mask being painted.

Scripting:
- `cmds.mirrorJoint(root, plane='YZ', function='behavior', search='lb_', replace='rb_', pairs=)`
- `cmds.searchReplaceNames('lb_', 'rb_', 'lb_arm', scope='hierarchy')`
- `cmds.mirrorSkinWeights(obj, plane=, direction='+', surface='closest point', association='name', pairs='lb_:rb_', layer=)`
- `cmds.transferInfluenceWeights(obj, 'lb_', 'rb_', mode='move'|'swap'|'copy')`
- Layers:
  - `cmds.skinLayersInit / skinLayerAdd(obj, name, group=, parent=, above=)`
  - `skinLayerEdit(obj, layer, name=, enabled=, opacity=, parent=, index=, active=)`
  - `skinLayerDelete / skinLayerDuplicate / skinLayerMergeDown`
  - `skinLayerFlood(obj, layer, influence=, value=, mode=, target='weights'|'mask')`
  - `skinLayerMask(obj, layer, op='clear'|'invert'|'empty')`
  - `skinLayersRemove`

### Grease Pencil (Create → Grease Pencil, Ctrl+Tab)

This is modeled on Blender's Grease Pencil as described in the current (5.2) manual. **Create → Grease Pencil → Blank / Stroke** adds an object; **Grease Pencil Mode** (Ctrl+Tab) enters Draw Mode. With nothing selected, it creates a blank object first. Tab toggles Draw / Edit, Ctrl+Tab cycles Draw → Edit → Sculpt → Vertex Paint, and right-click shows the mode/tool menu.

**Leaving:** Esc, the header's **Exit** button, or **Object Mode** in the header's mode menu.

**Blender-style layout (only while in the mode; the Maya layout comes back when you leave):**
- **Tool header** across the top:
  - the mode menu (Object / Draw / Edit / Sculpt / Vertex Paint);
  - the brush preset (pictures of Pencil, Pencil Soft, Ink Pen, Ink Pen Rough, Marker Bold, Marker Chisel, Airbrush);
  - the material, and the Material / Color switch with a color swatch;
  - **Radius** and **Strength**, each with a pen-pressure toggle;
  - the **Brush**, **Stroke**, **Randomize**, **Guides**, **Placement** and **Layer** popovers;
  - **Additive**, **Auto Key**, **Multiframe**, **2D Canvas** and **Exit**.
- **Toolbar** down the left with Blender-like icons for the mode's tools. In Draw mode: Draw, Fill, Erase, Tint, Cutter, Eyedropper, Line / Polyline / Arc / Curve / Box / Circle and Interpolate.
- **Properties dock** on the right:
  - **Tool** tab: brush grid, Brush Settings with **pen pressure curves**, Color, Stroke (stabilizer, post-processing including **Outline**), Randomize (with **Use Pressure**), Guides, Stroke Placement, the current tool's settings, edit operators and keyframe buttons.
  - **Data** tab: layers (masks, blend, opacity, onion skins…), materials, modifiers and object settings.
- **Dope Sheet** at the bottom, in place of the time slider, for animating the drawing:
  - Rows: one channel per layer, with show / lock / onion toggles. Keyframes are colored by type.
  - Playback: play / step / jump buttons, current frame and range, a scrubbing ruler.
  - Keys: click or Shift-click selects, box-drag selects, dragging moves keys, Shift+D duplicates, X deletes, R sets the key type, I inserts a key, Home frames all.
  - Header buttons: Onion Skin, Multiframe, and Interpolate Sequence with an easing choice.
  - Scripts: `cmds.gpKeySelect`, `gpKeysMove`, `gpKeysDelete`, `gpKeysSetType`.

**Drawing in 3D and 2D:**
- **Stroke Placement** puts lines on the drawing plane through the Origin or 3D Cursor, on the **Surface** of 3D objects under the pen (with an offset), or snapped onto existing strokes.
- The **Drawing Plane** is View, Front, Side, Top or 3D Cursor.
- **2D Canvas** switches to a front orthographic view, drawing on the front plane with 2D layer order. Turning it off restores the view.

**Pen pressure:** tablet pressure drives the radius and strength. Two **pressure curves** (with Linear / Soft / Firm / Ink presets) and a **Min Radius** shape the response, and the stroke preview shows the final widths. The HUD shows the live pen pressure. Sculpt brushes use the same pen pressure.

**Guides:** Circular, Radial, Parallel (angle), Grid and Isometric. Spacing and angle snapping are optional. The reference is the 3D cursor, the object or a custom point.

**Multiframe:** Edit / Sculpt / Vertex Paint reach every keyframe selected in the Dope Sheet, not only the current one.

**Data:**
- **Layers**: opacity, blend modes (Regular, Hard Light, Add, Subtract, Multiply, Divide), hide, lock, onion skinning, use lights, tint color/factor, and **masks** (any layers, each one invertible).
- **Keyframes per layer**, with Blender's keyframe types (keyframe, breakdown, moving hold, extreme, jitter, generated). A drawing holds until the next key.
- **Strokes**: per-point radius, strength and vertex color; cyclic; round/flat caps; fill color.
- **Materials**: stroke on/off with Line / Dots / Squares, fill on/off with Solid / Gradient, holdout.

**Draw mode tools:**
- **Draw** brush:
  - Size and strength, with pen pressure for either.
  - Caps, spacing, active smoothing, angle thinning, hardness.
  - **Stabilize** (lazy mouse; Shift+LMB toggles it per stroke).
  - **Post-processing**: smooth, iterations, subdivisions, simplify, trim.
  - **Randomize**: radius, strength, hue, saturation, value, jitter, per stroke or per point.
  - **Color**: material, or a color attribute with mix factor.
  - Alt+LMB for straight horizontal/vertical lines.
- **Erase**: Dissolve / Point / Stroke. Ctrl+LMB uses the eraser with any brush, and B does a box erase.
- **Fill**: a pixel flood fill of closed areas.
  - Layers: visible / active / above / below / all above / all below.
  - Boundary, precision, dilate/contract, stroke thickness, simplify, **gap closure**.
  - Alt-drag draws fill guide lines.
  - Unclosed areas are reported instead of filled.
- **Tint**: vertex color over strokes and/or fills; Ctrl erases it.
- **Line, Polyline, Arc, Curve, Box, Circle**:
  - Drag, then adjust the yellow end handles or cyan control handles.
  - Enter or middle mouse confirms; Esc or right-click cancels.
  - Shift snaps to 45° / squares / circles; Alt draws from the center; M flips an arc.
  - +/− or PageUp/PageDown change the point count; E chains the next shape from the end point.
  - Subdivisions and a thickness profile (constant / taper) in the settings.
- **Trim** (formerly Cutter): lasso strokes. Points are removed up to the next intersection with another stroke; optional flat caps.
- **Eyedropper**: makes a material from the color on screen. LMB makes a stroke material, Shift a fill material, Shift+Ctrl both.
- **Interpolate**: drag left/right between two keyframes to place a breakdown.

**Shortcuts:**
- F changes the brush size and Shift+F its strength (move the mouse, then click).
- Shift+I inserts a blank keyframe; Alt+I deletes the keyframe.
- Ctrl+E interpolates; Shift+Ctrl+E fills the sequence in between.
- Y picks the active layer and U the active material.

**Placement:**
- **Stroke placement**: Origin, 3D Cursor (the world origin; Forma has no 3D cursor), **Surface** (projects onto meshes, with an offset), or **Stroke** (the depth of the nearest existing point: all, end or first points).
- **Drawing plane**: View, Front (XZ), Side (YZ), Top (XY), Cursor.
- **Drawing options**:
  - **Additive drawing**: a new key starts from a copy of the drawing shown.
  - **Auto keying**: drawing on a frame without a key makes one; turned off, strokes go into the held key.
  - **AutoMerge**: joins a new stroke to a nearby stroke end.
  - **Draw on back**: new strokes go behind the others.

**Edit mode:**
- **Selection**: click, box, lasso and circle select, in points or strokes mode (1 / 2). A all, Alt+A none, Ctrl+I invert, L linked, Ctrl ± grow/shrink.
- **Transforms**: G / R / S (X/Y/Z constrain, click or Enter confirms, right-click or Esc cancels), Alt+S radius.
- **Operators**:
  - E extrude, Shift+D duplicate.
  - X delete (Points, Strokes, Dissolve, Dissolve Between, Keyframe), Ctrl+X dissolve.
  - F close / toggle cyclic, Ctrl+J join (Shift: join and copy).
  - M move to layer (or a new one), P separate (selection, material, layer), Ctrl+C copy, H show stroke direction.
- **Panel operators**: subdivide, simplify (adaptive, fixed, sample, merge), smooth, trim, switch direction, set caps, assign material, arrange (front, forward, backward, back), merge by distance.

**Sculpt mode:**
- Brushes: Smooth, Thickness, Strength, Randomize, Grab, Pull, Twist, Pinch (Ctrl: inflate), Clone (pastes what Ctrl+C copied).
- Settings: falloff, add/subtract direction (Ctrl inverts), which attributes Smooth and Randomize affect (position, strength, thickness).
- Auto-masking by layer or material, and a selection mask.

**Vertex Paint mode:** Paint, Blur, Average, Smear, Replace, on strokes, fills or both. Shift+X samples a color.

**Onion skinning**: Keyframes or Frames mode, before/after counts, opacity, fade, custom colors, filter by keyframe type. **Stroke depth order** is 3D location or 2D layers.

**Modifiers** (non-destructive, optionally limited to one layer, and can be applied):
- **Generate**: Array, Build (sequential / concurrent / additive; grow / shrink / vanish), Dot Dash, Envelope, Length, Mirror, Multiple Strokes, Simplify, Subdivide.
- **Deform**: Noise, Offset, Smooth, Thickness, Time Offset (regular / reverse / fixed / ping pong / chain).
- **Color**: Hue/Saturation, Opacity, Tint.

**Rendering:** Cycles renders strokes as round curves with their per-point thickness, and fills as polygons. They are unlit unless the layer has **Use lights** on. **Convert to Mesh** bakes the current frame to a mesh.

Scripting: `cmds.greasePencil`, `gpAddStroke(obj, points, radius=, opacity=, vcolor=, material=, layer=, frame=, cyclic=, additive=, autoKey=)`, plus:
- layers: `gpLayerAdd/Edit/Remove/Duplicate/MergeDown`;
- materials: `gpMaterialAdd/Edit/Remove`;
- keyframes: `gpFrameInsert/Delete/Move`;
- selection and editing: `gpSelect`, `gpDelete`, `gpSubdivide`, `gpSimplify`, `gpSmooth`, `gpTrim`, `gpStrokeEdit`, `gpJoin`, `gpDuplicate`, `gpExtrude`, `gpTransform`, `gpMergeByDistance`, `gpMoveToLayer`, `gpArrange`, `gpSeparate`, `gpInterpolate`;
- modifiers and settings: `gpModifierAdd/Edit/Remove/Apply`, `gpSettings`, `gpConvertToMesh`.

Not implemented from Blender's Grease Pencil:
- **Not built**: weight paint mode and the Armature / Hook / Lattice / Shrinkwrap modifiers, Line Art, visual effects (blur, glow, shadow…), texture materials, Bézier/NURBS stroke types and the Pen tool, guides, canvas grid, multiframe editing, and fill direction "Inverted".
- **Rendering differences**: dots and squares render as lines in Cycles, and the layer blend modes other than Regular / Add / Subtract are approximations.


**Line thickness:**
- **Brush size** is the line's full width in pixels when you draw, default 8. The stroke preview shows the real width; F resizes the brush.
- **Layers tab → Line thickness** thins or thickens every stroke of a layer (1 = as drawn).
- **Object tab:**
  - **Thinner / Thicker / Set width** change the selected strokes, or the whole frame when none are selected.
  - **Thickness scale** scales the whole object.
- Script: `cmds.gpLayerEdit(obj, layer, thickness=0.5)`, `cmds.gpStrokeThickness(obj, 0.8, mode='scale')`, `cmds.gpStrokeThickness(obj, 0.01, mode='set')`.

**Motion trails:** set the line thickness and keyframe size in the Create Editable Motion Trail option box or the Motion Trail Editor. The default is 1.5 px.

### Image planes (reference pictures and backgrounds)

- **Create → Free Image Plane:** pick a picture. You get an object you move, rotate and scale like any other, and click to select.
- **View → Image Plane → Import Image** (viewport menu): attaches the picture to that view's camera, either a camera node or the persp / front / side / top view. **View → Image Plane → Image Plane Attributes** selects it.
- **Camera Attribute Editor → Environment > Image Plane > Create:** the same, for a camera node. The plane is parented under the camera and deleted with it.

Camera planes face their camera at a **depth** and fit its film: the render gate for camera nodes, the view for persp / ortho. They follow the camera as it moves. With **Auto** depth they sit 100 units out in perspective views and just behind the scene centre in orthographic views, so a front/side reference never covers the model.

Attribute Editor settings:

| Setting | Options |
|---|---|
| **Image** | Image name (browse), **Use image sequence** (the last number in the file name becomes the frame, e.g. `plate.0001.png` → `plate.0012.png`, keeping the padding), **Frame offset**; shows the file and size currently displayed |
| **Display** | **Display mode** (None, Outline, RGB, RGBA, Luminance, RGBA Luminance); camera planes show only when **looking through** the camera or in **all views**; **Alpha gain**, **Colour gain** |
| **Placement** | **Fit** (best, fill, horizontal, vertical, to size), **Width / Height** (lock aspect to the image), **Offset** X/Y, **Depth** (Auto or a distance), **Rotate**, **Flip horizontal / vertical** |
| **Render** | **Visible in render**: Cycles renders free planes, and a camera's planes when that camera renders, as emissive picture quads, transparent where the image is (RGBA) |

**Show → Image Planes** toggles them per viewport. Several planes at different depths layer naturally, and geometry in front hides them. Depth compositing from EXR/IFF depth channels isn't supported: the planes are pictures only.

Scripting:
- `cmds.imagePlane(fileName, camera=None|'persp'|'front'|camNode, width=, ...)`
- `cmds.imagePlaneEdit(plane, imageName=, useFrameExtension=, frameOffset=, displayMode=, displayOnlyIfCurrent=, fit=, width=, height=, lockAspect=, offset=, depth=, rotate=, flipH=, flipV=, alphaGain=, colorGain=, render=)`
- `cmds.imagePlaneQuery(plane)`

### Snapping (status line magnet / Crv / Pnt / Ctr / Live buttons, or hold a key)

| Snap | Hold | What it does |
| --- | --- | --- |
| Grid | X | Moves land on grid intersections (Preferences → Snapping → Grid snap increment). |
| Curves / edges | C | Lands on the nearest point of a curve or mesh edge under the cursor. |
| Points | V | Lands on the nearest vertex, CV or pivot. |
| Projected center | (Ctr button) | Lands on the middle of the object under the cursor. |
| Live surface | (Live button, Modify → Make Live) | Lands on the surface of the live mesh. Press it again to stop. |
| Relative | J | Moves and scales in whole steps from where the drag started; rotates in steps. |

- Hold the key and drag (left-click a handle or middle-click anywhere). The status line buttons keep a snap on; the held key turns it on only while it is down.
- Dragging an **axis arrow** snaps along that axis only: the object slides until it lines up with the target. Dragging a plane handle keeps it on that plane.
- Objects and components never snap to themselves. In component mode this means you can snap a vertex onto another vertex of the same mesh, or onto other geometry.
- The CV Curve, Create Joints and Extrude to Cursor tools snap their clicks the same way.
- **Pivots:** hold **D**, or press **Insert** (Modify → Edit Pivot) to toggle, then use the move tool to move the pivot without moving the object. Combine it with V to put the pivot on a vertex.
- The snap distance in pixels is set in Preferences → Snapping.

### Preferences (Windows → Settings/Preferences → Preferences)

Maya-style categories:
- **Interface:** tooltips, status bar.
- **Display:** background, grid, selection color, HUD, manipulator and normal sizes.
- **Settings:** working units (mm … yd; used by FBX), angular and time units, up axis.
- **Animation:** auto key, playback.
- **Manipulators:** move, rotate and scale steps; manipulator size.
- **Selection:** click box, preselection highlight.
- **Snapping.**
- **Modeling:** merge threshold, default smoothing angle.
- **Files / Projects:** project folder, autosave every N minutes with N kept versions, crash recovery, asset
  library folders (see *Autosave and crash recovery* and *Asset Browser*).
- **Undo:** on/off, queue size.
- **Rendering:** Blender path, device.
- **Scripting:** command line language, echo all commands, user setup script.
- **Plug-ins.**

Changes apply at once. **Save** keeps them, **Cancel** puts back what you had, and **Restore Default Settings** resets everything. Settings are stored in `preferences.json` in the Forma settings folder. Set the `FORMA_CONFIG` environment variable to use another folder.

At startup Forma runs `userSetup.py` and `userSetup.fsl` from `<settings>/scripts`. That folder is also on the FSL script path and Python's `sys.path`.

### Shelves (Windows → Settings/Preferences → Shelf Editor)

- **Shelves:** create, rename, delete and reorder them.
- **Buttons:** add buttons and separators, duplicate, delete, reorder.
- **For each button:** label, tooltip, icon (built-in glyphs or any image file) with an optional text overlay, a **command** and a **double-click command**, each in Python or FSL.
- **From the shelf itself:** right-click a button to edit, duplicate or delete it; right-click the tab bar for shelf commands. Ctrl+Shift+click a menu item to add it to the current shelf.
- **From the Script Editor:** **Save Script to Shelf…** turns the current script into a button.
- Shelves are saved in `shelves.json`.

### FSL: Forma Script Language (Script Editor FSL tab, or the Python/FSL toggle on the command line)

FSL is a MEL-like language. Every `cmds` command is an FSL command, in shell or call syntax:

```
string $c = `polyCube -w 2 -n "crate"`;       // backticks capture a command's result
move -r 0 1 0 $c;                             // boolean flags take no value
setAttr ($c + ".rotateY") 45;
string $s = polySphere("-radius", 0.5);       // call syntax
global proc makeRow(int $n) {
    for ($i = 0; $i < $n; $i++) {
        string $o = `polyCube`;
        move $i 0 0 $o;
    }
}
makeRow 5;
```

**Language**
- **Types:** `int float string vector matrix`, arrays `string $a[]`, `global` variables.
- **Control flow:** `if/else while do for for-in switch break continue return`.
- **Procs:** `proc` and `global proc` (a `proc` is private to its file, as in MEL).
- **Values:** `{…}` arrays, `<<x, y, z>>` vectors. `*` between vectors is the dot product.
- **Expressions:** `?:`, `+=`, `++`.

**Flags:** they match the full name, a short alias, a unique prefix or the initials (`-sx` → `subdivisionsX`).

**Builtins**
- **Strings:** `print size tokenize substitute match gmatch substring toupper tolower strip stringArrayToString`.
- **Math:** `abs floor ceil sqrt sin cos min max clamp mag rand…`.
- **Evaluation:** `eval`, `python("…")` (runs Python and returns its value), `source "file.fsl"`, `catch(…)`.
- **Introspection:** `exists`, `whatIs`.
- **Messages:** `error`, `warning`.

**Running scripts:** calling an unknown proc `foo` sources `foo.fsl` from the scripts folder automatically. Errors report the line number.

### Custom tools (Custom Tools menu → Create Tool…)

A tool is named code (Python or FSL) with a label, a tooltip, an optional hotkey and the menu it appears in. You can also add it to the current shelf. Tools are saved in `tools.json` and show up in the Hotkey Editor.

```python
cmds.toolCommand('lift', 'string $s[] = `ls -sl`; for ($o in $s) move -r 0 1 0 $o;', language='fsl',
                 label='Lift', hotkey='Ctrl+Alt+L')
cmds.runTool('lift'); cmds.listTools(); cmds.toolCommand('lift', delete=True)
```

### File formats (File → Import… / Export All… / Export Selection…)

- **OBJ:** meshes and UVs, and a `.mtl` with every material channel: Kd / Ks / Ke / Ns / Ni / d / Tf, the PBR
  extension (Pr, Pm, Ps, Pc, Pcr, aniso) and textures (map_Kd, map_Pr, map_Pm, map_Ke, map_d, map_Ks, norm,
  map_Bump, disp). Importing reads the `.mtl` back into Principled materials.
- **Material channels (FBX / USD / OBJ):** every Principled value plus one texture per channel — base colour,
  metallic, roughness, normal map, bump, emission, alpha, specular, coat, sheen, transmission, displacement. Channels
  driven by procedural nodes (or painted layer stacks) are baked to PNGs in `<file>_textures` next to the export.
- **FBX** (needs Blender, which is also the renderer). It carries:
  - meshes with UVs and materials (all channels, see above);
  - hierarchies;
  - joints as an armature;
  - skin weights;
  - cameras and lights;
  - animation, baked per frame, so constraints and IK come out right;
  - blend shapes as shape keys, with their current weights and animated weights. On import, shape keys become
    a Forma blend shape again.
- **USD** (`.usd`, `.usda`, `.usdc`, `.usdz`; needs Blender). It carries:
  - meshes with UVs, normals and a UsdPreviewSurface material;
  - hierarchies, cameras and lights;
  - joints and skin (UsdSkel) and blend shapes;
  - animation over the playback range.
  - Meshes moved by clusters, lattices, point caches or physics are baked to per-frame points.
- **Alembic** (`.abc`; needs Blender). Alembic has no skeletons, so it carries:
  - meshes with UVs and normals, hierarchy, cameras and transforms;
  - every deformed mesh (skin, blend shapes, clusters, lattices, physics, point caches) baked to per-frame
    points over the playback range. Joints are written as plain transforms.
- **Geometry caches:** animated geometry read from Alembic or USD becomes a **pointCache** deformer on the mesh.
  It holds per-frame object-space points, plays back with the timeline, is saved in the scene and appears in
  `cmds.listDeformers`. Script: `deformers.add_point_cache(node, points, start)`.
- **Export Selection** works for every format. It writes the selection and everything under it.
- **Scale:** FBX, USD and Alembic use the working units in Preferences → Settings (default centimeters, as in
  Maya).
- **Not carried over:** Alembic materials, custom normals on import, and clusters / lattices into FBX (FBX
  exports the rest pose plus blend shapes).
- **Plug-in formats:** plug-ins can add more formats. The file dialog filter lists everything available.
- **Script:** `cmds.importFile(path)`, `cmds.exportFile(path, selection=False)`.

### Plug-ins (Windows → Settings/Preferences → Plug-in Manager)

**Full guide: [docs/PLUGINS.md](docs/PLUGINS.md)** covers the complete API, undo, FSL, file formats, a worked example and testing.

A plug-in is a `.py` file:

```python
"""Shown in the Plug-in Manager."""
PLUGIN_INFO = {'version': '1.0', 'author': 'me'}

def initializePlugin(forma):
    def hello(name='world'):
        forma.message(f'// hello {name}')
    forma.register_command('hello', hello, undoable=False)       # cmds.hello / FSL "hello -name you;"
    forma.add_menu_item('Say Hello', hello)                      # in a Plug-ins menu
    forma.add_shelf_button('Hello', 'cmds.hello()', 'Hi')
    forma.add_tool('helloTool', 'hello -name tool;', language='fsl', hotkey='Ctrl+Alt+H')
    forma.add_file_translator('My format', ['myf'], import_fn, export_fn)
    forma.on_scene_changed(callback)

def uninitializePlugin(forma):                                   # optional
    pass
```

- **What `forma` gives you:** `forma.cmds`, `forma.app` and `forma.window`. Commands registered with `undoable=True` (the default) can be undone like any other command.
- **Clean unload:** unloading removes everything the plug-in added. If `initializePlugin` fails, anything it already added is removed too.
- **Where plug-ins are found:** `plug-ins/` next to Forma (there is a sample, `scatter_tools.py`), `<settings>/plug-ins`, and the folders in Preferences → Plug-ins.
- **Plug-in Manager:** **Browse…** loads a file from anywhere. Tick **Auto load** to load a plug-in at startup.

### Maya layout, workspaces and icons

**Workspaces** (the menu bar's top-right **Workspace** box, or Windows → Workspaces)

| Workspace | Layout |
| --- | --- |
| Maya Classic | Everything on, Channel Box. |
| Modeling - Standard (default) | Outliner, Poly Modeling shelf, Modeling Toolkit, no time slider, as in Maya. |
| Modeling - Expert | Just the viewport and menus. |
| Sculpting | Sculpting shelf and menu set, Tool Settings. |
| Animation | Time slider and Animation shelf. |
| Rigging | Rigging shelf and menu set. |
| Rendering | Rendering shelf, Attribute Editor. |
| FX | FX shelf and menu set, time slider. |

The workspace is remembered between sessions.

**Status line**, left to right:

- menu set;
- new, open, save; undo, redo;
- **Selection mask** (which object types can be picked: polygons, curves, NURBS surfaces, joints, rendering, dynamics, miscellaneous; All On / All Off);
- object / vertex / edge / face / vertex-face modes;
- snap to grid / curve / point / projected center, Make Live, Soft Select;
- Render View, render the frame, **IPR** (the active view renders live with EEVEE), Render Settings, Hypershade;
- the **Live Surface** field;
- **Symmetry** (Off / Object X Y Z / World X Y Z);
- the Abs / Rel input box;
- the panel toggles: Modeling Toolkit, Attribute Editor, Tool Settings, Channel Box, Outliner.

**Shelves.** The gear on the left (Shelf Editor, New Shelf, Delete Shelf, Restore Defaults) and the tab list arrow. The default shelves are Curves / Surfaces, Poly Modeling, Sculpting, Rigging, Animation, Rendering, FX, Geometry Nodes and Custom. Shelves from earlier versions keep their buttons and gain the new shelves.

**Tool Box**

- **Tools:** Select, **Lasso** (draw around what to select), **Paint Selection** (brush over components or objects; Ctrl removes), Move, Rotate, Scale, Last Tool Used.
- **Quick layouts:** single, four views, two side by side, perspective / Outliner, perspective / Graph Editor.

**Outliner.** Display (expand / collapse all, sort alphabetically) and Show (all, polygon meshes, NURBS surfaces, curves, joints, lights, cameras, Geometry Nodes objects, groups) menus, with an icon per object type.

**Viewport panel**

- **Renderer menu and drop-down:** the panel's **Renderer** menu and the drop-down at the right end of its menu bar choose **Viewport (Default)**, **Material Preview (EEVEE)** or **Rendered (EEVEE)** for that view. The menu can also render with Cycles.
- **Camera tools:** select camera, camera attributes, camera bookmarks, image plane, Grease Pencil.
- **Gates:** grid, film gate, resolution gate (the render size with the outside dimmed).
- **Shading:** wireframe, smooth shade, wireframe on shaded, default material, textured, all lights, shadows.
- **EEVEE effects:** ambient occlusion and anti-aliasing for the EEVEE modes.
- **Isolate Select:** only the selection is drawn in that view.
- **X-Ray toggles:** X-Ray, X-Ray joints, X-Ray active components.
- **Color:** **exposure** and **gamma**, and color management with a view transform (sRGB gamma / Standard / Filmic / AgX).
- **Show Toolbar:** Panels → Show Toolbar hides the bar.
- **Poly Count HUD:** shows Verts / Edges / Faces / Tris / UVs for the scene, the selected objects and the selected components, like Maya.

**Modeling Toolkit** (right panel tab; the right panel's tabs run along the top as in Maya)

- **Component modes.**
- **Pick/Marquee, Drag** (paint selection), **Tweak/Marquee** (press on a component and drag it straight away).
- **Highlight Backfaces** and **Highlight Nearest Component**.
- **Camera Based Selection.**
- **Symmetry.**
- **Selection Constraint:** grow, shrink, edge loop, hard edges.
- **Transform Constraint:**
  - **Edge:** moves slide along edges.
  - **Surface:** moved vertices stay on the original surface.
- **Soft Selection.**
- **Mesh:** Combine, Separate, Smooth, Boolean (menu).
- **Components:** Extrude, Bevel, **Bridge**, **Add Divisions**.
- **Tools:** Multi-Cut, Target Weld, **Connect**, **Quad Draw**.
- **Transform settings** of the current tool: axis orientation, Edit / Reset Pivot, step snap.

**New modeling commands**

- **Bridge** (Edit Mesh, option box: divisions): joins two border edge loops or chains, or two face regions (which are removed), with quads. Winding matches the mesh.
- **Add Divisions** (Edit Mesh, option box: levels): splits the selected faces (or whole meshes) into quads; neighboring faces get the edge points.
- **Connect** (Mesh Tools):
  - edges: joins their midpoints across faces;
  - vertices: joins pairs that share a face.
- **Quad Draw** (Mesh Tools), simplified retopology:
  - click to drop dots on the live surface (or any mesh, or the ground);
  - Shift+click between four dots or vertices to make a quad (three: a triangle);
  - Ctrl+click removes a dot.

  The quads go into the selected mesh or a new `quadDraw` mesh.
- **Symmetry:** selecting components adds their mirror partners, and moving them moves the partners mirrored.
- **Script:** `cmds.polyBridgeEdge(divisions=1)`, `cmds.polySubdivideFacet(divisions=2)`, `cmds.polyConnectComponents()`, `cmds.symmetricModelling('object_x')`.

**Icons.** Every tool and option (all ~450 actions) has a painted icon in Maya's style, colored by family:

| Family | Color |
| --- | --- |
| Polygons | Orange |
| NURBS | Blue |
| Curves | Light blue |
| UVs | Green |
| Rigging | Gold |
| Constraints | Teal |
| Animation | Red |
| Lights / rendering | Yellow |
| Materials | Purple |
| FX | Magenta |
| Sculpting | Lavender |
| Display / editors | Grey-blue |

- **Badges:** small corner badges mark variants (+ create, × delete, gear options, axis arrows for X / Y / Z, ...).
- **Where they show:** menus show them, and dragging any menu item to the shelf (or adding it with the Shelf Editor) gives the button that action's picture (`act:<action id>`).
- **No text icons:** old text glyphs ("UVEd", "Pnt", ...) and unknown names map to pictures. Text is never drawn as an icon.
- **Code:** `forma/ui/maya_icons.py`. Icons are painted on demand at any size, sharp on high-DPI screens.

### Move, Rotate and Scale tool options (Tool Settings; hold W / E / R + LMB for the marking menus)

**Axis Orientation**

Each tool has its own Axis Orientation. Middle-click the combo box to switch back to the previous orientation.

| Orientation | Move | Rotate | Scale | Axes |
| --- | --- | --- | --- | --- |
| World | ✓ | ✓ | ✓ | Scene axes. |
| Object | ✓ | ✓ | ✓ | The object's axes, which rotate with it. |
| Parent (Local) | ✓ | ✓ | ✓ | The parent's axes. |
| Component | ✓ | ✓ | ✓ | X along the selected edges; Y along the face / vertex normal. |
| Normal | ✓ | | ✓ | Every vertex moves or scales along its own U / N / V (Y handle = along the normal). |
| Normal Average | | | ✓ | The selected vertices' average normal. |
| Gimbal | | ✓ | | The Euler rings: each ring changes only its own rotate channel. |
| Along Rotation Axis | ✓ | | ✓ | The object's rotation without scale (with joint orient for joints). |
| Along Live Object Axis | ✓ | ✓ | ✓ | The axes of the live surface (Modify → Make Live). |
| Custom | ✓ | ✓ | ✓ | The X / Y / Z angles typed in Tool Settings. |

**Custom axis**

Tool Settings → Custom Axis Orientation → **Set to** Point / Edge / Face / Object, then click in the viewport:

- **Point:** X aims from the pivot at the clicked vertex.
- **Edge:** X runs along the clicked edge.
- **Face:** Y follows the face normal.
- **Object:** uses that object's axes.

The same four commands are in the tool marking menus.

**Manipulator gestures**

| Gesture | Effect |
| --- | --- |
| Drag the center | Free move. |
| Drag an arrow | Move along one axis. |
| Drag a plane square | Move in a plane. |
| Click a handle, then middle-drag anywhere | Use that handle. |
| Ctrl + click an arrow | Switch to the plane handle perpendicular to it. |
| Shift + middle-drag | Move along the axis that lines up with the drag. |
| Shift + drag a handle | Duplicate objects, or extrude faces / edges, then transform. |
| Ctrl+Shift + drag (components) | Slide the vertices along their edges. |
| Rotate: drag the outer ring | Rotate in screen space. |
| Rotate: drag inside the rings | Free rotate (Center as Virtual Trackball). |

**Rotate options**

- **Step Size:** the increment for snapping (hold J).
- **Discrete Rotate:** always rotates in Step Size steps.
- **Relative:** when off, Gimbal rotations snap the channel itself to whole steps.

**Common options**

- **Preserve Child Transform:** moving, rotating or scaling a parent leaves its children where they were.
- **Preserve UVs:** moving components shifts their UVs so the texture stays put on the surface.

**Input Box (status line)**

- Choose **Abs** or **Rel**, type `X Y Z` (or one value for all three) and press Enter. This moves, rotates or scales the selection with the current tool.
- With components, Abs moves their center to that point; Rel moves them by it. Rotate and scale work around their center.
- Script: `cmds.transformComponents('move', 0, 1, 0, relative=True)`.

### Component space: world, object, parent (local) and component coordinates

**Component Editor** (Windows → General Editors → Component Editor):

- lists the selected vertices, edges and faces with their position: vertex position, edge middle or face center;
- shows each edge's length;
- switches between World, Object (measured from the pivot) and Parent coordinates;
- type a value to move the component there, or tick **Edit as offsets** to move it by that much.

**Align the pivot to an edge:** in pivot mode (Insert, or hold D), **Ctrl + click** (left or middle button) an edge, face or vertex.

- Ctrl + click orients the pivot to it without moving the pivot; a plain click also moves the pivot there.
- Modify → Pivot → **Bake Pivot Orientation** then bakes that orientation into the transform.

**Script:**

- `cmds.componentPosition('pCube1.e[3]', space='object')` returns name, x, y, z and, for edges, the length.
- `cmds.setComponentPosition('pCube1.e[3]', (0, 1, 0), space='object', relative=True)`.
- `cmds.componentAxes('pCube1.e[3]')`.

### Face, edge and vertex options

**Preferences**

Selection:
- **Select faces with:** Whole face (click anywhere on it) or Center (click its dot).
- **Camera based selection:** off lets a marquee also pick back-facing components.

Modeling:
- **Keep faces together:** also a toggle in Edit Mesh. Off makes Extrude, Duplicate and Extract treat every face on its own.
- **Create meshes single-sided:** new meshes get backface culling.
- **Convert component selection:** e.g. Extrude with vertices selected works on the faces they enclose.

Display:
- **Vertex size.**

**Edit Mesh**

- **Duplicate:** copies faces into a new object.
- **Collapse:** each connected group of selected edges, or region of faces, becomes one vertex.
- **Merge Vertex Tool:** drag one vertex onto another.
- **Merge** and **Merge to Center**, with a threshold.

**Mesh → Cleanup** (option box)

- **Operation:** cleanup, or select matching.
- **Scope:** selected meshes or all.
- **Fix by tessellation:** 4-sided faces, faces with more than 4 sides, concave faces, non-planar faces (with a tolerance).
- **Remove geometry:**
  - lamina faces;
  - non-manifold geometry (geometry, or normals and geometry);
  - zero-length edges;
  - zero-area faces;
  - faces with zero map area.

  Each has its own tolerance.
- **Script:** `cmds.polyCleanup(all=True, lamina=True, nonmanifold='geometry', selectOnly=True)`.

**Insert Edge Loop** (option box, or Ctrl+Shift+right-click while the tool is on)

- **Maintain position:** relative distance, equal distance from the edge, or multiple edge loops (number of loops).
- **Auto Complete:** when off, click a start edge and then an end edge on the same ring for a partial loop.
- **Edge flow:** use edge flow, and adjust edge flow (0 – 1).
- **Smoothing angle:** new edges sharper than it become hard.
- **Script:** `cmds.polyInsertEdgeLoop(obj, edge, mode='multiple', count=3)` or `endEdge=` for a partial loop.

**Offset Edge Loop** (option box)

- **Edge offset (0 – 0.5):** how far the new loops sit from the original.
- **Partial loops:**
  - A single selected edge offsets its whole loop.
  - A selected chain makes partial loops.
  - **Delete edge** joins their ends to the chain's ends, so no n-gons are left. When it's off, the ends stay on the end edges and **Start/end vertex offset** pulls them in.
- **Edge flow:** insert with edge flow, and adjust edge flow.
- **Smoothing angle.**

**Display → Polygons**

- **Vertices** and **Vertex Size**.
- **Face Normals**, **Vertex Normals**, **Normals Size**.
- **Tangents / Binormals:** red tangent, blue binormal, from the UVs.
- **Hard Edges.**
- **UVs** and **Unshared UVs:** a green dot per UV; split UVs show as several dots.
- **Component IDs:** vertex, edge, face and UV numbers.
- **Backface Culling.**
- **Script:** `cmds.polyOptions(obj, displayVertices=True, displayTangents=True, vertexIds='toggle', doubleSided=False)`.

**Mesh Display → Set Vertex Normal**

- Type X Y Z for the selected vertices.
- **Normalize Normal:** when off, the typed length is kept and the normal display shows it.
- Unlock Normals returns them to automatic.

### Geometry Nodes (Mesh → Geometry Nodes; Windows → General Editors → Geometry Node Editor)

A procedural node system modeled on Blender's Geometry Nodes.

**Attaching a node tree**

- **Add Geometry Nodes to Selected:** the mesh's current shape becomes the **Group Input** geometry. It works like a modifier, and the result is what the object shows and renders.
- **New Geometry Nodes Object:** an object made only by nodes.
- **Presets:** Scatter on Surface, Noise Displace, Curve Pipe (Spiral) and Random Grid Array.
- **Apply:** bakes the result into a plain mesh. Editing the result's vertices by hand also bakes it, and undo brings the tree back.

**Updates.** The tree re-evaluates when:
- you edit it or change a parameter;
- an object read through Object Info / Collection Info moves or changes;
- the frame changes, if the tree uses Scene Time.

Trees are saved in the scene file; duplicating an object duplicates its tree.

**Geometry.** Like Blender's geometry set, it holds five components (volumes are described below):
- a mesh;
- a point cloud;
- curves;
- instances;
- volumes.

Each component carries named attributes on its domains: point, edge, face, corner, curve and instance.

**Fields.** Fields (Position, Normal, Index, ID, Random Value, Noise Texture, math on them, …) are evaluated per element on whatever geometry and domain the receiving node works on. Diamond sockets mark inputs that default to a field, such as Set Position's Position.

**Nodes, by category (about 120)**

| Category | Nodes |
| --- | --- |
| Input | Group Input, Value, Integer, Boolean, Vector, String, Material, Object Info, Collection Info (a group's children), Scene Time, Position, Normal, Index, ID, Radius |
| Output | Group Output, Viewer |
| Attribute | Named Attribute, Store Named Attribute, Remove Named Attribute, Capture Attribute, Attribute Statistic |
| Geometry | Transform Geometry, Set Position, Join Geometry, Merge by Distance, Delete Geometry, Separate Geometry, Separate Components, Bounding Box, Convex Hull, Geometry to Instance, Geometry Proximity, Sample Index, Raycast, Sample Nearest Surface, Sample Nearest |
| Mesh | Extrude Mesh (faces as regions or individual / edges / vertices, with Top and Side outputs), Subdivide Mesh, Subdivision Surface, Triangulate, Flip Faces, Dual Mesh, Mesh Boolean (difference / union / intersect), Mesh to Points, Mesh to Curve, Split Edges, Scale Elements, Set Shade Smooth, Face Area, Edge Angle, Mesh Island |
| Mesh Primitives | Cube, UV Sphere, Ico Sphere, Cylinder, Cone, Grid, Mesh Line, Mesh Circle |
| Curve | Curve to Mesh (profile sweep, fill caps), Resample Curve, Fill Curve, Curve to Points, Set Curve Radius, Set Curve Tilt, Trim Curve, Reverse Curve, Subdivide Curve, Curve Length, Spline Parameter, Curve Tangent |
| Curve Primitives | Curve Line, Curve Circle, Arc, Spiral, Quadrilateral, Star |
| Point | Distribute Points on Faces (random / Poisson disk), Points, Points to Vertices, Set Point Radius |
| Instances | Instance on Points (with Pick Instance), Realize Instances, Translate / Rotate / Scale Instances, Instance Rotation, Instance Scale |
| Material | Set Material, Set Material Index, Material Index, Material Selection |
| Group | Group (a node group from the scene's library) |
| Simulation | Simulation Zone (Simulation Input / Output) |
| Volume | Volume Cube, Points to Volume, Mesh to Volume, Volume to Mesh, Distribute Points in Volume |
| Texture | Noise Texture (fBm Perlin), White Noise Texture |
| Utilities | Repeat Zone (Repeat Input / Output), Math (about 40 operations, with clamp), Compare, Boolean Math, Map Range (linear / stepped / smooth), Clamp, Mix, Switch, Float to Integer, Random Value, Align Euler to Vector, Rotate Euler, Accumulate Field |
| Vector | Vector Math (about 25 operations), Vector Rotate, Combine XYZ, Separate XYZ |

**Editor**

| Action | How |
| --- | --- |
| Add a node | Shift+A, the Add Node button, or right-click; type to search. Releasing a link on empty canvas opens the same menu and connects the new node. |
| Link | Drag from an output socket to an input. |
| Unlink | Drag a linked input away. |
| Cut links | Ctrl + right-drag across them. |
| Delete | X or Delete. |
| Duplicate | Shift+D. |
| Mute (bypass) | M. |
| Show a node in the Viewer | Ctrl+Shift+click; the viewport shows its geometry instead of the Group Output. |
| Frame all | Home. |
| Make group / ungroup | Ctrl+G / Ctrl+Alt+G. |
| Enter / leave a group | Tab (or the path bar above the canvas). |
| Side panel | N. |
| Pan / zoom | Middle-drag / wheel. |

- **Values:** click a value on a node to edit it; enums open a menu and booleans toggle.
- **Side panel:**
  - the active node's description and every setting;
  - its errors (the node turns red);
  - **Group Inputs:** add a name and type to expose a parameter, which appears as an output on the Group Input node and as a value per object.
- **Undo:** every edit is one undo step.

**Script**

- `cmds.geometryNodes(obj, preset='scatter')`, `cmds.gnAddNode(obj, 'mesh_cube', (0, 0), inputs={'Size': (2, 2, 2)})`.
- `cmds.gnConnect(obj, '3', 'Mesh', '2', 'Geometry')`, `cmds.gnSetInput`, `cmds.gnSetProp`.
- `cmds.gnInterface(obj, add='Height', type='FLOAT')`, `cmds.geometryNodesParam(obj, 'Height', 2.0)`.
- `cmds.gnViewer`, `cmds.gnMute`, `cmds.gnInfo`, `cmds.applyGeometryNodes()`.
- Groups: `cmds.gnMakeGroup(obj, ['4', '5'], name='Lift')`, `cmds.gnUngroup(obj, node)`, `cmds.gnAddGroupNode(obj, 'Lift')`, `cmds.gnAssignGroup`, `cmds.gnNewGroup`, `cmds.gnGroupInterface('Lift', add='Height', type='FLOAT', side='in')` (also `remove=`, `rename=(old, new)`, `move=(name, -1)`, `setDefault=(name, value)`), `cmds.gnGroups()`, `cmds.gnGroupInfo`, `cmds.gnRenameGroup`, `cmds.gnDuplicateGroup`, `cmds.gnDeleteGroup`. Every editing command above also takes `'group:Lift'` instead of an object to edit inside the group.
- Zones: `cmds.gnAddZone(obj, 'repeat' | 'simulation', location)`, `cmds.gnZoneItems(obj, node, add='Speed', type='VECTOR')` (`remove=`, `rename=`, `move=`), `cmds.gnBakeSimulation(obj, start, end)`, `cmds.gnFreeSimulation(obj)`.

**Node groups**

- **Make Group (Ctrl+G):** the selected nodes move into a new group in the scene's group library; links that crossed the selection become the group's inputs and outputs, and a group node takes their place. **Ungroup (Ctrl+Alt+G)** puts copies of the nodes back.
- **Tab** enters the selected group node (or leaves the group); the bar above the canvas shows the path (object › group › nested group) and each part is clickable.
- Inside a group the side panel edits the **Group Interface**: add, remove, rename and reorder inputs and outputs, and set input defaults. Group nodes everywhere follow.
- **Library:** the side panel lists the scene's groups (Add a node for one, Edit, Rename, Delete unused, New Empty Group); Shift+A → Group lists them too. One group can be used in many trees, objects and other groups (nested groups); editing it re-evaluates every object that uses it. Groups are saved with the scene and every edit is one undo step.

**Zones**

- **Repeat Zone** (Shift+A → Utilities): a Repeat Input / Repeat Output pair. The nodes between them run *Iterations* times; each pass reads the state items the previous pass produced (Geometry by default; add Float, Integer, Vector, Boolean, Color items in the side panel). Repeat Input also outputs the current Iteration.
- **Simulation Zone** (Shift+A → Simulation): the state is carried from frame to frame. On the start frame the Simulation Input outputs its inputs (Delta Time = 0) and the cache resets; each later frame runs the nodes in the zone once on the previous frame's state, with Delta Time = 1 / fps. Every frame is cached: scrubbing backward reads the cache, jumping forward simulates the missing frames. Skip passes the state through unchanged. **Bake** (side panel, or Mesh → Geometry Nodes → Bake Simulation) simulates the playback range and stores it with the file (a baked simulation ignores edits until **Free Bake**).
- A tinted frame on the canvas marks each zone.

**Per-face materials.** Set Material assigns materials per face (Selection), Set Material Index writes the `material_index` face attribute, Material Index reads it and Material Selection selects faces by material. Join Geometry keeps each face's material. The result object stores a material per face: the OpenGL and GPU viewports, EEVEE and Cycles render every face with its own material (Cycles gets material slots and a per-polygon material index). Faces without a material use the default material.

**Sampling.** **Raycast** casts a ray from each element (Source Position, Ray Direction, Ray Length = max distance) onto a target mesh: Is Hit, Hit Position, Hit Normal, Hit Distance, and an attribute of the target read at the hit (interpolated across the triangle, or the nearest corner). **Sample Nearest Surface** reads a field of a mesh at the closest point of its surface (barycentric interpolation); **Sample Nearest** gives the index of the closest point / edge / face / corner / instance.

**Volumes.** Geometry has a fifth component, volume grids (density on a regular grid), carried through Join / Transform. **Volume Cube** evaluates a Density field at every voxel (e.g. 1 − length(Position) gives a ball); **Points to Volume** fills spheres around points; **Mesh to Volume** fills the inside of a closed mesh (winding number); **Volume to Mesh** builds the closed iso-surface (marching cubes) at a threshold; **Distribute Points in Volume** scatters points (random by density, or on a grid) where the density is above a threshold. A volume left in the output shows as its bounding box.

**Differences from Blender**

- **Y-up:** Forma is Y-up, so flat primitives lie on the ground (XZ) and Cylinder / Spiral run along Y.
- **Degrees:** rotations are Euler degrees.
- **Volumes:** a volume is a dense density grid (no OpenVDB sparse tree); grids are capped at 256 voxels per side.
- **Simulation cache:** kept in memory per object (undo or reopening the file re-simulates from the start frame unless baked).

### Delete by Type (Edit → Delete by Type / Delete All by Type)

**Delete by Type** works on the selection; **Delete All by Type** works on the whole scene.

| Type | What it removes |
| --- | --- |
| History | Construction history, and skins: the current deformed shape is kept. Deleting a Boolean's history also deletes its hidden inputs. |
| Non-Deformer History | Construction history only; skins stay. |
| Channels | Animation curves. Uses the Channel Box selection when there is one. |
| Static Channels | Animation curves whose keys never change value. |
| Constraints | Constraints. |
| Motion Paths | Motion path constraints and their `uValue` keys. |
| Rigid Bodies | Rigid body physics. |

Delete All by Type can also remove particles, joints, IK handles, lights, cameras, NURBS curves, NURBS surfaces, image planes, Grease Pencil objects and unused materials.

Script: `cmds.deleteByType('staticChannels', all=True)`.

### Custom pivots (Modify → Pivot)

- **Edit Pivot:** press **Insert** to toggle pivot mode, or hold **D**. The move tool then moves the pivot instead of the object; the rotate tool rotates the pivot's orientation, which the manipulators then use as their axes.
- **Snapping:** in pivot mode, click a vertex, edge or face of the selection to snap the pivot there and orient it (Y along the normal). The X / C / V snaps work too.
- **Components:** with components selected, pivot mode edits a **component pivot**. It travels with the components and lasts while the selection does. **Pin Component Pivot** keeps it when the selection changes.
- **Reset Pivot:** the pivot goes back to the object origin (or the component pivot is dropped).
- **Bake Pivot Orientation:** the orientation moves into the object's rotation; the geometry is counter-rotated so nothing moves.
- **Script:** `cmds.manipPivot(obj, position=(x, y, z), orientation=(rx, ry, rz), reset=True, bake=True)`.

### Motion paths (Animation menu set → Constrain → Motion Paths)

- **Attach to Motion Path:** select the objects, then the curve.
  - Time range: the time slider or start/end frames.
  - U value: fraction of the curve's length, or the curve parameter.
  - Follow, with front and up axes and an inverse option for each.
  - World up: a vector, or the curve's normal.
  - Bank, with scale and limit.

  A keyable **U Value** drives the object, so you can key it yourself. Orange markers on the path show the frame of each U Value key.
- **Set Motion Path Key:** move the object, change the frame and set a key. The keyed positions build and rebuild a curve through them.
- **Script:** `cmds.pathAnimation('car', curve='route', startTime=1, endTime=120, follow=True, bank=True)` and `cmds.setMotionPathKey('ball')`.

### Animation tools (Animation menu set, F4, and the Animation shelf)

**Visualize → Create Editable Motion Trail** (option box: range, increment, frame numbers, in-betweens) draws the path each selected object travels:
- Keyframes appear as red squares with their frame numbers, and a white ring marks the current frame. The line fades away from the current frame.
- **Drag a key square in the viewport** to move that key. The object's translate keys at that frame change, in world space, even under an animated parent.
- **Visualize → Motion Trail Editor** lists every trail and edits its settings: time slider or start/end range, pre/post frames (only show a window around the current frame), increment, key size, thickness, trail and key colours, frame numbers, in-betweens, fade, visibility.
- Deleting the object deletes its trail.

**Visualize → Ghost Selected** (option box: every N frames before/after, or at the keyframes; colour) draws see-through copies of the object at other frames. Frames after the current one are lighter, and farther frames are fainter. Ghosting a group ghosts the meshes and curves under it. **Unghost Selected** / **Unghost All** remove them.

Trails and ghosts are computed a few frames at a time in the background, so long ranges and heavy rigs never freeze the viewport. They update after every edit; scrubbing reuses the frames already computed.

**Key:**
- **Set Key on Animated:** keys only the channels that already have animation.
- **Set Key on Translate / Rotate / Scale:** key all three channels of that kind.
- **Bake Animation** (option box: time range, sample by, hierarchy, remove constraints, sparse curves) keys every frame of what constraints, IK, driven keys and expressions do, so the animation plays without them. Only channels that actually move get keys.

**Constrain** (Animation and Rigging menu sets): Parent, Point, Orient, Scale, Aim and Pole Vector.

**Script:**
```python
cmds.motionTrail('ball', start=1, end=48, increment=2); cmds.motionTrailEdit('ball_motionTrail', pre=10, post=10)
cmds.motionTrailMoveKey('ball_motionTrail', 12, (0, 1, 0))     # move the frame-12 key up 1 (world)
cmds.ghost('ball', before=3, after=3, step=2, color='red'); cmds.unghost(all=True)
cmds.bakeResults('hero_L_wrist', time=(1, 120), removeConstraints=True, sparse=True)
cmds.setKeyframe('ball', animated=True)
```

### Set Driven Key (Key → Set Driven Key..., or Rigging → Deform)

One attribute drives others through curves keyed against the driver's value, e.g. a control's `smile` driving blend shape weights, or a `curl` attribute rotating finger joints.

1. Select the driver and click **Load Driver**, then pick its attribute.
2. Select the driven objects and click **Load Driven**, then pick their attributes. Several objects and attributes can be selected.
3. Set the driver value and pose the driven attributes, then click **Key**. Repeat for each pose.

Driven attributes show in blue in the list, and the window lists the keys. A driven attribute only changes when its driver changes, so you can pose it by hand before keying. Driven keys follow keyed drivers through time, chain (a driven attribute can drive another), save with the scene, and are removed if the driver is deleted.

```python
cmds.setDrivenKeyframe('finger.rotateZ', currentDriver='hand_ctrl.curl')      # at the current values
cmds.setDrivenKeyframe('finger.rotateZ', currentDriver='hand_ctrl.curl', driverValue=10, value=-90)
cmds.listDrivenKeys('finger'); cmds.deleteDrivenKeys('finger.rotateZ')
```

### Deformers (Rigging menu set → Deform, and the Rigging shelf)

Deformers stack in Maya's default order: **blend shapes → skin → clusters, lattices and shrinkwraps** (in creation order). They work on skinned meshes too, and binding or unbinding a skin keeps them.

- **Blend Shape:** select the target meshes, then the base mesh last.
  - Each target becomes a keyable 0–1 weight on the base, named after the target.
  - Target meshes stay linked: edit one and the shape updates. The shape survives deleting the target.
  - **Shape Editor** (double-click the shelf button): a slider, **Key**, **Edit** and **Delete** per target, plus **Create Blend Shape** and **Add Target**. **Edit** makes a linked copy of the target beside the base to sculpt or move points on, live.
- **Cluster** (option box: falloff radius): select vertices, or whole meshes in object mode, and create one.
  - A **C** handle appears at their centre, and moving, rotating or scaling it moves them.
  - With a falloff radius, nearby vertices follow partway too.
  - Deleting the handle puts the mesh back.
- **Lattice** (option box: divisions S/T/U, default 2 × 5 × 2) puts a box of control points around the selected meshes:
  - Select the lattice, go to vertex mode, and move or rotate its points to bend everything inside smoothly.
  - Moving the whole lattice object carries the meshes with it.
  - The lattice draws on top in purple, so its points stay visible inside the shape.
- **Shrinkwrap** (option box; also Mesh Tools → Shrinkwrap to Target for retopology): select the meshes to wrap, then the target last (or make the target live). The meshes stick to the target surface, and follow it when it moves or changes. Shrinkwraps evaluate with the clusters and lattices, after the skin.
  - **Wrap mode:** closest point on the surface, project (along vertex normals or the X / Y / Z axis; both directions, positive or negative; cull front or back faces; optional distance limit; points that hit nothing stay put), or closest vertex.
  - **Offset** pushes the points out along the target normal. The envelope (`shrinkWrapEdit(..., envelope=0.5)`) blends back to the original shape.
  - Lookups use a bounding volume hierarchy of the target triangles, cached until the target changes.
  - Deleting the target removes the shrinkwrap.
- **Conform to Surface** (Mesh Tools, option box with the same modes plus strength): a one-shot projection of the selected vertices, or whole meshes, onto the live surface (or the last selected mesh).
- **Delete Deformers** removes the blend shapes, clusters, lattices and shrinkwraps from the selected meshes (and their now-unused handles and lattices).

```python
cmds.shrinkWrap('retopo', target='scan', mode='project', direction='both', offset=0.01)
cmds.shrinkWrapEdit('retopo', mode='closest', envelope=1.0)
cmds.conformToSurface(target='scan')                         # the selected vertices, once
cmds.blendShape('smile', 'frown', 'head'); cmds.setAttr('head.smile', 0.7)
cmds.blendShapeAddTarget('head', 'blink'); cmds.blendShapeSculptTarget('head', 'blink')
cmds.cluster('sheet', falloff=2.0)                                   # or on the selected vertices
cmds.lattice('box', divisions=(3, 6, 3)); cmds.listDeformers('head'); cmds.deleteDeformers('box')
```

### Shelves: Animation and Rigging

New buttons are added after the existing ones on the **Animation** shelf:
- Create Editable Motion Trail (double-click: Motion Trail Editor), Motion Trail Editor
- Ghost Selected, Unghost Selected, Bake Animation
- Parent, Point, Orient, Scale, Aim and Pole Vector constraints
- Set Key on Animated, next to the existing Key Translate / Rotate / Scale

On the **Rigging** shelf: **Set Driven Key**, **Create Lattice**, **Create Cluster** and **Blend Shape** (double-click: Shape Editor).

Shelves you saved before only get the buttons they are missing, added at the end after a separator. Nothing you added, moved or removed is touched.

### Navigation gizmo (top right of every viewport; Show → Navigation Gizmo)

- **Align the view:** click an axis bubble: X shows the right side, Y the top, Z the front; the small bubbles are the opposite sides. In an orthographic view the matching ortho camera is used.
- **Orbit:** drag the ball (an orthographic view switches to perspective first).
- **Buttons:** drag the magnifier to zoom and the arrows to pan; click the house to frame everything.

### Booleans (Mesh → Booleans in the Modeling menu set)

- **Operations:** Union, Difference (A − B), Difference (B − A), Intersection, Slice, Hole Punch, Cut Out and Split Edges.
- **Master:** the first selected mesh is the master.
- **Results:** they are watertight (T-junctions are closed) and keep their UVs.
- **Boolean Stack:** the result (`polySurface`) keeps one, and its inputs are hidden but stay live — move one and the result updates. Mesh → Booleans → **Boolean Stack…** lists the layers:
  - per-layer operation, Enabled and Show;
  - Move Up / Down, Remove and **Add Selected**;
  - **Interactive update:** when off, the result waits until you finish dragging an input.
- **Baking:** editing the result's mesh bakes it.
- **Script:** `cmds.polyBoolean('a', 'b', operation='difference')`, `cmds.booleanStack(r, layer=1, operation='union')`, `cmds.booleanStack(r, add=['c'])`.

### Sculpting (Sculpting menu set, F7)

Select a polygon mesh, then pick a brush from the **Sculpt** menu or start the **Sculpt Tool**. Blender's keys work while sculpting:

| Key | Action |
| --- | --- |
| LMB | Sculpt |
| Ctrl | Invert the brush |
| Shift | Smooth |
| F / Shift+F | Radius / strength (move, click to set) |
| Ctrl+F | Texture angle (move, click to set) |
| Shift+S | Lazy mouse (Stabilize Stroke) on / off |
| RMB / Shift+RMB / Ctrl+RMB | Stencil texture: move / scale / rotate (add Alt for the Texture Mask stencil) |
| [ ] | Radius |
| X | Draw |
| C / Shift+C | Clay Strips / Crease |
| I | Inflate |
| G | Grab |
| S | Smooth |
| L | Layer |
| P | Pinch |
| K | Snake Hook |
| M | Mask |
| Shift+T | Flatten |
| Ctrl+I | Invert mask |
| Alt+M | Clear mask |
| Ctrl+R | Voxel remesh |
| Ctrl+D | Dyntopo on / off |
| Page Up / Page Down | Multires: step up / down a level |
| Esc | Leave |

- **Brushes:** Draw, Draw Sharp, Clay, Clay Strips, Clay Thumb, Layer, Inflate, Blob, Crease, Smooth, Flatten, Fill, Scrape, Multi-plane Scrape, Pinch, Grab, Elastic Deform, Snake Hook, Thumb, Pose, Nudge, Rotate, Slide Relax, Mask, Draw Face Sets, Cloth and Boundary.
- **Sculpt Mode UI (laid out like Blender's):** while sculpting, the Maya tool box and Channel Box give way to:
  - a **tool header** across the top: the brush (its picture; the menu is the brush grid), Radius and Strength sliders with pen-pressure toggles, Add / Subtract, the **Brush / Texture / Stroke / Falloff / Cursor** popovers, Lazy Mouse, Symmetry X / Y / Z, Dyntopo, Remesh and Exit;
  - a **brush toolbar** down the left, grouped as in Blender;
  - a **Properties panel** on the right with collapsible panels. Sliders work like Blender's: drag them, Shift drags slower, Ctrl drags in steps, and a click lets you type a value.

  Everything comes back when you leave.
- **Brush previews:** every brush has a picture made by running that brush on a clay patch. The pictures appear in the brush grid, the menus and the shelf. They are rendered once and cached in `<settings>/brush_previews_v1`.
- **Brush Settings:**
  - Radius, in view pixels or scene units, with optional pen pressure.
  - Strength, with optional pen pressure.
  - Direction, Normal Radius, Area Radius, Hardness, Auto-Smooth.
  - For the planar brushes: Plane Offset and **Plane Trim**.
  - For single brushes: **Pinch** (Crease), **Normal Weight** (Grab / Snake Hook / Thumb / Nudge), **Tip Roundness** (Clay Strips) and **Height** (Layer).
  - **Advanced:** Sculpt Plane (area / view / X / Y / Z), Original Normal, Original Plane, Front Faces Only, Accumulate.

  Rows that don't apply to the current brush are hidden. **Unified Radius / Strength** (in Options) shares the radius and strength across all brushes.
- **Texture (alphas) and Texture Mask:**
  - **Alpha library:** soft / hard round, square, noise, fine noise, cells, cracks, scales, skin pores, wrinkles, stripes, rings, spiral, crosshatch, dots, weave, bricks, stitches, star. **Load Image…** uses any picture as an alpha.
  - **Mapping:** View Plane, Area Plane, Tiled, 3D, Random or Stencil.
  - **Settings:** Angle (Ctrl+F), Rake, Random angle and range, Offset and Size X / Y / Z, Sample Bias, Invert.
  - **Texture Mask:** a second alpha on top of the texture. Its mappings are View Plane, Tiled, Random and Stencil.
  - **Stencils:** a translucent overlay you move, scale and rotate with the right mouse button. **Mask from Stencil** (like ZBrush's Mask by Alpha) masks the surface under it.
  - Alphas also shape the Mask brush. The cursor can show the texture inside the brush circle.
- **Stroke:**
  - Methods: Space, Dots, Drag Dot, Airbrush (with a Rate), Anchored and Line.
  - Spacing, Adjust Strength for Spacing, Dash Ratio / Dash Length, Jitter (relative or in pixels), Input Samples.
  - **Stabilize Stroke / Lazy Mouse** (Shift+S, or the header button): Radius and Factor. A line is drawn from the cursor to the trailing brush.
- **Falloff:**
  - Presets: Smooth, Smoother, Sphere, Root, Sharp, Linear, Sharper, Inverse Square, Constant.
  - **Custom:** a curve editor. Drag points, double-click to add one, right-click to remove one. Editing a preset turns it into Custom.
  - Falloff Shape: **Sphere**, or **Projected** (a screen circle).
- **Cursor:** show or hide the brush, and set the texture overlay's opacity.
- **Symmetry and locks:** mirror X / Y / Z, lock X / Y / Z, and **radial symmetry** with any number of copies around X, Y or Z.
- **Auto-masking:** by topology, face sets or mesh boundary.
- **Mask:** invert, clear, fill, grow, shrink, smooth, sharpen, random. Masked areas are shown darkened.
- **Face sets:** from loose parts, from the mask, clear, randomize colors. Each Draw Face Sets stroke makes a new set.
- **Remesh:** voxel remesh (an even quad mesh, watertight; voxel size in the options) and smooth subdivision.
- **Cloth brush:** a small cloth simulation under the brush (position-based dynamics: edge-length constraints, mass, damping, gravity, stiffness). The outer ring of the simulated area stays pinned. Deformation modes: drag, push, pinch, expand, inflate, grab. The settings show in the panel's **Cloth / Boundary brush** group.
- **Boundary brush:** deforms the open boundary nearest the stroke start. Modes: bend (around the boundary), expand, inflate, grab, twist and smooth. The effect fades with the distance from the boundary into the mesh (propagation, times the radius). Along the boundary it can be constant, fade with the brush radius, or cover the whole loop. Closed meshes have no boundary, so the brush does nothing on them.
- **Dyntopo (dynamic topology):** turn it on in the panel's **Dyntopo** group or with Ctrl+D. While you sculpt, triangle edges under the brush that are longer than the detail size are split, and edges shorter than 40% of it are collapsed. The mesh stays manifold, and the work stays local to the brush, so 50k-triangle meshes stay interactive. Detail size modes:
  - **relative:** screen pixels.
  - **constant:** object units.
  - **brush:** a percentage of the radius.

  The refine method is subdivide, collapse or both. **Detail Flood Fill** remeshes the whole surface to the constant detail. The first dyntopo stroke triangulates the mesh. Face sets, the mask and vertex colors follow the new triangles. UVs, locked normals and hard edges are removed, with a warning, as in Blender. Dyntopo is off on multires meshes.
- **Leaving Sculpt Mode:** Esc, the header's **Exit** button, or **Object Mode** in the header's mode menu.
- **Sculpt layers** (Layers panel), like ZBrush's:
  - Each layer stores its own displacement. Strokes go into the highlighted layer, or into the **Base Mesh**.
  - A layer's **strength** can be any value; negative inverts its detail. The eye hides it.
  - Add, Duplicate, Remove, Merge Down, Bake All. Double-click a layer to rename it.
  - Layers are saved with the scene and undo like any edit.
  - Dyntopo, remeshing and multires change the topology, so they bake the layers first and say so.
  - Scripts: `cmds.sculptLayerAdd`, `sculptLayerEdit`, `sculptLayerRemove`, `sculptLayerDuplicate`, `sculptLayerMergeDown`, `sculptLayersBake`.
- **Quad Remesher** (Quad Remesher panel, the header's Remesh popover, or Sculpting → Remesh → Quad Remesh). Rebuilds the mesh as clean quads:
  - **Modes:**
    - **Organic:** adaptive size, so it is denser where the surface bends.
    - **Hard Surface:** edges sharper than the Feature Angle stay crisp, corners exact, and they are marked hard. Near-duplicate vertices and degenerate faces are cleaned up first.
    - **Cloth:** open borders and face-set seams are kept exactly, with even quads.
  - **Target Faces:** with **Exact Face Count** on, the count is exact. The one exception is an odd target on a closed all-quad mesh, which can only have an even count; it lands one below and says so.
  - **Options:** All Quads or quad-dominant; X / Y / Z symmetry; keep open borders; face-set borders as edges; denser where masked; relax passes.
  - **Reversible:** Keep Original stores the mesh as it was. Running again remeshes from that original with the new settings. **Revert to Original** brings it back, and **Apply** drops it.
  - **Transfer and bake:** vertex colors, the mask and face sets carry over. **Bake Textures** gives the new mesh UVs and bakes the original's color (vertex colors or texture) and a normal map of its detail into images. They are assigned to the material and saved in a `remesh_bake` folder in the temp directory.
  - **Limits:** about 5000 quads from 14k triangles takes ~3 s. Very large reductions (e.g. 50k → 2k) take ~10 s. Edge flow is not curvature-aligned like dedicated field-based remeshers.
  - Scripts: `cmds.quadRemesh`, `quadRemeshRevert`, `quadRemeshApply`, `quadRemeshBake`.
- **Multires (Multires menu, or the panel's Multires group):** works like Blender's Multiresolution modifier.
  - **Subdivide** adds a Catmull-Clark level on top.
  - **Step Up / Step Down** (Page Up / Page Down) move the sculpt level.
  - **Viewport level** sets what the viewport shows outside Sculpt mode.
  - **Apply Base** moves the base cage toward the sculpted shape; every level keeps its shape.
  - **Delete Higher** drops the levels above the sculpt level.
  - **Apply Multires** keeps the sculpt level as a plain mesh.

  Each level stores its displacement from the smoothed level below, in the surface's tangent frame. So an edit at a low level carries the higher-level detail along with it. The data lives on the node and saves compactly (base64 float32 per level). The mask, vertex colors and face sets carry between levels. UVs are interpolated onto the levels. If another tool changes the mesh topology, the multires commands refuse to run until you undo that change or remove the multires data.
- **Vertex Paint (Sculpting → Paint, or Mesh Display → Color → Paint Vertex Color Tool):** paints an RGBA color per vertex (`mesh.colors`).
  - **Tools:** paint (blend modes mix / add / subtract / multiply / lighten / darken / screen / overlay / erase alpha / add alpha), blur (or Shift) and smear.
  - **Colors:** primary and secondary color (Ctrl paints the secondary; X swaps them), plus color pickers.
  - **Brush:** radius, strength, alpha, falloff, front faces only and spacing.
  - **Fill, Smooth and Clear:** Fill covers the selected components in component mode, otherwise the whole mesh.
  - **Sample:** S picks up the color under the cursor.

  The viewport shows vertex colors in both the OpenGL and the GPU viewport. They replace the base color, or multiply it (panel or `cmds.vertexColorDisplay`). Display → Polygons → **Toggle Vertex Color Display** switches the display. Cycles renders get a `Col` color attribute wired into the material's base color through a Color Attribute node. Copying, saving and undo keep the colors. Topology operations interpolate them where they can (subdivision, multires, dyntopo, combine, deleting faces) and drop them otherwise.
- **Undo:** one undo step per stroke.
- **Script:** `cmds.sculptStroke(obj, 'draw', points, radius=0.3)`, `cmds.sculptMask`, `cmds.sculptFaceSets`, `cmds.voxelRemesh`, `cmds.sculptSubdivide`.
  - `sculptStroke` also takes `dyntopo=<detail size>`, `refine=` and `brushSettings={'cloth_mode': 'push'}`.
  - Dyntopo: `cmds.dyntopoFloodFill(obj, detailSize=0.05)`, `cmds.dyntopoTriangulate`.
  - Multires: `cmds.multiresSubdivide(obj, levels=2)`, `cmds.multiresLevel(obj, step=-1 | level=1 | viewport=0)`, `cmds.multiresApplyBase`, `cmds.multiresDeleteHigher`, `cmds.multiresApply`, `cmds.multiresRemove`, `cmds.multiresInfo`.
  - Vertex colors: `cmds.vertexColorFill(obj, color=[1, 0, 0, 1])`, `cmds.vertexColorStroke(obj, points, color=..., radius=0.3, tool='paint' | 'blur' | 'smear')`, `cmds.vertexColorSmooth`, `cmds.vertexColorClear`, `cmds.vertexColorSample(obj, point)`, `cmds.vertexColorDisplay(show=True, mode='multiply')`.

### Particles and physics (FX menu set, F5)

- **Particle systems:** FX → Particles → Emitter / Hair from Selected.
  - Emission: count, frame start/end, lifetime (+ random), from faces / verts / volume, seed.
  - Velocity: normal, object-aligned, random.
  - Physics: Newtonian or none, mass, size (+ random), drag, brownian, damping, gravity weight.
  - Collisions (optionally die on hit).
  - Display: halo points or an instanced object; hair strands with length and segments.
- **Force fields:** Force, Wind, Vortex, Turbulence, Drag, Harmonic, Charge. Settings: strength, shape (point / plane), falloff power, max distance, noise. Fields act along their local +Y.
- **Collision:** on any mesh, with damping, friction, permeability, stickiness and thickness. Particles, cloth and soft bodies collide with it.
- **Rigid bodies:**
  - Active or passive, with shapes box, sphere, convex hull or mesh (passive).
  - Mass, friction, bounciness, margin, damping.
  - Animated passive bodies follow their keys.
  - Stacks are stable.
- **Rigid body constraints (FX → Rigid Body → Connect → Fixed / Point (Ball) / Hinge / Slider / Spring):**
  - Select one rigid body (connects it to the world) or two (connected at their midpoint); with more, neighbours are chained. Meshes that aren't rigid bodies yet become active ones.
  - Each constraint is its own node (a green icon in the viewport). Its position is the pivot, its local Z the hinge / slider axis and its local X the hinge's zero angle.
  - Hinge: optional angle limits and a motor (target velocity in degrees per second, max impulse). Slider: distance limits and a linear motor. Spring: a damped spring between the two centers (stiffness, damping, rest length; -1 means the starting distance).
  - Every type: enabled, disable collisions between the pair (on by default), and breakable with a threshold.
  - Solved with the contacts (sequential impulses with position correction) and cached like everything else. Edit the settings in the Physics Editor.
- **Cloth and soft body:**
  - Quality, mass, air damping, and tension / shear / bending stiffness.
  - Pin selected vertices.
  - Collision distance; soft bodies pull back toward their shape (goal strength).
  - **Self collision** (FX → Cloth → Cloth Self Collision On/Off, or Physics Editor): keeps every vertex at least *self distance* from the cloth's other triangles, on the side it came from, so folds and layers don't pass through each other. It uses a spatial hash and costs roughly 0.3 s per frame for a 3,000-vertex cloth in full contact.
  - Files keep the rest shape.
- **Hair dynamics (FX → Particles → Make Hair Dynamic / Static):** hair strands are simulated as chains: gravity weight, fields, stiffness (0-1 bending), goal (pull toward the rest strand), damping and collision with collision objects. Roots ride on the emitter, so hair swings and settles when the emitter moves. The viewport and renders draw the simulated strands.
  - **Deformed emitters:** roots are bound to the triangles they grow from (barycentric position plus the strand in the triangle's frame), so static and dynamic hair follow a skinned / deformed / cloth emitter's surface, not only its transform. Faces are picked by their rest-shape area, so deformation never reshuffles the strands.
  - **Strand-to-strand collision (FX → Particles → Hair Self Collision On/Off, or the Physics Editor):** points and segment midpoints of different strands are kept at least *hair self distance* apart (spatial hash, position-based, roots fixed). *Hair friction* (0-1) damps the sliding of touching strands; *hair volume* (0-1) pushes strands out of dense regions (volume preservation through a density grid, after Petrovic et al.). About 0.1–0.2 s per frame for 1,000 strands × 8 segments at 10 substeps.
- **Animated objects:** each simulated frame poses keyframed objects (emitters, colliders, pins, animated passive bodies) at that frame, so scrubbing or baking gives the same result as playing.
- **Simulation:** runs forward from the start frame into a cache. Scrubbing and playing read the cache; changing settings or start positions rebuilds it.
  - **Bake** keeps the cache; **Free Bake** drops it.
  - World settings: gravity, substeps, iterations, start/end, time scale.
- **Physics Editor (FX → Particles → Physics Editor):** shows all settings of the selected object, plus the world settings.
- **Rendering:** particles render in Cycles and EEVEE as small spheres or instanced objects; hair renders as thin tubes.
- **Script:** `cmds.particleSystem`, `cmds.forceField('wind', strength=5)`, `cmds.rigidBody(obj, shape='box')`, `cmds.collision`, `cmds.cloth`, `cmds.softBody`, `cmds.clothPin`, `cmds.physicsWorld(substeps=10)`, `cmds.bakeSimulation()`, `cmds.rigidConstraint(a, b, type='hinge', use_limits=True)`, `cmds.rigidConstraintEdit`, `cmds.rigidConstraintInfo` (live angle / offset / length / broken), `cmds.hairDynamics(obj, stiffness=0.3)`, `cmds.hairSelfCollision(obj, distance=0.02, friction=0.3, volume=0.2)`, `cmds.clothSelfCollision(obj, distance=0.02)`.
- **Hotkeys:** FX takes F5, like Maya. Sculpting, which Maya has no menu set for, uses F7 instead.

### Fluids and smoke (FX menu set → Fluids), like Blender's Mantaflow

- **Domain:** FX → Fluids → Create Smoke Domain / Create Liquid Domain makes a box (its local cube; scale it to resize). It is drawn as its outline, and its mesh becomes the simulated result every frame, so every viewport and both renderers show it.
  - Settings: type (smoke / liquid), resolution (cells along the longest side, default 32), time scale, cache start/end, border (auto / open / closed), substeps (CFL), pressure iterations / tolerance.
  - Smoke: vorticity, buoyancy (density / heat), dissipation, cooling, burn rate, flame smoke / heat, display threshold / smoothing.
  - Liquid: FLIP ratio, particles per cell, mesh upres / smoothing / iso.
- **Flows:** Make Flow: Smoke / Fire / Fire + Smoke / Liquid on the selected meshes, plus Make Outflow.
  - Behavior: inflow (every frame), geometry (initial fluid, liquid default) or outflow (removes fluid).
  - Source: volume (inside the closed mesh) or surface (a shell, for open meshes).
  - Density, temperature, fuel, initial velocity, frame start/end.
- **Obstacles:** Make Obstacle (with thickness). They block smoke and liquid particles; animated flows and obstacles are followed.
  - **Moving obstacles push the fluid:** an animated obstacle's velocity (its translation and rotation between frames, taken as the generator of the motion so a spinning propeller is a true rigid rotation) is the boundary condition of the pressure solve (u·n = u_obstacle·n on every face next to it). A paddle moving through still smoke or water pushes it along; a propeller sets it spinning. Liquid particles the obstacle moves onto are swept along in front of it, with its velocity. *velocity factor* scales this (0 = a static wall re-placed each frame).
  - **Flows can add their own motion:** *use object velocity* (with *object velocity factor*) adds the emitter's motion, rotation included, to the emitted smoke / liquid.
- **Spray, foam and bubbles (liquid domains: use spray / use foam / use bubbles):** secondary particles like Blender's FLIP "Particles" (after Ihmsen et al. 2012).
  - Generated every frame from **trapped air** (a particle's velocity difference to the smoothed flow) and **wave crests** (surface particles moving outward along the normal of a convex surface), scaled by their kinetic energy. Settings: amount, wave crest / trapped air sampling, energy min / max, lifetime (+ random), max count, size, bubble buoyancy / drag, display size.
  - Classified by where they are: **spray** above the surface flies ballistically and falls back, **foam** on the surface is carried by the flow and dissipates over its lifetime, **bubbles** under it rise (buoyancy + drag toward the flow). Spray that lands becomes foam, sunk foam becomes bubbles, surfacing bubbles become foam.
  - The viewport draws them as point clouds (spray pale blue, foam white, bubbles blue). Cycles renders them as small smooth-shaded octahedra with a white foam material the domain gets when they are turned on (up to 50k per domain). They are cached, baked to disk and restored with the rest of the state; `fluidInfo` counts them.
- **Smoke and fire:** stable fluids on a staggered grid.
  - Semi-Lagrangian (RK2) advection, buoyancy from density and temperature, vorticity confinement, dissipation and cooling.
  - Fuel burns into flame, heat and smoke.
  - Pressure projection with a preconditioned conjugate gradient.
  - The viewport shows a translucent iso-surface of the density (fire: an emissive orange material). Domain **display mode** *volume* (or *both*) draws the smoke as a true volume instead: alpha-blended slices through the density / flame grid along the axis facing the camera, back to front, tinted by the domain material and glowing orange where there is flame (*display volume density* sets the opacity).
- **Liquids:** FLIP/PIC particles on the grid, with walls and obstacles. The surface is marching cubes (its own vectorised implementation) on the particle density splatted to a 2× finer grid and smoothed. New domains get a water material.
- **Cycles:** smoke and fire render as real volumes. Each frame's density / flame / temperature is written to OpenVDB inside Blender and shaded with a Principled Volume, with flame as emission. If OpenVDB is missing, the iso-surface renders instead. Liquids render as their mesh.
- **Cache:** frames from cache start are simulated once and kept. Scrubbing back reads the cache; changing a domain, flow or obstacle setting (or moving them) re-simulates.
  - **Bake Fluid** keeps the whole range; **Bake Fluid to Disk** also writes one `.npz` per frame next to the scene (`<scene>_fluids/<domain>/`) or in the temp folder, and reopening the scene reads it back.
  - **Free Fluid Bake** drops it.
- **Quick Smoke / Quick Fire / Quick Liquid:** turn the selected meshes into flows and build a domain around them.
- **Fluid Editor (FX → Fluids → Fluid Editor):** shows the settings of the selected domain / flow / obstacle, the grid size, cached frames and time per frame, with Bake / Free Bake.
- **Speed (numpy only):** 32³ smoke is about 10 frames/s. A 32³ liquid with about 20k particles takes 0.05–0.15 s per frame, plus about 0.05 s for the surface.
- **Script:**
  - `cmds.fluidDomain('smoke', resolution=48)`, `cmds.fluidFlow(obj, type='fire')`, `cmds.fluidFlow(obj, type='liquid', behavior='geometry', velocity=(1, 0, 0))`, `cmds.fluidEffector(obj)`.
  - `cmds.fluidSettings(domain, vorticity=0.5)`, `cmds.fluidBake(domain, disk=True)`, `cmds.fluidFreeBake(domain)`, `cmds.fluidInfo(domain)`, `cmds.quickSmoke(obj)`.
  - `fluids.volume_grid(node, frame)` returns (density, flame / temperature, voxel → world matrix).
  - `cmds.fluidEffector(paddle, velocity_factor=1.0)`, `cmds.fluidFlow(obj, use_object_velocity=True)`, `cmds.fluidSettings(domain, use_spray=True, use_foam=True, use_bubbles=True, secondary_amount=2.0)`, `fluids.secondary_particles(scene, domain, frame)` (world positions per kind), `cmds.fluidSettings(domain, display_mode='volume')`.
  - Spray / foam / bubbles cost about 40% on top of the liquid step (a 24³ splash: 0.065 → 0.09 s per frame).

### EEVEE real-time engine (viewport Shading → Material Preview (8) / Rendered (9); Render Settings → engine)

- **Shading:** principled GGX shading. Lights have a size, so highlights are soft.
- **Lights and shadows:** scene lights with soft shadow maps — sun and spot use 2D maps, point and area lights use cube maps.
- **World lighting:** from the world color or HDRI (`.exr`, `.hdr`, PNG, JPEG), with diffuse from spherical harmonics and glossy reflections from a mipmapped environment.
- **Effects:** screen-space ambient occlusion, screen-space reflections, bloom (threshold, knee, radius, intensity), and camera depth of field (camera DoF with f-stop and focus distance).
- **Transparency:** the material's blend mode — blended (sorted), alpha clip, or dithered (a different cut every sample, so it averages out as samples accumulate); alpha can come from a texture or any node graph.
- **Every Principled layer:** Specular IOR Level and Tint with the IOR's own reflectance, anisotropic highlights and reflections (tangent from the UVs, Anisotropic Rotation), Coat (its own sharp lobe with IOR, tint and roughness over the base), Sheen (microfiber lobe with tint and roughness), Transmission (IOR Fresnel), Emission, Subsurface; per-pixel maps for roughness, metallic, normal, emission, alpha, coat, sheen, transmission and specular; the Displacement output as bump.
- **Vertex colours:** colour attributes (Vertex Paint) show as in Cycles: a material with a Color Attribute node reads them, otherwise the vertex colour display setting replaces / multiplies the base colour.
- **View transforms:** Standard, Filmic or AgX, with exposure and film transparency.
- **Anti-aliasing:** progressive. While nothing changes, jittered samples accumulate up to the viewport or render sample count.
- **Material Preview:** uses a built-in studio light. **Rendered** uses the scene's lights and world.
- **Final renders:** Render Settings → Render engine → EEVEE renders right inside Forma (no Blender needed) to PNG or JPEG, frame or sequence. The EEVEE tab holds the settings.
- **OpenEXR:** world HDRIs and Image Texture nodes read `.exr` (and `.hdr`) files. `forma/exr.py` decodes scanline EXRs itself — half / float / uint channels with NONE, RLE, ZIPS, ZIP or PXR24 compression, including Blender's multilayer channel names. PIZ, DWAA/DWAB, B44, HTJ2K, tiled and multi-part files are converted once through Blender (when installed) and cached in the temp folder. Image Format → OPEN_EXR makes EEVEE renders write the linear image as a half-float EXR. The HDRI layout and rotation match Cycles.
- **Subsurface scattering:** Principled BSDF Subsurface Weight, Radius × Scale (the colour is the Base Color, as in Blender 4+). Light wraps further past the terminator in the channels with the larger radius, and thin parts such as ears glow when lit from behind. The thickness light travels through comes from the shadow maps, so the light needs shadows on. Toggle: EEVEE → Subsurface scattering.
- **Volumetrics:** world fog (Render Settings → Environment → Fog density, color, anisotropy, absorption; Cycles renders it as a world Principled Volume) and objects whose material drives the Material Output's **Volume** socket with Principled Volume, Volume Scatter, Volume Absorption, Emission, or Add / Mix of these. Objects with no Surface link are volume only. Rendering is per-pixel ray marching from Volume start to Volume end in Volume steps. Light scatters with Henyey-Greenstein anisotropy. Volume shadows (on by default) include the lights' shadow maps and the volumes' own self-shadowing. Up to 4 volume objects are drawn at once, each filling its convex hull. Fog is shown in Rendered and in final renders. Volume objects also show in Material Preview.
- **Motion blur:** EEVEE → Motion blur, Shutter (in frames, centred on the frame) and Motion steps (0 = a new time for every sample). Samples are spread over the shutter, the scene is evaluated at each sub-frame, so animated objects, deformations and cameras blur, and the frame is restored afterwards. `eevee.render_image()` does the same from scripts. **Motion blur in the Rendered viewport** (EEVEE tab) does it live: every accumulated viewport sample is drawn at its own sub-frame, so the blur builds up progressively.
- **Light probes:** Create → Light Probes (also Rendering → Lighting/Shading → Light Probes) offers three kinds:
  - *Reflection Cubemap*: a sphere or box (`influenceBox`) influence of `influenceDistance`, with falloff, clipStart / clipEnd and optional `parallax` / `parallaxDistance`. Glossy reflections of objects inside it come from a cubemap captured at the probe; smaller probes blend over larger ones, up to 4.
  - *Irradiance Volume*: a grid of resolutionX/Y/Z samples inside the probe's box, each storing L1 spherical harmonics. It gives diffuse indirect light, so colour bleeds from walls onto the floor.
  - *Reflection Plane*: the probe's XZ square facing +Y, with an influence distance. It re-renders the mirrored view every frame for mirrors and water.

  Probes capture when they appear or change, on **Bake Light Probes** (Rendering → Lighting/Shading → Light Probes, or the Render Settings EEVEE tab), and at the start of every EEVEE render. In the viewport, irradiance bakes are spread over a few redraws. Probe attributes are keyable channels in the Channel Box. Commands: `lightProbe(type, ...)`, `lightProbeEdit`, `lightProbeQuery`, `bakeLightProbes()`. Probes are used in Rendered mode and in final renders.

### GPU acceleration (Windows → Settings/Preferences → Preferences → GPU Acceleration)

Forma uses the graphics card through **wgpu** (WebGPU): **Vulkan** or **Direct3D 12** on Windows, **Metal** on
macOS, Vulkan on Linux. Everything falls back to the CPU (numpy) when no GPU is found or a driver fails, and the
result is the same either way.

- **Cycles renders and bakes** run on the GPU: Render Settings → Device (`auto` tries OptiX, CUDA, HIP, Metal,
  oneAPI, then the CPU). **Detect GPUs** lists what Blender can use. The Texture Painter's bakes use the same device.
- **GPU compute** (Preferences → GPU Acceleration → Compute backend): UV rasterisation for map baking and the
  Texture Painter (about 5× faster), Noise and Voronoi texture nodes in material previews (about 20× faster), and
  skinning of meshes with 20 000+ vertices. `auto` picks Vulkan (then D3D12) on Windows and Metal on macOS. `cpu`
  turns GPU compute off.
- **Viewport renderer**: `opengl` is the classic renderer. `gpu` draws the Shaded / Wireframe views with the
  compute backend (Vulkan / D3D12 / Metal): meshes with their material colour, base and normal maps, wireframes,
  selection, components, curves, NURBS, joints, locators, cameras, lights, lattices and ghosts. `auto` uses Metal on
  macOS and OpenGL elsewhere. Material Preview, Rendered, Grease Pencil, particles, image planes and the sculpt /
  weight-paint overlays still draw with OpenGL. The view switches by itself, and the bottom-right corner says which
  renderer is drawing.
- Environment overrides: `FORMA_GPU=vulkan|d3d12|metal|opengl|cpu`, `FORMA_VIEWPORT=gpu|opengl`.

### Asset Browser (Windows → General Editors → Asset Browser), like Blender's Asset Browser / Maya's Content Browser

- **Libraries:** Preferences → Files / Projects → *Asset library folders* (one per line; default
  `~/Documents/Forma Assets`, created on first use). Pick the library in the browser's drop-down, or right-click →
  *Add Library Folder…*. Subfolders are **categories** (tree on the left; right-click → *New Category…*).
- **Grid:** thumbnails with a search field (name, tags, description, category — every word must match) and a type
  filter: Models (models, rigs, scenes), Rigs, Scenes, Materials, Poses.
- **Save Selection as Asset** (File menu, *Save Sel* button or right-click): the selected objects with everything
  under them, the skeletons their skins use and their materials go into `<name>.forma` (a normal scene file — top
  objects keep their world placement), plus a `<name>.png` thumbnail rendered from the active viewport framing the
  selection (grid / HUD hidden, the camera is restored) and a `<name>.asset.json` sidecar with name, type (auto: *rig*
  when there are joints, else *model*), tags and description.
- **Save Material as Asset** (File menu / *Save Mat*): the lead object's material (or one picked from the list) as
  `<name>.formamat` (the shader graph) with a preview-sphere thumbnail. **Save Pose** stores the selected nodes'
  translate / rotate / scale as `<name>.formapose`.
- **Use:** double-click a model to import it (fresh names and ids; identical materials are reused, clashing ones
  renamed; undoable); drag it into a viewport to place its base centre where the cursor meets the ground plane.
  Double-click / drop a material to assign it to the selection (or to the object under the cursor); with nothing
  selected it is just added to the scene's materials. Pose assets apply to the nodes with the same names.
- Right-click: Import, Open as Scene, Apply, Rename…, Edit Tags / Description…, Update Thumbnail from Viewport,
  Reveal in File Browser, Delete, Refresh.
- Scripting: `cmds.saveAsset(name, *objs, folder=, tags=, description=, type=)`, `cmds.saveMaterialAsset(material)`,
  `cmds.savePoseAsset(name, *objs)`, `cmds.importAsset(path, position=None)`, `cmds.applyMaterialAsset(path, *objs)`,
  `cmds.applyPoseAsset(path)`, `cmds.listAssets(search, type)`; `forma.assets.import_asset(scene, path,
  reference=False)` is the library entry point (references are not supported yet: it imports a copy).

### Autosave and crash recovery (Preferences → Files / Projects)

- **Autosave** is on by default: every *Interval* minutes (default 5), when the scene has unsaved changes, a copy is
  written to `<name>_autosave_<N>.forma` in the autosave folder (default `<project>/autosave` when a project folder is
  set, else `~/.forma/autosave`); the newest *Number of auto saves kept* (default 5) are kept. The current file
  path and the unsaved-changes star are not touched. File → *Auto Save Now* forces one; File → *Open Auto Save
  Folder* shows them.
- **Crash recovery:** each session writes a `session_<pid>.lock` file in the autosave folder and removes it on a
  clean exit. On the next start, a lock whose process is gone means Forma crashed; if an autosave newer than that
  session's start exists, Forma asks *Recover unsaved work?* and opens it as unsaved work (the title shows
  *(recovered)*; Save writes back to the original scene file when it is known).
- **Unhandled errors** no longer lose work: the error is reported (with details) and, if there are unsaved changes,
  the scene is first saved to `<name>_emergency.forma`; Forma keeps running.
- File → **Recent Autosaves** lists the autosave and emergency files (newest first, with times) to open as unsaved
  work.

### Dope Sheet, weighted tangents, animation layers and the Time Editor (Animation menu set)

- **Dope Sheet** (Windows → Animation Editors, or Key → Dope Sheet). Keys appear as ticks on a frame grid: a
  summary row, a row per object and a row per channel.
  - **Select:** click, Shift / Ctrl, marquee.
  - **Edit:** drag in time (snaps to frames), scale around the current frame, reverse, copy / paste at the current
    frame, duplicate (Shift+D), insert (I), delete, set tangents.
  - **View:** A / F frame all / selection, the wheel zooms, the middle mouse pans.
- **Weighted tangents**, like Maya's Curves → Weighted Tangents in the Graph Editor (or Key → Weighted Tangents).
  Handles get a length as well as an angle, for longer or snappier eases. Tangents → Lock / Free Tangent Weight.
  Script: `cmds.keyTangent('ball', attribute='translateY', time=1, outWeight=8, outAngle=0)`.
- **Animation layers.** The Layer Editor sits under the Channel Box and has an Anim tab.
  - **Additive** layers add to the animation below (scale multiplies). **Override** layers replace it, blended by
    the layer weight. The weight can be keyed.
  - **Mute / Solo / Lock** per layer.
  - **Keying:** click a layer to make it active, and keys go into it. Keying BaseAnimation under layers keys the
    value that, with the layers on top, gives the current pose.
  - **Merge Layers** bakes them down into the base animation.
  - Commands: `animLayerCreate`, `animLayerAdd`, `animLayerEdit` (weight, mode, mute, solo, lock, rename,
    moveTo), `animLayerSetActive`, `animLayerKeyWeight`, `animLayerMerge`, `animLayerDelete`.
- **Time Editor (non-linear animation).** Create Clip turns the selected objects' keys into a reusable clip on a
  track.
  - **Clips:** drag them to move (also between tracks), drag the right edge to change speed, Shift+drag it to loop.
    Clips also have weight, blend in / out ramps, hold, override or additive mode, and mute.
  - **Reuse:** Place at Current Time adds another instance. Place on Selected plays the clip on another character,
    with joints matched by name without namespaces.
  - **Bake to Keys** turns the result back into keys.
  - Commands: `clipCreate`, `clipPlace`, `clipEdit`, `clipDelete`, `clipTrackCreate` / `Edit` / `Delete`,
    `clipBake`, `clipList`.

### Motion capture and retargeting (Animation → Mocap, File → Import Motion Capture)

- **Import BVH:** a joint hierarchy keyed every frame at the file's frame rate, under a namespace
  (`mocap:Hips`). Any rotation order is supported, and `scale` converts units.
- **Export BVH:** writes the selected skeleton.
- **Retarget Animation:** select the source root, then the target root.
  - **Matching:** joints are matched by their role (hips, spine chain, neck, head, collar / upper arm / forearm /
    hand, up leg / leg / foot / toe, fingers), found from names *and* structure. Mixamo's / CMU's "LeftShoulder"
    is a collarbone; Maya's "L_shoulder" is an upper arm.
  - **Motion:** each target joint gets the source joint's world rotation change from the rest pose. The hips get
    the root motion scaled by the hip-height ratio, so different proportions and joint orients work.
  - **Different rest poses:** each target bone is lined up with its source bone at rest first, so an A-pose
    rig takes T-pose mocap (`matchRest=False` turns this off).
  - **Options:** `inPlace`, `mapping={target: source}`, `sourceRestFrame`.
  - Show Retarget Joint Mapping lists the matches.

### Playblast, sound and geometry caches

- **Playblast** (Windows → Playblast, Animation → Sound). Records the active viewport without manipulators or
  selection highlighting.
  - **Output:** MP4 when ffmpeg is installed (`pip install imageio-ffmpeg`), else Motion-JPEG AVI, or a PNG / JPG
    sequence.
  - **Options:** window, render-settings or custom size; scale; quality; HUD (camera and frame); grid; sound.
  - **Flipbook:** it opens when the playblast is done. It plays in real time with sound, loops and scrubs.
- **Sound** (File → Import Audio): WAV, or MP3 / OGG / FLAC / M4A with ffmpeg, starting at a frame.
  - The Time Slider draws the waveform.
  - Playback runs in real time in sync with the sound (frames are skipped if the scene is slow).
  - Scrubbing plays the frame under the cursor.
  - Commands: `importAudio`, `audioEdit` (offset, mute, volume), `audioDelete`.
- **Geometry cache** (Animation → Cache): bakes what skinning, blend shapes, deformers and simulations do to the
  selected meshes into per-frame points (`.npz` in `~/Documents/Forma/cache`).
  - The baked points play back instead of the rig, so heavy characters play in real time.
  - Enable / Disable switches between the cache and the live rig; Delete removes the cache.
  - Alembic (.abc) import / export is under File formats.

### Display layers (Layer Editor → Display tab)

- **Membership:** create a layer from the selection; objects belong to one layer, and children follow their
  parent's layer.
- **V (visibility):** hides the layer's objects.
- **Display type (click to cycle):**
  - **T, template:** grey wireframe that can't be selected in the viewport.
  - **R, reference:** shaded, but can't be selected.
- **Colour:** a swatch sets the wireframe colour.
- **Right-click menu:** add / remove / select objects, rename, delete.
- Commands: `createDisplayLayer`, `editDisplayLayerMembers`, `removeFromDisplayLayer`, `displayLayerEdit`
  (visible, display, color, rename, moveTo), `selectLayerMembers`, `deleteDisplayLayer`.

### File references (File → Create Reference, Reference Editor)

Reference another `.forma` file (a character, a set) under a namespace. Its nodes appear as `hero:hips`, drawn
blue in the Outliner.

- **What you can do with them:** animate, pose, constrain to and parent them like any other node.
- **What gets saved:** only your edits (transforms, animation, visibility, attribute values, material assignment,
  parenting). Geometry and rig come from the file each time the scene opens, so fixing the character file updates
  every shot.
- **Reference Editor:** Reload, Unload / Load, Replace (another file, edits kept), change Namespace, Select Nodes,
  Import Objects (make local), Remove.
- **Links:** referenced nodes keep their ids, so local constraints and parenting to them survive reloads.
- **Limitation:** edits to referenced geometry, skin or constraints are not stored.
- Commands: `createReference`, `referenceReload`, `referenceUnload`, `referenceLoad`, `referenceReplace`,
  `referenceNamespace`, `referenceImport`, `referenceRemove`, `referenceList`.

### Blender-style icons

Every icon name of the Blender manual's icon list is available — about 650, from `add` and `mod_array` to `force_vortex`, `greasepencil` and `sculptmode_hlt`. They are original artwork in Blender's style: light glyphs, objects orange, data green, modifiers and constraints blue.

Use them for shelf buttons and tools: Shelf Editor → Icon → **Browse…** opens a searchable grid. In code, use `icon('mod_boolean')`, or set a shelf item's glyph to the name.

## Scripting

Every UI action goes through `forma.cmds`, so actions are undoable and echoed to the Script Editor:

```python
c = cmds.polyCube(width=2, sx=3)
cmds.move(0, 1, 0, c)
cmds.setAttr(f'{c}.rotateY', 45)
cmds.select(f'{c}.f[0:2]'); cmds.polyExtrudeFacet(thickness=0.5)
cmds.setKeyframe(c); cmds.currentTime(24)
```

## Tests

`python -m pytest -q tests` runs the core tests (meshes, transforms, undo, components, animation).
`python tests/smoke_gui.py OUTDIR` drives the real UI and saves screenshots (every `tests/smoke_*.py` works the same
way; `smoke_prefs.py` covers preferences, shelves, FSL, plug-ins and snapping; `smoke_options.py` the tool, face, edge
and vertex options; `smoke_geonodes.py` the Geometry Node Editor; `smoke_layout.py` the Maya layout, icons,
workspaces and selection tools). The FBX test is skipped when Blender
is not installed.

## Not implemented yet

NURBS: surfaces export to FBX as polygons and curves not at all (Blender's FBX exporter has no NURBS -
use IGES); open-curve trims on closed (periodic) directions; weight painting on NURBS skins.
