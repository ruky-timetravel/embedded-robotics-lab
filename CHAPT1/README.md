# 第一章：Ubuntu、编程与 ROS 2 初体验

[返回仓库首页](../README.md) · [进入第二章](../CHAPT2/README.md) · [小海龟实验](TURTLESIM.md) · [本章排错记录](TROUBLESHOOTING.md)

本章把 Ubuntu 终端操作、C/C++ 与 Python 的最小程序、CMake 构建，以及 turtlesim 小海龟实验放在一起。目标是先走通“编辑源码 → 执行或构建 → 观察输出”，为后续编写 ROS 2 节点做准备。

学习参考：[课程视频](https://www.bilibili.com/video/BV1iE421w7d5)。本仓库记录个人代码、实验现象与排错过程，章节按实际练习内容组织。

## 学习要点

- 分清源码、可执行文件和构建产物；在源码目录配置项目，用独立目录存放生成文件。
- Python 可以由解释器执行；C 与 C++ 需要先编译，再运行生成的程序。
- CMake 的 `add_executable(learn_cmake hello_word.cpp)` 把源码与目标程序关联起来。
- 在 turtlesim 中认识节点、话题和消息，观察键盘输入与海龟运动之间的关系。
- 理解 `if __name__ == '__main__':` 如何控制 Python 文件的直接执行入口。

## 文件导航

| 文件 | 内容 |
| --- | --- |
| [hello_word.py](hello_word.py) | Python 最小输出示例，打印 `hello word!` |
| [hello_word.cpp](hello_word.cpp) | C++ 最小输出示例，打印 `hello word` |
| [main.c](main.c) | 用目标速度与实际速度之差演示变量、减法和输出，预期输出 `Speed error: 20` |
| [CMakeLists.txt](CMakeLists.txt) | 生成 `learn_cmake` 目标的最小 CMake 配置 |
| [TURTLESIM.md](TURTLESIM.md) | 小海龟实验的详细操作与观察 |
| [EVIDENCE.md](EVIDENCE.md) | Ubuntu 环境与实验过程记录 |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | CMake 拼写错误等问题的现象、原因与修复 |
| [images/](images/) | Ubuntu 实验和排错截图 |

文件名沿用练习时的 `hello_word`，运行命令与实际文件名保持一致。

## 运行源码

以下示例在 Ubuntu 终端执行，先从仓库根目录进入本章。需要 Python 3、C/C++ 编译器与 CMake。

```bash
cd CHAPT1
python3 hello_word.py
```

用 CMake 构建 C++ 示例：

```bash
cmake -S . -B build/cmake
cmake --build build/cmake
./build/cmake/learn_cmake
```

单独练习 C 编译：

```bash
mkdir -p build/manual
gcc main.c -o build/manual/speed_error
./build/manual/speed_error
```

`hello_word.py` 已在本次整理所用的 Windows Python 3 环境执行，输出 `hello word!`。C/C++ 的输出仍是按源码推导的预期结果。本章保留了早期 CMake 报错截图；当前上传的配置已修正拼写，但尚未补充这份源码在 Ubuntu 重新构建后的完整终端验收截图。

## turtlesim 实验

当前学习环境使用 ROS 2 Lyrical，示例沿用该环境的安装路径。每个新终端都先加载 ROS 2 环境。

完整操作见[小海龟实验](TURTLESIM.md)，环境和过程材料见[实验记录](EVIDENCE.md)。

终端一启动海龟窗口：

```bash
source /opt/ros/lyrical/setup.bash
ros2 run turtlesim turtlesim_node
```

终端二启动键盘控制，把焦点放在该终端后按方向键：

```bash
source /opt/ros/lyrical/setup.bash
ros2 run turtlesim turtle_teleop_key
```

终端三观察节点、话题和速度消息：

```bash
source /opt/ros/lyrical/setup.bash
ros2 node list
ros2 topic list
ros2 topic echo /turtle1/cmd_vel
```

键盘操作产生速度指令；`/turtle1/cmd_vel` 中的消息可以帮助理解“输入 → 消息 → 海龟运动”的关系。停止节点时，在相应终端按 `Ctrl+C`。若环境中尚未安装 turtlesim，需要先完成与 ROS 2 发行版对应的组件安装。

### 实验截图

![Ubuntu 中的小海龟实验](images/ubuntu-turtlesim.png)

![turtlesim 节点与话题关系](images/turtlesim-graph.png)

### Python 入口语法补充

```python
if __name__ == '__main__':
    main()
```

直接运行文件时，Python 将 `__name__` 设为 `'__main__'`，于是调用 `main()`；被其他文件导入时，不会执行这里的调用。本章的 `hello_word.py` 只有一条输出语句；带此入口判断的实际示例见[第二章独立 Python 节点](../CHAPT2/ros2_python_node.py)。

![Python 入口判断的学习截图](images/python-main-guard.png)

## 排错速查

| 现象 | 已确认的原因或检查重点 | 处理 |
| --- | --- | --- |
| `Unknown CMake command "cmake_minmum_required"` | `minimum` 少了字母 `i` | 改为 `cmake_minimum_required(VERSION 3.8)`，保存后重新配置 |
| 找不到目标程序 | 运行路径应与构建目录和目标名对应 | 本章命令生成的程序为 `build/cmake/learn_cmake` |
| 按键后海龟不动 | 检查两个节点是否运行、焦点是否在键盘控制终端 | 结合节点列表与话题消息逐项检查，不能仅凭窗口判断原因 |

![CMake 命令拼写错误的原始截图](images/cmake-command-error.png)

完整过程见[本章排错记录](TROUBLESHOOTING.md)。

## 本章边界与下一步

当前练习覆盖最小程序、构建入口和 turtlesim 观察；尚未在本章编写自定义发布者、订阅者或机械臂控制程序。后续在[第二章](../CHAPT2/README.md)学习 `rclpy` 节点、Python 功能包、`colcon` 构建和环境加载，再逐步连接到机器人控制与机械臂方向。
