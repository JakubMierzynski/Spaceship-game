import math
import sys
import pygame
from rocket import Rocket
from asteroid import Asteroid

# Version
print(pygame.__version__)


class Game(object):
    def __init__(self):
        # Config
        # pygame.display.set_caption('Paper space plane')
        self.max_tps = 60  # ticks per second
        self.resolution = (1280, 720)
        self.screen_width = self.resolution[0]
        self.screen_height = self.resolution[1]
        self.screen = pygame.display.set_mode(size=self.resolution)
        self.box_rect = pygame.Rect(590, 310, 100, 100)
        self.time_of_play = 0

        # Initialization
        pygame.init()
        self.pause_text = pygame.font.SysFont('Consolas', 32).render('Pause', True, pygame.color.Color('White'))
        self.player = Rocket(self)
        self.screen = pygame.display.set_mode(size=self.resolution)
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.asteroid = Asteroid(self)

        # BACKGROUND VARIABLES
        # Background
        self.background = pygame.image.load('/Users/jakubmierzynski/Desktop/Pygame/Background2.jpg.webp')
        self.background_width = self.background.get_width()
        # Tiles
        self.tiles = math.ceil(self.screen_width / self.background_width) + 1
        # # Scroll
        self.scroll = 0
        self.scroll_vel = 1

        RUNNING, PAUSE = 0, 1
        state = RUNNING

        while True:
            # Handle event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p and state is RUNNING:
                        state = PAUSE
                        self.pause()
                    else:
                        state = RUNNING

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.max_tps:
                self.tick()
                self.tps_delta -= 1 / self.max_tps

            if state is RUNNING:
                # DRAWING
                self.screen.fill(color="black")

                # Drawing Background
                for i in range(0, self.tiles):
                    self.screen.blit(self.background, (i * self.background_width + self.scroll, 0))
                # Changing scroll to make movement
                self.scroll -= self.scroll_vel

                # Reset scroll to make it infitnie
                if abs(self.scroll) > self.background_width:
                    self.scroll = 0

                # Draw border of the game
                pygame.draw.rect(self.screen, "red", (0, 0, 1279, 719), 3)

                # Check masks overlap if collision- restart
                if self.player.rocket_mask.overlap(
                        self.asteroid.asteroid_mask, (self.asteroid.pos[0] - self.player.pos[0],
                                                      self.asteroid.pos[1] - self.player.pos[1])):
                    Game()
                else:
                    pass

                # Use Draw Function that draws player and later obstacles
                self.draw()

            if state is PAUSE:
                self.pause()

    def tick(self):
        self.player.tick()
        self.asteroid.tick()

    def pause(self):
        pause_text = pygame.font.SysFont('Consolas', 32).render('Pause', True, pygame.color.Color('White'))
        self.screen.blit(pause_text, (0, 0))

    def draw(self):
        # If player hits border: Restart.
        if self.player.pos.x <= 0 or self.player.pos.y <= 0 or self.player.pos.x >= 1280 or self.player.pos.y >= 720:
            Game()

        # Drawing Background
        for i in range(0, self.tiles):
            self.screen.blit(self.background, (i * self.background_width + self.scroll, 0))
        # Changing scroll to make movement
        self.time_of_play += 1 / 250

        # Reset scroll to make it infitnie
        if abs(self.scroll) > self.background_width:
            self.scroll = 0

        self.player.draw()
        self.asteroid.draw()
        pygame.display.flip()


if __name__ == "__main__":
    Game()
