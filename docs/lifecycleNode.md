原文地址：https://design.ros2.org/articles/node_lifecycle.html

# 使用背景

我们使用launch文件启动的ROS系统可能很复杂，启动的多个节点之间也有很大的概率是有联系（有先后启动关系）。有的节点必须在一些节点准备好了之后才可以启动，否则没有意义，比如一切处理数据的节点，他必须在硬件驱动节点启动之后才可以发挥其作用，否则如果系统不够完善，很可能会发生未知的错误。这个时候我们就可以控制他们的启动顺序，以确保launch系统稳定

# 生命周期节点

生命周期节点，顾名思义，即有生命周期的结点。在整个生命周期（从创建到销毁）中，他将会有多个不同的状态。

![The proposed node life cycle state machine](../assets/lifecycle.png)

上面表示一个生命周期的全部状态，包括蓝色的四个主要状态

- `Unconfigured`
- `Inactive`
- `Active`
- `Finalized`

通过外部的action，可以将这几个状态进行转换，下面是图中黄色的六个转换状态，即中间态

- `Configuring`
- `CleaningUp`
- `ShuttingDown`
- `Activating`
- `Deactivating`
- `ErrorProcessing`

在转换态逻辑中，他们最终会返回成功或者失败。下面是7种可以被监督到的过程，上图蓝色线

- `create`
- `configure`
- `cleanup`
- `activate`
- `deactivate`
- `shutdown`
- `destroy`

所有的黄色结点，即中间态和Acitive状态都有可能发生错误，然后转到ErrorProcessing

