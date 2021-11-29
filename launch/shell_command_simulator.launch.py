from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Node(
        #     package='learning_ros2_launch_by_example',
        #     executable='learning_ros2_launch_by_example_node',
        #     name='learning_ros2_launch_by_example_node',
        #     output="screen",
        # ),
        ExecuteProcess(
            cmd=["ros2", "run", "learning_ros2_launch_by_example", 
            "learning_ros2_launch_by_example_node", "--ros-args", "-r", 
            "__node:=learning_ros2_launch_by_example_node"],            
            output="screen"
        )
    ])