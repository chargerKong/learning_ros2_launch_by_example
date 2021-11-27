from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    test_var = LaunchConfiguration("test_var", default="A_param_value")
    return LaunchDescription([
        DeclareLaunchArgument(
            "test_var",
            default_value=test_var,
            description="This is the test variable to be sent into node parameter"
        ),

        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='parameter_test',
            output="screen",
            parameters=[{"test_param_value": test_var}]
        ),
    ])