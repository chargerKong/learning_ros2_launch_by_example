#include <chrono>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class LaunchTest: public rclcpp::Node
{
  public:
    LaunchTest()
    : Node("launct_test"), count_(0){
      str_pub_ = this->create_publisher<std_msgs::msg::String>("origin_topic_name", 10);
      heart_timer_ = this->create_wall_timer(
         std::chrono::seconds(1), std::bind(&LaunchTest::heart_callback, this));
      this->declare_parameter("test_param_value");
      this->get_parameter_or<std::string>("test_param_value", test_param_value, "null");
      if (test_param_value.compare("null") != 0) {
        RCLCPP_INFO(this->get_logger(), "Capture the param, test_param_value: %s", test_param_value.c_str());
      }
    }

    void heart_callback() {
      auto message = std_msgs::msg::String();
      message.data = "Topic name: " + std::to_string(count_++);
      RCLCPP_INFO(this->get_logger(), "Publishing %s ", message.data.c_str());
      str_pub_->publish(message);
    }
    
  private:
    std::string test_param_value = "";
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr str_pub_;
    rclcpp::TimerBase::SharedPtr heart_timer_;
    int count_ = 0;
};