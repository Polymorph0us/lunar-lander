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
         for event