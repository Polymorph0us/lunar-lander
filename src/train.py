import gymnasium as gym

from stable_baselines3 import PPO

# Create the environment
env = gym.make(
    "LunarLander-v3"
)

# Create the PPO model
model = PPO(
    policy="MlpPolicy",
    env=env,
    verbose=1,
    tensorboard_log="logs/"
)
TOTAL_TIMESTEPS = 1000000  # Total timesteps for training
# Train
model.learn(
    total_timesteps=TOTAL_TIMESTEPS
)

# Save
model.save("models/lunar_ppo")

env.close()