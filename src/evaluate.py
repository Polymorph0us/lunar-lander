import gymnasium as gym
from stable_baselines3 import PPO

from visualization import LanderUI


env = gym.make(
    "LunarLander-v3",
    render_mode="rgb_array"
)

ui = LanderUI()

model = PPO.load("models/lunar_ppo")

NUM_EPISODES = 10
SUCCESS_THRESHOLD = 200.0

episode_rewards = []
successes = 0

for episode in range(NUM_EPISODES):

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

        action = int(action)

        observation, reward, terminated, truncated, info = env.step(
            action
        )

        total_reward += reward
        step += 1

        frame = env.render()

        ui.update(
            frame=frame,
            observation=observation,
            reward=reward,
            action=action,
            episode=episode + 1,
            step=step,
            done=terminated or truncated
        )

        if not ui.running:
            terminated = True
            break

    episode_rewards.append(total_reward)

    if total_reward >= SUCCESS_THRESHOLD:
        successes += 1


average_reward = sum(episode_rewards) / NUM_EPISODES
best_reward = max(episode_rewards)
worst_reward = min(episode_rewards)

success_rate = successes / NUM_EPISODES * 100
crash_rate = 100 - success_rate


print(f"Episodes: {NUM_EPISODES}")
print()
print(f"Average Reward: {average_reward:.1f}")
print()
print(f"Best Reward: {best_reward:.1f}")
print()
print(f"Worst Reward: {worst_reward:.1f}")
print()
print(f"Success Rate: {success_rate:.0f}%")
print()
print(f"Crash Rate: {crash_rate:.0f}%")


env.close()
ui.close()