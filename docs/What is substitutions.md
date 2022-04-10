# 什么是substitution

Launch文件用于启动节点，服务和进程。在这些actions中会有参数影响着他们的行为，Substitution可以作为他们的参数从而更具灵活性，Substitution在launch description中被执行之前不能被直接计算的，Substitution有许多可能的变体，所有的变体都继承自`class:launch.Substitution`

substitution可用于获取特定信息，如launch configuration、环境变量或 任意 Python 表达式。



通过查看源代码，我们可以发现，所有launch中的substitution为

```python
__all__ = [
    'AnonName',
    'Command',
    'EnvironmentVariable',
    'FindExecutable',
    'LaunchConfiguration',
    'LocalSubstitution',
    'PathJoinSubstitution',
    'PythonExpression',
    'SubstitutionFailure',
    'TextSubstitution',
    'ThisLaunchFile',
    'ThisLaunchFileDir',
]
```



所有的substitution都可以在LaunchDescription 中直接使用

基本上，他们都是string的一个包装，都可以直接

- describe()
- 通过OpaqueFunction函数，perform()
- 在各种actions中当做str使用



# 使用举例

关于之前提及的加载yaml文件。

```python
def generate_launch_description():

    config_yaml_file = PathJoinSubstitution([
        FindPackageShare('learning_ros2_launch_by_example'),
        'config',
        'launch_test.yaml'
    ])
    
    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='parameter_test',
            output="screen",
            parameters=[config_yaml_file]
        ),
    ])
```



PythonPression

```python
num = LaunchConfiguration("num", default="1")
if (PythonExpression([num, "== 1"]))：
	do_something()
```



LaunchConfiguration

...