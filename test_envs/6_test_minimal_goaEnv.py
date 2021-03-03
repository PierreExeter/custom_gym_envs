import gym
import gym_envs


env = gym.make('my_goal_env-v0')

print("isinstance(env, gym.GoalEnv)", isinstance(env, gym.GoalEnv))