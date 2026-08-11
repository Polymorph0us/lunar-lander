import gymnasium as gym
import numpy as np

from stable_baselines3 import PPO

from visualization import LunarMissionUI


MODEL_PATH = "models/lunar_ppo"

NUM_EPISODES = 5


env = gym.make(
    "LunarLander-v3"
)

model = PPO.load(MODEL_PATH)

ui = LunarMissionUI()


for episode in range(1, NUM_EPISODES + 1):

    observation, info = env.reset()

    terminated = False
    truncated = False

    total_reward = 0.0
    step = 0

    while not (terminated or truncated):

        action, _ = model.predict(
            observation,
            deterministic=True
        )

        # Convert numpy action -> Python integer
        action = int(
            np.asarray(action).reshape(-1)[0]
        )

        observation, reward, terminated, truncated, info = env.step(
            action
        )

        total_reward += reward
        step += 1

        ui.update(
            observation=observation,
            action=action,
            reward=reward,
            total_reward=total_reward,
            episode=episode,
            step=step,
            done=terminated or truncated
        )

    print(
        f"Episode {episode} | "
        f"Steps: {step} | "
        f"Reward: {total_reward:.2f}"
    )


env.close()
ui.close()