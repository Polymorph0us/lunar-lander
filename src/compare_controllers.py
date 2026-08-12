import gymnasium as gym
import numpy as np
from stable_baselines3 import PPO

from controllers.human_controller import HumanController


MODEL_PATH = "models/lunar_ppo"
NUM_EPISODES = 10


def evaluate_ppo():

    env = gym.make("LunarLander-v3")
    model = PPO.load(MODEL_PATH)

    rewards = []
    steps = []
    successes = 0

    for episode in range(NUM_EPISODES):

        observation, info = env.reset()

        terminated = False
        truncated = False

        total_reward = 0.0
        episode_steps = 0

        while not (terminated or truncated):

            action, _ = model.predict(
                observation,
                deterministic=True
            )

            action = int(
                np.asarray(action).reshape(-1)[0]
            )

            observation, reward, terminated, truncated, info = env.step(
                action
            )

            total_reward += reward
            episode_steps += 1

        success = (
            observation[6] == 1
            and observation[7] == 1
            and abs(observation[4]) < 0.2
        )

        if success:
            successes += 1

        rewards.append(total_reward)
        steps.append(episode_steps)

    env.close()

    return {
        "successes": successes,
        "success_rate": successes / NUM_EPISODES * 100,
        "average_reward": np.mean(rewards),
        "average_steps": np.mean(steps),
    }


def print_results(name, results):

    print("\n" + "=" * 40)
    print(name)
    print("=" * 40)

    print(
        f"Successful landings : "
        f"{results['successes']}/{NUM_EPISODES}"
    )

    print(
        f"Success rate        : "
        f"{results['success_rate']:.1f}%"
    )

    print(
        f"Average reward      : "
        f"{results['average_reward']:.2f}"
    )

    print(
        f"Average steps       : "
        f"{results['average_steps']:.1f}"
    )


print("Evaluating PPO...")

ppo_results = evaluate_ppo()

print_results(
    "PPO",
    ppo_results
)