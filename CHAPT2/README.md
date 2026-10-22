# 第二章：ROS 2 节点与 Python 功能包

[返回仓库首页](../README.md) · [返回第一章](../CHAPT1/README.md) · [本章排错记录](TROUBLESHOOTING.md)

本章从直接运行 Python 节点开始，再把节点封装为 ROS 2 Python 功能包，通过 `colcon build` 构建并使用 `ros2 run` 启动。学习重点是理清源码目录、Python 导入入口、ROS 2 包注册和终端环境之间的关系。

## 已完成的实验

最后的终端截图确认：

- `colcon list` 将 `demo_python_pkg` 识别为 `ros.ament_python`。
- `colcon build --packages-select demo_python_pkg` 显示 `1 package finished`。
- 加载 `install/setup.bash` 后，`ros2 run demo_python_pkg python_node` 成功输出 `INFO` 与 `WARN` 两条“你好”日志。

![Python 功能包识别、构建与节点运行成功](images/python-node-success.png)

黄色 `WARN` 是源码主动调用 `warning('你好')` 的结果，不能据此判断节点启动失败。日志打印一次之后，程序进入 `rclpy.spin(node)` 等待事件，不会自动重复打印。

## 学习要点

- `rclpy.init()` 初始化 ROS 2，`Node('python_node')` 创建节点，`get_logger()` 输出日志。
- `rclpy.spin(node)` 让节点处理回调和事件；当前示例尚未创建发布者、订阅者或定时器。
- 外层 `demo_python_pkg/` 是 ROS 2 功能包目录，内层同名目录是 Python 可导入的包。
- `setup.py` 的入口将命令名映射到 `模块:函数`；`package.xml` 声明包信息、依赖与构建类型。
- 构建成功、包能被 ROS 2 发现、Python 模块能被导入，是需要分别确认的环节。

## 文件导航

| 文件 | 作用 |
| --- | --- |
| [ros2_python_node.py](ros2_python_node.py) | 可直接用 `python3` 执行的节点示例，带 `__main__` 入口判断 |
| [demo_python_pkg/demo_python_pkg/python_node.py](demo_python_pkg/demo_python_pkg/python_node.py) | 安装为功能包的节点实现，提供 `main()` |
| [demo_python_pkg/setup.py](demo_python_pkg/setup.py) | Python 包发现、ROS 2 注册文件安装与 `console_scripts` 入口 |
| [demo_python_pkg/setup.cfg](demo_python_pkg/setup.cfg) | 将启动脚本安装到 `lib/demo_python_pkg` |
| [demo_python_pkg/package.xml](demo_python_pkg/package.xml) | 包名、`rclpy` 依赖及 `ament_python` 构建类型 |
| [demo_python_pkg/resource/demo_python_pkg](demo_python_pkg/resource/demo_python_pkg) | 安装到 ament 索引的包标记文件，内容可以为空 |
| [demo_python_pkg/demo_python_pkg/__init__.py](demo_python_pkg/demo_python_pkg/__init__.py) | 标记 Python 包 |
| [demo_python_pkg/test/](demo_python_pkg/test/) | 创建功能包时生成的检查模板；本章不据此声称所有测试已通过 |
| [ros2_cpp_node.cpp](ros2_cpp_node.cpp) | 使用 `rclcpp` 的 C++ 节点源码，当前未附运行验收截图 |
| [CMakeLists.txt.back](CMakeLists.txt.back) | C++ 示例的 CMake 配置备份；并非 CMake 默认读取的活动配置文件 |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | 从模块导入错误到包识别恢复的完整排错记录 |

关键源码结构：

```text
CHAPT2/
├── ros2_python_node.py
├── ros2_cpp_node.cpp
├── CMakeLists.txt.back
└── demo_python_pkg/
    ├── package.xml
    ├── setup.py
    ├── setup.cfg
    ├── resource/
    │   └── demo_python_pkg
    └── demo_python_pkg/
        ├── __init__.py
        ├── py.typed
        └── python_node.py
```

## 运行与复现

以下命令在 Ubuntu 终端中执行，环境沿用学习时的 ROS 2 Lyrical。`CHAPT2` 就是本章的 colcon 工作空间，功能包直接放在本章目录下。应在本章根目录构建，避免进入 `install/` 中构建或修改生成文件。

### 直接运行节点

从仓库根目录开始：

```bash
cd CHAPT2
source /opt/ros/lyrical/setup.bash
python3 ros2_python_node.py
```

观察日志后按 `Ctrl+C` 停止，再继续构建练习。

### 构建并运行功能包

在 `CHAPT2` 目录执行：

```bash
source /opt/ros/lyrical/setup.bash
colcon list
colcon build --packages-select demo_python_pkg
source install/setup.bash
ros2 pkg prefix demo_python_pkg
ros2 run demo_python_pkg python_node
```

检查结果：

1. `colcon list` 中的类型应为 `(ros.ament_python)`。
2. 构建应结束于 `1 package finished`，并检查是否另有错误。
3. `ros2 pkg prefix` 应输出当前工作空间中该包的安装前缀。
4. 节点打印 `INFO` 和 `WARN` 的“你好”日志后等待事件。

打开新终端后，需要重新加载 ROS 2 及本工作空间的环境。`source install/setup.bash` 依赖当前目录，运行时应位于 `CHAPT2`。

### 自定义与恢复日志格式

先停止正在运行的节点，再在同一个终端设置格式并重启：

```bash
export RCUTILS_CONSOLE_OUTPUT_FORMAT='[{function_name}:{line_number}]:{message}'
ros2 run demo_python_pkg python_node
```

恢复默认格式时，先停止节点，再执行：

```bash
unset RCUTILS_CONSOLE_OUTPUT_FORMAT
ros2 run demo_python_pkg python_node
```

这里的 `FORMAT` 不能写成 `FROMAT`。环境变量在进程启动时被继承，因此应在修改后重新启动节点。

## 关键配置

入口配置：

```python
'python_node = demo_python_pkg.python_node:main'
```

左边 `python_node` 是 `ros2 run` 使用的可执行入口名；右边 `demo_python_pkg.python_node` 对应内层包中的 `python_node.py`；`:main` 表示调用其中的 `main()`。

ROS 2 注册路径：

```python
('share/ament_index/resource_index/packages',
 ['resource/' + package_name])
```

包清单中的依赖和构建类型：

```xml
<depend>rclpy</depend>
<export>
  <build_type>ament_python</build_type>
</export>
```

这些配置与源码目录共同决定包的发现、安装和启动，不能只检查其中一项。

## 排错速查

| 现象 | 本次排查中的原因或证据 | 修复或检查 |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'demo_python_pkg.python_node'` | 节点曾放在外层目录；入口还曾多写 `.ros2` | 将节点放入内层 Python 包，并让入口与实际模块名一致 |
| `Summary: 0 packages finished` | 在 `install/.../lib/demo_python_pkg` 中执行了构建 | 返回本章工作空间根目录构建 |
| `Package 'demo_python_pkg' not found` | 曾有 `amet_index` 拼写错误；之后虽已存在注册文件，包仍被识别为普通 `(python)` | 修正 `ament_index`，继续检查 `package.xml`，不能以注册文件存在作为全部修复依据 |
| `colcon list` 显示 `(python)`，环境前缀只有 `/opt/ros/lyrical` | 依赖标签曾写成 `<depend>rclpy<depend>`，XML 不合法；修正后类型恢复为 `ros.ament_python` | 改为 `<depend>rclpy</depend>`，保存、重新构建并加载环境 |
| `install/setup.bush: 没有那个文件或目录` | 加载脚本扩展名拼错 | 使用 `source install/setup.bash` |
| 日志格式保持默认 | 变量名写成 `RCUTILS_CONSOLE_OUTPUT_FROMAT` | 改为 `RCUTILS_CONSOLE_OUTPUT_FORMAT`，重启节点 |

完整的现象、定位依据和修复顺序见[本章排错记录](TROUBLESHOOTING.md)。

<details>
<summary>查看排错过程截图</summary>

节点模块导入失败：

![Python 模块未找到](images/python-module-not-found.png)

源码布局和包配置检查：

![Python 包配置检查](images/python-package-config.png)

注册文件存在，但包识别类型和环境前缀异常：

![colcon 包识别与环境诊断](images/colcon-package-diagnosis.png)

日志格式环境变量拼写错误：

![日志格式变量拼写错误](images/log-format-typo.png)

</details>

## 已知限制与下一步

Python 功能包已由用户的 Ubuntu 终端运行截图确认启动成功；本次仓库整理不等同于在其他系统重新验证 ROS 2 环境。C++ 节点目前仅保留源码和 CMake 备份，尚未整理为独立 `ament_cmake` 功能包，也没有对应运行成功截图。

节点示例还没有话题通信、服务、动作、机械臂接口或 VLA 推理。下一步先完成 Python/C++ 节点的发布与订阅练习，再连接机器人描述、仿真、机械臂控制和具身智能方向。
