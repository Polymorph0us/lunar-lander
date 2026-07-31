import gymnasium as gym
import time


ACTION_NAMES = {
    0: "Do Nothing",
    1: "Fire Left Engine",
    2: "Fire Main Engine",
    3: "Fire Right Engine",
}


def print_observation(observation, reward, action):
    position_x, position_y, velocity_x, velocity_y, angle, angular_velocity, left_leg_contact, right_leg_contact = observation

    print("------------------------")
    print(f"Position:\n  x = {position_x:.2f}\n  y = {position_y:.2f}")
    print(f"\nVelocity:\n  vx = {velocity_x:.2f}\n  vy = {velocity_y:.2f}")
    print(f"\nAngle:\n  {angle:.2f}")
    print(f"\nAngular Velocity:\n  {angular_velocity:.2f}")
    print(f"\nLeft Leg Contact:\n  {bool(left_leg_contact)}")
    print(f"\nRight Leg Contact:\n  {bool(right_leg_contact)}")
    print(f"\nReward:\n  {reward:.2f}")
    print(f"\nChosen Action:\n  {ACTION_NAMES.get(action, str(action))}")


env = gym.make("LunarLander-v3", render_mode="human")

observation, info = env.reset()

done = False

while not done:
    action = env.action_space.sample()  # Random action for demonstration
    observation, reward, terminated, truncated, info = env.step(action)
    print_observation(observation, reward, action)

    done = terminated or truncated

    time.sleep(0.05)

env.close()