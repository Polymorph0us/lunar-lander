import pygame
import numpy as np


ACTION_NAMES = {
    0: "DO NOTHING",
    1: "LEFT ENGINE",
    2: "MAIN ENGINE",
    3: "RIGHT ENGINE",
}


class LanderUI:

    def __init__(self, width=1200, height=700):

        pygame.init()

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode(
            (width, height)
        )

        pygame.display.set_caption(
            "LUNAR DESCENT — AI LANDING SIMULATOR"
        )

        self.clock = pygame.time.Clock()

        self.font_small = pygame.font.SysFont(
            "consolas",
            18
        )

        self.font_medium = pygame.font.SysFont(
            "consolas",
            24,
            bold=True
        )

        self.font_large = pygame.font.SysFont(
            "consolas",
            32,
            bold=True
        )

        self.running = True

    # --------------------------------------------------
    # EVENT HANDLING
    # --------------------------------------------------

    def process_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

    # --------------------------------------------------
    # TEXT
    # --------------------------------------------------

    def draw_text(
        self,
        text,
        x,
        y,
        font=None,
    ):

        if font is None:
            font = self.font_small

        surface = font.render(
            str(text),
            True,
            (235, 240, 245)
        )

        self.screen.blit(
            surface,
            (x, y)
        )

    # --------------------------------------------------
    # MAIN UPDATE
    # --------------------------------------------------

    def update(
    self,
    frame,
    observation,
    reward,
    action,
    episode,
    step,
    fuel=None,
    done=False,
    mode="AI",
):

        self.process_events()

        if not self.running:
            return

        # ------------------------------------------------
        # Convert Gym frame to pygame surface
        # ------------------------------------------------

        frame = np.asarray(frame)

        frame = np.transpose(
            frame,
            (1, 0, 2)
        )

        frame_surface = pygame.surfarray.make_surface(
            frame
        )

        # Resize the game frame
        game_width = 780
        game_height = 585

        frame_surface = pygame.transform.smoothscale(
            frame_surface,
            (game_width, game_height)
        )

        # ------------------------------------------------
        # Background
        # ------------------------------------------------

        self.screen.fill(
            (8, 12, 20)
        )

        # ------------------------------------------------
        # Header
        # ------------------------------------------------

        pygame.draw.rect(
            self.screen,
            (15, 22, 35),
            (0, 0, self.width, 70)
        )

        self.draw_text(
            "LUNAR DESCENT",
            25,
            18,
            self.font_large
        )

        self.draw_text(
            f"{mode.upper()} CONTROL",
            335,
            25,
            self.font_small
        )

        self.draw_text(
            f"EPISODE {episode}",
            1000,
            25,
            self.font_small
        )

        # ------------------------------------------------
        # Game viewport
        # ------------------------------------------------

        pygame.draw.rect(
            self.screen,
            (25, 30, 40),
            (15, 90, game_width + 10, game_height + 10)
        )

        self.screen.blit(
            frame_surface,
            (20, 95)
        )

        # ------------------------------------------------
        # Right HUD panel
        # ------------------------------------------------

        panel_x = 820
        panel_y = 90
        panel_width = 365
        panel_height = 585

        pygame.draw.rect(
            self.screen,
            (15, 22, 35),
            (
                panel_x,
                panel_y,
                panel_width,
                panel_height
            ),
            border_radius=8
        )

        self.draw_text(
            "FLIGHT TELEMETRY",
            panel_x + 25,
            panel_y + 25,
            self.font_medium
        )

        # ------------------------------------------------
        # Observation
        # ------------------------------------------------

        if observation is not None and len(observation) >= 8:

            x = float(observation[0])
            y = float(observation[1])

            vx = float(observation[2])
            vy = float(observation[3])

            angle = float(observation[4])
            angular_velocity = float(observation[5])

            left_leg = bool(observation[6])
            right_leg = bool(observation[7])

        else:

            x = y = vx = vy = 0.0
            angle = angular_velocity = 0.0

            left_leg = False
            right_leg = False

        row = panel_y + 85

        telemetry = [
            ("ALTITUDE", f"{y:.2f}"),
            ("VERTICAL V", f"{vy:.2f}"),
            ("HORIZONTAL V", f"{vx:.2f}"),
            ("ANGLE", f"{np.degrees(angle):.1f}°"),
            ("ANGULAR V", f"{angular_velocity:.2f}"),
        ]

        for label, value in telemetry:

            self.draw_text(
                label,
                panel_x + 25,
                row,
                self.font_small
            )

            self.draw_text(
                value,
                panel_x + 210,
                row,
                self.font_medium
            )

            row += 42

        # ------------------------------------------------
        # Fuel
        # ------------------------------------------------

        row += 10

        self.draw_text(
            "FUEL",
            panel_x + 25,
            row,
            self.font_small
        )

        if fuel is None:

            fuel_text = "N/A"

        else:

            fuel_text = f"{fuel:.1f}"

        self.draw_text(
            fuel_text,
            panel_x + 210,
            row,
            self.font_medium
        )

        row += 40

        # Fuel bar

        bar_x = panel_x + 25
        bar_y = row

        bar_width = 315
        bar_height = 18

        pygame.draw.rect(
            self.screen,
            (50, 55, 65),
            (
                bar_x,
                bar_y,
                bar_width,
                bar_height
            ),
            border_radius=5
        )

        if fuel is not None:

            percentage = max(
                0.0,
                min(1.0, fuel / 100.0)
            )

            pygame.draw.rect(
                self.screen,
                (255, 140, 50),
                (
                    bar_x,
                    bar_y,
                    int(bar_width * percentage),
                    bar_height
                ),
                border_radius=5
            )

        # ------------------------------------------------
        # Engine status
        # ------------------------------------------------

        row += 55

        self.draw_text(
            "CURRENT ACTION",
            panel_x + 25,
            row,
            self.font_small
        )

        action_name = ACTION_NAMES.get(
            int(action),
            "UNKNOWN"
        )

        self.draw_text(
            action_name,
            panel_x + 25,
            row + 28,
            self.font_medium
        )

        # ------------------------------------------------
        # Landing gear
        # ------------------------------------------------

        row += 85

        self.draw_text(
            "LANDING GEAR",
            panel_x + 25,
            row,
            self.font_small
        )

        self.draw_text(
            f"LEFT   {'CONTACT' if left_leg else 'AIR'}",
            panel_x + 25,
            row + 28
        )

        self.draw_text(
            f"RIGHT  {'CONTACT' if right_leg else 'AIR'}",
            panel_x + 25,
            row + 52
        )

        # ------------------------------------------------
        # Reward
        # ------------------------------------------------

        row += 100

        self.draw_text(
            "STEP REWARD",
            panel_x + 25,
            row,
            self.font_small
        )

        self.draw_text(
            f"{reward:.2f}",
            panel_x + 210,
            row,
            self.font_medium
        )

        # ------------------------------------------------
        # Episode status
        # ------------------------------------------------

        if done:

            pygame.draw.rect(
                self.screen,
                (25, 40, 30),
                (
                    20,
                    620,
                    780,
                    50
                ),
                border_radius=6
            )

            self.draw_text(
                "EPISODE COMPLETE",
                45,
                633,
                self.font_medium
            )

        # ------------------------------------------------
        # Present
        # ------------------------------------------------

        pygame.display.flip()

        self.clock.tick(30)

    # --------------------------------------------------
    # CLOSE
    # --------------------------------------------------

    def close(self):

        pygame.quit()