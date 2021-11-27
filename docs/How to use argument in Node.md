# launch Node中arguments作用

通过在Node结点中加入arguments参数，可以把arguments参数的内容直接传入main函数中

# 使用效果

```
ros2 launch learning_ros2_launch_by_example node_arguments.launch.py
```

可以看见

```c++
[INFO] [launch]: All log files can be found below /home/kong/.ros/log/2021-11-26-17-36-40-115645-r9000x-2021-59576
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [learning_ros2_launch_by_example_node-1]: process started with pid [59578]
[learning_ros2_launch_by_example_node-1] [INFO] [1637919400.235300220] [For arguements]: The number of arguments is 6， They are
[learning_ros2_launch_by_example_node-1] [INFO] [1637919400.235349389] [For arguements]: -d
[learning_ros2_launch_by_example_node-1] [INFO] [1637919400.235356513] [For arguements]: arugment_val
[learning_ros2_launch_by_example_node-1] [INFO] [1637919400.235362659] [For arguements]: --ros-args
[learning_ros2_launch_by_example_node-1] [INFO] [1637919400.235367967] [For arguements]: -r
[learning_ros2_launch_by_example_node-1] [INFO] [1637919400.235373275] [For arguements]: __node:=arguement_test
```

这些都是通过`int main(int argc, char * argv[])`， 打印main函数中的argc和argv获得的

# 使用实例

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='arguement_test',
            output="screen",
            arguments=["-d", "arugment_val"]
        ),
    ])
```

这个launch文件的内容相当于

```
ros2 run learning_ros2_launch_by_example learning_ros2_launch_by_example_node -d arugment_val --ros-args -r __node:=arguement_test
```

因此，这些命令行参数，可以从main函数中读到

```c++
int main(int argc, char * argv[])
{
  RCLCPP_INFO(rclcpp::get_logger("For arguements"), 
  "The number of arguments is %d， They are", argc);
  for (int i = 1; i < argc; ++i)
  {
    RCLCPP_INFO(rclcpp::get_logger("For arguements"), argv[i]);
  }
  ...
}
```

