import gym
import gym_envs
import random
import numpy as np 
import rospy

# First of all, launch Jaco in Gazebo in another terminal with:
# roslaunch kinova_gazebo robot_launch_noRender_noSphere.launch kinova_robotType:=j2n6s300
# OR
# roslaunch kinova_gazebo robot_launch_render.launch kinova_robotType:=j2n6s300

rospy.init_node("kinova_client", anonymous=True, log_level=rospy.INFO)
env = gym.make('JacoReachGazebo-v1')

print('Environment:', env)
print('Action space:', env.action_space)
print(env.action_space.high)
print(env.action_space.low)
print('State space:', env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)


for episode in range(3):

    obs = env.reset()
    rewards = []

    for t in range(20):

        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)

        print("timestep:", t)
        print("action: ", action)
        print("observation: ", obs)
        print("reward: ", reward)
        print("done: ", done)
        print("info: ", info)

        rewards.append(reward)

    cumulative_reward = sum(rewards)
    print("episode {} | cumulative reward : {}".format(episode, cumulative_reward))  

env.close()

