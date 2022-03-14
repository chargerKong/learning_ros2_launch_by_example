import sys

from launch import LaunchService
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='launch_service_test',
            output="screen",
        ),
    ])

if __name__ == '__main__':
    desc = generate_launch_description()
    service = LaunchService(argv=sys.argv[1:])
    service.include_launch_description(desc)
    service.run()