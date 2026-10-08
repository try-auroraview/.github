<p align="center"><img src="https://raw.githubusercontent.com/try-auroraview/.github/main/profile/assets/auroraview-original.png" width="240" alt="AuroraView"></p>

# AuroraView

**Web interfaces for people. Explicit tool contracts for agents. Native creative hosts.**

AuroraView brings modern web interfaces into Digital Content Creation (DCC)
applications. Start with familiar HTML, CSS and JavaScript, connect existing host
logic, and build asset browsers, scene inspectors and production panels. Ordinary
developers, technical artists and agents can work with clear, documented contracts
instead of learning a separate interface stack for every host.

[Website](https://try-auroraview.github.io/) ·
[Documentation](https://try-auroraview.github.io/auroraview/) ·
[How it works](https://try-auroraview.github.io/how-it-works/) ·
[Host matrix](https://try-auroraview.github.io/ecosystem/) ·
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

## Shared runtime direction — proposed

AuroraView focuses on modern web interfaces, rendering and native docking. The
planned thin integration reuses DCC-MCP Core's existing server, tool and Skill
registry, host execution bridge, scheduling and lifecycle. DCC-MCP retains its
automation responsibilities. This shared integration has not yet been delivered.

The intended visual panel and explicit agent tools call the same host business
capabilities. An integration should attach to an existing host service when
available. Closing a panel releases its own subscriptions and tasks; only the
owner closes a service. See the website's
[current and proposed architecture](https://try-auroraview.github.io/#architecture)
for the implementation boundary.

## Explore the projects

| Project | What to use it for |
| --- | --- |
| [auroraview](https://github.com/try-auroraview/auroraview) | Rust core, Python package, TypeScript SDK, CLI, Gallery and documentation |
| [Maya adapter](https://github.com/try-auroraview/auroraview-maya) | Maya host integration and dispatch |
| [Maya Outliner demo](https://github.com/try-auroraview/auroraview-maya-outliner) | A separate Vue/TypeScript scene-tree tutorial with Maya Python operations |
| [Houdini adapter](https://github.com/try-auroraview/auroraview-houdini) · [Nuke adapter](https://github.com/try-auroraview/auroraview-nuke) | Qt host integration packages |
| [Blender integration](https://github.com/try-auroraview/auroraview-blender) | Native add-on with HTML and scene interaction; input, DPI and cleanup acceptance continues |
| [Unreal integration](https://github.com/try-auroraview/auroraview-unreal) | Engine plugin under active development; check native build and host evidence |
| [Unity integration](https://github.com/try-auroraview/auroraview-unity) | Windows Editor integration under development; check its verification report |

Published framework wheels, CLI binaries and Gallery applications are available
in [Releases](https://github.com/try-auroraview/auroraview/releases).
Host integration maturity varies. The [host matrix](https://try-auroraview.github.io/ecosystem/)
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
