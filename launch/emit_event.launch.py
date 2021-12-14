from launch import LaunchDescription
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

    ld = LaunchDescription()
    ld.add_entity(configure_talker)
    ld.add_entity(launch.actions.TimerAction(period=2.0, actions=[activate_talker]))
    ld.add_entity(launch.actions.TimerAction(period=5.0, actions=[shutdown_talker]))
    ld.add_entity(talker)  

    return ld
