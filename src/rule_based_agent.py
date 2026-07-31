import gymnasium as gym
import time

env = gym.make("LunarLander-v3", render_mode="human")

observation, info = env.reset()

done = False
total_reward = 0.0

def choose_action(obs):
    x, y, vx, vy, angle, angular_velocity, left_leg, right_leg = obs

    # 1. DYNAMIC DESCENT (Y-axis)
    # The closer to the ground (y -> 0), the slower we want to fall.
    # We subtract 0.05 to ensure the target velocity is always slightly downward so it eventually lands.
    target_vy = -0.4 * y - 0.05 
    y_error = target_vy - vy     # Positive if we are falling faster than target_vy

    # 2. DYNAMIC HORIZONTAL CONTROL (X-axis)
    # To move toward the center (x=0) and stop horizontal speed (vx=0), we must tilt the lander.
    target_angle = (x * 0.5) + (vx * 1.0)
    
    # Clamp the target angle to prevent the lander from flipping upside down
    target_angle = max(-0.4, min(target_angle, 0.4))

    # 3. ROTATIONAL STABILITY (Angle & Angular Velocity)
    # Calculate how far we are from our target angle.
    angle_error = target_angle - angle
    
    # Subtracting angular_velocity acts as a dampener (brakes) so we don't overshoot and spin.
    turn_signal = (angle_error * 0.5) - (angular_velocity * 1.0)

    # 4. ACTION SELECTION
    # Safety first: If the legs are touching the ground, cut the main engine and just try to stay upright.
    if left_leg or right_leg:
        if angle > 0.05: 
            return 3
        if angle < -0.05: 
            return 1
        return 0

    # Prioritize firing main engine if we are falling too fast, or if we are dangerously tilted.
    if y_error > 0 or abs(angle) > 0.5:
        return 2  # Fire Main Engine

    # If vertical speed is stable, use side engines to adjust orientation/position.
    if turn_signal > 0.05:
        return 1  # Fire Left Engine (tilts counter-clockwise / moves right)
    elif turn_signal < -0.05:
        return 3  # Fire Right Engine (tilts clockwise / moves left)

    return 0  # Do Nothing

while not done:
    action = choose_action(observation)

    observation, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    done = terminated or truncated
    time.sleep(0.03)

print(f"Total Reward: {total_reward:.2f}")
env.close()