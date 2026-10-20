# ROS 2 学习路线

开始日期：2026-10-21。现有基础：C++、Linux。当前主线：VMware Ubuntu + ROS 2 Lyrical + C++。以现有仓库 [embedded-robotics-lab](https://github.com/ruky-timetravel/embedded-robotics-lab) 记录学习。

路线按实践验收推进，不规定每天必须学完的内容。当前学习鱼香 ROS 机器人《ROS 2机器人开发从入门到实践》，进度为 [1.3 运行你的第一个机器人](https://www.bilibili.com/video/BV1iE421w7d5)，先围绕已经运行的 TurtleSim 理解节点与话题。

## 已有证据

- 当前终端 `printenv ROS_DISTRO` 输出 `lyrical`。
- 已看到 TurtleSim 窗口和 `rqt_graph` 中的 `/teleop_turtle`、`/turtlesim`、`/turtle1/cmd_vel` 连接。
- 键盘运动、命令输出和概念掌握情况尚待验收。
- Ubuntu 具体版本和环境加载路径需补充实际输出。

## 分阶段计划

| 阶段 | 内容 | 验收结果 | 当前状态 |
|---|---|---|---|
| 0 | 核对现有 Ubuntu、Lyrical 和仓库记录方式 | 保存环境信息，能在新终端加载同一环境 | 部分确认，版本与路径记录待补 |
| 1 | 视频 1.3：TurtleSim、节点、包、话题、消息 | 控制海龟运动，观察 `cmd_vel` 和 `pose`，能解释节点图 | 进行中，已观察到启动和图，实际操作待验收 |
| 2 | C++ `rclcpp`、工作空间、`ament_cmake`、`colcon` | 自建包并编译运行发布者和订阅者，能修改消息或发布频率 | 待开始 |
| 3 | 用 C++ 节点控制 TurtleSim | 发布 `Twist`、订阅位姿，完成一个可重复的简单控制实验 | 待开始 |
| 4 | 在已有小实验上学习 Service、参数和 Launch | 调用一次服务、修改一个参数，并用启动文件复现实验 | 待开始 |

本课完成后，可先看 [1.4.5 环境变量](https://www.bilibili.com/video/BV1pm42137bR/)，再进入 [2.1.2 编写你的第一个节点 C++ 示例](https://www.bilibili.com/video/BV1FH4y1c7Px/)。后续内容随视频和实际需求补充，当前先完成 TurtleSim 与 C++ 基础通信。

## 环境约定

固定使用当前已观察到的 Lyrical。每个新终端加载同一套环境；使用已核实存在的安装路径，不混用其他发行版教程中的 `source` 路径。

Lyrical Luth 于 2026 年 5 月 22 日发布，属于支持至 2031 年 5 月的 LTS。其 Ubuntu Tier 1 平台为 26.04；Ubuntu 24.04 为 Tier 3，需要源码构建。当前虚拟机的 Ubuntu 版本尚未核对，不从 ROS 2 发行版名称推断系统版本，也不因此直接重装。

## 每次学习的记录方式

1. 选一个可验证目标，写清预期现象。
2. 实际执行，保存关键命令、输出或截图。
3. 用自己的话解释结果，记录失败和未完成项。
4. 更新阶段状态，向现有 GitHub 仓库提交本次实际成果。

使用 [学习日志模板](daily-log-template.md) 作为记录模板。观察到节点启动、完成实验、理解概念是三种不同证据，应分别记录。没有实际运行的预期结果不能写成已完成结果。

提交围绕真实成果，例如 `docs: 记录 TurtleSim 节点与话题检查` 或 `feat: 添加 C++ 速度发布节点`，不为增加提交次数编造学习进度。

## 官方参考

- [Lyrical 官方文档概览](https://docs.ros.org/en/lyrical/)
- [Lyrical 官方学习路径源文件](https://github.com/ros2/ros2_documentation/blob/lyrical/source/First-Steps.rst)
- [Lyrical 官方 C++ 发布与订阅教程源文件](https://github.com/ros2/ros2_documentation/blob/lyrical/source/ROS-Framework/client-libraries/Working-with-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber.rst)
- [官方发行版与支持期限](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst)
- [Lyrical 官方支持平台](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases/lyrical/supported-platforms.rst)
