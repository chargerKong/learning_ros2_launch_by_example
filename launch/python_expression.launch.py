from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch.substitutions import PythonExpression

def generate_launch_description():
    var = LaunchConfiguration("run_example_node", default="'abc'")
    num = LaunchConfiguration("test_num", default="1")
    node_name = PythonExpression(["'test_name1' if ", num, "==2 else 'test_name2'"])

    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name=node_name,
            output="screen",
            condition=IfCondition(PythonExpression([var, "== 'abc'"]))
        ),
    ])