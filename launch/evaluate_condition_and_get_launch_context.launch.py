from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch.substitutions import PythonExpression
from launch import LaunchContext

lc = LaunchContext()

def generate_launch_description():
    var = LaunchConfiguration("run_example_node", default="'abc'")
    num = LaunchConfiguration("test_num", default="1")
    node_name = PythonExpression(["'test_name1' if ", num, "==2 else 'test_name2'"])
    print(f"run_example_node value: {var.perform(lc)}")
    print(f"test_num value : {num.perform(lc)}")
    print(f"node_name : {node_name.perform(lc)}")
    if (IfCondition(PythonExpression([num, "+ 1 == 2"])).evaluate(lc)):
        print("Good")
    else:
        print("Bad")
    return LaunchDescription([
        # Node(
        #     package='learning_ros2_launch_by_example',
        #     executable='learning_ros2_launch_by_example_node',
        #     name=node_name,
        #     output="screen",
        #     condition=IfCondition(PythonExpression([var, "== 'abc'"]))
        # ),
    ])