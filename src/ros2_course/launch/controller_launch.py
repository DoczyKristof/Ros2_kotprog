from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_prefix

def generate_launch_description():
    turtlebot3_gazebo_prefix = get_package_prefix('turtlebot3_gazebo')

 
 def generate_launch_description():
    ld = LaunchDescription()

    # Create the node
    controller_node = Node(
        package="ros2_course",
        executable="controller",
        name="controller"
    )

    # Add the node to the launch description
    ld.add_action(controller_node)

    return ld


if __name__ == '__main__':
    generate_launch_description()
 
 
'''  return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value='empty',
            description='Choose an empty world or your own world file'
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            output='screen',
            arguments=['-entity', 'robot', '-x', '0.0', '-y', '0.0', '-z', '0.0']
        ),
        Node(
            package='gazebo_ros',
            executable='gzserver',
            name='gzserver',
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='gzclient',
            name='gzclient',
            output='screen'
        ),
        Node(
            package='ros2_course',
            namespace='robot',
            executable='controller',
            name='controller',
            output='screen'
        )
        ExecuteProcess(
            cmd=['ros2', 'launch', turtlebot3_gazebo_prefix + '/share/turtlebot3_gazebo/launch/turtlebot3_world.launch.py'],
            output='screen'
        ),
        Node(
            package='ros2_course',
            namespace='robot',
            executable='controller',
            output='screen'
        )
    ]) '''
