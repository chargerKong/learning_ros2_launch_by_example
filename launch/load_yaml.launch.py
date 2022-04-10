import os

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():

    config_yaml_file = PathJoinSubstitution([
        FindPackageShare('learning_ros2_launch_by_example'),
        'config',
        'launch_test.yaml'
    ])

    # config_yaml_file = os.path.join(
    #     get_package_share_directory('learning_ros2_launch_by_example'),
    #     'config',
    #     'launch_test.yaml'
    # )
    
    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='parameter_test',
            output="screen",
            parameters=[config_yaml_file]
        ),
    ])