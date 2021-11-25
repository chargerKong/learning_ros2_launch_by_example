#include "rclcpp/rclcpp.hpp"

class LaunchTest: public rclcpp::Node
{
  public:
    LaunchTest()
    : Node("launct_test"), count_(0){}
    
  private:
    int count_ = 0;

}