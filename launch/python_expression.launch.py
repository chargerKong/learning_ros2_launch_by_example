from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch.substitutions import PythonExpression

def generate_launch_description():
    var = LaunchConfiguration("run_example_node", default="'abc'")
    var1 = LaunchConfiguration("a", default="1")
    if (PythonExpression([var1, "+ 1 == 2"])):
        print("Good")
    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='learning_ros2_launch_by_example_node',
            output="screen",
            condition=IfCondition(PythonExpression([var, "== 'abc'"]))
        ),
    ])