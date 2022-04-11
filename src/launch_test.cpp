#include "launch_test.hpp"
#include "rclcpp/rclcpp.hpp"
#include <iostream>

int main(int argc, char * argv[])
{
  RCLCPP_INFO(rclcpp::get_logger("For arguements"), 
      "The number of arguments is %d， They are", argc);
  for (int i = 0; i < argc; ++i)
  {
    RCLCPP_INFO(rclcpp::get_logger("For arguements"), argv[i]);
  }
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<LaunchTest>());
  rclcpp::shutdown();
  return 0;
}