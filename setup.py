from setuptools import setup

setup(name='gym_envs',
      version='0.0.1',
      install_requires=['gym',
                        'pybullet',
                        'numpy',
                        # 'rospy' # comment rospy if ROS not installed
                        ]
)
