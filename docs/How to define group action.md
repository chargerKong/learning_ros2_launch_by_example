如果我们需要定义一组操作，比如硬件启动，当选择了雷达型号之后需要不仅需要启动驱动还要启动滤波节点等。这个时候就可以把不同的雷达型号作为一个group，一旦要启动，就要启动一个组（group）

# GroupAction 介绍

此action将产生其他action，但可以与条件语句关联(允许您在组操作上使用条件语句，而不是单独在每个子操作上使用条件语句)，并且可以选择确定启动配置的范围。



# 实现示例

这里，我们随便找了两个action，把他们强行加入到一个组中，可以通过参数`use_xxx_group`来设置到底要不要启动这个组。还可以配置这个组的参数（很遗憾我还暂时不知道应该设置什么）

注意GroupAction 中actions 参数可以是任何一个action

```python
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import GroupAction, ExecuteProcess
from launch.conditions import IfCondition


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
            actions=[action_1, action_2],
            condition=IfCondition(use_xxx_group),
            launch_configurations={}
        )
    return LaunchDescription([
        xxx_group
    ])
```

# 使用示例

```
ros2 launch learning_ros2_launch_by_example group_actions.launch.py
```

可以看见发布的消息信息，以及一个小乌龟窗口

```
ros2 launch learning_ros2_launch_by_example group_actions.launch.py use_xxx_group:=false
```

则无事发生