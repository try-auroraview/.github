<p align="center">
  <img src="https://raw.githubusercontent.com/try-auroraview/.github/main/profile/assets/auroraview.png" width="92" alt="AuroraView logo">
</p>

# AuroraView

**Web interfaces for people. Explicit tool contracts for agents. Native creative hosts.**

AuroraView connects HTML, CSS and JavaScript interfaces to Python tools and a Rust
WebView core. It helps technical artists and pipeline developers build asset
browsers, scene inspectors and production panels inside Digital Content Creation
(DCC) applications. Bring the web's interface ecosystem and AI-assisted development
into the software where creative work happens.

[Website](https://try-auroraview.github.io/) ·
[Documentation](https://try-auroraview.github.io/auroraview/) ·
[Examples](https://try-auroraview.github.io/#examples) ·
[中文](README_zh.md)

![Concept illustration: people use web interfaces while agents use registered contracts; both connect to native creative tools.](https://raw.githubusercontent.com/try-auroraview/.github/main/profile/assets/framework-concept.png)

*Concept illustration. See the linked demos for actual application behavior.*

## Why AuroraView exists

Web technologies make it easier to build polished interfaces and let agents
participate in development. Studio tools also need a very specific host API.
Rebuilding that interface for each application's widget toolkit adds work;
shipping a separate browser loses the scene context and native lifecycle.

AuroraView lets the web layer handle layout and interaction while host code owns
scene access, docking, thread scheduling and cleanup. Front-end developers can
use familiar web tools, and pipeline developers can keep their existing Python
logic. On Windows, the native WebView2 backend uses the system browser runtime;
the Python binding is packaged as an extension module.

The same tool should be usable through a visual panel and a declared automation
contract. AuroraView's optional DCC-MCP integration explicitly registers a live
panel for discovery and invocation. Scene operations still need host tools with
schemas, permissions and a defined context; interface controls do not become
agent tools automatically.

## How the pieces fit

| Layer | Responsibility | Source |
| --- | --- | --- |
| Web interface | HTML/CSS, TypeScript calls and event subscriptions | [SDK](https://github.com/try-auroraview/auroraview/tree/main/packages/auroraview-sdk) |
| Bridge and core | RPC, events, resources and WebView backend contracts | [Rust crates](https://github.com/try-auroraview/auroraview/tree/main/crates) |
| Python integration | Exposed methods, lifecycle hooks and Qt integration | [Python package](https://github.com/try-auroraview/auroraview/tree/main/python/auroraview) |
| Native host adapter | Host UI ownership, main-thread work and teardown | [Integration guides](https://try-auroraview.github.io/auroraview/dcc/) |
| Optional agent integration | Registered panel tools and instance context | [DCC-MCP integration](https://github.com/try-auroraview/auroraview/tree/main/python/auroraview/dcc_mcp) |

Calls travel from JavaScript to host methods; host events return through
`window.auroraview.trigger()`. Qt hosts retain their event loop. Blender and game
engines need their own native integration. WebView objects must stay on their
owning UI thread. Sharing the protocol does not remove those host boundaries.

The current DCC-MCP panel adapter exposes `eval_js`, `screenshot`, `load_url` and
`load_html`. Its context describes the panel, process and detected host; it does
not itself own a scene graph, selection model or Undo stack.

Beyond panels, the framework includes [browser APIs and extension compatibility](https://try-auroraview.github.io/auroraview/guide/chrome-extension-apis)
and [application packaging](https://try-auroraview.github.io/auroraview/guide/packing).
Extensions add capabilities to the web layer; packaging collects application
code and assets for distribution. Native host plugins keep their own lifecycle
and installation requirements. See the [layered architecture](https://try-auroraview.github.io/#architecture).

## Explore the projects

| Project | What to use it for |
| --- | --- |
| [auroraview](https://github.com/try-auroraview/auroraview) | Rust core, Python package, TypeScript SDK, CLI, Gallery and documentation |
| [Maya adapter](https://github.com/try-auroraview/auroraview-maya) | Maya host integration and dispatch |
| [Maya Outliner demo](https://github.com/try-auroraview/auroraview-maya-outliner) | A separate Vue/TypeScript scene-tree tutorial with Maya Python operations |
| [Houdini adapter](https://github.com/try-auroraview/auroraview-houdini) · [Nuke adapter](https://github.com/try-auroraview/auroraview-nuke) | Qt host integration packages |
| [Blender integration](https://github.com/try-auroraview/auroraview-blender) | Native add-on; floating WebView remains experimental |
| [Unreal integration](https://github.com/try-auroraview/auroraview-unreal) | Engine plugin under active development; check native build and host evidence |
| [Unity integration](https://github.com/try-auroraview/auroraview-unity) | Windows Editor integration under development; check its verification report |

Published framework wheels, CLI binaries and Gallery applications are available
in [Releases](https://github.com/try-auroraview/auroraview/releases).
Host integration maturity varies. The [website project directory](https://try-auroraview.github.io/#ecosystem)
links source, checks and native runtime evidence separately. A successful build
alone does not establish an interactive host demo.

## Start with a small tool

Install the package in a development Python environment:

```bash
pip install auroraview
```

```python
from auroraview import run_desktop

run_desktop(
    title="Scene tool prototype",
    html="<h1>My first AuroraView tool</h1>",
    width=720,
    height=480,
)
```

This opens a standalone prototype. For an embedded tool, follow the
[host integration guide](https://try-auroraview.github.io/auroraview/dcc/)
and use the host's Python environment and UI lifecycle. Linux requires the
documented GTK/WebKit system packages; Windows requires WebView2 Runtime.

Learn the complete front-end-to-host workflow with the
[Maya Outliner tutorial](https://github.com/try-auroraview/auroraview-maya-outliner).
Browse the [Gallery](https://try-auroraview.github.io/auroraview/guide/gallery)
for interface and bridge examples.

## Contribute

Focused host adapters, reproducible demos, tests and documentation are welcome.
Report the host version, operating system, package version and reproduction steps
in the relevant project's issue tracker. Start with the framework's
[contribution guide](https://github.com/try-auroraview/auroraview/blob/main/CONTRIBUTING.md).

