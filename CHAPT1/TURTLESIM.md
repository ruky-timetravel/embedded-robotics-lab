# CHAPT1：从 turtlesim 理解节点与话题

[本章入口](README.md) · [环境与截图](EVIDENCE.md) · [下一章节点与功能包](../CHAPT2/README.md)

对应鱼香 ROS 机器人《ROS 2机器人开发从入门到实践》1.3「运行你的第一个机器人」。学习环境使用已有 VMware Ubuntu 和 ROS 2 Lyrical，后续编程以 C++ 为主；已有 C++、Linux 基础，无需重新从语言和终端入门。本笔记为结合当前环境编写的概念与练习记录。

## 当前证据与待完成事项

本章保留的实际界面记录显示：

- Ubuntu 终端中 `printenv ROS_DISTRO` 输出 `lyrical`。
- TurtleSim 窗口已经打开。
- `rqt_graph` 显示 `/teleop_turtle` 经 `/turtle1/cmd_vel` 连接到 `/turtlesim`，并能看到 Action 的反馈和状态相关连接。
- 历史命令 `source /opt/ros/humble/setup.bash` 报文件不存在；该命令与当前显示的 Lyrical 不对应。

这些证据确认了当前节点已启动、图中存在连接。键盘是否成功控制运动、实际消息内容和概念掌握情况仍待实践验收，不能由窗口和连接图直接推断。

## 1. 用现有画面理解三个概念

| 概念 | 含义 | 当前例子 |
|---|---|---|
| 节点（Node） | 承担一项明确职责的 ROS 2 组件 | `/teleop_turtle` 处理键盘控制，`/turtlesim` 负责仿真 |
| 包（Package） | 组织可执行程序、配置和依赖的单位 | `turtlesim` 包提供两个示例程序 |
| 话题（Topic） | 节点发布和订阅消息的通道 | `/turtle1/cmd_vel` 传递速度指令 |

当前主要数据流是：

```text
键盘输入 → /teleop_turtle → /turtle1/cmd_vel → /turtlesim → 海龟运动
```

速度消息类型为 `geometry_msgs/msg/Twist`，包含 `linear` 和 `angular` 两组分量。二维海龟示例主要使用 `linear.x` 和 `angular.z`。实际值要通过命令观察，不把教程预期值写成本机结果。

`ros2 run <包名> <可执行程序名>` 从包中启动程序。例如 `turtlesim` 是包名，`turtle_teleop_key` 是可执行程序名，它默认创建的节点名是 `/teleop_turtle`。一个可执行程序可以包含一个或多个节点。

图中的 Action 反馈和状态连接属于另一种通信机制。本课先关注 `/turtle1/cmd_vel` 这一条话题，不把“看见 Action 连接”记为“已完成 Action 学习”。

## 2. 在 Ubuntu 终端核对环境

以下命令在 VMware Ubuntu 的 Bash 终端执行，不在 Windows PowerShell 中执行。先只读记录环境：

```bash
cat /etc/os-release
ls /opt/ros
printenv ROS_DISTRO
command -v ros2
```

当前终端已观察到发行版为 `lyrical`，Ubuntu 的具体版本和完整安装目录仍应保存实际输出。

每个新终端都需要加载同一套环境。先检查预期环境文件：

```bash
test -r /opt/ros/lyrical/setup.bash && printf 'Lyrical 环境文件存在\n'
```

确认文件存在后执行：

```bash
source /opt/ros/lyrical/setup.bash
printenv ROS_DISTRO
```

预期输出 `lyrical`。如果环境文件不存在，记录结果并核对实际安装位置，不改用 Humble 或其他发行版路径尝试。`/opt/ros` 缺失也不能单独证明没有 ROS 2，源码安装可能位于其他位置。

## 3. 检查现有节点与话题

保留已运行的 TurtleSim 和键盘控制终端，在一个加载 Lyrical 的新终端执行：

```bash
ros2 pkg executables turtlesim
ros2 node list
ros2 node info /teleop_turtle
ros2 node info /turtlesim
ros2 topic list -t
ros2 topic info /turtle1/cmd_vel
ros2 interface show geometry_msgs/msg/Twist
```

把实际输出记录下来，重点寻找以下关系：

- `/teleop_turtle` 是否发布 `/turtle1/cmd_vel`？
- `/turtlesim` 是否订阅同一个话题？
- 话题类型是否为 `geometry_msgs/msg/Twist`？
- `Twist` 的 `linear`、`angular` 各有哪些字段？

上面的提问用于自行验收，目前没有预先填写答案。发布者和订阅者数量会随额外观察工具变化，例如 `ros2 topic echo` 也会创建订阅，不要求所有人的数量始终相同。

如果将来关闭了现有节点，可按需重新启动；当前运行时不要重复启动同名节点：

```bash
# 终端 A：先加载 Lyrical，再运行仿真
ros2 run turtlesim turtlesim_node
```

```bash
# 终端 B：先加载 Lyrical，再运行键盘控制
ros2 run turtlesim turtle_teleop_key
```

```bash
# 终端 C：可选，重新打开节点图
ros2 run rqt_graph rqt_graph
```

## 4. 动手：让按键、消息与运动对应起来

1. 在观察终端运行：

   ```bash
   ros2 topic echo /turtle1/cmd_vel
   ```

2. 将焦点切回运行 `turtle_teleop_key` 的终端，分别按上、下、左、右方向键，观察海龟和消息。焦点要在键盘控制终端；只有打开 TurtleSim 窗口并不能接收这些按键。
3. 记录至少一组前进或后退时的 `linear.x`，以及一组转向时的 `angular.z`，比较符号和运动方向。
4. 按 `Ctrl+C` 结束观察终端中的 `echo`，再运行：

   ```bash
   ros2 topic echo /turtle1/pose
   ```

5. 再次控制海龟，观察位置或方向字段如何变化，并记录实际字段名和样本。按 `Ctrl+C` 结束观察。

`cmd_vel` 表达控制指令，`pose` 表达仿真返回的状态。请用本次实际输出说明二者的区别。

## 5. 验收与 GitHub 记录

已观察到的启动证据：

- [x] 当前终端显示 ROS 2 发行版为 Lyrical。
- [x] 已看到 TurtleSim 窗口。
- [x] 已看到两个节点及 `/turtle1/cmd_vel` 连接图。

仍待实践：

- [ ] 保存 Ubuntu 版本和实际环境加载路径。
- [ ] 通过命令确认节点的发布与订阅关系。
- [ ] 在键盘控制终端按方向键，观察海龟成功运动。
- [ ] 保存 `/turtle1/cmd_vel` 的实际消息，解释分量及符号。
- [ ] 保存 `/turtle1/pose` 的实际消息，说明指令与状态的区别。
- [ ] 用自己的话说明包名、可执行程序名、节点名和话题名。
- [ ] 将真实实验结果提交到现有 GitHub 仓库。

本实验记录集中保存在 `CHAPT1/`，截图与环境见 [EVIDENCE.md](EVIDENCE.md)。当前笔记中的命令是操作指南，只有保存实际证据后才勾选对应项。

环境变量、Python 节点和功能包实践已整理到 [CHAPT2](../CHAPT2/README.md)，Python 与 C++ 包均已有构建和启动成功截图。C++ 新包的排错与运行见 [CPP_NODE.md](../CHAPT2/CPP_NODE.md)，完整源码待同步；官方 talker/listener 可作为发布与订阅练习的参考。

## 参考

- [鱼香 ROS 机器人：1.3 运行你的第一个机器人](https://www.bilibili.com/video/BV1iE421w7d5)
- [后续视频：1.4.5 环境变量](https://www.bilibili.com/video/BV1pm42137bR/)
- [后续视频：2.1.2 编写你的第一个节点 C++ 示例](https://www.bilibili.com/video/BV1FH4y1c7Px/)
- [ROS 2 Lyrical 官方文档概览](https://docs.ros.org/en/lyrical/)
- [Lyrical 官方文档源：TurtleSim](https://github.com/ros2/ros2_documentation/blob/lyrical/source/Get-Started/Introducing-Turtlesim/Introducing-Turtlesim.rst)
- [Lyrical 官方文档源：节点](https://github.com/ros2/ros2_documentation/blob/lyrical/source/ROS-Framework/nodes/Working-with-nodes/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.rst)
- [Lyrical 官方文档源：话题](https://github.com/ros2/ros2_documentation/blob/lyrical/source/ROS-Framework/interfaces/topics/Understanding-ROS2-Topics/Understanding-ROS2-Topics.rst)

参考链接保留对应的官方 `lyrical` 分支，操作时仍以实际环境和官方说明为准。
