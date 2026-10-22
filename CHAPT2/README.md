# 第二章：ROS 2 C++ / Python 节点与功能包

[首页](../README.md) · [第一章](../CHAPT1/README.md) · [Python 包排错](TROUBLESHOOTING.md) · [C++ 实验](CPP_NODE.md) · [类、继承与日志排错](OOP_NODES.md)

本章记录节点创建、功能包构建、Python 类与继承、ROS 2 初始化及日志输出。源码统一放在 `chapt2_ws/src`，截图和排错留在本章，按内容持续补充。

## 已有结果与验证边界

- Python 日志节点与 C++ 节点已由 Ubuntu 截图确认构建和启动成功。
- `person_node` 从普通 Python 类示例推进到继承 `rclpy.node.Node`，成功输出节点日志并进入 spin。
- `writer_node` 已验证父类初始化、方法重写和直接继承父类 `eat()`。历史截图分别展示重写版本的一条完整日志，以及直接继承版本的两条日志。
- 本次按最后要求实现“复用父类 eat、输出一条完整日志”：父类支持返回文本，子类不重写 eat，最后统一输出。此修改已进行本地逻辑检查；该版本的 Ubuntu/ROS 2 运行截图仍待补充。
- C++ 包清单补充 `rclcpp` 依赖，避免依赖解析只依靠本机已经安装的库。

早期 Python 包运行证据：

![Python 节点启动成功](images/python-node-success.png)

## 源码导航

| 文件 | 内容 |
| --- | --- |
| [Python 包配置](chapt2_ws/src/demo_python_pkg/setup.py) | python_node、person_node、writer_node 三个入口 |
| [Python 包清单](chapt2_ws/src/demo_python_pkg/package.xml) | rclpy 依赖与 ament_python 构建类型 |
| [Python 脚本安装配置](chapt2_ws/src/demo_python_pkg/setup.cfg) | 脚本安装到 lib/demo_python_pkg |
| [python_node.py](chapt2_ws/src/demo_python_pkg/demo_python_pkg/python_node.py) | 创建节点、输出 INFO/WARN 日志 |
| [person_node.py](chapt2_ws/src/demo_python_pkg/demo_python_pkg/person_node.py) | Node 继承、姓名年龄属性、eat 方法 |
| [writer_node.py](chapt2_ws/src/demo_python_pkg/demo_python_pkg/writer_node.py) | PersonNode 继承、作品属性与组合日志 |
| [Python 包测试模板](chapt2_ws/src/demo_python_pkg/test/) | 原始生成的 lint 检查模板；未声称 ROS 测试全部通过 |
| [C++ CMake 配置](chapt2_ws/src/demo_cpp_pkg/CMakeLists.txt) | rclcpp::rclcpp 链接及 install(TARGETS) |
| [C++ 包清单](chapt2_ws/src/demo_cpp_pkg/package.xml) | ament_cmake 与 rclcpp 依赖 |
| [cpp_node.cpp](chapt2_ws/src/demo_cpp_pkg/src/cpp_node.cpp) | C++ 节点初始化、日志与 spin |
| [早期独立 Python 示例](ros2_python_node.py) · [C++ 示例](ros2_cpp_node.cpp) · [配置备份](CMakeLists.txt.back) | 保留学习过程；备份不是活动 CMakeLists.txt |

```text
CHAPT2/
├── chapt2_ws/
│   └── src/
│       ├── demo_cpp_pkg/
│       │   ├── CMakeLists.txt
│       │   ├── package.xml
│       │   └── src/cpp_node.cpp
│       └── demo_python_pkg/
│           ├── setup.py
│           ├── setup.cfg
│           ├── package.xml
│           ├── resource/demo_python_pkg
│           └── demo_python_pkg/
│               ├── __init__.py
│               ├── python_node.py
│               ├── person_node.py
│               └── writer_node.py
├── TROUBLESHOOTING.md
├── CPP_NODE.md
├── OOP_NODES.md
└── images/
```

旧版直接位于 `CHAPT2/demo_python_pkg` 的包已迁移到上面的工作空间，避免 colcon 发现两个同名包。原始截图中的旧路径保留作历史证据。

## 构建与运行

在已安装相应依赖的 Ubuntu Bash 中，从仓库根目录执行：

```bash
cd CHAPT2/chapt2_ws
source /opt/ros/lyrical/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon list
colcon build
source install/setup.bash
ros2 pkg prefix demo_cpp_pkg
ros2 pkg prefix demo_python_pkg
```

`rosdep` 命令要求已经安装并初始化 rosdep；依赖已齐全时可直接构建。构建成功后分别运行，停止当前节点后再启动下一个：

```bash
ros2 run demo_cpp_pkg cpp_node
ros2 run demo_python_pkg python_node
ros2 run demo_python_pkg person_node
ros2 run demo_python_pkg writer_node
```

每个新终端都需加载 ROS 2 及当前工作空间环境。构建应从 `chapt2_ws` 根目录执行，不在包目录或 install 中构建。日志打印一次后进入 spin；当前没有周期性定时器或话题通信。

## 日志与退出

设置格式需在启动进程前完成：

```bash
export RCUTILS_CONSOLE_OUTPUT_FORMAT='[{function_name}:{line_number}]:{message}'
```

恢复默认格式使用 `unset RCUTILS_CONSOLE_OUTPUT_FORMAT`，随后重新启动节点。注意 FORMAT 不要写成 FROMAT。

按 Ctrl+C 停止当前基础示例时，可能出现 KeyboardInterrupt 堆栈。它与启动失败不同；整洁退出的可选处理见 [类与节点记录](OOP_NODES.md)。目前上传的生命周期保持原练习方式，尚未统一改成上下文管理形式。

## 排错与下一步

包注册、XML、入口逗号等见 [Python 排错](TROUBLESHOOTING.md)；CMake 版本差异与安装关键字见 [C++ 排错](CPP_NODE.md)；模块位置、super、作用域、参数和单条日志见 [OOP_NODES.md](OOP_NODES.md)。

源码来自本次提供的 embedded-learning 文件夹，排除 build/install/log、缓存、二进制和机器配置。归档时仅按前面要求调整单条日志设计，并补齐 C++ rclcpp 清单依赖；原始截图不因此改写。下一步补充当前版本在 Ubuntu 的复测，再学习发布/订阅、服务、参数和 Launch；机械臂与 VLA 仍为后续方向。
