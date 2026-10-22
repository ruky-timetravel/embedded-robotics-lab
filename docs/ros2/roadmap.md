# ROS 2 学习路线

现有基础：C++、Linux。当前主线：VMware Ubuntu + ROS 2 Lyrical，结合 C++ 与 Python 学习。长期方向：机械臂操作、具身智能、VLA 与 π0.7；Python 也用于后续数据处理和策略实验。以现有仓库 [embedded-robotics-lab](https://github.com/ruky-timetravel/embedded-robotics-lab) 记录学习，源码、排错和截图统一按章节归档。

路线按实践结果推进。当前学习鱼香 ROS 机器人《ROS 2机器人开发从入门到实践》：第一章包含 [1.3 运行你的第一个机器人](https://www.bilibili.com/video/BV1iE421w7d5)与编程基础；第二章已实践 C++ / Python 节点与功能包。课程进度与本仓库章节分别记录，以实际完成的实验为准。

## 当前章节入口

| 章节 | 源码、实验与排错 | 当前结果 |
| --- | --- | --- |
| CHAPT1 | [本章入口](../../CHAPT1/README.md) · [TurtleSim](../../CHAPT1/TURTLESIM.md) · [环境截图](../../CHAPT1/EVIDENCE.md) · [排错](../../CHAPT1/TROUBLESHOOTING.md) | 已有编程源码、小海龟窗口和节点图；保留 CMake 报错过程，当前源码完整重跑证据待补 |
| CHAPT2 | [本章入口](../../CHAPT2/README.md) · [Python 排错](../../CHAPT2/TROUBLESHOOTING.md) · [C++ 排错与截图](../../CHAPT2/CPP_NODE.md) | Python 与 C++ 包构建、发现和 `ros2 run` 日志输出均已确认；新建 C++ 包完整源码待同步 |

## 已有证据

- 当前终端 `printenv ROS_DISTRO` 输出 `lyrical`。
- 已看到 TurtleSim 窗口和 `rqt_graph` 中的 `/teleop_turtle`、`/turtlesim`、`/turtle1/cmd_vel` 连接。
- Python 功能包已被识别为 `ros.ament_python`，构建结束于 `1 package finished`，`ros2 run` 成功打印 INFO/WARN“你好”，证据见 [CHAPT2 运行截图](../../CHAPT2/images/python-node-success.png)。
- C++ 包已完成 CMake 配置、编译与安装修复，最终两个包构建完成，`ros2 run demo_cpp_pkg cpp_node` 打印“你好”，见 [C++ 实验与截图](../../CHAPT2/CPP_NODE.md)。新包完整源码尚待同步；小海龟的键盘运动、实际消息样本和概念解释仍待记录。
- Ubuntu 具体版本和环境加载路径需补充实际输出。

## 分阶段计划

| 阶段 | 内容 | 验收结果 | 当前状态 |
|---|---|---|---|
| 0 | 核对现有 Ubuntu、Lyrical 和仓库记录方式 | 保存环境信息，能在新终端加载同一环境 | 部分确认，版本与路径记录待补 |
| 1 | 视频 1.3：TurtleSim、节点、包、话题、消息 | 控制海龟运动，观察 `cmd_vel` 和 `pose`，能解释节点图 | 进行中，已观察到启动和图，实际操作待验收 |
| 2 | `rclpy` / `rclcpp`、工作空间、`ament_python` / `ament_cmake`、`colcon` | 自建包、运行节点，再完成发布者与订阅者，能修改消息或发布频率 | Python 与 C++ 日志节点均已运行；新 C++ 包源码归档和通信实验待完成 |
| 3 | 用 C++ 节点控制 TurtleSim | 发布 `Twist`、订阅位姿，完成一个可重复的简单控制实验 | 待开始 |
| 4 | 在已有小实验上学习 Service、参数和 Launch | 调用一次服务、修改一个参数，并用启动文件复现实验 | 待开始 |

节点和环境变量实践见 [CHAPT2](../../CHAPT2/README.md)。可对照 [1.4.5 环境变量](https://www.bilibili.com/video/BV1pm42137bR/)与 [2.1.2 编写你的第一个节点 C++ 示例](https://www.bilibili.com/video/BV1FH4y1c7Px/)复盘，后续同步 C++ 新包源码并进入发布/订阅通信实验。

## 机械臂与具身智能拓展目标

先完成上面的 ROS 2 基础，再逐步建立「感知 → 数据采集 → 策略学习 → 动作执行 → 评估」流程。以下阶段均为后续计划，目前尚无机械臂、模型训练或 VLA 实验成果。

| 阶段 | 方向与学习内容 | 计划验收成果 | 当前状态 |
| --- | --- | --- | --- |
| 5 | 机械臂基础：坐标变换、URDF/Xacro、TF2、正逆运动学和关节限制 | 在 RViz 中展示机械臂；用样例说明关节角与末端位姿的关系，保存模型和操作步骤 | 待开始 |
| 6 | 机械臂操作：MoveIt 2、ros2_control、轨迹执行、夹爪与碰撞检查 | 在核对兼容的仿真环境完成一次抓取放置；记录起止状态、场景、规划结果和失败案例 | 待开始 |
| 7 | 示教数据：遥操作、相机/关节状态/动作/任务语言的同步，数据格式与回放 | 从公开数据或仿真入手，检查一个完整 episode 的时间戳、单位、坐标、动作定义与缺失数据 | 待开始 |
| 8 | 模仿学习：Python、PyTorch、行为克隆与 ACT 等基线 | 划分训练与评估任务，完成一项基线；记录版本、数据、配置、任务成功数/总次数和失败原因 | 待开始 |
| 9 | VLA：视觉/语言/动作表示，π0、π0.5 等公开模型的推理与条件允许时微调 | 在固定任务与评估条件下运行公开模型；比较指令和场景变化，记录成功率、推理延迟、资源使用和限制 | 待开始 |
| 10 | π0.7：多模态条件、视觉子目标、语言引导与组合泛化 | 形成论文笔记、模型比较和实验设计；明确已公开与尚未取得的资源，使用可用公开模型做方法对照 | 待研究 |

### π0.7 研究与公开模型实践

- 以 [π0.7 官方介绍](https://www.pi.website/blog/pi07)与[论文](https://arxiv.org/abs/2604.15483)为依据，重点分析输入条件、数据来源、动作接口与评估设定。
- 开始实验前，在 [openpi 官方仓库](https://github.com/Physical-Intelligence/openpi)核对模型实现、权重、训练配置与许可证的实际公开情况。π0.7 先作为论文与方法研究目标；公开实现实验按届时可用资源开展。
- 公开模型的官方评估结果作为参考，本仓库的成功率、泛化和延迟结论须来自自己实际完成的实验。

### 实验安排与记录

当前优先仿真与公开数据。模型推理或训练前核对 GPU、显存、依赖和许可证；MoveIt 2、ros2_control 及仿真环境的版本在进入该阶段时单独核对，不从当前已运行 Lyrical 推断兼容性。模型实验可使用独立环境，并记录它与 ROS 2 观察、动作接口之间的映射。

后续机械臂实验记录关节/末端动作定义、单位、坐标、控制频率、关节与速度限制，以及任务停止条件。具备真实硬件后，从标定和受限动作验证开始，再逐步增加任务复杂度。

每个实验保留源码版本、数据来源与划分、随机种子、配置、日志、演示及失败案例。训练损失和离线动作误差与闭环任务结果分别记录；有足够算力和数据后再安排微调。

参考入口：[MoveIt 2](https://moveit.picknik.ai/) · [ros2_control](https://control.ros.org/) · [LeRobot](https://huggingface.co/docs/lerobot/index) · [openpi](https://github.com/Physical-Intelligence/openpi)。

## 环境约定

固定使用当前已观察到的 Lyrical。每个新终端加载同一套环境；使用已核实存在的安装路径，不混用其他发行版教程中的 `source` 路径。

Ubuntu 26.04.1 LTS / x86_64 沿用此前用户报告，完整系统版本和工具版本按章节记录补充。涉及新工具或模型时，重新核对官方依赖和支持平台，不从当前节点能运行推断所有组件均已兼容。

## 按章节记录

1. 将目标归入对应 `CHAPT`，写清预期现象与实际文件导航。
2. 在该章节保存源码、复现命令、输出与 `images/` 截图。
3. 将问题、诊断、修改和复测写入该章节 `TROUBLESHOOTING.md`，用自己的话解释结果。
4. 更新章节状态与[总体进度](../progress.md)，提交真实成果。

使用 [章节记录模板](../chapter-record-template.md) 作为新增内容的参考。观察到节点启动、完成实验、理解概念是三种不同证据，应分别记录。没有实际运行的预期结果不能写成已完成结果。

提交围绕真实成果，例如 `docs: 记录 TurtleSim 节点与话题检查` 或 `feat: 添加 C++ 速度发布节点`，不为增加提交次数编造学习进度。

## 官方参考

- [Lyrical 官方文档概览](https://docs.ros.org/en/lyrical/)
- [Lyrical 官方学习路径源文件](https://github.com/ros2/ros2_documentation/blob/lyrical/source/First-Steps.rst)
- [Lyrical 官方 C++ 发布与订阅教程源文件](https://github.com/ros2/ros2_documentation/blob/lyrical/source/ROS-Framework/client-libraries/Working-with-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber.rst)
- [官方发行版与支持期限](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst)
- [Lyrical 官方支持平台](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases/lyrical/supported-platforms.rst)
