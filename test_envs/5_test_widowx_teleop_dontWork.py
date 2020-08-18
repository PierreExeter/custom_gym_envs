import gym
import gym_envs
import pybullet as p
import numpy as np

# not working well yet

# env = gym.make('widowx_reacher-v0').start_sim(goal_oriented=False, render_bool=True)   # or .start_rospy(goal_oriented=False)
# env = gym.make('widowx_reacher-v1').start_rospy(goal_oriented=False)                   # requires a roscore to be running
# env = gym.make('widowx_reacher-v2')                                              # requires a roscore to be running
# env = gym.make('widowx_reacher-v3')                                              # requires a roscore to be running
# env = gym.make('widowx_reacher-v4').start_sim(goal_oriented=False, render_bool=True)
env = gym.make('widowx_reacher-v5')
# env = gym.make('widowx_reacher-v6')  
# env = gym.make('widowx_reacher-v7')  
# env = gym.make('widowx_reacher-v8')  
# env = gym.make('widowx_reacher-v12')  
# env = gym.make('widowx_reacher-v13')  

obs = env.reset()

keys_actions = {
    p.B3G_LEFT_ARROW: np.array([-0.01, 0, 0]), 
    p.B3G_RIGHT_ARROW: np.array([0.01, 0, 0]), 
    p.B3G_UP_ARROW: np.array([0, 0, 0.01]), 
    p.B3G_DOWN_ARROW: np.array([0, 0, -0.01]),
    p.B3G_ALT: np.array([0, 0.01, 0]), 
    p.B3G_SHIFT: np.array([0, -0.01, 0])
    }

# Get the position and orientation of the end effector
position, orientation = p.getLinkState(env.arm, 5, computeForwardKinematics=True)[4:6]


while True:

    keys = p.getKeyboardEvents()
    for key, action in keys_actions.items():
        if key in keys and keys[key] & p.KEY_IS_DOWN:
            position += action

    # IK to get new joint positions (angles) for the robot
    target_joint_positions = p.calculateInverseKinematics(env.arm, 5, position, orientation)
    target_joint_positions = target_joint_positions[:6]

    # Get the joint positions (angles) of the robot arm
    joint_positions = env._get_current_joint_positions()

    # Set joint action to be the error between current and target joint positions
    joint_action = (target_joint_positions - joint_positions) / 10000

    # print("YOPO")
    # print(target_joint_positions)
    # print(joint_positions)
    # print(joint_action)
    obs, reward, done, info = env.step(joint_action)

