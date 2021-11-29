经过前面的例子，我们可以发现，无论是执行

- 终端的命令（`launch.actions.ExecuteProcess`）

- 还是加载一个其他的launch文件`launch.actions.IncludeLaunchDescription`

- 还是执行一个节点`launch_ros.actions.Node`

他们都需要写在LaunchDescription中， launch文件的结构，最后一定长这样

```python
def generate_launch_description():
    return LaunchDescription([
        action_1,
        action_2,
        ...
        action_3
    ])
```

这些action可以是我们之前提出过的ExecuteProcess，IncludeLaunchDescription或者Node。他还可以是一个注册或者注销一个事件（event），修改环境变量等操——后续介绍。

因此代码中的action_n可以是一个动作也可以是一系统的动作（include），他表示要执行的一些事情，这些动作最后都需要被LaunchDescription 执行。





剩余还有没有讲到的action，这里简单做一下列举

- launch.actions.TimerAction
- launch.actions.GroupAction
- launch.actions.SetLaunchConfiguration
- launch.actions.RegisterEventHandler
- launch.actions.UnregisterEventHandler
- launch.actions.LogInfo
- launch.actions.RaiseError
- launch.actions.EmitEvent

