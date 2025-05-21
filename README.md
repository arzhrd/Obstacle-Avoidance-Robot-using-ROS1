# Obstacle-Avoidance-Robot-using-ROS1Here's a `README.md` 
---

````markdown
# 🛑 ROS 1 Obstacle Avoidance Robot Simulation (Gazebo + TurtleBot3)

This project simulates an obstacle-avoiding mobile robot using **ROS 1**, **Gazebo**, and the **TurtleBot3** platform. A basic Python node reads LaserScan data and commands the robot to turn when an obstacle is detected.

## 📦 Features

- 🐢 Uses TurtleBot3 (Burger model)
- 🏃‍♂️ Autonomous obstacle avoidance using LaserScan
- 🧪 Gazebo simulation-ready
- 💡 Simple logic, beginner-friendly

## 🧰 Requirements

- Ubuntu 20.04
- ROS 1 Noetic
- Gazebo (comes with ROS Desktop Full)
- TurtleBot3 packages:

```bash
sudo apt install ros-noetic-turtlebot3*
````

## 📁 Project Structure

```
obstacle_avoidance/
├── launch/
│   └── avoid_obstacles.launch
├── scripts/
│   └── avoid_obstacles.py
├── CMakeLists.txt
└── package.xml
```

## 🚀 Setup Instructions

### 1. Clone and Build

```bash
cd ~/catkin_ws/src
git clone https://github.com/yourusername/obstacle_avoidance.git
cd ..
catkin_make
source devel/setup.bash
```

### 2. Run the Simulation

```bash
export TURTLEBOT3_MODEL=burger
roslaunch obstacle_avoidance avoid_obstacles.launch
```

## 🤖 How It Works

* Subscribes to `/scan` topic for LIDAR data
* Detects obstacles in front of the robot
* If an obstacle is closer than `0.5m`, the robot stops and turns
* Otherwise, it moves forward

## 📝 Code Snippet

```python
front = min(min(data.ranges[0:15] + data.ranges[-15:]), 10)
if front < 0.5:
    self.msg.linear.x = 0.0
    self.msg.angular.z = 0.5  # Turn
else:
    self.msg.linear.x = 0.2
    self.msg.angular.z = 0.0
```



```
