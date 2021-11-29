本文介绍如何去模拟一个shell的命令

# ExecuteProcess 介绍

通过ExecuteProcess的cmd命令，可以十分快速简单的模拟终端的命令，终端的空格用逗号分开即可，例如

```
ros2 run learning_ros2_launch_by_example learning_ros2_launch_by_example_node
```

需要写为

```
cmd=["ros2", "run", "learning_ros2_launch_by_example",  "learning_ros2_launch_by_example_node"],
```

**当然，这不仅限于ROS2的指令，任何操作系统的指令都可以尝试去运行，比如执行一个python脚本**

```
cmd=['python3', 'path/to/your_script.py']
```



# 使用实例

以下注释的内容，即Node启动方式和ExecuteProcess启动的方式效果是一样的，启动被注释的Node就是在终端输入以下命令

```
ros2 run learning_ros2_launch_by_example learning_ros2_launch_by_example_node --ros-args -r __node:=learning_ros2_launch_by_example_node
```



```python
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Node(
        #     package='learning_ros2_launch_by_example',
        #     executable='learning_ros2_launch_by_example_node',
        #     name='learning_ros2_launch_by_example_node',
        #     output="screen",
        # ),
        ExecuteProcess(
            cmd=["ros2", "run", "learning_ros2_launch_by_example", "learning_ros2_launch_by_example_node", "--ros-args", "-r", "__node:=learning_ros2_launch_by_example_node"],
            output="screen"
        )
    ])
```

# 运行示例

```
ros2 launch learning_ros2_launch_by_example shell_command_simulator.launch.py
```

输出

```
[INFO] [launch]: All log files can be found below /home/kong/.ros/log/2021-11-29-11-01-08-788521-r9000x-2021-11740
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [ros2-1]: process started with pid [11742]
[ros2-1] [INFO] [1638154869.036260971] [For arguements]: The number of arguments is 4， They are
[ros2-1] [INFO] [1638154869.036311116] [For arguements]: --ros-args
[ros2-1] [INFO] [1638154869.036317751] [For arguements]: -r
[ros2-1] [INFO] [1638154869.036322500] [For arguements]: __node:=learning_ros2_launch_by_example_node
...
```

成功执行了我们期望的输出