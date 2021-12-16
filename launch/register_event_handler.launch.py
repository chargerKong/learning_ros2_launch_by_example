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
        launch.event_handlers.OnProcessStart(
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
