本文依然是针对于生命周期结点，本文介绍如何对一个事件注册，并定义回调。以lifecycle的lifecycle_talker为例子。

本代码copy了一份名为lifecycle_talker_node结点

# RegisterEventHandler

RegisterEventHandler顾名思义，他注册了一个事件，**就是在发生了一个被注册过的事件之后该如何做出响应**

使用案例

```python
    reg_event_handler_talker_configured = launch.actions.RegisterEventHandler(
        launch_ros.event_handlers.OnStateTransition(
            target_lifecycle_node=talker,
            goal_state='inactive',
            entities=[
                launch.actions.LogInfo(
                    msg="Node talk configuring"),
                activate_talker
            ]
        )
    )
```

此代码注册了一个OnStateTransition事件，即当定义的talker节点完成状态转换并且目标转换状态为inactive的时候，启动entities中的事件

```python
    reg_event_handler_process_start = launch.actions.RegisterEventHandler(
        launch.event_handlers.on_process_start.OnProcessStart(
            target_action=talker,
            on_start=[
                configure_talker
            ]
        )
    )
```

此代码注册了一个进程启动事件的注册，当launch文件完全启动，则调用configure_talker

## 生命周期节点参考图

![The proposed node life cycle state machine](../assets/lifecycle.png)

在上一个文档中，我们介绍了talker节点，从unconfigured状态通过configure()转换到inactive，又通过activate()转换到active。但是发出事件的时间都是同步的，不过是我们设置了延迟时间。

在本文中，我们将多个事件的发出时间将根据不同的状态来确定

# launch 代码示例

在本代码中，我们依然了三个发出事件的action，同时我们还注册了三个事件。这三个发出事件的action并没有直接添加到LaunchDescription中，而是把他们全部注册到了RegisterEventHandler中

**代码流程：**

- 启动代码
- 触发reg_event_handler_process_start，发出事件转换，即configure_talker
- talker节点进入状态转换，状态为从unconfigured进入inactive
- 如果转换成功。触发reg_event_handler_talker_configured，打印log，发出转换事件，即activate_talker，transition_id为TRANSITION_ACTIVATE
- talker节点进入状态转换，状态为从inactive进入active
- 如果转换成功。触发reg_event_handler_talker_activate，打印log，发出转换事件，即shutdown_talker，transition_id为TRANSITION_ACTIVE_SHUTDOWN
- talker节点进入状态转换，状态为从active进入finalized

```python
from launch import LaunchDescription
import launch
import launch.events
import launch_ros.event_handlers
import launch_ros.events.lifecycle
import launch_ros.actions
import launch.event_handlers

import lifecycle_msgs.msg


def generate_launch_description():
    
    talker = launch_ros.actions.LifecycleNode(
        name='talker',
        package='learning_ros2_launch_by_example',
        executable='lifecycle_talker_node',
        output='screen')

    configure_talker = launch.actions.EmitEvent(
        event=launch_ros.events.lifecycle.ChangeState(
            lifecycle_node_matcher=launch.events.matches_action(talker),
            transition_id=lifecycle_msgs.msg.Transition.TRANSITION_CONFIGURE
        )
    )

    activate_talker = launch.actions.EmitEvent(
        event=launch_ros.events.lifecycle.ChangeState(
            lifecycle_node_matcher=launch.events.matches_action(talker),
            transition_id=lifecycle_msgs.msg.Transition.TRANSITION_ACTIVATE
        )
    )

    shutdown_talker = launch.actions.EmitEvent(
        event=launch_ros.events.lifecycle.ChangeState(
            lifecycle_node_matcher=launch.events.matches_action(talker),
            transition_id=lifecycle_msgs.msg.Transition.TRANSITION_ACTIVE_SHUTDOWN
        )
    )

    reg_event_handler_process_start = launch.actions.RegisterEventHandler(
        launch.event_handlers.on_process_start.OnProcessStart(
            target_action=talker,
            on_start=[
                configure_talker
            ]
        )
    )

    reg_event_handler_talker_configured = launch.actions.RegisterEventHandler(
        launch_ros.event_handlers.OnStateTransition(
            target_lifecycle_node=talker,
            goal_state='inactive',
            entities=[
                launch.actions.LogInfo(
                    msg="Node talk configuring"),
                activate_talker
            ]
        )
    )

    reg_event_handler_talker_activate = launch.actions.RegisterEventHandler(
        launch_ros.event_handlers.OnStateTransition(
            target_lifecycle_node=talker,
            goal_state='active',
            entities=[
                launch.actions.LogInfo(
                    msg="Node talk activating"),
                launch.actions.TimerAction(period=10.0, actions=[shutdown_talker])
            ]
        )
    )

    ld = LaunchDescription()
    ld.add_entity(reg_event_handler_talker_configured)
    ld.add_entity(reg_event_handler_talker_activate)
    ld.add_entity(reg_event_handler_process_start)
    ld.add_entity(talker)
    
    return ld

```



# 运行示例

```
ros2 launch learning_ros2_launch_by_example register_event_handler.launch.py 
```

结果

```
[lifecycle_talker_node-1] [INFO] [1639644742.751164719] [talker]: on_configure() is called.
[INFO] [launch.user]: Node talk configuring
[lifecycle_talker_node-1] [INFO] [1639644742.756135413] [talker]: on_activate() is called.
[lifecycle_talker_node-1] [INFO] [1639644744.756463543] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #1]
[INFO] [launch.user]: Node talk activating
[lifecycle_talker_node-1] [INFO] [1639644745.751143486] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #2]
[lifecycle_talker_node-1] [INFO] [1639644746.751175934] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #3]
[lifecycle_talker_node-1] [INFO] [1639644747.751150623] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #4]
[lifecycle_talker_node-1] [INFO] [1639644748.751131945] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #5]
[lifecycle_talker_node-1] [INFO] [1639644749.751102022] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #6]
[lifecycle_talker_node-1] [INFO] [1639644750.751092769] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #7]
[lifecycle_talker_node-1] [INFO] [1639644751.751009764] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #8]
[lifecycle_talker_node-1] [INFO] [1639644752.751032983] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #9]
[lifecycle_talker_node-1] [INFO] [1639644753.751012411] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #10]
[lifecycle_talker_node-1] [INFO] [1639644754.750979127] [talker]: Lifecycle publisher is active. Publishing: [Lifecycle HelloWorld #11]
[lifecycle_talker_node-1] [INFO] [1639644754.762227912] [talker]: on shutdown is called from state active.
```

流程和所期望的一致


