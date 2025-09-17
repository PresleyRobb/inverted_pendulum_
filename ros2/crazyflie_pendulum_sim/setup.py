from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'crazyflie_pendulum_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/sim.launch.py']),
    ],
    install_requires=['setuptools', 'rclpy', 'geometry_msgs', 'nav_msgs', 'std_msgs', 'numpy'],
    zip_safe=True,
    maintainer='presrobb',
    maintainer_email='presrobb@yourdomain.com',
    description='ROS 2 package for controlling a Crazyflie drone and inverted pendulum simulation using reinforcement learning.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            
        ],
    },
)



