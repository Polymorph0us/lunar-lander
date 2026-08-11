import gymnasium as gym
import pygame

from controllers.human_controller import HumanController


env = gym.make(
    "LunarLander-v3",
    render_mode="human",
    gravity=-1
)

controller = HumanController()

observation, info = env.reset()

terminated = False
truncated = False

total_reward = 0.0

while not (terminated or truncated):

    action = controller.get_action()

    if not controller.running:
        break

    observation, reward, terminated, truncated, info = env.step(
        action
    )

    total_reward += reward


print(
    f"Human episode reward: {total_reward:.2f}"
)

env.close()
pygame.quit()