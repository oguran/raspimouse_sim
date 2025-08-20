# The MIT License (MIT)
#
# Copyright 2025 Takuya Ogura <oguran29@gmail.com>

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import SetParameter
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    intern_world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            get_package_share_directory('raspimouse_gazebo'),
            '/launch/raspimouse_with_intern_world_01.launch.py'
        ]),
        launch_arguments={
            'lidar': 'urg',
            'use_rgb_camera': 'true'
        }.items()
    )

    # リマッピング用のリレーノード
    relay_scan = Node(
        package='topic_tools',
        executable='relay',
        arguments=['/scan', '/bridge/scan'],
        name='scan_relay'
    )
   
    return LaunchDescription([
        SetParameter(name='use_sim_time', value=True),
        intern_world_launch,
        relay_scan,
    ])
