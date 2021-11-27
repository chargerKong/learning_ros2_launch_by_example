# launch parameters 的作用

通过在Node中添加parameter，把参数以键值对的方式发送给相应的Node

> 注意：在ROS2中，参数服务器是相对于节点的，而不是总的一个参数服务器。因此需要使用node->get_parameters来获取



# parameters 效果

通过launch文件中的Node，把Node的parameter传入给相应的节点

```
ros2 launch learning_ros2_launch_by_example node_paramters.launch.py 
```

在

```
[learning_ros2_launch_by_example_node-1] [INFO] [1637980712.930372230] [parameter_test]: Publishing Topic name: 0 
```

之前，打印了从参数服务器接受到的值

```
[learning_ros2_launch_by_example_node-1] [INFO] [1637980711.930034327] [parameter_test]: Capture the param, test_param_value: A_param_value
```

# 使用示例

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='parameter_test',
            output="screen",
            parameters=[{"test_param_value": "A_param_value"}]
        ),
    ])
```



在对应的节点中，需要声明parameter，然后再进行get

```c++
	  this->declare_parameter<std::string>("test_param_value");
      this->get_parameter_or<std::string>("test_param_value", test_param_value, "");
      if (test_param_value.compare("") != 0) {
        RCLCPP_INFO(this->get_logger(), "Capture the param, test_param_value: %s", test_param_value.c_str());
      }
```

