import os

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable, ExecuteProcess
from launch.substitutions import EnvironmentVariable
def generate_launch_description():
    
    os.environ["FOOBAR"] = "Goodbye, World"
    return LaunchDescription([
        # SetEnvironmentVariable('FOOBAR', 'Goodbye, World'),
        ExecuteProcess(
            cmd=['echo', EnvironmentVariable('FOOBAR')],
            additional_env={'FOOBAR': 'Hello, World'},
            output='screen'),
    ])
