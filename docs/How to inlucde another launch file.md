# IncludeLaunchDescription 介绍

此函数的功能是加载一个其他的launch文件，利用此功能可以把一个复杂的启动系统简单化



# 使用示例

IncludeLaunchDescription 和Node一样放到LaunchDescription 当中即可，在这里我们include的是一个Python启动文件, 在入参的list中，需要添加的是路径，ThisLaunchFileDir()，就是一个路径

对于被include的文件的启动参数，可以通过launch_arguments 传入，同时在此文件也要声明对应变量的LaunchConfiguration

```python
import launch
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    inlucde_other_file = LaunchConfiguration("inlucde_other_file", default="true")
    test_var = LaunchConfiguration('test_var', default="test_var_2")
    return launch.LaunchDescription([
        launch.actions.IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [ThisLaunchFileDir(), '/launch_declare_launch_argument.launch.py']
            ),
            condition=IfCondition(inlucde_other_file),
            launch_arguments={'test_var': test_var}.items(),
        )
    ])
```

# 启动示例

```
ros2 launch learning_ros2_launch_by_example include_launch_script.launch.py 
```

可以看见输出

```
[learning_ros2_launch_by_example_node-1] [INFO] [1638153610.256244345] [parameter_test]: Capture the param, test_param_value: test_var_2
```

说明参数传递是成功的