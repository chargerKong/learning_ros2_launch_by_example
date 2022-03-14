# launch启动方式

launch的启动方式有两种情况，一种是基于`ros2 launch`的方式启动，是本身基于ros系统的启动方式。另一种是把launch文件当做是一个python3的可执行文件运行在系统中。下面先介绍以`ros2 launch`的方式启动

## ros2 launch + 包名字 + launch文件名

```
ros2 launch <pkg_name> <launch_name>
```

例如，我们可以直接运行

```
ros2 launch learning_ros2_launch_by_example launch_service.launch.py
```

来启动该launch文件。注意在此之前不要忘记source

## ros2 launch + launch文件名

通过在launch后面添加文件的相对或者绝对路径，也可以启动相应的launch文件

```
ros2 launch <path_to_your_launch_file>
```

例如，我们导航到该工程的launch文件下，然后直接键入

```
ros2 launch launch_service.launch.py
```

## python3 + launch 文件名

如果不借用ros2 launch 的接口，我们手动启动一个launch文件，需要为该launch文件添加一个入口，在你的launch文件的最后添加如下内容

```python
if __name__ == '__main__':
    desc = generate_launch_description()
    service = LaunchService(argv=sys.argv[1:])
    service.include_launch_description(desc)
    service.run()
```

在上面的代码中，我们建立了一个launch的服务，该服务可以控制launch系统的启动，关闭等事件。我们对服务添加了需要执行的行为，然后启动服务。这样的效果是和ros2 launch 启动的效果是一样的。

可以通过以下语句执行

```
python3 <path_to_your_launch_file>
```

例如，我们导航到该工程的launch文件下，然后直接如下内容即可

```
python3 launch_service.launch.py
```

该文件修改为

```python
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
```

