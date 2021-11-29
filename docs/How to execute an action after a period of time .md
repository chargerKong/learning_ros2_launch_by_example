有些时候两个action是有一个先后关系的，需要一个动作执行完之后才可以执行下一个action，比如硬件启动的节点先要启动几秒后，才可以继续数据操作的节点。这个时候需要对一些action进行一个延时执行的操作

# TimerAction

TimerAction 可以在指定的时间后执行一个action。需要接受参数有

- period：接受一个float, 延迟的时间
- actions：接受一个list, [action_1, action_2,...]，列表中装要执行的action

# 应用示例

本案例是在launch文件启动五秒之后，再启动例子结点

```python
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction


def generate_launch_description():
    action_1 = Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='learning_ros2_launch_by_example_node',
            output="screen",
        )
    
    return LaunchDescription([
        TimerAction(period=5.0, actions=[action_1])
    ])
```

# 运行示例

```
ros2 launch learning_ros2_launch_by_example timer_actions.launch.py 
```

等待五秒，便可以看见终端输出topic pub的信息