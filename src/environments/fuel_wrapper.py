import gymnasium as gym
import numpy as np
from gymnasium import spaces


class FuelWrapper(gym.Wrapper):

    def __init__(
        self,
        env,
        initial_fuel=100.0,
        main_engine_cost=0.30,
        side_engine_cost=0.10,
    ):
        super().__init__(env)

        self.initial_fuel = initial_fuel
        self.main_engine_cost = main_engine_cost
        self.side_engine_cost = side_engine_cost

        self.fuel = initial_fuel

        # Original LunarLander observation has 8 values.
        # We add fuel as the 9th value.
        low = np.append(
            self.env.observation_space.low,
            0.0
        )

        high = np.append(
            self.env.observation_space.high,
            initial_fuel
        )

        self.observation_space = spaces.Box(
            low=low,
            high=high,
            dtype=np.float32
        )

    def reset(self, **kwargs):

        observation, info = self.env.reset(**kwargs)

        self.fuel = self.initial_fuel

        observation = self._add_fuel(observation)

        return observation, info

    def step(self, action):

        # Calculate fuel consumption BEFORE stepping.
        fuel_used = self._fuel_cost(action)

        self.fuel = max(
            0.0,
            self.fuel - fuel_used
        )

        observation, reward, terminated, truncated, info = (
            self.env.step(action)
        )

        # If fuel reaches zero, the lander can no longer use engines.
        # We terminate the episode so the agent must learn to manage fuel.
        if self.fuel <= 0.0:
            terminated = True

        observation = self._add_fuel(observation)

        # Add fuel information to info for evaluation/UI.
        info = dict(info)
        info["fuel"] = self.fuel
        info["fuel_used"] = fuel_used

        return (
            observation,
            reward,
            terminated,
            truncated,
            info,
        )

    def _fuel_cost(self, action):

        action = int(action)

        if action == 2:
            # Main engine
            return self.main_engine_cost

        if action in (1, 3):
            # Side engines
            return self.side_engine_cost

        # Do nothing
        return 0.0

    def _add_fuel(self, observation):

        return np.append(
            observation,
            self.fuel
        ).astype(np.float32)