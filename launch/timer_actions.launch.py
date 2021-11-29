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