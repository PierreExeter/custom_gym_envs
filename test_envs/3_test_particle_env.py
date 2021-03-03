import gym
import gym_envs
import time


env = gym.make('particle-v0')
# env.render(mode="human")   

print("Action space: ", env.action_space)
print(env.action_space.high)
print(env.action_space.low)
print("Observation space: ", env.observation_space)
# print(env.observation_space.high)
# print(env.observation_space.low)


print("isinstance(env, gym.GoalEnv)", isinstance(env, gym.GoalEnv))

for episode in range(200):
    obs = env.reset()             
    rewards = []
    
    for t in range(100):
        env.render()  
        action = env.action_space.sample()  
        obs, reward, done, info = env.step(action) 
        rewards.append(reward)
        time.sleep(1./30.) 

        print("action: ", action)
        print("obs: ", obs)
        print("reward: ", reward)
        print("done: ", done)
        print("info: ", info)
        print("timestep: ", t)


    cumulative_reward = sum(rewards)
    print("episode {} | cumulative reward : {}".format(episode, cumulative_reward))  
    
env.close()


