# learning-ros2-launch-by-example

在本人学习ROS2的时候，发现launch文件的详细教程十分少，因此把一些简单的例子做了一些整理

所有的例子尽量都在foxy下运行

## 安装
## Install 

clone此仓库到你的ROS2工作目录的src文件夹下

```
git clone https://github.com/chargerKong/learning_ros2_launch_by_example
```
然后编译

```
colcon build --packages-select learning_ros2_launch_by_example
source install/local_setup.bash
```

## 文档
## Docs 
目录

- [如何启动一个节点](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/launch/single_node.launch.py)
- [如何通过Node改变topic的名字](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20use%20remapping%20in%20Node.md)
- [Node中argument有什么用？如何通过argument给main函数传递参数](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20use%20argument%20in%20Node.md)
- [如何通过Node设置parameter参数](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20use%20parameters%20in%20Node.md)
- [如何通过命令行修改parameter参数](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20change%20parameters%20from%20command%20line.md)
- [查看DeclareLaunchArgument，我应该在命令行中设置哪些参数](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/What%20arguements%20should%20I%20set%20in%20command%20line.md)
- [如何对节点添加启动条件](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20conditionally%20start%20a%20node.md)
- [如何从LaunchConfiguration中获得数据](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20get%20context%20from%20LaunchConfiguration%20instance.md)
- [如何引入其他launch文件](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20inlucde%20another%20launch%20file.md)
- [如何模拟终端的命令](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20simulate%20a%20shell%20command.md)
- [什么是action？](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/What%20is%20action.md)
- [如何在一段时间之后再执行一个节点](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20execute%20an%20action%20after%20a%20period%20of%20time%20.md) 
- [如何定义group action](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20define%20group%20action.md)
- [如何添加namespace](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20specify%20a%20namespace%20to%20node%20and%20gourp.md)
- [如何设定环境变量](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/how%20to%20set%20envirnment.md)
- [什么是生命周期节点](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/lifecycleNode.md)
- [如何触发一个事件](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How%20to%20emit%20an%20action.md)
- [如何处理注册事件回调](https://github.com/chargerKong/learning_ros2_launch_by_example/blob/main/docs/How_to_use_register_event_handler.md)
