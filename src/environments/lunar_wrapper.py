import gymnasium as gym
from math import sqrt

from environments.reward_functions import distance_reward


class LunarLandingWrapper(gym.Wrapper):

    def __init__(self, render_mode=None):

        env = gym.make(
            "LunarLander-v3",
            render_mode=render_mode
        )

        super().__init__(env)

        self.previous_distance = None

    def reset(self, **kwargs):

        observation, info = self.env.reset(**kwargs)

        x, y = observation[:2]
        self.previous_distance = sqrt((x ** 2) + (y ** 2))

        return observation, info
    
    def step(self, action):

        observation, original_reward, terminated, truncated, info = self.env.step(action)

        x, y = observation[:2]
        current_distance = sqrt((x ** 2) + (y ** 2))

        distance_bonus = distance_reward(
            previous_distance=self.previous_distance,
            current_distance=current_distance
        )

        final_reward = original_reward + distance_bonus

        print(f"Original Reward : {original_reward:.2f}")
        print(f"Distance Bonus  : {distance_bonus:.2f}")
        print(f"Final Reward    : {final_reward:.2f}")

        self.previous_distance = current_distance

        return observation, final_reward, terminated, truncated, info

    