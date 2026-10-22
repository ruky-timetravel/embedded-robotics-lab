# 第二章排错记录：从模块导入失败到 Python 节点启动

[本章入口](README.md) · [功能包源码](demo_python_pkg/) · [成功截图](images/python-node-success.png)

这次排查涉及多个问题。先修复源码位置与入口，再核对构建目录、安装索引和环境，最终通过修正 `package.xml` 的 XML 闭合标签恢复 ROS 2 包识别。下面按排查顺序记录，当前上传的源码已经包含这些修正。

## 1. 启动脚本存在，但 Python 模块找不到

**现象：** 在安装目录执行 `./python_node`，出现：

```text
ModuleNotFoundError: No module named 'demo_python_pkg.python_node'
```

![模块导入失败](images/python-module-not-found.png)

检查文件后发现，`python_node.py` 曾位于外层功能包目录；`setup.py` 的入口还曾写为 `demo_python_pkg.ros2.python_node:main`，与实际模块结构不一致。

![源码布局与配置检查](images/python-package-config.png)

**修复：** 把节点放在内层 Python 包：

```text
demo_python_pkg/                       ← ROS 2 功能包目录
├── setup.py
├── setup.cfg
├── package.xml
├── resource/demo_python_pkg
└── demo_python_pkg/                   ← Python 可导入包
    ├── __init__.py
    ├── py.typed
    └── python_node.py
```

入口改为：

```python
'python_node = demo_python_pkg.python_node:main'
```

左侧是可执行入口名；右侧是 `模块:函数`。当前代码见 [setup.py](demo_python_pkg/setup.py) 和 [python_node.py](demo_python_pkg/demo_python_pkg/python_node.py)。应修改源码并重新构建，安装目录里的启动脚本由构建生成。

## 2. 在安装目录构建，发现 0 个包

**现象：** 当前目录为 `CHAPT2/install/demo_python_pkg/lib/demo_python_pkg`，执行 `colcon build`，得到 `Summary: 0 packages finished`。

![构建目录错误](images/wrong-build-directory.png)

**原因：** 构建起点位于生成的安装目录，该处没有需要构建的源码包。

**修复：** 返回工作空间根目录再构建。本章工作空间是 `CHAPT2`，包直接放在这个目录下：

```bash
cd ~/embedded-learning/CHAPT2
source /opt/ros/lyrical/setup.bash
colcon list
colcon build --packages-select demo_python_pkg
source install/setup.bash
```

克隆本仓库时，将第一行改为自己实际的仓库路径下的 `CHAPT2`。后续运行使用 `ros2 run demo_python_pkg python_node`。

![回到根目录后构建成功但仍找不到包](images/package-not-found.png)

这一步的 `1 package finished` 只说明构建任务完成，之后仍需验证 ROS 包发现和 Python 导入。

## 3. 核对 ament 索引与环境加载脚本

**索引拼写：** 历史配置中曾写成 `share/amet_index/resource_index/packages`，`ament` 少了 `n`。修正为：

```python
data_files=[
    ('share/ament_index/resource_index/packages',
     ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
],
```

**脚本拼写：** 一次手动重试还把 `setup.bash` 写成了 `setup.bush`，所以出现“没有那个文件或目录”。

![环境加载脚本拼写错误](images/setup-script-typo.png)

应在 `CHAPT2` 执行 `source install/setup.bash`。这个拼写错误解释了该次加载失败，但不能解释先前正确加载 `.bash` 后仍找不到包的现象。

## 4. 注册文件存在，为什么仍找不到包

进一步收集的证据：

```bash
colcon list
grep -n -A6 'data_files' demo_python_pkg/setup.py
find install -path '*/resource_index/packages/*' -print
printf 'AMENT_PREFIX_PATH=%s\n' "$AMENT_PREFIX_PATH"
```

![包识别与环境诊断](images/colcon-package-diagnosis.png)

截图显示：

- 包标记文件已存在于正确的 `ament_index/resource_index/packages` 目录。
- `colcon list` 类型仍为普通 `(python)`，未识别成 `(ros.ament_python)`。
- 加载后 `AMENT_PREFIX_PATH` 只有 `/opt/ros/lyrical`，未包含本章包的安装前缀。

因此继续检查包清单，而不是仅凭标记文件存在就判断修复完成。

## 5. 关键修复：闭合 `package.xml` 的依赖标签

学习者发现依赖写成了：

```xml
<depend>rclpy<depend>
```

这不是合法闭合的 XML。修正为：

```xml
<depend>rclpy</depend>
```

同时保留正确的构建类型：

```xml
<export>
  <build_type>ament_python</build_type>
</export>
```

原始配置全图见[配置检查截图](images/python-package-config.png)，当前修正版见 [package.xml](demo_python_pkg/package.xml)。修改并保存后，重新运行：

```bash
cd ~/embedded-learning/CHAPT2
source /opt/ros/lyrical/setup.bash
colcon list
colcon build --packages-select demo_python_pkg
source install/setup.bash
ros2 pkg prefix demo_python_pkg
ros2 run demo_python_pkg python_node
```

最终截图中，包类型恢复为 `(ros.ament_python)`，构建显示 `1 package finished`，节点成功打印两条“你好”日志。

![最终构建与运行成功](images/python-node-success.png)

`colcon-ros` 识别 ROS 包时会解析 `package.xml`；清单解析失败可使 ROS 包识别失败，而普通 Python 包识别仍可能成功。此处结合错误标签、前后包类型和最终运行结果定位问题。曾考虑过扩展缺失的可能性，但没有安装扩展的修复证据，因此不把它记为本次原因或已执行步骤。

实现参考：[colcon-ros 包识别](https://github.com/colcon/colcon-ros/blob/master/colcon_ros/package_identification/ros.py)、[ament_python 构建与环境钩子](https://github.com/colcon/colcon-ros/blob/master/colcon_ros/task/ament_python/build.py)、[ROS 2 官方 Python 包配置示例](https://github.com/ros2/examples/blob/lyrical/rclpy/topics/minimal_publisher/setup.py)。

## 6. 日志格式没有变化，如何恢复默认

历史命令把变量写成了 `RCUTILS_CONSOLE_OUTPUT_FROMAT`，正确拼写是 `FORMAT`。

![日志环境变量拼写错误](images/log-format-typo.png)

先按 `Ctrl+C` 停止节点，在同一终端中设置并重新运行：

```bash
export RCUTILS_CONSOLE_OUTPUT_FORMAT='[{function_name}:{line_number}]:{message}'
ros2 run demo_python_pkg python_node
```

恢复默认格式：

```bash
unset RCUTILS_CONSOLE_OUTPUT_FORMAT
ros2 run demo_python_pkg python_node
```

可额外用 `unset RCUTILS_CONSOLE_OUTPUT_FROMAT` 清除误写的变量。若将设置写入了 `~/.bashrc`，也需修改对应行；当前没有证据表明已写入。格式变量参考 [rcutils 日志实现](https://github.com/ros2/rcutils/blob/lyrical/src/logging.c)。

## 结果与尚未覆盖的内容

`INFO` 和黄色 `WARN` 都来自本章源码主动输出。节点随后进入 `rclpy.spin(node)`，等待事件；它没有定时器，不会周期性打印。按 `Ctrl+C` 可停止。

本次已验证 Python 功能包在学习者 Ubuntu 环境中启动成功，证据为上方真实终端截图。C++ 节点目前只保留源码与 CMake 备份，尚无运行成功证据。上传源码以修复后的当前文件为准，排错截图保留修复前后状态。
