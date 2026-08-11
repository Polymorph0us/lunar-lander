import pygame


class HumanController:

    def __init__(self):
        self.running = True

    def get_action(self):

        # Process window events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.running = False

        # If user closed/escaped
        if not self.running:
            return 0

        # Check keys that are currently being held
        keys = pygame.key.get_pressed()

        # Main engine
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            return 2

        # Left engine
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            return 1

        # Right engine
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            return 3

        # Nothing pressed
        return 0