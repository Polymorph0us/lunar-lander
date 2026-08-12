import gymnasium as gym

from environments.fuel_wrapper import FuelWrapper


env = FuelWrapper(
    gym.make("LunarLander-v3")
)

observation, info = env.reset()

print("Initial observation:")
print(observation)

print("\nInitial fuel:")
print(observation[8])

for i in range(10):

    action = 2  # Main engine

    observation, reward, terminated, truncated, info = env.step(
        action
    )

    print(
        f"Step {i + 1:02d} | "
        f"Fuel: {observation[8]:.2f} | "
        f"Fuel used: {info['fuel_used']:.2f}"
    )

    if terminated or truncated:
        break

env.close()