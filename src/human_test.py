import gymnasium as gym
import pygame

from controllers.human_controller import HumanController
from visualization import LanderUI


NUM_EPISODES = 5


env = gym.make(
    "LunarLander-v3",
    render_mode="rgb_array"
)

controller = HumanController()
ui = LanderUI()

episode_rewards = []


for episode in range(NUM_EPISODES):

    observation, info = env.reset()

    terminated = False
    truncated = False

    total_reward = 0.0
    step = 0

    # Make sure controller is ready for the new episode
    controller.running = True

    while not (terminated or truncated):

        # Keyboard-controlled action
        action = controller.get_action()

        if not controller.running:
            break

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
            done=terminated or truncated,
            mode="HUMAN"
        )

        if not ui.running:
            controller.running = False
            break

    episode_rewards.append(total_reward)

    if not ui.running:
        break

    print(
        f"Human Episode {episode + 1}: "
        f"Reward = {total_reward:.2f}"
    )


# ----------------------------------------
# Summary
# ----------------------------------------

if episode_rewards:

    average_reward = (
        sum(episode_rewards) / len(episode_rewards)
    )

    best_reward = max(episode_rewards)
    worst_reward = min(episode_rewards)

    print("\n" + "=" * 40)
    print("HUMAN CONTROL RESULTS")
    print("=" * 40)

    print(
        f"Episodes completed : {len(episode_rewards)}"
    )

    print(
        f"Average reward     : {average_reward:.2f}"
    )

    print(
        f"Best reward        : {best_reward:.2f}"
    )

    print(
        f"Worst reward       : {worst_reward:.2f}"
    )


env.close()
ui.close()
pygame.quit()