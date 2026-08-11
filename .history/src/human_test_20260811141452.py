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

for episode in range(NUM_EPISODES):
    observation,info = env.reset()

    terminated=False
    truncated=False

    total_reward=0.0
    steps=0

    controller.running = True

    while not (terminated or truncated):

        action = controller.get_action()

        if not controller.running:
            break

        observation, reward, terminated, truncated, info = env.step(
            action
        )

        total_reward += reward
        steps += 1

    success = (
        terminated
        and observation[6] == 1
        and observation[7] == 1
        and abs(observation[4]) < 0.2
    )

    results.append({
        "episode": episode,
        "reward": total_reward,
        "steps": steps,
        "success": success
    })

    print(
        f"Episode {episode:02d} | "
        f"Reward: {total_reward:8.2f} | "
        f"Steps: {steps:3d} | "
        f"Success: {success}"
    )


print("\n========== HUMAN RESULTS ==========")

successful = sum(
    result["success"]
    for result in results
)

average_reward = sum(
    result["reward"]
    for result in results
) / len(results)

success_rate = (
    successful / NUM_EPISODES
) * 100

print(f"Successful landings : {successful}/{NUM_EPISODES}")
print(f"Success rate        : {success_rate:.1f}%")
print(f"Average reward      : {average_reward:.2f}")


env.close()
pygame.quit()