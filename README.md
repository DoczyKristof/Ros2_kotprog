# ROS 2 TurtleBot3 Gazebo Simulation Documentation
## About

![image](https://github.com/DoczyKristof/Ros2_kotprog/assets/44243837/3860de94-c763-4675-bd19-89655e9564ca)

## Controller Node (controller)



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
    - `hello`: Executes the `main` function from the `ros2_course.hello` module.
    - `controller`: Executes the `main` function from the `ros2_course.controller` module.


## Launch Configuration (launch.py)

This launch configuration sets up a Gazebo simulation for TurtleBot3, including the robot spawn, Gazebo server, Gazebo client, and a custom controller.

### Components

- **Empty World Argument:**
  - A launch argument to choose an empty world or provide your own world file.

- **Spawn Robot Entity Node:**
  - Spawns a Gazebo entity named 'robot' at coordinates (0.0, 0.0, 0.0).

- **Gazebo Server Node:**
  - Launches the Gazebo server for simulation.

- **Gazebo Client Node:**
  - Launches the Gazebo client for visualization.

- **Controller Node:**
  - Runs the `controller` node from the `ros2_course` package under the 'robot' namespace.

- **Execute Process - Launch World:**
  - Executes a ROS 2 launch command to load the TurtleBot3 Gazebo world.

- **Move TurtleBot Node:**
  - Runs the `move_turtlebot` node from the `ros2_course` package under the 'robot' namespace.


## Usage

How to *build* and use the package.

    cd ~/ros2_ws
    colcon build --symlink-install

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
