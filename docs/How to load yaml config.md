# 如何加载yaml参数文件

之前我们介绍了如何通过Node中的parameter参数来加载参数，如果参数很多很多，那么我们就应该把参数拉到一个参数文件yaml文件中。假设现在手上有一个yaml文件在config文件夹下，其名字为launch_test.yaml。使用如下的方式进行加载

```python
import os

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    config_yaml_file = os.path.join(
        get_package_share_directory('learning_ros2_launch_by_example'),
        'config',
        'launch_test.yaml'
    )
    
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

注意，在运行之前，需要将config文件安装到share文件夹下，在CMakeLists.txt中添加

```cmake
install(DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)
```



#  如何写yaml文件

我们针对于如何使用parameter参数的文件，把该文件中的parameter变量写入yaml文件

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='learning_ros2_launch_by_example',
            executable='learning_ros2_launch_by_example_node',
            name='parameter_test',
            output="screen",
            parameters=[{"test_param_value": "A_param_value"}]
        ),
    ])
```

下面是针对于上面parameter的写法

```yaml
/parameter_test:
  ros__parameters:
    test_param_value: "A_param_value"
```



第一行表示Node的name，

第二行是必写的参数，代表下面是ros的参数，需要注意，中间是两个下划线，

第三行是冒号左边参数名字不需要加引号，冒号右边需要加引号



## 如何指定添加namespace

1. yaml文件

   ```yaml
   /node_namespace/node_name:
     ros__parameters:
       test_param_value: "A_param_value"
   ```

2. launch中的node需要指定 namespace

   ```python
   Node(
       package='learning_ros2_launch_by_example',
       executable='learning_ros2_launch_by_example_node',
       name='parameter_test',
       namespace='your_namespace'
       output="screen",
       parameters=[config_yaml_file]
   ),
   ```

   

# 运行

```
ros2 launch learning_ros2_launch_by_example load_yaml.launch.py
```

我们可以看见log中的一条信息，说明参数传递成功

```
[learning_ros2_launch_by_example_node-1] [INFO] [1647418583.008851348] [parameter_test]: Capture the param, test_param_value: A_param_value
```

