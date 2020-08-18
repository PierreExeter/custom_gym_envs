import gym, gym_envs, time


# env = gym.make('widowx_reacher-v0').start_sim(goal_oriented=False, render_bool=True)   # or .start_rospy(goal_oriented=False)
# env = gym.make('widowx_reacher-v1').start_rospy(goal_oriented=False)                   # requires a roscore to be running
# env = gym.make('widowx_reacher-v2')                                              # requires a roscore to be running
# env = gym.make('widowx_reacher-v3')                                              # requires a roscore to be running
# env = gym.make('widowx_reacher-v4').start_sim(goal_oriented=False, render_bool=True)
env = gym.make('widowx_reacher-v5')
# env = gym.make('widowx_reacher-v6')  
# env = gym.make('widowx_reacher-v7')  
# env = gym.make('widowx_reacher-v8')  
# env = gym.make('widowx_reacher-v12')  
# env = gym.make('widowx_reacher-v13')  


print("isinstance(env, gym.GoalEnv)", isinstance(env, gym.GoalEnv))
print(env)

# # comment this when using widowx_reacher-v3 and widowx_reacher-v6 (goal oriented env, observation is a dict)
print("Action space: ", env.action_space)
print(env.action_space.high)
print(env.action_space.low)
print("Observation space: ", env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)


for episode in range(10):
    obs = env.reset()             
    rewards = []
    
    for t in range(1002):
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
