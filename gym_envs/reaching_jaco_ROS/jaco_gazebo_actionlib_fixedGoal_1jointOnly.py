import gym
import numpy as np
import random
import time

from gym import error, spaces, utils
from gym.utils import seeding
from gym_envs.reaching_jaco_ROS.ros_scripts.jaco_gazebo_action_client import JacoGazeboActionClient



class JacoEnv(gym.Env):

    def __init__(self):

        self.robot = JacoGazeboActionClient()

        self.action_dim = 1
        self.obs_dim = 4

        high = np.ones([self.action_dim])
        self.action_space = gym.spaces.Box(-high, high)
        
        high = np.ones([self.obs_dim])
        self.observation_space = gym.spaces.Box(-high, high)
        

    def convert_action_to_new_range(self, a, OldMin, OldMax, NewMin, NewMax):
    
        OldRange = (OldMax - OldMin)  
        NewRange = (NewMax - NewMin)  

        return (((a - OldMin) * NewRange) / OldRange) + NewMin
    
    
    def action2increment(self, action):
        self.max_increment_step = 10  # in degree. Decrease to increase accuracy but reduce amplitude motion.

        self.angle_increment = self.convert_action_to_new_range(action, OldMin=-1, OldMax=1, NewMin=-(2*np.pi/360*self.max_increment_step), NewMax=2*np.pi/360*self.max_increment_step)
        return self.angle_increment


    def step(self, action):

        # read old angle
        self.old_angle1 = self.robot.read_angle_joint1()

        # calculate new angle
        self.angle_change1 = self.action2increment(action) 
        self.new_angle1 = self.old_angle1 + self.angle_change1

        # create array of joint angles and move arm 
        self.joint_angles = np.concatenate((self.new_angle1, [np.pi, np.pi/2, 0, 0, 0]), axis=None)
        self.robot.move_arm(self.joint_angles)
       
        # get state
        self.angle1 = self.robot.read_angle_joint1()

        self.obs = np.concatenate((self.angle1, self.target_vect), axis=None)

        # calculate reward
        self.tip_coord = self.robot.get_tip_coord()
        self.dist_to_target = np.linalg.norm(self.tip_coord - self.target_vect)
        self.reward = - self.dist_to_target 

        # create info
        self.info = {"tip position": self.tip_coord, "goal position": self.target_vect, "total_distance": self.dist_to_target}

        # create done
        self.done = False

        # IF DEFINING DONE AS FOLLOWS, THE EPISODE ENDS EARLY AND A GOOD AGENT WILL RECEIVED A PENALTY FOR BEING GOOD
        # COOMENT THIS
        # if self.dist_to_target < 0.01:
            # self.done = True
            
        # print("tip position: ", self.tip_coord)
        # print("target vect: ", self.target_vect)
        # print("dist_to_target: ", self.dist_to_target)

        return self.obs, self.reward, self.done, self.info


    def reset(self): 

        self.robot.cancel_move()

        pos = [0, np.pi, np.pi/2, 0, 0, 0]

        self.robot.move_arm(pos)
        # time.sleep(2)
        print("Jaco reset to initial position")

        # get observation
        self.obs = self.robot.read_angle_joint1()

        # Fixed target coordinates
        x_target = 0.7
        y_target = 0
        z_target = 0.7

        self.target_vect = np.array([x_target, y_target, z_target])
        print("Fixed target coordinates initialised")

        # if testing: graphically move the sphere target, if training, comment this line
        # self.robot.move_sphere(self.target_vect)

        return self.obs


    def render(self, mode='human', close=False):
        pass
