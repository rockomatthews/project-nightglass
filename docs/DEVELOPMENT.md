# M0 development setup

## Current status

The C++ project, Game/Editor/Client/Server targets, connection-logging game mode and map-generation script are present. They have **not** been compiled or run in Unreal. The test map binary has not been generated. DefaultPawn provides a flying connection-test pawn, not spy/merc gameplay. Teams, combat, objectives, best-of-three logic and wagers are not implemented.

Host inspection on 2026-10-16 found macOS 26.5.2, Xcode 26.6, no Unreal installation in the standard locations, and only 3.7 GiB free. This blocks engine installation and runtime verification here. Do not download an engine onto this volume until space is available.

## Install on the operator's Mac

1. Install [Epic Games Launcher](https://www.unrealengine.com/download), then stable Unreal Engine 5.8 through its Library. The source baseline is 5.8.0. If the Launcher offers a newer 5.8 patch only, record the installed version and review/update the baseline rather than pretending it is 5.8.0.
2. Install Xcode 26.1.1 alongside existing Xcode; this is Epic's documented recommended version for UE 5.8. The currently installed 26.6 has not been validated for this project. See [Mac requirements](https://dev.epicgames.com/documentation/en-us/unreal-engine/macos-development-requirements-for-unreal-engine).
3. Plan approximately 150–200 GB for initial editor/project/build work (planning allowance, not an official minimum); a source engine build can require more. Use a suitable external SSD if necessary. Do not remove unrelated files to make room.
4. Open Xcode once and finish its required components. Select its developer directory for this build using the `DEVELOPER_DIR` environment variable if multiple versions are installed.

Mac editor work does not prove Windows support. Windows remains the first release target. A successful Windows build and dedicated-server connection run are still M0 gates.

## Get the project

```sh
git clone https://github.com/rockomatthews/project-nightglass.git
cd project-nightglass
git lfs install --local
git lfs pull
```

Keep the repository on a volume with space for Intermediate/Saved data. Generated engine/build products stay ignored. Do not commit Unreal source. `.uasset`/`.umap` use Git LFS.

## Windows source build and map creation (not yet executed)

Obtain the authorized **5.8.0** source release from Epic; follow [Epic's dedicated-server guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-dedicated-servers-in-unreal-engine). Record source revision, Visual Studio/compiler and SDK before claiming a reproducible build.

PowerShell, from this repository, with `$EngineRoot` set to the source checkout containing `Engine/`:

```powershell
$Project = (Resolve-Path '.\Nightglass.uproject').Path
& "$EngineRoot\Engine\Build\BatchFiles\Build.bat" NightglassEditor Win64 Development "-Project=$Project" -WaitMutex
# Stop if the build fails. Open a fresh editor session after success.
& "$EngineRoot\Engine\Binaries\Win64\UnrealEditor.exe" $Project
```

In a fresh editor session with no unsaved work, enable the Python console and run (substitute the real absolute path):

```python
exec(open(r'C:\path\project-nightglass\Scripts\create_m0_map.py', encoding='utf-8').read())
```

This creates `/Game/Nightglass/Maps/M0_Connection` with a primitive floor, four starts and light; refuses to overwrite an existing map. The configured default map will be missing until this step succeeds. Save and verify it, then commit the `.umap` through LFS. It references built-in engine primitives without copying engine files into the repository.

Build remaining targets, checking each command's exit status before continuing:

```powershell
& "$EngineRoot\Engine\Build\BatchFiles\Build.bat" NightglassServer Win64 Development "-Project=$Project" -WaitMutex
& "$EngineRoot\Engine\Build\BatchFiles\Build.bat" NightglassClient Win64 Development "-Project=$Project" -WaitMutex
& "$EngineRoot\Engine\Build\BatchFiles\Build.bat" Nightglass Win64 Development "-Project=$Project" -WaitMutex
```

Cook the map for WindowsServer and WindowsClient using the editor's Platforms → Windows target selection and Cook workflow in Epic's guide. Compiled executables alone are not a cooked build.

After successful cooking, in separate terminals:

```powershell
.\Binaries\Win64\NightglassServer.exe /Game/Nightglass/Maps/M0_Connection -log -port=7777
.\Binaries\Win64\NightglassClient.exe 127.0.0.1:7777 -windowed -ResX=800 -ResY=450 -log
.\Binaries\Win64\NightglassClient.exe 127.0.0.1:7777 -windowed -ResX=800 -ResY=450 -log
```

Use a trusted private test network for remote clients; no public server deployment is included. Verify two distinct connected clients, movement/input in each, and join/disconnect logging. Capture logs and exact commands with commit and engine revision. These instructions are a candidate procedure until executed successfully; record corrections rather than claiming success.

## M0 gate

Reference observations plus clean Windows compilation, successful map generation/cook, dedicated server and two connected clients. Local document/syntax checks are not a substitute. No engine build CI is configured yet.
