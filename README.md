# 嵌入式与机器人 Linux 学习实验室

记录 ROS 2、C/C++、Python 与 Linux 实践，逐步进入**机械臂操作、具身智能与视觉语言动作模型（VLA）**，持续学习 **π0.7（pi0.7）** 等机器人基础模型。

学习内容按章节组织：每章包含源码、运行步骤、排错过程与截图，后续在对应章节持续更新。

[学习视频](https://www.bilibili.com/video/BV1iE421w7d5/) · [ROS 2 课程索引](docs/ros2/README.md) · [学习进度](docs/progress.md) · [后续路线](docs/ros2/roadmap.md)

## 章节导航

| 章节 | 内容与文件 | 排错与实验记录 | 当前结果 |
| --- | --- | --- | --- |
| [第一章：Ubuntu、编程与 ROS 2 初体验](CHAPT1/README.md) | C/C++、Python 最小程序、CMake、小海龟与节点图 | [排错过程](CHAPT1/TROUBLESHOOTING.md) · [Ubuntu 实验与截图](CHAPT1/EVIDENCE.md) | 已观察小海龟与节点图，CMake 配置已修正；C++ 构建验收待补 |
| [第二章：ROS 2 C++ / Python 节点与功能包](CHAPT2/README.md) | `rclpy`、`rclcpp`、包结构、入口配置、CMake、colcon 与环境加载 | [Python 排错](CHAPT2/TROUBLESHOOTING.md) · [C++ 排错与截图](CHAPT2/CPP_NODE.md) · [类与日志实验](CHAPT2/OOP_NODES.md) | Python、C++ 包均已构建并启动；C++ / Python 新工作空间源码已归档 |

首页只提供章节入口，截图在各章说明和排错记录内查看。

## 当前学习成果

- Ubuntu 虚拟机中已运行 TurtleSim，并观察 `/teleop_turtle`、`/turtlesim` 与 `/turtle1/cmd_vel` 的关系。
- 已收录第一章最小程序与第二章节点、Python 功能包的实际源码。
- Python 包已识别为 `ros.ament_python`，构建完成，并成功输出 `INFO`、`WARN` 两条“你好”日志。
- C++ 包 `demo_cpp_pkg` 已通过构建、安装前缀查询及 `ros2 run`，节点输出 `[cpp_node]: 你好`。
- 已归档 chapt2_ws 中两个完整功能包，以及 PersonNode / WriterNode 的继承、作用域与日志组合练习。
- 已记录 CMake 拼写、Python 模块路径、入口配置、构建目录、ament 索引、环境脚本及 XML 标签等排错过程。

已同步两个功能包与人物类源码，后续继续发布/订阅、服务、参数和 Launch 练习。小海龟实际运动与速度消息样本也继续补入第一章。

## 使用仓库

```bash
git clone https://github.com/ruky-timetravel/embedded-robotics-lab.git
cd embedded-robotics-lab
```

从 [CHAPT1](CHAPT1/README.md) 或 [CHAPT2](CHAPT2/README.md) 进入相应运行步骤。本仓库沿用实际学习环境 **VMware Ubuntu + ROS 2 Lyrical**；ROS 2 命令在安装了对应依赖的 Ubuntu Bash 终端执行。

```text
CHAPT1/                  编程基础、小海龟、环境记录与截图
CHAPT2/                  C++ / Python 节点与功能包、排错与截图
docs/                    章节索引、进度、路线与记录模板
```

源码来自学习者提供的 `embedded-learning` 文件夹，保留原有 `CHAPT1`、`CHAPT2` 命名及当前修正版文件。生成的 `build/`、`install/`、`log/`、CMake 缓存、二进制和本机编辑器配置不上传。

## 机械臂、具身智能与 VLA 方向目标

长期建立「感知 → 数据采集 → 策略学习 → 动作执行 → 评估」的实验流程，按实际完成的项目记录成果。

| 方向 | 学习目标 | 计划成果 |
| --- | --- | --- |
| 机械臂建模与运动学 | URDF/Xacro、TF2、关节限制、正逆运动学 | RViz 模型及关节运动与末端位姿实验 |
| 机械臂规划与控制 | MoveIt 2、ros2_control、轨迹执行与夹爪控制 | 仿真抓取放置、配置、运行日志与失败分析 |
| 示教与机器人数据 | 遥操作、图像/状态/动作/语言指令同步、检查与回放 | 带任务说明的数据样例和检查脚本 |
| 模仿学习 | Python、PyTorch、行为克隆与 ACT 等基线 | 可复现的基线实验与任务评估 |
| VLA 实践 | 视觉、语言与动作表示，公开模型推理与条件允许时微调 | 固定任务下的成功率、延迟和失败案例 |
| π0.7（pi0.7）研究 | 论文阅读、多模态条件、视觉子目标与组合泛化 | 方法笔记、模型比较及基于可用公开资源的实验方案 |

实施顺序和验收条件见[机械臂与具身智能拓展目标](docs/ros2/roadmap.md#机械臂与具身智能拓展目标)。当前先完成 ROS 2 基础，之后用仿真与公开数据推进；真实机械臂实验在具备硬件后补充。

研究入口：[π0.7 官方介绍](https://www.pi.website/blog/pi07) · [论文](https://arxiv.org/abs/2604.15483) · [openpi](https://github.com/Physical-Intelligence/openpi) · [MoveIt 2](https://moveit.picknik.ai/) · [LeRobot](https://huggingface.co/docs/lerobot/index)。这些是后续学习方向，目前尚无本仓库机械臂或 VLA 实验成果。

## 记录约定

每章按「目标 → 源码与命令 → 实际结果 → 问题与修复 → 下一步」积累，使用[章节记录模板](docs/chapter-record-template.md)。错误现场和修复后的结果都保留，尚未运行的预期结果注明待验证。

[Linux 环境说明](docs/linux-setup.md) · [嵌入式项目路线](docs/roadmap.md) · [原始路线资料](docs/reference/README.md) · [ROS 2 Lyrical 官方文档](https://docs.ros.org/en/lyrical/)

文档由 AI 辅助整理，源码和截图来自实际学习材料。第三方课程与文档保留原作者链接。
