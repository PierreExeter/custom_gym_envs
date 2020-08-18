import gym
import gym_envs


env = gym.make('tictac-v0')

for e in range(3):
    env.reset()
    print("######")
    print("EPISODE: ", e)
    print("######")

    for t in range(9):
        env.render()
        action = t
        state, reward, done, info = env.step(action) 
        print("reward: ", reward)
        print("******")

env.close()
