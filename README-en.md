# learning-ros2-launch-by-example
The repo is created for learning ros2 launch system due to the lack of detailed description of how to write the launch file.

All of the examples could be run in foxy

## Install 

Clone  the repo to your ROS2 workspace which is under src file folder

```
git clone https://github.com/chargerKong/learning_ros2_launch_by_example
```

And then build it

```
colcon build --packages-select learning_ros2_launch_by_example
source install/local_setup.bash
```

## Docs 

Here is the brief contents

- [How to launch a node](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/launch/single_node.launch.py)
- [three ways to execute launch file](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/three_ways_launch.md)
- [How to change topic name in Node](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20use%20remapping%20in%20Node.md)
- [How to transfer argument into main function](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20use%20argument%20in%20Node.md)
- [How to set parameters to a Node](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20use%20parameters%20in%20Node.md)
- [How to load yaml file](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20load%20yaml%20config.md)
- [How to change parameters from command line](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20change%20parameters%20from%20command%20line.md)
- [What arguments should I set in command line](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/What%20arguements%20should%20I%20set%20in%20command%20line.md)
- [How to conditionally start a node](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20conditionally%20start%20a%20node.md)
- [How to use PythonExpression](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20use%20pythonexpression.md)
- [How to get context from LaunchConfiguration instance](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20get%20context%20from%20LaunchConfiguration%20instance.md)
- [How to include another launch file](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20inlucde%20another%20launch%20file.md)
- [How to simulate shell command in launch file](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20simulate%20a%20shell%20command.md)
- [What is action？](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/What%20is%20action.md)
- [How to execute an action after a period of time](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20execute%20an%20action%20after%20a%20period%20of%20time%20.md) 
- [How to define group action](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20define%20group%20action.md)
- [How to set envirnment](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20set%20envirnment.md)
- [What is lifecycle node](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/lifecycleNode.md)
- [How to emit an action](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20emit%20an%20action.md)
- [How_to_use_register_event_handler](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How_to_use_register_event_handler.md)