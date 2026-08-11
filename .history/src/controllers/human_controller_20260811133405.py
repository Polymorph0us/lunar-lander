import pygame

class HumanController:
    def __init__(self):
        self.append=True

    def get_action(self):
         """
        Convert keyboard input into a LunarLander action.

        Returns:
            0 = Do Nothing
            1 = Fire Left Engine
            2 = Fire Main Engine
            3 = Fire Right Engine
        """

         action=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    action=1
                elif event.key==pygame.K_UP:
                    action=2
                elif event.key==pygame.K_RIGHT:
                    action=3
            return action
