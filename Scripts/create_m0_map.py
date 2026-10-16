"""Run in a fresh Unreal Editor session after compiling NightglassEditor.
Creates original arrangement of engine primitives; never overwrites a map.
Engine primitives are referenced, not redistributed in this repository.
"""
import unreal

MAP = "/Game/Nightglass/Maps/M0_Connection"
if unreal.EditorAssetLibrary.does_asset_exist(MAP):
    raise RuntimeError("M0 map already exists; refusing to overwrite")
levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
if not levels.new_level(MAP):
    raise RuntimeError("Could not create M0 map")
cube = unreal.load_asset("/Engine/BasicShapes/Cube.Cube")
if cube is None:
    raise RuntimeError("Engine cube asset unavailable")
floor = actors.spawn_actor_from_class(unreal.StaticMeshActor, unreal.Vector(0, 0, -50))
floor.static_mesh_component.set_static_mesh(cube)
floor.set_actor_scale3d(unreal.Vector(30, 30, 1))
floor.set_actor_label("M0_Floor")
for index, (x, y) in enumerate([(-400, -400), (400, -400), (-400, 400), (400, 400)]):
    start = actors.spawn_actor_from_class(unreal.PlayerStart, unreal.Vector(x, y, 150))
    start.set_actor_label("M0_Start_" + str(index + 1))
light = actors.spawn_actor_from_class(unreal.DirectionalLight, unreal.Vector(0, 0, 800), unreal.Rotator(-45, 0, 0))
light.set_actor_label("M0_Light")
if not levels.save_current_level():
    raise RuntimeError("Could not save M0 map")
unreal.log("M0 map generated. Compile, cook and connection checks remain required.")
