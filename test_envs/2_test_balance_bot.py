import gym
import gym_envs
import time


env = gym.make("balancebot-v0")
# env = gym.make('ReacherPyBulletEnv-v0')

env.render(mode="human")  # this needs to be placed BEFORE env.reset() 
# env.reset() 

print("Action space: ", env.action_space)
# print(env.action_space.high)
# print(env.action_space.low)
print("Observation space: ", env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)


for episode in range(20):
    obs = env.reset()             
    rewards = []
    
    for t in range(200):               
        action = env.action_space.sample()  
        # action = [0.00001, 0]

        state, reward, done, info = env.step(action) 
        rewards.append(reward)

        print("action: ", action)
        print("obs: ", obs)
        print("reward: ", reward)
        print("done: ", done)
        print("info: ", info)
        print("timestep: ", t)

        time.sleep(1./30.) 

    cumulative_reward = sum(rewards)
    print("episode {} | cumulative reward : {}".format(episode, cumulative_reward))  
    
env.close()




