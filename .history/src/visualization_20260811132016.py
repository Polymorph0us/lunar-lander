import math
import pygame


ACTION_NAMES = {
    0: "DO NOTHING",
    1: "LEFT ENGINE",
    2: "MAIN ENGINE",
    3: "RIGHT ENGINE",
}


class LunarMissionUI:

    def __init__(self, width=1100, height=700):

        pygame.init()

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption(
            "Lunar Autonomous Landing | Mission Control"
        )

        self.clock = pygame.time.Clock()

        # Fonts
        self.title_font = pygame.font.SysFont(
            "consolas", 24, bold=True
        )

        self.section_font = pygame.font.SysFont(
            "consolas", 16, bold=True
        )

        self.text_font = pygame.font.SysFont(
            "consolas", 14
        )

        self.small_font = pygame.font.SysFont(
            "consolas", 12
        )

        # Game area
        self.game_width = 760
        self.panel_x = self.game_width
        self.panel_width = self.width - self.game_width

        # Stars are fixed so they don't move every frame
        self.stars = [
            (70, 80),
            (140, 150),
            (220, 65),
            (310, 120),
            (390, 55),
            (470, 170),
            (550, 90),
            (640, 135),
            (710, 60),
            (100, 230),
            (300, 210),
            (500, 250),
            (680, 220),
        ]

    # --------------------------------------------------
    # BASIC DRAWING
    # --------------------------------------------------

    def text(self, message, x, y, font=None):

        if font is None:
            font = self.text_font

        surface = font.render(
            str(message),
            True,
            (225, 225, 230)
        )

        self.screen.blit(surface, (x, y))

    def line(self, x1, y1, x2, y2):

        pygame.draw.line(
            self.screen,
            (65, 70, 80),
            (x1, y1),
            (x2, y2),
            1
        )

    # --------------------------------------------------
    # STAR FIELD
    # --------------------------------------------------

    def draw_stars(self):

        for x, y in self.stars:

            pygame.draw.circle(
                self.screen,
                (180, 185, 195),
                (x, y),
                1
            )

    # --------------------------------------------------
    # MOON TERRAIN
    # --------------------------------------------------

    def draw_terrain(self):

        ground = [
            (0, 545),
            (70, 520),
            (140, 535),
            (215, 500),
            (290, 525),
            (365, 505),
            (440, 540),
            (520, 515),
            (600, 535),
            (680, 510),
            (760, 530),
            (760, 700),
            (0, 700),
        ]

        pygame.draw.polygon(
            self.screen,
            (82, 84, 88),
            ground
        )

        # Surface line
        pygame.draw.lines(
            self.screen,
            (155, 157, 162),
            False,
            ground[:11],
            2
        )

        # Craters
        self.draw_crater(130, 585, 55, 18)
        self.draw_crater(400, 610, 75, 23)
        self.draw_crater(650, 580, 45, 16)

        # Small rocks
        self.draw_rock(250, 510, 10)
        self.draw_rock(560, 515, 13)
        self.draw_rock(710, 505, 8)

        # Landing zone
        self.draw_landing_zone()

    def draw_crater(self, x, y, width, height):

        pygame.draw.ellipse(
            self.screen,
            (55, 56, 60),
            (
                x - width,
                y - height,
                width * 2,
                height * 2
            )
        )

        pygame.draw.arc(
            self.screen,
            (125, 127, 132),
            (
                x - width,
                y - height,
                width * 2,
                height * 2
            ),
            math.pi,
            math.pi * 2,
            2
        )

    def draw_rock(self, x, y, size):

        points = [
            (x - size, y),
            (x - size // 2, y - size),
            (x + size // 2, y - size // 2),
            (x + size, y),
            (x + size // 2, y + size // 2),
            (x - size // 2, y + size // 2),
        ]

        pygame.draw.polygon(
            self.screen,
            (105, 107, 112),
            points
        )

    def draw_landing_zone(self):

        x1 = 300
        x2 = 460
        y = 505

        # Landing zone surface
        pygame.draw.line(
            self.screen,
            (90, 190, 170),
            (x1, y),
            (x2, y),
            4
        )

        # Landing zone markers
        pygame.draw.line(
            self.screen,
            (90, 190, 170),
            (x1, y),
            (x1, y - 18),
            2
        )

        pygame.draw.line(
            self.screen,
            (90, 190, 170),
            (x2, y),
            (x2, y - 18),
            2
        )

        self.text(
            "SAFE LANDING ZONE",
            318,
            475,
            self.small_font
        )

    # --------------------------------------------------
    # SPACECRAFT
    # --------------------------------------------------

    def draw_lander(
        self,
        observation,
        action
    ):

        x = observation[0]
        y = observation[1]
        angle = observation[4]

        # Convert LunarLander coordinates into screen coordinates.
        screen_x = 380 + int(x * 230)

        # Higher y = higher on screen
        screen_y = 470 - int(y * 230)

        # Spacecraft dimensions
        body_width = 48
        body_height = 58

        # Create transparent surface
        craft = pygame.Surface(
            (130, 150),
            pygame.SRCALPHA
        )

        center_x = 65
        center_y = 55

        # ------------------------------------------------
        # MAIN BODY
        # ------------------------------------------------

        body = [
            (center_x - 24, center_y - 20),
            (center_x + 24, center_y - 20),
            (center_x + 18, center_y + 28),
            (center_x - 18, center_y + 28),
        ]

        pygame.draw.polygon(
            craft,
            (170, 175, 185),
            body
        )

        pygame.draw.polygon(
            craft,
            (95, 100, 110),
            body,
            2
        )

        # ------------------------------------------------
        # COCKPIT
        # ------------------------------------------------

        pygame.draw.ellipse(
            craft,
            (55, 105, 125),
            (
                center_x - 15,
                center_y - 15,
                30,
                22
            )
        )

        pygame.draw.ellipse(
            craft,
            (120, 190, 205),
            (
                center_x - 11,
                center_y - 12,
                22,
                15
            ),
            2
        )

        # ------------------------------------------------
        # SIDE MODULES
        # ------------------------------------------------

        pygame.draw.rect(
            craft,
            (115, 120, 130),
            (
                center_x - 37,
                center_y - 5,
                13,
                30
            )
        )

        pygame.draw.rect(
            craft,
            (115, 120, 130),
            (
                center_x + 24,
                center_y - 5,
                13,
                30
            )
        )

        # ------------------------------------------------
        # LANDING LEGS
        # ------------------------------------------------

        pygame.draw.line(
            craft,
            (145, 150, 160),
            (center_x - 17, center_y + 25),
            (center_x - 34, center_y + 48),
            5
        )

        pygame.draw.line(
            craft,
            (145, 150, 160),
            (center_x + 17, center_y + 25),
            (center_x + 34, center_y + 48),
            5
        )

        pygame.draw.line(
            craft,
            (180, 185, 190),
            (center_x - 34, center_y + 48),
            (center_x - 43, center_y + 48),
            4
        )

        pygame.draw.line(
            craft,
            (180, 185, 190),
            (center_x + 34, center_y + 48),
            (center_x + 43, center_y + 48),
            4
        )

        # ------------------------------------------------
        # MAIN ENGINE
        # ------------------------------------------------

        if action == 2:

            flame = [
                (center_x - 10, center_y + 28),
                (center_x + 10, center_y + 28),
                (center_x, center_y + 62),
            ]

            pygame.draw.polygon(
                craft,
                (240, 145, 50),
                flame
            )

            pygame.draw.polygon(
                craft,
                (255, 220, 120),
                [
                    (center_x - 5, center_y + 30),
                    (center_x + 5, center_y + 30),
                    (center_x, center_y + 55),
                ]
            )

        # ------------------------------------------------
        # SIDE ENGINE FLAMES
        # ------------------------------------------------

        if action == 1:

            pygame.draw.polygon(
                craft,
                (240, 145, 50),
                [
                    (center_x - 38, center_y + 5),
                    (center_x - 50, center_y + 12),
                    (center_x - 38, center_y + 18),
                ]
            )

        if action == 3:

            pygame.draw.polygon(
                craft,
                (240, 145, 50),
                [
                    (center_x + 38, center_y + 5),
                    (center_x + 50, center_y + 12),
                    (center_x + 38, center_y + 18),
                ]
            )

        # Rotate entire spacecraft
        rotated = pygame.transform.rotate(
            craft,
            math.degrees(angle)
        )

        rect = rotated.get_rect(
            center=(screen_x, screen_y)
        )

        self.screen.blit(
            rotated,
            rect
        )

    # --------------------------------------------------
    # HUD
    # --------------------------------------------------

    def draw_hud(
        self,
        observation,
        action,
        reward,
        total_reward,
        episode,
        step,
        done
    ):

        x = self.panel_x

        # Panel
        pygame.draw.rect(
            self.screen,
            (20, 23, 28),
            (
                x,
                0,
                self.panel_width,
                self.height
            )
        )

        pygame.draw.line(
            self.screen,
            (90, 95, 105),
            (x, 0),
            (x, self.height),
            2
        )

        px = x + 25

        # Header
        self.text(
            "LUNAR LANDING",
            px,
            25,
            self.title_font
        )

        self.text(
            "MISSION CONTROL",
            px,
            57,
            self.small_font
        )

        self.line(
            px,
            82,
            self.width - 25,
            82
        )

        # Episode
        self.text(
            f"EPISODE       {episode}",
            px,
            105,
            self.section_font
        )

        self.text(
            f"STEP          {step}",
            px,
            132
        )

        # Position
        self.text(
            "POSITION",
            px,
            175,
            self.section_font
        )

        self.text(
            f"X             {observation[0]: .3f}",
            px,
            202
        )

        self.text(
            f"Y             {observation[1]: .3f}",
            px,
            226
        )

        # Velocity
        self.text(
            "VELOCITY",
            px,
            268,
            self.section_font
        )

        self.text(
            f"VX            {observation[2]: .3f}",
            px,
            295
        )

        self.text(
            f"VY            {observation[3]: .3f}",
            px,
            319
        )

        # Attitude
        self.text(
            "ATTITUDE",
            px,
            361,
            self.section_font
        )

        self.text(
            f"ANGLE         {math.degrees(observation[4]): .2f}°",
            px,
            388
        )

        self.text(
            f"ANGULAR VEL   {observation[5]: .3f}",
            px,
            412
        )

        # Landing gear
        self.text(
            "LANDING GEAR",
            px,
            454,
            self.section_font
        )

        self.text(
            f"LEFT          {'CONTACT' if observation[6] else 'CLEAR'}",
            px,
            481
        )

        self.text(
            f"RIGHT         {'CONTACT' if observation[7] else 'CLEAR'}",
            px,
            505
        )

        # Action
        self.text(
            "THRUSTER COMMAND",
            px,
            547,
            self.section_font
        )

        self.text(
            ACTION_NAMES.get(
                int(action),
                "UNKNOWN"
            ),
            px,
            574
        )

        # Reward
        self.text(
            f"REWARD        {reward: .2f}",
            px,
            616
        )

        self.text(
            f"TOTAL         {total_reward: .2f}",
            px,
            640
        )

        # Status
        status = (
            "MISSION COMPLETE"
            if done
            else "AUTONOMOUS FLIGHT"
        )

        self.text(
            status,
            px,
            675,
            self.small_font
        )

    # --------------------------------------------------
    # MAIN UPDATE
    # --------------------------------------------------

    def update(
        self,
        observation,
        action,
        reward,
        total_reward,
        episode,
        step,
        done=False
    ):

        # Window events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.close()
                raise SystemExit

        # Background
        self.screen.fill(
            (5, 7, 12)
        )

        # Scene
        self.draw_stars()

        self.draw_terrain()

        self.draw_lander(
            observation,
            action
        )

        # HUD
        self.draw_hud(
            observation,
            action,
            reward,
            total_reward,
            episode,
            step,
            done
        )

        pygame.display.flip()

        self.clock.tick(60)

    def close(self):

        pygame.quit()