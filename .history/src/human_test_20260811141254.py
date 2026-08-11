import gymnasium as gym
import pygame

from controllers.human_controller import HumanController


env = gym.make(
    "LunarLander-v3",
    render_mode="human"
)