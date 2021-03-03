import time

import gym_envs.kuka_gym.kuka_moving_button_gym_env as kuka_env

# env = kuka_env.KukaButtonGymEnv(renders=True, is_discrete=True, log_folder="mobile_robot", record_data=False, random_target=False)
env = kuka_env.KukaMovingButtonGymEnv(renders=True)

timesteps = 1000  # must be greater than MAX_STEPS
episodes = 100
env.seed(1)
i = 0

print('Starting episodes...')
start_time = time.time()
try:
    for _ in range(episodes):
        observation = env.reset()
        for t in range(timesteps):
                action = env.action_space.sample()
                observation, reward, done, info = env.step(action)
                env.render()  # render() requires first the observation to be obtained
                if done:
                    print("Episode finished after {} timesteps".format(t + 1))
                    break
                i += 1
except KeyboardInterrupt:
    pass
print("Avg. frame rate: {:.2f} FPS".format(i / (time.time() - start_time)))
