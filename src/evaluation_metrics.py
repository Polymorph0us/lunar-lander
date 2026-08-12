import math


def calculate_landing_metrics(observation, total_reward, steps):
    """
    Calculate metrics from the final LunarLander observation.
    """

    x = float(observation[0])
    y = float(observation[1])
    vx = float(observation[2])
    vy = float(observation[3])
    angle = float(observation[4])

    left_leg = bool(observation[6])
    right_leg = bool(observation[7])

    # Target is the center of the landing zone.
    # LunarLander's default target is approximately x = 0.
    landing_distance = math.sqrt(
        x ** 2 + y ** 2
    )

    return {
        "success": (
            left_leg
            and right_leg
            and abs(vx) < 0.3
            and abs(vy) < 0.3
            and abs(angle) < 0.2
        ),

        "landing_distance": landing_distance,

        "final_vx": abs(vx),

        "final_vy": abs(vy),

        "final_angle": abs(angle),

        "reward": float(total_reward),

        "steps": int(steps),
    }