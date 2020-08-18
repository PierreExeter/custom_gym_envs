import os
import copy
import numpy as np

import gym
from gym import error, spaces
from gym.utils import seeding
from collections import OrderedDict


def goal_distance(goal_a, goal_b):
    assert goal_a.shape == goal_b.shape
    return np.linalg.norm(goal_a - goal_b, axis=-1)


class ParticleEnv(gym.GoalEnv):
    def __init__(self):
        self.metadata = {
            #TODO understand what to do with render modes
            'render.modes': ['human', 'rgb_array'],
            'video.frames_per_second': 50
        }

        # Env variables
        self.min_action = -1.0
        self.max_action = 1.0
        self.min_position = -1.0
        self.max_position = 1.0
        self.distance_threshold = 0.05 # Default 0.05
        self.max_speed = 0.05
        self.power = self.max_speed/20
        self.state = None
        self.reward_type = "sparse"

        # Env Spaces
        self.min_positions = np.array([self.min_position, self.min_position])
        self.max_positions = np.array([self.max_position, self.max_position])
        min_state = np.array([self.min_position, self.min_position,
                              -self.max_speed, -self.max_speed])
        max_state = np.array([self.max_position, self.max_position,
                             self.max_speed, self.max_speed])
        min_action = np.array([-1, -1])
        max_action = np.array([1, 1])
        self.action_space = spaces.Box(min_action, max_action, dtype='float32')
        self.start_state_space = spaces.Box(low=min_state, high=max_state)
        self.observation_space = spaces.Dict(dict(
            desired_goal=spaces.Box(self.min_positions, self.max_positions, dtype='float32'),
            achieved_goal=spaces.Box(self.min_positions, self.max_positions, dtype='float32'),
            observation=spaces.Box(min_state, max_state, dtype='float32'),
        ))

        # Setup
        self.viewer = None
        self.seed()
        self.goal = self._sample_goal()
        self.reset()

    # Env methods
    # ----------------------------

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        position = self.state[0:2].copy()
        velocity = self.state[2:4].copy()
        force = np.clip(action, self.action_space.low, self.action_space.high)
        velocity += force*self.power
        velocity = np.clip(velocity, np.array([-self.max_speed, -self.max_speed]),
                           np.array([self.max_speed, self.max_speed]))
        position += velocity
        clip_position = np.clip(position, self.min_positions, self.max_positions)
        # Invert appropriate velocity component after collision and bounce off
        # of a wall.
        collision = (position == clip_position).astype(int)
        collision[collision == 0] = -1
        velocity = np.multiply(velocity, collision)
        # Set state
        self.state[0:2] = clip_position
        self.state[2:4] = velocity
        obs = self._get_obs()
        info = {
            'is_success': self._is_success(obs['achieved_goal'], self.goal),
        }
        done = info['is_success']
        reward = self.compute_reward(obs['achieved_goal'], self.goal, info)
        return obs, reward, done, info

    def reset(self):
        self.state = self.start_state_space.sample().copy()
        self.goal = self._sample_goal().copy()
        obs = self._get_obs()
        return obs

    def close(self):
        if self.viewer is not None:
            self.viewer.finish()
            self.viewer = None

    def render(self, mode='human'):
        screen_width = 400
        screen_height = 400

        world_width = self.max_position - self.min_position
        scale_w = screen_width / world_width
        scale_h = screen_height / world_width
        point_radius = np.ceil(scale_w * self.distance_threshold / 2)

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)
            self.agent_trans = rendering.Transform()
            agent_circle = rendering.make_circle(point_radius)
            agent_circle.set_color(.8, .2, .2)
            agent_circle.add_attr(self.agent_trans)
            self.viewer.add_geom(agent_circle)
            self.goal_trans = rendering.Transform()
            goal_circle = rendering.make_circle(point_radius)
            goal_circle.set_color(.2, .8, .2)
            goal_circle.add_attr(self.goal_trans)
            self.viewer.add_geom(goal_circle)

        pos = self.state[0:2]
        self.agent_trans.set_translation((pos[0] - self.min_position) * scale_w,
                                         (pos[1] - self.min_position) * scale_h)
        self.goal_trans.set_translation((self.goal[0] - self.min_position) * scale_w,
                                         (self.goal[1] - self.min_position) * scale_h)

        return self.viewer.render(return_rgb_array=mode == 'rgb_array')

    # Extension methods
    # ----------------------------
    def _get_obs(self):
        return OrderedDict([("desired_goal", self.goal.copy()),
                            ("achieved_goal", self.state[0:2].copy()),
                            ("observation", self.state.copy())])

    def _is_success(self, achieved_goal, desired_goal):
        """Indicates whether or not the achieved goal successfully achieved the desired goal.
        """
        success = ((goal_distance(desired_goal, achieved_goal) <
                   self.distance_threshold)).astype(np.float32)
        if success:
            print("Success!!! With distance of {} between a_g:{}, and d_g {}"
                  "!".format(goal_distance(achieved_goal, desired_goal),
                             achieved_goal, desired_goal))
        return success

    def _sample_goal(self):
        """Samples a new goal and returns it.
        """
        goal = self.observation_space.sample()["desired_goal"].copy()
        return goal

    # GoalEnv methods
    # ----------------------------

    def compute_reward(self, achieved_goal, goal, info):
        dist = goal_distance(achieved_goal, goal)
        if self.reward_type == 'sparse':
            return (dist <= self.distance_threshold).astype(np.float32)
        else:
            return -dist
