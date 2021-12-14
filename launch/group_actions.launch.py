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