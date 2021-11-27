从之前的介绍我们可以知道，Launch文件的变量可以通过LaunchConfiguration 直接从命令行传递，并且可以将其直接传进Node。如果现在需要根据传入的变量做一些其他设定，那么就需要获取LaunchConfiguration示例中的context，以下是获取内容的其中一种方式

# 如何实现获取

我们在以往的LaunchDescription中返回的是OpaqueFunction，OpaqueFunction返回的是一个Python List，其中可以包括多个结点，多个Action

在这个函数里面，通过对LaunchConfiguration函数调用perform(context)，即可获得没有封装到LaunchConfiguration的从命令行传入的值

```python
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import OpaqueFunction

def launch_setup(context):
    test_var = LaunchConfiguration("test_var", default="A_param_value")
    print("test_var: {}\nthe type is: {}".format(test_var, test_var.__class__))
    test_var_context = test_var.perform(context)
    print("test_var_context: {}\nthe type is: {}".format(test_var_context, test_var_context.__class__))
    return [
        # DeclareLaunchArgument(
        #     "test_var",
        #     default_value=test_var,
        #     description="This is the test variable to be sent into node parameter"
        # ),

        # Node(
        #     package='learning_ros2_launch_by_example',
        #     executable='learning_ros2_launch_by_example_node',
        #     name='parameter_test',
        #     output="screen",
        #     parameters=[{"test_param_value": test_var}]
        # ),
    ]

def generate_launch_description():
    return LaunchDescription([
        OpaqueFunction(function=launch_setup),
    ])
```

# 运行效果

```
test_var: <launch.substitutions.launch_configuration.LaunchConfiguration object at 0x7fe5cf836e80>
the type is: <class 'launch.substitutions.launch_configuration.LaunchConfiguration'>
test_var_context: new_var
the type is: <class 'str'>
```

可以看见，在之前和之后的对象内容分别为LaunchConfiguration的对象示例和str的对象示例。拿到了str的对象实例，我们就可以方便的进行Python的其他操作
