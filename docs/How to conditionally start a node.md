# IfCondition介绍

IfCondition 接受一个值为bool类型的变量。在构建一个节点的时候，可以作为启动条件进行判定





# 使用示例

```python
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition

def generate_launch_description():
    run_example_node = LaunchConfiguration("run_example_node", default="true")
    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='learning_ros2_launch_by_example_node',
            output="screen",
            condition=IfCondition(run_example_node)
        ),
    ])
```

在Node中添加了condition的条件，为run_example_node，注意他的值为布尔型变量，可以为true, false, 1, 0 中的任何一个，否则报错

> 注意：应该添加DeclareLaunchArgument在LaunchDescription中，要让使用的人，明白变量名，以及他的含义是什么。但是为了文档的简洁性起见，这里没有加



# IFCondition 使用效果

```
ros2 launch learning_ros2_launch_by_example node_ifcondition.launch.py 
```

节点正常启动，可以看见会持续输出发布的消息.



关闭，再一次启动，并添加变量，禁止此节点启动

```shell
ros2 launch learning_ros2_launch_by_example node_ifcondition.launch.py run_example_node:=false
```

可以看见，launch文件不会在启动节点
