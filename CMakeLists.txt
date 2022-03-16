cmake_minimum_required(VERSION 3.8)
project(learning_ros2_launch_by_example)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# find_package(rclcpp REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)
find_package(lifecycle_msgs REQUIRED)
find_package(std_msgs REQUIRED)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

set(dependencies
  # rclcpp
  lifecycle_msgs
  rclcpp_lifecycle
)

include_directories(
  include
)

add_executable(${PROJECT_NAME}_node src/launch_test.cpp)
add_executable(lifecycle_listener_node src/lifecycle_listener.cpp)
add_executable(lifecycle_service_client_node src/lifecycle_service_client.cpp)
add_executable(lifecycle_talker_node src/lifecycle_talker.cpp)

ament_target_dependencies(${PROJECT_NAME}_node 
${dependencies})
ament_target_dependencies(lifecycle_listener_node
${dependencies})
ament_target_dependencies(lifecycle_service_client_node
${dependencies})
ament_target_dependencies(lifecycle_talker_node
${dependencies})

install(TARGETS ${PROJECT_NAME}_node
  DESTINATION lib/${PROJECT_NAME})
install(TARGETS lifecycle_listener_node
  DESTINATION lib/${PROJECT_NAME})
install(TARGETS lifecycle_service_client_node
  DESTINATION lib/${PROJECT_NAME})
install(TARGETS lifecycle_talker_node
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
