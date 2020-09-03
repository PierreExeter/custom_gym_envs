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
env = gym.make('JacoReachGazebo-v0')

print('Environment:', env)
print('Action space:', env.action_space)
# print(env.action_space.high)
# print(env.action_space.low)
print('State space:', env.observation_space)
# print(env.observation_space.high)
# print(env.observation_space.low)



state = env.reset()
print("current state: ", state)

action = [0, 90, 180, 60, 0, 0]
state = env.step(action)



# for t in range(3):

#     # create action
#     ang0 = 0
#     ang1 = 180
#     ang2 = random.randrange(90, 270)
#     ang3 = random.randrange(0, 359)
#     ang4 = random.randrange(0, 359)
#     ang5 = random.randrange(0, 359)
#     action = [ang0, ang1, ang2, ang3, ang4, ang5]
#     print("action sent: ", action)

#     state = env.step(action)
#     print("current state: ", state)


#     print("time step {}".format(t))

env.close()