# launch Node中remapping作用



把节点中topic的名字重新映射为其他的名字

# remapping 效果

在本代码中，可以通过如下方式查看remapping的效果

打开一个没有经过remapping的launch文件

```
ros2 launch learning_ros2_launch_by_example single_node.launch.py
```

查看发布的topic名字

```shell
ros2 topic list

/parameter_events
/rosout
/origin_topic_name
```

可以看见，发布消息的topic名字为origin_topic_name



关闭程序，打开另外一个launch文件

```
ros2 launch learning_ros2_launch_by_example single_node_remapping.launch.py
```

查看发布的topic名字

```shell
/other_topic_name
/parameter_events
/rosout
```

可以看见，发布消息的topic名字从origin_topic_name转换为other_topic_name

# 使用示例

```c++
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='remapping_test',
            output="screen",
            remappings=[("origin_topic_name", "other_topic_name")]
        ),
    ])
```

如果有多个topic需要更改，则按照如下形式更改

```python
remapping=[
	('origin1', 'other1'),
	('origin2', 'other2')
]
```



