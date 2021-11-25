#include <launch_test.hpp>

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<LaunchTest>());
  rclcpp::shutdown();
  return 0;
}