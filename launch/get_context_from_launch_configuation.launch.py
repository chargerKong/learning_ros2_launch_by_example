from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import OpaqueFunction

def launch_setup(context):
    test_var = LaunchConfiguration("test_var", default="A_param_value")
    print("test_var: {}\nthe type is: {}".format(test_var, test_var.__class__))
    test_var_context = test_var.perform(context)
    print("test_var_context: {}\nthe type is: {}".format(test_var_context, test_var_context.__class__))
    return [
        # DeclareLaunchArgument(
        #     "test_var",
        #     default_value=test_var,
        #     description="This is the test variable to be sent into node parameter"
        # ),

        # Node(
        #     package='learning_ros2_launch_by_example',
        #     executable='learning_ros2_launch_by_example_node',
        #     name='parameter_test',
        #     output="screen",
        #     parameters=[{"test_param_value": test_var}]
        # ),
    ]

def generate_launch_description():
    return LaunchDescription([
        OpaqueFunction(function=launch_setup),
    ])