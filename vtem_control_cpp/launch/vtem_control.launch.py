from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    common_params = {"num_valves": 16, "modbus_node": "192.168.4.3", "modbus_service": "502"}
    return LaunchDescription([
        Node(
            package='vtem_control_cpp',
            namespace='vtem_control',
            executable='input_pressures_sub_node',
            parameters=[
                common_params,
                {"input_pressures_topic": "input_pressures", "max_pressure": 300*100.0}
            ]
        ),
        Node(
            package='vtem_control_cpp',
            namespace='vtem_control',
            executable='output_pressures_pub_node',
            parameters=[
                common_params,
                {"output_pressures_topic": "output_pressures", "pub_freq": 50., "vtem_status_topic": 'vtem_status'}
            ]
        ),
    ])