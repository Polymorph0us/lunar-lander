import pygame

class HumanController:
    def __init__(self):
        self.append=True

    def get_action(self, observation):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return 0  # Move left
                elif event.key == pygame.K_RIGHT:
                    return 1  # Move right
                elif event.key == pygame.K_UP:
                    return 2  # Thrust
                elif event.key == pygame.K_DOWN:
                    return 3  # No action / do nothing
        return None  # No action taken