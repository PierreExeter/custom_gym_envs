from gym_envs.reacher2D.goal_envs.env_bases import BaseBulletEnv
from gym_envs.reacher2D.goal_envs.scene_bases import SingleRobotEmptyScene
from gym import GoalEnv, spaces
import numpy as np
from gym_envs.reacher2D.goal_envs.reacher import Reacher1
from gym_envs.reacher2D.goal_envs.reacher import Reacher2
from gym_envs.reacher2D.goal_envs.reacher import Reacher3
from gym_envs.reacher2D.goal_envs.reacher import Reacher4
from gym_envs.reacher2D.goal_envs.reacher import Reacher5
from gym_envs.reacher2D.goal_envs.reacher import Reacher6


class ReacherBulletEnv1(BaseBulletEnv, GoalEnv):
    def __init__(self):
        self.robot = Reacher1()
        BaseBulletEnv.__init__(self, self.robot)

        self.REWARD_WEIGHTS = np.array([1, 0.3])
        self.SUCCESS_GOAL_REWARD = 0.12

    def create_single_player_scene(self, bullet_client):
        return SingleRobotEmptyScene(bullet_client, gravity=0.0, timestep=0.0165, frame_skip=1)

    def step(self, a):
        assert (not self.scene.multiplayer)

        self.robot.apply_action(a)
        self.scene.global_step()

        current_state = self.robot.calc_state()  # sets self.to_target_vec

        # potential_old = self.potential
        # self.potential = self.robot.calc_potential()

        # electricity_cost = (
        #         -0.10 * (     
        #                 np.abs(a[0] * self.robot.angle0_dot)  
        #                 )   # work torque*angular_velocity
        #         - 0.01 * (
        #         np.abs(a[0])  
        #                  )  # stall torque require some energy
        #                     )

        # stuck_joint_cost = 0  # stuck joint don't apply when the robot only has 1 joint

        
        # self.rewards = [float(self.potential - potential_old), float(electricity_cost), float(stuck_joint_cost)]
        # self.HUD(current_state, a, False)
        # tot_reward = sum(self.rewards)

        # define info
        info = self.robot.extra_info()

        obs = {'observation': current_state, 'achieved_goal': info['fingertip_coord'], 'desired_goal': info['target_coord']}

        tot_reward = self.compute_reward(obs['achieved_goal'], obs['desired_goal'], info)  # new HER goal

        # Define done: an episode is successful if the distance fingertip - target <= 0.01
        done = False

        # update info
        # info['is_success'] = self._is_success(obs['achieved_goal'], obs['desired_goal'])

        # if info["dist_ft_t"] <= 0.01:    
            # print("target reached!")
            # tot_reward += 10
            # done=True

        return obs, tot_reward, done, info

    # this should be equivalent ?
    def compute_reward(self, achieved_goal, desired_goal, info):
        self.dist_vec = np.array(achieved_goal - np.array(desired_goal))   
        return - np.linalg.norm(self.dist_vec)
        
    
    # def compute_reward(self, achieved_goal, desired_goal, p=0.5):
    #     """
    #         Proximity to the goal is rewarded

    #         We use a weighted p-norm
    #     :param achieved_goal: the goal that was achieved
    #     :param desired_goal: the goal that was desired
    #     :param p: the Lp^p norm used in the reward. Use p<1 to have high kurtosis for rewards in [0, 1]
    #     :return: the corresponding reward
    #     """
    #     return - np.power(np.dot(np.abs(achieved_goal - desired_goal), self.REWARD_WEIGHTS), p)


    # def _is_success(self, achieved_goal, desired_goal):
    #     return self.compute_reward(achieved_goal, desired_goal) > -self.SUCCESS_GOAL_REWARD


    # def extra_info(self):
    #     dist_ft_origin, dist_t_origin, dist_ft_t, max_reach, target_vect, fingertip_vect = self.robot.robot_info()

    #     info = {
    #         "dist_ft_origin": dist_ft_origin,
    #         "dist_t_origin": dist_t_origin,
    #         "dist_ft_t": dist_ft_t,
    #         "max_reach": max_reach,
    #         "target_coord": target_vect,
    #         "fingertip_coord": fingertip_vect
    #         }
        
    #     return info

    def camera_adjust(self):
        x, y, z = self.robot.fingertip.pose().xyz()
        x *= 0.5
        y *= 0.5
        self.camera.move_and_look_at(0.3, 0.3, 0.3, x, y, z)


class ReacherBulletEnv2(BaseBulletEnv):
    def __init__(self):
        self.robot = Reacher2()
        BaseBulletEnv.__init__(self, self.robot)

    def create_single_player_scene(self, bullet_client):
        return SingleRobotEmptyScene(bullet_client, gravity=0.0, timestep=0.0165, frame_skip=1)

    def step(self, a):
        assert (not self.scene.multiplayer)
        self.robot.apply_action(a)
        self.scene.global_step()

        current_state = self.robot.calc_state()  # sets self.to_target_vec

        # potential_old = self.potential
        # self.potential = self.robot.calc_potential()

        # electricity_cost = (
        #         -0.10 * (     
        #                 np.abs(a[0] * self.robot.angle0_dot) + 
        #                 np.abs(a[1] * self.robot.angle1_dot)
        #                 )   # work torque*angular_velocity
        #         - 0.01 * (
        #         np.abs(a[0]) + 
        #         np.abs(a[1])
        #                  )  # stall torque require some energy
        #                     )

        # stuck_joint_cost = 0
        # if np.abs(np.abs(self.robot.angle1) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        
        # self.rewards = [float(self.potential - potential_old), float(electricity_cost), float(stuck_joint_cost)]
        # self.HUD(current_state, a, False)
        # tot_reward = sum(self.rewards)

        # define info
        info = self.robot.extra_info()

        obs = {'observation': current_state, 'achieved_goal': info['fingertip_coord'], 'desired_goal': info['target_coord']}

        tot_reward = self.compute_reward(obs['achieved_goal'], obs['desired_goal'], info)  # new HER goal

        # Define done: an episode is successful if the distance fingertip - target <= 0.01
        done = False

        # update info
        # info['is_success'] = self._is_success(obs['achieved_goal'], obs['desired_goal'])

        # if info["dist_ft_t"] <= 0.01:    
            # print("target reached!")
            # tot_reward += 10
            # done=True

        return obs, tot_reward, done, info

    # this should be equivalent ?
    def compute_reward(self, achieved_goal, desired_goal, info):
        self.dist_vec = np.array(achieved_goal - np.array(desired_goal))   
        return - np.linalg.norm(self.dist_vec)
        
    
    # def compute_reward(self, achieved_goal, desired_goal, p=0.5):
    #     """
    #         Proximity to the goal is rewarded

    #         We use a weighted p-norm
    #     :param achieved_goal: the goal that was achieved
    #     :param desired_goal: the goal that was desired
    #     :param p: the Lp^p norm used in the reward. Use p<1 to have high kurtosis for rewards in [0, 1]
    #     :return: the corresponding reward
    #     """
    #     return - np.power(np.dot(np.abs(achieved_goal - desired_goal), self.REWARD_WEIGHTS), p)


    # def _is_success(self, achieved_goal, desired_goal):
    #     return self.compute_reward(achieved_goal, desired_goal) > -self.SUCCESS_GOAL_REWARD


    # def extra_info(self):
    #     dist_ft_origin, dist_t_origin, dist_ft_t, max_reach, target_vect, fingertip_vect = self.robot.robot_info()

    #     info = {
    #         "dist_ft_origin": dist_ft_origin,
    #         "dist_t_origin": dist_t_origin,
    #         "dist_ft_t": dist_ft_t,
    #         "max_reach": max_reach,
    #         "target_coord": target_vect,
    #         "fingertip_coord": fingertip_vect
    #         }
        
    #     return info



    def camera_adjust(self):
        x, y, z = self.robot.fingertip.pose().xyz()
        x *= 0.5
        y *= 0.5
        self.camera.move_and_look_at(0.3, 0.3, 0.3, x, y, z)



class ReacherBulletEnv3(BaseBulletEnv):
    def __init__(self):
        self.robot = Reacher3()
        BaseBulletEnv.__init__(self, self.robot)

    def create_single_player_scene(self, bullet_client):
        return SingleRobotEmptyScene(bullet_client, gravity=0.0, timestep=0.0165, frame_skip=1)

    def step(self, a):
        assert (not self.scene.multiplayer)

        self.robot.apply_action(a)
        self.scene.global_step()

        current_state = self.robot.calc_state()  # sets self.to_target_vec

        # potential_old = self.potential
        # self.potential = self.robot.calc_potential()

        # electricity_cost = (
        #         -0.10 * (     
        #                 np.abs(a[0] * self.robot.angle0_dot) + 
        #                 np.abs(a[1] * self.robot.angle0_dot) + 
        #                 np.abs(a[2] * self.robot.angle1_dot)
        #                 )   # work torque*angular_velocity
        #         - 0.01 * (
        #         np.abs(a[0]) + 
        #         np.abs(a[1]) + 
        #         np.abs(a[2])
        #                  )  # stall torque require some energy
        #                     )

        # stuck_joint_cost = 0
        # if np.abs(np.abs(self.robot.angle1) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        # if np.abs(np.abs(self.robot.angle2) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        
        # self.rewards = [float(self.potential - potential_old), float(electricity_cost), float(stuck_joint_cost)]
        # self.HUD(current_state, a, False)
        # tot_reward = sum(self.rewards)

        # define info
        info = self.robot.extra_info()

        obs = {'observation': current_state, 'achieved_goal': info['fingertip_coord'], 'desired_goal': info['target_coord']}

        tot_reward = self.compute_reward(obs['achieved_goal'], obs['desired_goal'], info)  # new HER goal

        # Define done: an episode is successful if the distance fingertip - target <= 0.01
        done = False

        # update info
        # info['is_success'] = self._is_success(obs['achieved_goal'], obs['desired_goal'])

        # if info["dist_ft_t"] <= 0.01:    
            # print("target reached!")
            # tot_reward += 10
            # done=True

        return obs, tot_reward, done, info

    # this should be equivalent ?
    def compute_reward(self, achieved_goal, desired_goal, info):
        self.dist_vec = np.array(achieved_goal - np.array(desired_goal))   
        return - np.linalg.norm(self.dist_vec)
        
    
    # def compute_reward(self, achieved_goal, desired_goal, p=0.5):
    #     """
    #         Proximity to the goal is rewarded

    #         We use a weighted p-norm
    #     :param achieved_goal: the goal that was achieved
    #     :param desired_goal: the goal that was desired
    #     :param p: the Lp^p norm used in the reward. Use p<1 to have high kurtosis for rewards in [0, 1]
    #     :return: the corresponding reward
    #     """
    #     return - np.power(np.dot(np.abs(achieved_goal - desired_goal), self.REWARD_WEIGHTS), p)


    # def _is_success(self, achieved_goal, desired_goal):
    #     return self.compute_reward(achieved_goal, desired_goal) > -self.SUCCESS_GOAL_REWARD


    # def extra_info(self):
    #     dist_ft_origin, dist_t_origin, dist_ft_t, max_reach, target_vect, fingertip_vect = self.robot.robot_info()

    #     info = {
    #         "dist_ft_origin": dist_ft_origin,
    #         "dist_t_origin": dist_t_origin,
    #         "dist_ft_t": dist_ft_t,
    #         "max_reach": max_reach,
    #         "target_coord": target_vect,
    #         "fingertip_coord": fingertip_vect
    #         }
        
    #     return info



    def camera_adjust(self):
        x, y, z = self.robot.fingertip.pose().xyz()
        x *= 0.5
        y *= 0.5
        self.camera.move_and_look_at(0.3, 0.3, 0.3, x, y, z)




class ReacherBulletEnv4(BaseBulletEnv):
    def __init__(self):
        self.robot = Reacher4()
        BaseBulletEnv.__init__(self, self.robot)

    def create_single_player_scene(self, bullet_client):
        return SingleRobotEmptyScene(bullet_client, gravity=0.0, timestep=0.0165, frame_skip=1)

    def step(self, a):
        assert (not self.scene.multiplayer)
        self.robot.apply_action(a)
        self.scene.global_step()

        current_state = self.robot.calc_state()  # sets self.to_target_vec

        # potential_old = self.potential
        # self.potential = self.robot.calc_potential()

        # electricity_cost = (
        #         -0.10 * (     
        #                 np.abs(a[0] * self.robot.angle0_dot) + 
        #                 np.abs(a[1] * self.robot.angle0_dot) + 
        #                 np.abs(a[2] * self.robot.angle0_dot) + 
        #                 np.abs(a[3] * self.robot.angle1_dot)
        #                 )   # work torque*angular_velocity
        #         - 0.01 * (
        #         np.abs(a[0]) + 
        #         np.abs(a[1]) + 
        #         np.abs(a[2]) + 
        #         np.abs(a[3])
        #                  )  # stall torque require some energy
        #                     )

        # stuck_joint_cost = 0
        # if np.abs(np.abs(self.robot.angle1) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        # if np.abs(np.abs(self.robot.angle2) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        # if np.abs(np.abs(self.robot.angle3) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        
        # self.rewards = [float(self.potential - potential_old), float(electricity_cost), float(stuck_joint_cost)]
        # self.HUD(current_state, a, False)
        # tot_reward = sum(self.rewards)

        # define info
        info = self.robot.extra_info()

        obs = {'observation': current_state, 'achieved_goal': info['fingertip_coord'], 'desired_goal': info['target_coord']}

        tot_reward = self.compute_reward(obs['achieved_goal'], obs['desired_goal'], info)  # new HER goal

        # Define done: an episode is successful if the distance fingertip - target <= 0.01
        done = False

        # update info
        # info['is_success'] = self._is_success(obs['achieved_goal'], obs['desired_goal'])

        # if info["dist_ft_t"] <= 0.01:    
            # print("target reached!")
            # tot_reward += 10
            # done=True

        return obs, tot_reward, done, info

    # this should be equivalent ?
    def compute_reward(self, achieved_goal, desired_goal, info):
        self.dist_vec = np.array(achieved_goal - np.array(desired_goal))   
        return - np.linalg.norm(self.dist_vec)
        
    
    # def compute_reward(self, achieved_goal, desired_goal, p=0.5):
    #     """
    #         Proximity to the goal is rewarded

    #         We use a weighted p-norm
    #     :param achieved_goal: the goal that was achieved
    #     :param desired_goal: the goal that was desired
    #     :param p: the Lp^p norm used in the reward. Use p<1 to have high kurtosis for rewards in [0, 1]
    #     :return: the corresponding reward
    #     """
    #     return - np.power(np.dot(np.abs(achieved_goal - desired_goal), self.REWARD_WEIGHTS), p)


    # def _is_success(self, achieved_goal, desired_goal):
    #     return self.compute_reward(achieved_goal, desired_goal) > -self.SUCCESS_GOAL_REWARD


    # def extra_info(self):
    #     dist_ft_origin, dist_t_origin, dist_ft_t, max_reach, target_vect, fingertip_vect = self.robot.robot_info()

    #     info = {
    #         "dist_ft_origin": dist_ft_origin,
    #         "dist_t_origin": dist_t_origin,
    #         "dist_ft_t": dist_ft_t,
    #         "max_reach": max_reach,
    #         "target_coord": target_vect,
    #         "fingertip_coord": fingertip_vect
    #         }
        
    #     return info



    def camera_adjust(self):
        x, y, z = self.robot.fingertip.pose().xyz()
        x *= 0.5
        y *= 0.5
        self.camera.move_and_look_at(0.3, 0.3, 0.3, x, y, z)



class ReacherBulletEnv5(BaseBulletEnv):
    def __init__(self):
        self.robot = Reacher5()
        BaseBulletEnv.__init__(self, self.robot)

    def create_single_player_scene(self, bullet_client):
        return SingleRobotEmptyScene(bullet_client, gravity=0.0, timestep=0.0165, frame_skip=1)

    def step(self, a):
        assert (not self.scene.multiplayer)
        self.robot.apply_action(a)
        self.scene.global_step()

        current_state = self.robot.calc_state()  # sets self.to_target_vec

        # potential_old = self.potential
        # self.potential = self.robot.calc_potential()

        # electricity_cost = (
        #         -0.10 * (     
        #                 np.abs(a[0] * self.robot.angle0_dot) + 
        #                 np.abs(a[1] * self.robot.angle0_dot) + 
        #                 np.abs(a[2] * self.robot.angle0_dot) + 
        #                 np.abs(a[3] * self.robot.angle0_dot) + 
        #                 np.abs(a[4] * self.robot.angle1_dot)
        #                 )   # work torque*angular_velocity
        #         - 0.01 * (
        #         np.abs(a[0]) + 
        #         np.abs(a[1]) + 
        #         np.abs(a[2]) + 
        #         np.abs(a[3]) + 
        #         np.abs(a[4])
        #                  )  # stall torque require some energy
        #                     )

        # stuck_joint_cost = 0
        # if np.abs(np.abs(self.robot.angle1) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        # if np.abs(np.abs(self.robot.angle2) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        # if np.abs(np.abs(self.robot.angle3) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        # if np.abs(np.abs(self.robot.angle4) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        
        # self.rewards = [float(self.potential - potential_old), float(electricity_cost), float(stuck_joint_cost)]
        # self.HUD(current_state, a, False)
        # tot_reward = sum(self.rewards)

        # define info
        info = self.robot.extra_info()

        obs = {'observation': current_state, 'achieved_goal': info['fingertip_coord'], 'desired_goal': info['target_coord']}

        tot_reward = self.compute_reward(obs['achieved_goal'], obs['desired_goal'], info)  # new HER goal

        # Define done: an episode is successful if the distance fingertip - target <= 0.01
        done = False

        # update info
        # info['is_success'] = self._is_success(obs['achieved_goal'], obs['desired_goal'])

        # if info["dist_ft_t"] <= 0.01:    
            # print("target reached!")
            # tot_reward += 10
            # done=True

        return obs, tot_reward, done, info

    # this should be equivalent ?
    def compute_reward(self, achieved_goal, desired_goal, info):
        self.dist_vec = np.array(achieved_goal - np.array(desired_goal))   
        return - np.linalg.norm(self.dist_vec)
        
    
    # def compute_reward(self, achieved_goal, desired_goal, p=0.5):
    #     """
    #         Proximity to the goal is rewarded

    #         We use a weighted p-norm
    #     :param achieved_goal: the goal that was achieved
    #     :param desired_goal: the goal that was desired
    #     :param p: the Lp^p norm used in the reward. Use p<1 to have high kurtosis for rewards in [0, 1]
    #     :return: the corresponding reward
    #     """
    #     return - np.power(np.dot(np.abs(achieved_goal - desired_goal), self.REWARD_WEIGHTS), p)


    # def _is_success(self, achieved_goal, desired_goal):
    #     return self.compute_reward(achieved_goal, desired_goal) > -self.SUCCESS_GOAL_REWARD


    # def extra_info(self):
    #     dist_ft_origin, dist_t_origin, dist_ft_t, max_reach, target_vect, fingertip_vect = self.robot.robot_info()

    #     info = {
    #         "dist_ft_origin": dist_ft_origin,
    #         "dist_t_origin": dist_t_origin,
    #         "dist_ft_t": dist_ft_t,
    #         "max_reach": max_reach,
    #         "target_coord": target_vect,
    #         "fingertip_coord": fingertip_vect
    #         }
        
    #     return info



    def camera_adjust(self):
        x, y, z = self.robot.fingertip.pose().xyz()
        x *= 0.5
        y *= 0.5
        self.camera.move_and_look_at(0.3, 0.3, 0.3, x, y, z)


class ReacherBulletEnv6(BaseBulletEnv):
    def __init__(self):
        self.robot = Reacher6()
        BaseBulletEnv.__init__(self, self.robot)

    def create_single_player_scene(self, bullet_client):
        return SingleRobotEmptyScene(bullet_client, gravity=0.0, timestep=0.0165, frame_skip=1)

    def step(self, a):
        assert (not self.scene.multiplayer)
        self.robot.apply_action(a)
        self.scene.global_step()

        current_state = self.robot.calc_state()  # sets self.to_target_vec

        # potential_old = self.potential
        # self.potential = self.robot.calc_potential()

        # electricity_cost = (
        #         -0.10 * (     
        #                 np.abs(a[0] * self.robot.angle0_dot) + 
        #                 np.abs(a[1] * self.robot.angle0_dot) + 
        #                 np.abs(a[2] * self.robot.angle0_dot) + 
        #                 np.abs(a[3] * self.robot.angle0_dot) + 
        #                 np.abs(a[4] * self.robot.angle0_dot) + 
        #                 np.abs(a[5] * self.robot.angle1_dot)
        #                 )   # work torque*angular_velocity
        #         - 0.01 * (
        #         np.abs(a[0]) + 
        #         np.abs(a[1]) + 
        #         np.abs(a[2]) + 
        #         np.abs(a[3]) + 
        #         np.abs(a[4]) + 
        #         np.abs(a[5])
        #                  )  # stall torque require some energy
        #                     )

        # stuck_joint_cost = 0
        # if np.abs(np.abs(self.robot.angle1) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        # if np.abs(np.abs(self.robot.angle2) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        # if np.abs(np.abs(self.robot.angle3) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        # if np.abs(np.abs(self.robot.angle4) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        # if np.abs(np.abs(self.robot.angle5) - 1) < 0.01:
        #     stuck_joint_cost -= 0.1
        
        # self.rewards = [float(self.potential - potential_old), float(electricity_cost), float(stuck_joint_cost)]
        # self.HUD(current_state, a, False)
        # tot_reward = sum(self.rewards)

        # define info
        info = self.robot.extra_info()

        obs = {'observation': current_state, 'achieved_goal': info['fingertip_coord'], 'desired_goal': info['target_coord']}

        tot_reward = self.compute_reward(obs['achieved_goal'], obs['desired_goal'], info)  # new HER goal

        # Define done: an episode is successful if the distance fingertip - target <= 0.01
        done = False

        # update info
        # info['is_success'] = self._is_success(obs['achieved_goal'], obs['desired_goal'])

        # if info["dist_ft_t"] <= 0.01:    
            # print("target reached!")
            # tot_reward += 10
            # done=True

        return obs, tot_reward, done, info

    # this should be equivalent ?
    def compute_reward(self, achieved_goal, desired_goal, info):
        self.dist_vec = np.array(achieved_goal - np.array(desired_goal))   
        return - np.linalg.norm(self.dist_vec)
        
    
    # def compute_reward(self, achieved_goal, desired_goal, p=0.5):
    #     """
    #         Proximity to the goal is rewarded

    #         We use a weighted p-norm
    #     :param achieved_goal: the goal that was achieved
    #     :param desired_goal: the goal that was desired
    #     :param p: the Lp^p norm used in the reward. Use p<1 to have high kurtosis for rewards in [0, 1]
    #     :return: the corresponding reward
    #     """
    #     return - np.power(np.dot(np.abs(achieved_goal - desired_goal), self.REWARD_WEIGHTS), p)


    # def _is_success(self, achieved_goal, desired_goal):
    #     return self.compute_reward(achieved_goal, desired_goal) > -self.SUCCESS_GOAL_REWARD


    # def extra_info(self):
    #     dist_ft_origin, dist_t_origin, dist_ft_t, max_reach, target_vect, fingertip_vect = self.robot.robot_info()

    #     info = {
    #         "dist_ft_origin": dist_ft_origin,
    #         "dist_t_origin": dist_t_origin,
    #         "dist_ft_t": dist_ft_t,
    #         "max_reach": max_reach,
    #         "target_coord": target_vect,
    #         "fingertip_coord": fingertip_vect
    #         }
        
    #     return info



    def camera_adjust(self):
        x, y, z = self.robot.fingertip.pose().xyz()
        x *= 0.5
        y *= 0.5
        self.camera.move_and_look_at(0.3, 0.3, 0.3, x, y, z)
