import launch
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    inlucde_other_file = LaunchConfiguration("inlucde_other_file", default="true")
    test_var = LaunchConfiguration('test_var', default="test_var_2")
    return launch.LaunchDescription([
        launch.actions.IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [ThisLaunchFileDir(), '/launch_declare_launch_argument.launch.py']
            ),
            condition=IfCondition(inlucde_other_file),
            launch_arguments={'test_var': test_var}.items(),
        )
    ])