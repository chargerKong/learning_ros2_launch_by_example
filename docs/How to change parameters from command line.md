# LaunchConfiguration 介绍

通过sudo apt install的仓库都是别人打包好的代码，倘若此时需要修改launch文件中的参数，直接修改文件内容是不合适的，基于代码开发的开闭原则来说是不合适的。一般来说，此时我们都可以通过在命令行，在启动launch的时候，添加修改参数的命令即可

# 使用示例

```
ros2 launch learning_ros2_launch_by_example launch_configuration.launch.py
```

可以看见，现在默认的值`A_param_value`

```
[learning_ros2_launch_by_example_node-1] [INFO] [1637983283.608953683] [parameter_test]: Capture the param, test_param_value: A_param_value
```



我们可以通过命令行对参数进行重新配置，语法为`var:=value`

```
ros2 launch learning_ros2_launch_by_example launch_configuration.launch.py test_var:=new_val
```

可以看见，默认值已经被我们修改

```
[learning_ros2_launch_by_example_node-1] [INFO] [1637983302.558026551] [parameter_test]: Capture the param, test_param_value: new_val
```



# 如何实现

```python
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    test_var = LaunchConfiguration("test_var", default="A_param_value")
    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='parameter_test',
            output="screen",
            parameters=[{"test_param_value": test_var}]
        ),
    ])
```

通过launch中的LaunchConfiguration函数，他可以从命令行接受到参数，我们把接收到的参数直接传到Node的parameter中。



**但是有一个问题是，在我们不查看源代码的情况下，是如何得知有什么参数，并且参数有什么作用？**

