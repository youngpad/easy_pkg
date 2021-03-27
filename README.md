# Easy Package

Easy ROS2 package for testing.

Two nodes, a publisher and subscriber:
* Publisher waits for user input and publishes String-message (std_msgs) to /words-topic.
* Subscriber subscribes to /words-topic and prints message to terminal.

easy_pub -> /words -> easy_sub

## How to use

Launch publisher:
```
ros2 run easy_pkg easy_pub
```

Launch subscriber:
```
ros2 run easy_pkg easy_sub
```
