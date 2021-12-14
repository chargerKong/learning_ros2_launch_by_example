# 向节点指定namespace

通过launch文件向节点添加namespace，指定关键字namespace即可，举例

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
            parameters=[{"test_param_value": "A_param_value"}],
            remappings=[("origin_topic_name", "other_topic_name")],
            namespace="AnyName"
        ),
    ])
```

我们向此节点指定namespace为AnyName，话题的名字由原来的`other_topic_name`改为`/AnyName/other_topic_name`

## **注意**、

 有以下情况namespace无效

- 节点本来就已经有了namespace了。
- 定义发布节点的时候，topic名字的前面加上了符号`/`。

## 运行

```
ros2 launch learning_ros2_launch_by_example node_namespace.launch.py
```

打开一个新终端

```
ros2 topic list
```

可以看见

```
/AnyName/other_topic_name
```

# 向group指定namespace

指定了group action, 我们也可以为此group添加namespace

```python
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import GroupAction, ExecuteProcess
from launch.conditions import IfCondition
from launch_ros.actions import PushRosNamespace


def generate_launch_description():
    action_1 = Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='learning_ros2_launch_by_example_node',
            output="screen",
        )
    action_2 = ExecuteProcess(cmd=['ros2', 'run', 'turtlesim', 'turtlesim_node'])
    
    use_xxx_group = LaunchConfiguration("use_xxx_group", default="true")
    
    xxx_group = GroupAction(
            actions=[
                PushRosNamespace("AnyName"),
                action_1,
                action_2,
                ],
            condition=IfCondition(use_xxx_group),
            launch_configurations={}
        )
    return LaunchDescription([
        xxx_group
    ])
```

通过关键字PushRosNamespace 向此group添加 namespace ，需要注意的内容和上面一样，他只能给没有命名空间的节点有效，例如下面

```
ros2 launch learning_ros2_launch_by_example group_actions.launch.py
```

打开另外一个终端

```
ros2 topic list
```

可以发现

```
/AnyName/origin_topic_name
/parameter_events
/rosout
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

原本有namespace的topic并不会被修改