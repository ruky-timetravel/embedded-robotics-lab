# 嵌入式与机器人 Linux 学习实验室

从 C 语言与调试出发，逐步完成设备通信协议、FreeRTOS 任务协作、电机与双轮底盘软件仿真，以及 ROS 2 机器人仿真。这个仓库用于保存可复现的代码、学习记录和项目证据。

**当前阶段：ROS 2 入门（2026-10-21）。** 跟随《ROS 2机器人开发从入门到实践》视频，从 1.3 小海龟实验开始，沿用 VMware 中的 Ubuntu 与 ROS 2 Lyrical。已观察到 TurtleSim 窗口和节点关系图，具体命令输出与学习者解释继续补充；此前 C/GDB 课程的验收状态保留在进度记录中。

## 当前内容

| 内容 | 路径 | 当前状态 |
| --- | --- | --- |
| ROS 2 视频学习、第一课与日志 | [ROS 2 学习入口](docs/ros2/README.md) | Lyrical；从 1.3 小海龟实验开始 |
| Linux 环境与 VMware 配置 | [环境配置](docs/linux-setup.md) | 已整理安装与检查步骤；版本记录见文档 |
| C 程序编译与断点调试 | [第一课](lessons/day01/README.md) | 已提供示例与复现步骤；学习者验收待补充 |
| 16 周学习与项目计划 | [学习路线](docs/roadmap.md) | Linux 路线，按验收进展调整 |
| 学习进度与证据 | [进度记录](docs/progress.md) | 只记录实际完成并能说明来源的内容 |
| 原始路线资料 | [原始文档](docs/reference/original-roadmap.md) | 保留原始版本作为参考，执行以 Linux 路线为准 |

## 学习环境

- Ubuntu 26.04.1 LTS，VMware 虚拟机，x86_64。
- 学习者已回报：Git 2.53.0、Python 3.14.4、VS Code 1.142.0。
- GCC、GDB 的完整版本与学习者本机运行记录待补充。
- 初期使用电脑中的模拟数据，后续根据条件增加硬件验证。

## 运行第一课

在 Ubuntu 中取得本仓库后，进入仓库根目录，安装基础工具：

```bash
sudo apt update
sudo apt install build-essential gdb git python3 python3-venv
```

直接编译并运行：

```bash
mkdir -p build/day01
gcc -std=c11 -Wall -Wextra -g -O0 lessons/day01/main.c -o build/day01/demo
./build/day01/demo
```

预期输出：

```text
Speed error: 20
```

也可以使用根目录的 Makefile：

```bash
make day01
make run-day01
make verify
```

`make verify` 是第一课的编译及输出冒烟检查。它验证示例输出，不代表学习者已经掌握调试，也不验证后续机器人项目。

仓库包含 GitHub Actions 自动检查配置：使用 Ubuntu 24.04 runner 编译同一份标准 C 代码、检查输出并打印 GDB 中的误差值。CI 环境与学习者的 Ubuntu 26.04 虚拟机分别记录；是否成功以 Actions 的实际运行结果为准。

查看变量与单步调试的步骤见[第一课说明](lessons/day01/README.md)。

## 后续项目

| 项目 | 要解决的问题 | 预期交付物 | 状态 |
| --- | --- | --- | --- |
| PC 设备通信协议 | 字节流分段、校验、边界与错误恢复 | C 解析器、虚拟设备、Python 测试、故障日志 | 待开始 |
| 电机与双轮底盘软件仿真 | 速度闭环、积分饱和、运动学与超时停车 | C 控制器、仿真模型、CSV、曲线和场景记录 | 待开始 |
| ROS 2 机器人仿真 | 节点接口、坐标变换、导航任务与恢复 | ROS 2 节点、配置、仿真任务和结果分析 | 基础入门已开始；导航项目待开始 |

详细验收条件见[学习路线](docs/roadmap.md)。后期机器人软件按 Ubuntu 26.04 匹配版本，开始安装时复核官方兼容文档。

## 怎样积累可展示的项目经历

每完成一个小目标，提交对应源码、复现步骤、实际输出和自己的分析。出现问题时记录现象、定位过程、修复方法与再次验证结果。

提交信息示例：

```text
feat: add bounded ring buffer
fix: recover parser after invalid frame length
docs: record GDB investigation of buffer wraparound
```

当前可以描述为“嵌入式与机器人 Linux 学习实践，持续进行中”。协议系统、闭环控制与导航等功能在实现、验证后，再按实际成果补充到项目介绍。PC 仿真与真实外设、MCU 实时性能分别记录。

## 内容来源

本仓库基于学习者提供的《嵌入式与机器人：16 周学习路线及项目清单》及后续学习交流整理。第一课代码和操作说明由 AI 辅助准备；学习者的独立修改、理解、运行结果和实验结论通过后续提交持续补充。引用的第三方文档保留官方链接。
