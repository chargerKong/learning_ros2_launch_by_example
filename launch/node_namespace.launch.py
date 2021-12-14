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