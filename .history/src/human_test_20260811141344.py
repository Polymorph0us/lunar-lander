import gymnasium as gym
import pygame

from controllers.human_controller import HumanController

NUM_EPISODES=5
env = gym.make(
    "LunarLander-v3",
    render_mode="human"
)

controller=HumanController()

results=[]

for episo