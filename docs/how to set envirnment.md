一些程序在启动之前需要从环境变量去读取一些值，除了在终端直接设置之外，也可以在launch文件中直接设定

# SetEnvironmentVariable和EnvironmentVariable

一个是设置环境变量，一个获取环境变量，可以参考如下写法。

SetEnvironmentVariable 也是一个action， 因此可以直接写在LaunchDescription里面

```python
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, ExecuteProcess
from launch.substitutions import EnvironmentVariable

def generate_launch_description():

    return LaunchDescription([
        SetEnvironmentVariable('FOOBAR', 'Goodbye, World'),
        ExecuteProcess(
            cmd=['echo', EnvironmentVariable('FOOBAR')],
            additional_env={'FOOBAR': 'Hello, World'},
            output='screen'),
    ]
```



# 输出结果

```
ros2 launch learning_ros2_launch_by_example environment_setting.launch.py
```

可以看见，输出的环境变量已经变为

```
[echo-1] Goodbye, World
```



# os.environ

除了launch文件，也可以通过Python本身的语法来设置环境变量。当然他只能写在LaunchDescription之外

```python
import os

from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, ExecuteProcess
from launch.substitutions import EnvironmentVariable
def generate_launch_description():
    
    os.environ["FOOBAR"] = "Goodbye, World"
    return LaunchDescription([
        # SetEnvironmentVariable('FOOBAR', 'Goodbye, World'),
        ExecuteProcess(
            cmd=['echo', EnvironmentVariable('FOOBAR')],
            additional_env={'FOOBAR': 'Hello, World'},
            output='screen'),
    ])
```

效果和通过 SetEnvironmentVariable的一致



# 系统内置的环境变量

一些关于log的环境变量设定的含义，可以参考https://docs.ros.org/en/foxy/Tutorials/Logging-and-logger-configuration.html