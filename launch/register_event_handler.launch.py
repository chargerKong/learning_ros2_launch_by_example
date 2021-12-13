from launch import LaunchDescription
from launch import LaunchIntrospector
from launch import LaunchService
import launch
import launch.events
import launch_ros.event_handlers
import launch_ros.events.lifecycle
import launch_ros.actions

import lifecycle_msgs.msg


def generate_launch_description():
    
    talker = launch_ros.actions.LifecycleNode(
        name='talker',
        package='learning_ros2_launch_by_example',
        executable='lifecycle_talker_node',
        output='screen')

    # listener = launch_ros.actions.LifecycleNode(
    #     name='listener',
    #     package='learning_ros2_launch_by_example',
    #     executable='lifecycle_listener_node',
    #     output='screen')

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
    
    # shutdown_talker = launch.actions.EmitEvent(
    #     event=launch_ros.events.lifecycle.ChangeState(
    #         lifecycle_node_matcher=launch.events.matches_action(talker),
    #         transition_id=lifecycle_msgs.msg.Transition.TRANSITION_DESTROY
    #     )
    # )

    # reg_event_handler_talker_configured = launch.actions.RegisterEventHandler(
    #     launch_ros.event_handlers.OnStateTransition(
    #         target_lifecycle_node=talker, 
    #         goal_state='inactive',
    #         entities=[
    #             launch.actions.LogInfo(
    #                 msg="Node talk configuring"),
    #             configure_talker
    #         ]
    #     )
    # )

    # reg_event_handler_talker_activate = launch.actions.RegisterEventHandler(
    #     launch_ros.event_handlers.OnStateTransition(
    #         target_lifecycle_node=talker,
    #         start_state='inactive',
    #         goal_state='active',
    #         entities=[
    #             launch.actions.LogInfo(
    #                 msg="Node listener configured, activating"),
    #             # configure_talker,
    #             launch.actions.TimerAction(period=10.0, actions=[configure_talker])
    #         ]
    #     )
    # )
    
    # reg_event_handler_talker_shutdown = launch.actions.RegisterEventHandler(
    #     launch_ros.event_handlers.OnStateTransition(
    #         target_lifecycle_node=talker,
    #         start_state='active',
    #         goal_state='shuttingdown',
    #         entities=[
    #             launch.actions.LogInfo(
    #                 msg="Node listener configured, activating"),
    #             shutdown_talker
    #         ]
    #     )
    # )
    
    # reg_event_handler_talker_final= launch.actions.RegisterEventHandler(
    #     launch_ros.event_handlers.OnStateTransition(
    #         target_lifecycle_node=talker, 
    #         goal_state='finalized',
    #         entities=[
    #             launch.actions.LogInfo(
    #                 msg="finalized"),
                
    #         ]
    #     )
    # )
    
    ld = LaunchDescription()
    # ld.add_entity(reg_event_handler_talker_configured)
    # ld.add_entity(reg_event_handler_talker_activate)
    # ld.add_entity(reg_event_handler_talker_shutdown)
    # ld.add_entity(reg_event_handler_talker_final)
    
    ld.add_entity(configure_talker)
    ld.add_entity(launch.actions.TimerAction(period=2.0, actions=[activate_talker]))
    # ld.add_entity(activate_talker)
    ld.add_entity(launch.actions.TimerAction(period=5.0, actions=[shutdown_talker]))

    ld.add_entity(talker)
    # ld.add_entity(listener)
    
    
    # print(LaunchIntrospector().format_launch_description(ld))
    
    return ld
