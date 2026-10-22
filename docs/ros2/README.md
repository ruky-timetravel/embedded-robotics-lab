# ROS 2 学习入口

跟随鱼香 ROS 机器人《ROS 2机器人开发从入门到实践》，在已有 C++ / Linux 基础上学习。记录按章节组织，不按学习日期建立目录。当前环境为 VMware Ubuntu，ROS 2 发行版在终端中显示为 Lyrical。

## 章节导航

| 章节 | 内容与材料 | 当前证据 |
| --- | --- | --- |
| [CHAPT1：Ubuntu、编程与 ROS 2 初体验](../../CHAPT1/README.md) | C/C++、Python、CMake；[小海龟实验](../../CHAPT1/TURTLESIM.md)；[Ubuntu 截图](../../CHAPT1/EVIDENCE.md)；[排错记录](../../CHAPT1/TROUBLESHOOTING.md) | 已看到 TurtleSim 窗口与节点图；保留 CMake 拼写错误截图，尚未补充当前源码完整构建验收截图 |
| [CHAPT2：C++ / Python 节点与功能包](../../CHAPT2/README.md) | `rclpy`、`rclcpp`、日志、包目录、入口、CMake 与 `colcon`；[Python 排错](../../CHAPT2/TROUBLESHOOTING.md) · [C++ 排错与截图](../../CHAPT2/CPP_NODE.md) | Python 包识别与启动已确认；C++ 包也已编译、安装并通过 `ros2 run` 打印日志，新包完整源码待同步 |

## 从当前结果继续

Python 功能包已走通：

```text
package.xml 与 setup.py → colcon build → source install/setup.bash
→ ros2 run demo_python_pkg python_node → INFO/WARN 日志
```

C++ 包也已完成 `colcon build`、包前缀查询与 `ros2 run demo_cpp_pkg cpp_node`，过程见 [C++ 实验记录](../../CHAPT2/CPP_NODE.md)。这些结果验证节点启动和日志输出。后续同步新 C++ 包源码，再完成发布/订阅、服务、参数和 Launch 练习。TurtleSim 的运动与消息对应关系仍需要保存实际消息样本和自己的解释。

- [总体进度与证据](../progress.md)
- [ROS 2、机械臂、具身智能、VLA 与 π0.7 方向目标](roadmap.md)
- [新增章节时使用的模板](../chapter-record-template.md)

## 环境约定

每个新终端先加载当前发行版的环境：

```bash
source /opt/ros/lyrical/setup.bash
```

构建自定义功能包后，还要在工作空间根目录执行 `source install/setup.bash`。不要将旧教程中的 Humble 加载路径直接套到当前 Lyrical 环境。Ubuntu 具体版本沿用已有用户报告，完整系统版本输出和工具版本仍按实际记录补充。

## 参考

- [课程视频：1.3 运行你的第一个机器人](https://www.bilibili.com/video/BV1iE421w7d5/)
- [ROS 2 Lyrical 官方文档](https://docs.ros.org/en/lyrical/)
- [Lyrical 官方 TurtleSim 教程源文件](https://github.com/ros2/ros2_documentation/blob/lyrical/source/Get-Started/Introducing-Turtlesim/Introducing-Turtlesim.rst)

笔记由 AI 辅助整理，源码和截图来自学习过程。运行结果、待实践内容和未来目标按各章证据分别标注。
