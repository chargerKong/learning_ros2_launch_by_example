# PythonExpression

PythonExpression 可以帮助我们去计算substitutions的Python表达式运算。

比如我们得到的LaunchConfiguration，他就是一个substitutions，它没法直接用于Python的运算，譬如

```python
num = LaunchConfiguration("num", default="1")
node_name = 'test_name' if num==1 else 'test_name2'
```

num是LaunchConfiguration的一个对象，父类是一个substitutions，无法直接做Python运算。

此时PythonExpression就派上用场了，可以把上述代码修改为

```python
num = LaunchConfiguration("num", default="1")
node_name = PythonExpression(["'test_name1' if ", num, "==1 else 'test_name2'"])
```

PythonExpression 会自动提取substitutions中的值，然后帮助我们进行计算

注意：此时返回的node_name仅为一个PythonExpression的对象，不能str的对象，我们需要把该变量放入框架中运算



# 代码示例

上面的代码，我们调用了两次PythonExpression

- 第一次是利用substitutions做一次运算控制节点的名字
- 第二次利用运算结果配合condition 启动节点

注意，我们对变量abc 添加了引号，将其变为字符串。如果不加引号，则会报错abc未定义。

```python
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
```



# 运行

```
ros2 launch learning_ros2_launch_by_example python_expression.launch.py 
```

我们可以看见节点成功运行，节点的名字被重新命名为test_name1

