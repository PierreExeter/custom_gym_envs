import gym
import gym_envs
import time


env = gym.make("balancebot-v0")
# env = gym.make('ReacherPyBulletEnv-v0')

env.render(mode="human")  # this needs to be placed BEFORE env.reset() 
# env.reset() 

print(env.action_space)
# print(env.action_space.high)
# print(env.action_space.low)
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)


for episode in range(20):
    state = env.reset()             
    rewards = []
    
    for t in range(1000):
        # env.render(mode="human")                 
        action = 1 #env.action_space.sample()  
        # action = [0.00001, 0]
        print(action)
        state, reward, done, info = env.step(action) 
        rewards.append(reward)
        time.sleep(1./30.) 

    cumulative_reward = sum(rewards)
    print("episode {} | cumulative reward : {}".format(episode, cumulative_reward))  
    
env.close()




