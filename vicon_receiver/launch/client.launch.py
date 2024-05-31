from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    buffer_size = 200
    topic_namespace = 'vicon'

    return LaunchDescription([
        DeclareLaunchArgument(
            'ip_vicon_pc', default_value='192.168.10.1'
        ),
        Node(
            package='vicon_receiver', executable='vicon_client', output='screen',
            parameters=[{
                'hostname': LaunchConfiguration('ip_vicon_pc'), 
                'buffer_size': buffer_size, 
                'namespace': topic_namespace
            }])
    ])
