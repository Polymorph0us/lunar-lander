from environments.lunar_wrapper import LunarLandingWrapper

env = LunarLandingWrapper()

observation, info = env.reset()

done = False

while not done:

    action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(action)

    done = terminated or truncated

env.close()