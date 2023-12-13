# ROS 2 TurtleBot3 Gazebo Simulation Documentation
## About

![image](https://github.com/DoczyKristof/Ros2_kotprog/assets/44243837/02a05edd-119d-46d5-91b8-a8adca719538)

## Controller Node (controller)

The `MoveTurtlebotNode` is a ROS 2 node designed to control a TurtleBot3 in a Gazebo simulation based on laser scan data. It adjusts the robot's velocity to navigate and avoid obstacles.

### Node Structure

- **Node Name:** `controller`
- **Published Topic:**
  - `/cmd_vel` (Twist): Velocity commands for controlling the TurtleBot's movement.

- **Subscribed Topic:**
  - `/scan` (LaserScan): Laser scan data for obstacle detection.

- **Node Behavior:**
  - Uses laser scan data to determine distances in the front, front-right, and front-left directions.
  - If any of these distances is less than a threshold of 0.8 meters, the robot stops (`linear.x = 0.0`) and rotates clockwise (`angular.z = 2.5`).
  - If all distances are greater than or equal to 0.8 meters, the robot moves forward (`linear.x = 0.5`) and does not rotate (`angular.z = 0.0`).

### Usage

To run the `MoveTurtlebotNode`, use the following command:

```bash
ros2 run ros2_course controller
```

## Package Setup (setup.py)

This package configuration is for the `ros2_course` ROS 2 package. It defines package metadata, dependencies, and entry points for executable scripts.

### Package Information

- **Name:** `ros2_course`
- **Version:** 0.0.0

### Package Structure

- **Packages:**
  - The package includes all sub-packages, excluding the 'test' package.

- **Data Files:**
  - Registers resource files for the Ament package index and includes the 'package.xml' file.

- **Launch Files:**
  - Gathers all launch files from the 'launch' directory and places them in the 'share/ros2_course' directory.

### Dependencies

- **Required Dependency:**
  - `setuptools`: Necessary for packaging and distribution.

### Maintainer Information

- **Maintainer:** `ros_user`
- **Maintainer Email:** `ros_user@todo.todo`

### Package Description and License

- **Description:** TODO: Add a description of the package.

- **License:** TODO: Declare the license for the package.

### Tests

- **Test Requirements:**
  - The package requires `pytest` for testing.

### Entry Points

- **Console Scripts:**
  - Defines two console scripts:
    - `hello`: Executes the `main` function from the `ros2_course.hello` module. (legacy)
    - `controller`: Executes the `main` function from the `ros2_course.controller` module.

## ~~Launch Configuration (launch.py)~~ (deprecated)

~~This launch configuration sets up a Gazebo simulation for TurtleBot3, including the robot spawn, Gazebo server, Gazebo client, and a custom controller.~~

### ~~Components~~

- ~~**Empty World Argument:**~~
  - ~~A launch argument to choose an empty world or provide your own world file.~~

- ~~*Spawn Robot Entity Node:**~~
  - ~~Spawns a Gazebo entity named 'robot' at coordinates (0.0, 0.0, 0.0).~~

- ~~**Gazebo Server Node:**~~
  - ~~Launches the Gazebo server for simulation.~~

- ~~**Gazebo Client Node:**~~
  - ~~aunches the Gazebo client for visualization.~~

- ~~**Controller Node:**~~
  - ~~uns the `controller` node from the `ros2_course` package under the 'robot' namespace.~~

- ~~**Execute Process - Launch World:**~~
  - ~~Executes a ROS 2 launch command to load the TurtleBot3 Gazebo world.~~

- ~~**Move TurtleBot Node:**~~
  - ~~Runs the `move_turtlebot` node from the `ros2_course` package under the 'robot' namespace.~~


## TurtleBot3, ROS 2, and Gazebo Simulation
### TurtleBot3:
TurtleBot3 is a popular open-source robot platform designed for education, research, and development.
Features:
Compact and affordable.
Widely used for learning ROS and robotic applications.
#### ROS 2:
ROS 2 is the second version of the Robot Operating System, providing a flexible framework for writing robot software.
Key Features:
Distributed architecture.
Real-time capabilities.
Improved communication protocols.
### Gazebo Simulation:
Gazebo is a powerful open-source robot simulation tool.
Features:
Realistic physics engine.
3D visualization.
Support for ROS integration.

## Usage

### How to *try and make it work*

- .bashrc
      
      source ~/ros2_ws/install/setup.bash
      export ROS_DOMAIN_ID=11
      export TURTLEBOT3_MODEL=burger
      source /opt/ros/humble/setup.bash
      export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:`ros2 pkg \
      prefix turtlebot3_gazebo \
      `/share/turtlebot3_gazebo/models/

- Install debian packages
  
      sudo apt-get update
      sudo apt install ros-humble-turtlebot3*

- Using rosdep get dependencies

      rosdep update
      rosdep install --from-paths src --ignore-src  -y  #(I don't think i used this one)

- Build the workspace

      cd ~/ros2_ws
      colcon build --symlink-install

- Launch the `simulation` and the `controller`
      
      ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
      ros2 run ros2_course controller

      



https://github.com/DoczyKristof/Ros2_kotprog/assets/44243837/6592b23b-fa14-4bca-b14c-488aacb71d2b


