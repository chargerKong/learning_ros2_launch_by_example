通过LaunchConfiguation设置过的变量可以通过命令行的方式进行赋值，那我们如何得知有什么参数需要被设置呢？

# DeclareLaunchArgument作用

说明本launch文件需要配置的文件以及相应的变量含义



# 使用效果

```
ros2 launch learning_ros2_launch_by_example launch_declare_launch_argument.launch.py --show-args
```

输出

```
Arguments (pass arguments as '<name>:=<value>'):

    'test_var':
        This is the test variable to be sent into node parameter
        (default: LaunchConfig('test_var'))
```

通过--show-args 我们就可以看见 此launch 文件的配置参数，他的默认值和他的具体含义



# 如何实现

```python
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    test_var = LaunchConfiguration("test_var", default="A_param_value")
    return LaunchDescription([
        DeclareLaunchArgument(
            "test_var",
            default_value=test_var,
            description="This is the test variable to be sent into node parameter"
        ),
        
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='parameter_test',
            output="screen",
            parameters=[{"test_param_value": test_var}]
        ),
    ])
```

在LaunchDescription的实参，列表中添加DeclareLaunchArgument，按照格式变量名，默认值和描述文字进行声明即可