# Development setup

## Available now

This is a planning repository. There is no `.uproject`, game executable, server executable or validated game build command yet. Start with documentation and the M0 bootstrap issue.

```sh
git clone https://github.com/rockomatthews/project-nightglass.git
cd project-nightglass
git lfs install --local
git lfs pull
```

Install Git LFS separately before cloning assets. `.uasset` and `.umap` are LFS-managed lockable files; coordinate binary edits in issues. Do not commit build products or engine files.

## M0 contributor prerequisites and deliverable

Use Windows with an Epic-authorized Unreal Engine **5.8.0** source checkout and the Visual Studio toolchain supported by that release. Follow [Epic's dedicated-server instructions](https://dev.epicgames.com/documentation/unreal-engine/setting-up-dedicated-servers-in-unreal-engine) for prerequisites. Record exact source revision, compiler version, SDK and successful build commands in this document as part of M0.

Create the original C++ project at the repository root, with `Nightglass.uproject`, `Source/`, `Config/`, and `Content/Nightglass/`. Add Game, Editor and Server targets. Do not copy Epic engine source or paid sample assets into this repository. Add a minimal test level and reproducible server/client launch instructions. Check the engine pin before opening assets; upgrades require review, not automatic conversion.

Do not advertise a working build until a fresh Windows checkout compiles and the documented dedicated-server/client session succeeds. Public CI for engine builds is deferred until an authorized runner and license/access configuration exist; do not upload engine source to CI artifacts.
