# Linux 开发环境准备

本项目从 Linux 下的 C 语言编译和调试开始，逐步学习嵌入式与机器人开发。当前使用 Windows 宿主机中的 VMware Ubuntu 虚拟机。

## 已知环境与验证范围

| 项目 | 当前记录 | 依据与状态 |
| --- | --- | --- |
| Linux 发行版 | Ubuntu 26.04.1 LTS | 用户提供的 `/etc/os-release` 截图 |
| 处理器架构 | `x86_64` | 用户回传的 `uname -m` 输出 |
| Git | 2.53.0 | 用户回传的版本输出 |
| Python | 3.14.4 | 用户回传的版本输出 |
| VS Code | 1.142.0，`x64` | 用户回传的版本输出 |
| GCC、GDB | 待补充完整版本 | 仅收到部分版权文字，尚不足以确认版本 |
| VMware 复制粘贴与拖放 | 待验证 | 已提供安装方法，尚未收到成功使用的结果 |

版本号用于记录本次学习环境，并非本项目要求的固定版本。程序编译、运行和断点调试的验收结果见 [第一课](../lessons/day01/README.md)，目前仍待学习者回传。

## 1. 安装基础工具

以下命令均在 **Ubuntu 虚拟机的终端**执行。

```bash
sudo apt update
sudo apt install build-essential gdb git python3 python3-venv
```

输入 `sudo` 密码时，终端不会显示密码字符。安装程序询问是否继续时，输入 `Y` 并回车。

| 软件包 | 学习中的用途 |
| --- | --- |
| `build-essential` | 提供 GCC、G++、Make 等基础编译工具 |
| `gdb` | 设置断点、单步执行、查看变量 |
| `git` | 保存代码修改记录并同步到 GitHub |
| `python3` | 后续编写测试脚本和处理数据 |
| `python3-venv` | 为后续 Python 项目建立独立虚拟环境 |

Ubuntu 官方软件包信息：[build-essential](https://packages.ubuntu.com/resolute/build-essential)。

## 2. 安装编辑器

Ubuntu 中尚未安装 VS Code 时，执行：

```bash
sudo snap install code --classic
```

打开编辑器：

```bash
code
```

按 **Ctrl + Shift + X** 打开扩展面板，搜索并安装 **Microsoft 发布的 C/C++ 扩展**。编辑器负责编辑和显示调试界面，GCC 负责实际编译，GDB 负责实际调试。

官方资料：[VS Code Linux 安装](https://code.visualstudio.com/docs/setup/linux)、[Linux 下配置 C/C++](https://code.visualstudio.com/docs/cpp/config-linux)。

## 3. 安装 VMware 交互工具

在 Ubuntu 中安装：

```bash
sudo apt update
sudo apt install -y open-vm-tools open-vm-tools-desktop
```

保存正在编辑的文件，再重启虚拟机：

```bash
sudo reboot
```

在 Windows 的 VMware 中进入 **虚拟机设置 → 选项 → 客户机隔离**，检查以下选项：

- 启用复制和粘贴。
- 启用拖放。

复制粘贴测试：在 Windows 中用 **Ctrl + C** 复制一小段文本，再在 Ubuntu 终端中用 **Ctrl + Shift + V** 粘贴。

VMware 的复制粘贴与拖放在 Wayland 会话下存在限制，安装工具后仍需实际测试。遇到无法使用的情况，先查看会话类型：

```bash
echo "$XDG_SESSION_TYPE"
```

记录输出是 `wayland` 还是 `x11`，以及哪项交互功能失败，再针对环境排查。Ubuntu 26.04 默认桌面使用 Wayland，不能仅凭工具已安装就认定交互功能可用。

官方资料：[Ubuntu open-vm-tools-desktop 软件包](https://packages.ubuntu.com/search?keywords=open-vm-tools-desktop)、[Ubuntu 26.04 LTS 发行说明](https://documentation.ubuntu.com/release-notes/26.04/summary-for-lts-users/)、[VMware 复制粘贴与拖放说明](https://knowledge.broadcom.com/external/article/320995)。

## 4. 检查工具并保存结果

在 Ubuntu 终端逐条执行：

```bash
gcc --version
gdb --version
git --version
python3 --version
code --version
uname -m
```

保留版本输出，便于重现学习环境。不要把 GPL 版权或许可证文字作为 GCC、GDB 已成功完成第一课的证据；版本检查与程序编译、运行、调试是不同的验收项目。

完成安装后，从仓库根目录打开项目：

```bash
code .
```

接着进行 [第一课：编译运行与断点调试](../lessons/day01/README.md)。
