# ROS 2 视频学习记录

从 2026-10-21 开始，跟随鱼香 ROS 机器人《ROS 2机器人开发从入门到实践》，在已有 C++ / Linux 基础上学习。当前对应 [1.3 运行你的第一个机器人](https://www.bilibili.com/video/BV1iE421w7d5/)。

## 当前环境与进度

- 环境：VMware 中的 Ubuntu；Ubuntu 26.04.1 LTS / x86_64 沿用仓库此前用户报告。
- ROS 2：本次直接观察到终端 `printenv ROS_DISTRO` 输出 `lyrical`。
- 已看到 TurtleSim 窗口以及 `/teleop_turtle`、`/turtlesim` 的节点连接图。
- 键盘控制、话题消息的原始输出与自己的解释，继续在今日记录中补充。
- 当前以 C++ 为编程主线，Python 示例按视频需要阅读。

## 从这里继续

| 内容 | 链接 |
| --- | --- |
| 第一课：小海龟、节点与话题 | [概念、命令和练习](lesson-01-turtlesim.md) |
| 今天的真实记录与 Ubuntu 截图 | [2026-10-21](2026-10-21.md) |
| 后续学习安排 | [按验收推进的路线](roadmap.md) |
| 下次学习时复制填写 | [日志模板](daily-log-template.md) |
| 仓库总体进度 | [学习进度与证据](../progress.md) |

今天的核心关系：

```text
键盘 → /teleop_turtle → /turtle1/cmd_vel → /turtlesim → 海龟运动
```

`/teleop_turtle` 是节点，`/turtle1/cmd_vel` 是话题，`geometry_msgs/msg/Twist` 是消息类型。包名、可执行程序名、节点名分别对应不同概念，详见第一课。

## 现在做一个小练习

保留已经运行的小海龟和键盘控制程序。在 Ubuntu 的新终端执行：

```bash
source /opt/ros/lyrical/setup.bash
ros2 node list
ros2 topic list -t
ros2 topic info /turtle1/cmd_vel
ros2 topic echo /turtle1/cmd_vel
```

切回运行 `turtle_teleop_key` 的终端，按方向键，让观察终端收到速度消息。记录一组 `linear.x` 和 `angular.z`，解释它们与海龟运动的关系；按 `Ctrl+C` 结束消息观察。

## 视频与当前系统的差异

当前使用 Lyrical。若视频或旧笔记中出现 `/opt/ros/humble/setup.bash`，应以实际安装版本为准。截图已经记录该 Humble 路径不存在的报错，后续加载 `/opt/ros/lyrical/setup.bash`。

Lyrical 的 TurtleSim、节点、话题核心概念可按本课练习；遇到安装命令、包名或接口变化时，查对应发行版官方文档。本记录不将视频评论中的 ROS 1 命令用作 ROS 2 步骤。

- [课程视频：1.3 运行你的第一个机器人](https://www.bilibili.com/video/BV1iE421w7d5/)
- [ROS 2 Lyrical 官方文档](https://docs.ros.org/en/lyrical/)
- [Lyrical 官方 TurtleSim 教程源文件](https://github.com/ros2/ros2_documentation/blob/lyrical/source/Get-Started/Introducing-Turtlesim/Introducing-Turtlesim.rst)

本目录的操作说明由 AI 辅助整理；截图来自本次真实 Ubuntu 虚拟机画面。已观察到的现象、待运行的命令和学习者自己的理解分别记录。课程内容保留原作者链接。
