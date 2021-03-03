import gym
import gym_envs
import time


# env = gym.make("balancebot-v0")
# env = gym.make('Reacher6Dof-v0')
env = gym.make('ReachingJaco-v1')

env.reset()
nb_timesteps = 100000

start = time.time()

for t in range(nb_timesteps):
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    print(t)

end = time.time()
tot = end - start
print("Execution time (s): ", tot)
print("Pybullet simulation time (s): ", nb_timesteps / 240)
print("Pybullet step time (s): ", 1/240)
print("Measured step time (s): ", tot / nb_timesteps)


env.close()