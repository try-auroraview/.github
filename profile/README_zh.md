<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/try-auroraview/.github/main/profile/assets/auroraview-lockup-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/try-auroraview/.github/main/profile/assets/auroraview-lockup-light.svg">
    <img src="https://raw.githubusercontent.com/try-auroraview/.github/main/profile/assets/auroraview-lockup-light.svg" width="480" alt="AuroraView">
  </picture>
</p>

# AuroraView

**人使用 Web 界面，Agent 调用显式工具契约，创作能力留在原生宿主中。**

AuroraView 将 HTML、CSS 和 JavaScript 界面连接到 Python 工具与 Rust WebView
核心，帮助技术美术和管线开发者在数字内容创作（DCC）软件中构建资产浏览器、
场景检查器和生产面板，将 Web 界面生态和 AI 辅助开发带入实际创作环境。

[官网](https://try-auroraview.github.io/zh/) ·
[中文文档](https://try-auroraview.github.io/auroraview/zh/) ·
[教学示例](https://try-auroraview.github.io/zh/#examples) ·
[English](README.md)

![概念示意：人通过 Web 界面、Agent 通过注册契约，共同连接原生创作工具。](https://raw.githubusercontent.com/try-auroraview/.github/main/profile/assets/framework-concept.png)

*此图为概念插画。应用的实际行为请参阅对应演示。*

## 为什么需要 AuroraView

Web 技术更容易构建精美界面，也适合 Agent 参与开发。工作室工具同时依赖各宿主
独有的场景 API。为每个应用的控件系统
重复实现界面会增加维护成本；单独打开浏览器，又难以融入场景上下文与原生生命周期。

AuroraView 让 Web 层负责布局与交互，让宿主代码负责场景访问、停靠、线程调度和清理。
前端开发者可以使用熟悉的 Web 工具，管线开发者可以保留已有的 Python 逻辑。
Windows 原生 WebView2 后端使用系统浏览器运行时；Python 绑定以扩展模块分发。

同一个工具可以同时提供可视化面板和声明式自动化契约。AuroraView 的可选 DCC-MCP
集成通过显式注册，让运行中的面板可以被发现和调用。场景操作仍需宿主工具提供参数
契约、权限和限定的上下文；界面控件不会自动变成 Agent 工具。

## 各层如何协作

| 层次 | 职责 | 源码 |
| --- | --- | --- |
| Web 界面 | HTML/CSS、TypeScript 调用和事件订阅 | [SDK](https://github.com/try-auroraview/auroraview/tree/main/packages/auroraview-sdk) |
| 桥接与核心 | RPC、事件、资源与 WebView 后端契约 | [Rust crates](https://github.com/try-auroraview/auroraview/tree/main/crates) |
| Python 集成 | 暴露方法、生命周期钩子与 Qt 集成 | [Python 包](https://github.com/try-auroraview/auroraview/tree/main/python/auroraview) |
| 原生宿主适配 | 宿主界面所有权、主线程调度与销毁 | [集成指南](https://try-auroraview.github.io/auroraview/zh/dcc/) |
| 可选 Agent 集成 | 注册的面板工具与实例上下文 | [DCC-MCP 集成](https://github.com/try-auroraview/auroraview/tree/main/python/auroraview/dcc_mcp) |

JavaScript 调用宿主方法，宿主事件经 `window.auroraview.trigger()` 返回界面。
Qt 宿主保留事件循环；Blender 和游戏引擎需要各自的原生集成。
WebView 对象必须留在其所属 UI 线程上。共享协议并不消除这些宿主边界。

当前 DCC-MCP 面板适配器提供 `eval_js`、`screenshot`、`load_url` 和 `load_html`。
它的上下文描述面板、进程和检测到的宿主，本身不拥有场景图、选择模型或 Undo 栈。

框架还包含[浏览器 API 与扩展兼容能力](https://try-auroraview.github.io/auroraview/zh/guide/chrome-extension-apis)
以及[应用打包](https://try-auroraview.github.io/auroraview/zh/guide/packing)。
扩展为 Web 层增加能力，打包收集应用代码与资产以便分发；原生宿主插件保留各自的
生命周期和安装要求。完整关系见[分层架构](https://try-auroraview.github.io/zh/#architecture)。

## 共享运行时方向（规划）

AuroraView 专注现代 Web 界面、渲染与原生停靠。规划中的薄集成复用 DCC-MCP Core
已有的 Server、工具与 Skill 注册、宿主执行桥、线程调度和生命周期；DCC-MCP 保持
自身的自动化职责。这部分实际整合尚未交付。

可视面板与显式 Agent 工具将调用同一组宿主业务能力。存在宿主服务时优先附着；
关闭面板只释放自身订阅和任务，仅资源所有者关闭服务。实现边界见官网的
[当前与规划架构](https://try-auroraview.github.io/zh/#architecture)。

## 项目生态

| 项目 | 用途 |
| --- | --- |
| [auroraview](https://github.com/try-auroraview/auroraview) | Rust 核心、Python 包、TypeScript SDK、CLI、Gallery 与文档 |
| [Maya 适配器](https://github.com/try-auroraview/auroraview-maya) | Maya 宿主集成与调度 |
| [Maya Outliner 演示](https://github.com/try-auroraview/auroraview-maya-outliner) | 独立的 Vue/TypeScript 场景树教程，连接 Maya Python 操作 |
| [Houdini 适配器](https://github.com/try-auroraview/auroraview-houdini) · [Nuke 适配器](https://github.com/try-auroraview/auroraview-nuke) | Qt 宿主集成包 |
| [Blender 集成](https://github.com/try-auroraview/auroraview-blender) | 原生插件；浮动 WebView 仍为实验功能 |
| [Unreal 集成](https://github.com/try-auroraview/auroraview-unreal) | 正在开发的引擎插件，请核对原生构建与宿主运行证据 |
| [Unity 集成](https://github.com/try-auroraview/auroraview-unity) | 正在开发的 Windows Editor 集成，请查看其验证报告 |

已发布的框架 wheel、CLI 和 Gallery 应用见
[Releases](https://github.com/try-auroraview/auroraview/releases)。
各宿主成熟度不同。[官网项目目录](https://try-auroraview.github.io/zh/#ecosystem)
分别链接源码、检查结果和原生运行证据。构建成功本身不能证明交互演示已经通过。

## 从一个小工具开始

在开发用 Python 环境安装：

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

此示例打开独立窗口。嵌入工具请遵循
[宿主集成指南](https://try-auroraview.github.io/auroraview/zh/dcc/)，
使用宿主的 Python 环境与 UI 生命周期。Linux 需要文档列出的 GTK/WebKit
系统包，Windows 需要 WebView2 Runtime。

通过 [Maya Outliner 教程](https://github.com/try-auroraview/auroraview-maya-outliner)
学习完整的前端到宿主工作流；在
[Gallery](https://try-auroraview.github.io/auroraview/zh/guide/gallery)
查看界面与桥接示例。

## 参与贡献

欢迎提交职责清楚的宿主适配器、可复现的演示、测试与文档。报告问题时请附上宿主版本、
操作系统、包版本和复现步骤，并提交到对应项目。开始前请阅读框架的
[贡献指南](https://github.com/try-auroraview/auroraview/blob/main/CONTRIBUTING.md)。
