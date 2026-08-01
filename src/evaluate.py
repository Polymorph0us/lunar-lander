import gymnasium as gym
from stable_baselines3 import PPO

# Create environment with rendering enabled
env = gym.make(
    "LunarLander-v3",
    render_mode="human"
)

# Load the trained model
model = PPO.load("models/lunar_ppo")

# Number of episodes to evaluate
NUM_EPISODES = 5

for episode in range(NUM_EPISODES):

    observation, info = env.reset()

    terminated = False
    truncated = False

    total_reward = 0
    step = 0

    while not (terminated or truncated):

        # Ask the trained model what action to take
        action, _ = model.predict(
            observation,
            deterministic=True
        )

        observation, reward, terminated, truncated, info = env.step(action)

        total_reward += reward
        step += 1

    print(f"Episode {episode + 1}")
    print(f"Steps: {step}")
    print(f"Total Reward: {total_reward:.2f}")
    print("-" * 40)

env.close()