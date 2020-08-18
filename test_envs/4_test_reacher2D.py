import gym
import time
import pybullet_envs
import gym_envs

# env = gym.make('ReacherBulletEnv-v0')
# env = gym.make('Reacher1Dof-v0')
# env = gym.make('Reacher2Dof-v0')
# env = gym.make('Reacher3Dof-v0')
# env = gym.make('Reacher4Dof-v0')
# env = gym.make('Reacher5Dof-v0')
env = gym.make('Reacher6Dof-v0')

# with goal env
# env = gym.make('Reacher1Dof-v1')
# env = gym.make('Reacher2Dof-v1')
# env = gym.make('Reacher3Dof-v1')
# env = gym.make('Reacher4Dof-v1')
# env = gym.make('Reacher5Dof-v1')
# env = gym.make('Reacher6Dof-v1')


env.render(mode="human")   

print("Action space: ", env.action_space)
print(env.action_space.high)
print(env.action_space.low)
print("Observation space: ", env.observation_space)
# print(env.observation_space.high)   # comment for goalEnv
# print(env.observation_space.low)    # comment for goalEnv


for episode in range(50):
    obs = env.reset()             
    rewards = []
    
    for t in range(200):
        action = env.action_space.sample()  
        obs, reward, done, info = env.step(action) 

        print("action: ", action)
        print("obs: ", obs)
        print("reward: ", reward)
        print("done: ", done)
        print("info: ", info)
        print("timestep: ", t)

        rewards.append(reward)
        time.sleep(1./30.) 

    cumulative_reward = sum(rewards)
    print("episode {} | cumulative reward : {}".format(episode, cumulative_reward))  
    
env.close()


