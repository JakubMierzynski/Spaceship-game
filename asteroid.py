import pygame
from pygame.math import Vector2


class Asteroid(object):

    def __init__(self, game):
        self.game = game
        self.size = game.screen.get_size()
        self.pos = Vector2(1100, 300) # Position
        self.gravity = Vector2(1, 0)
        self.vel = Vector2(0, 0)  # Velocity
        self.acc = Vector2(0, 0)  # Acceleration
        self.acc_value = 4.0

        # ASTEROID
        self.asteroid_img = pygame.image.load("/Users/jakubmierzynski/Desktop/Pygame/asteroid3.png")
        self.asteroid_model = pygame.transform.scale(self.asteroid_img, (100, 100))
        self.rocket_rect = self.asteroid_model.get_rect()
        self.rocket_mask = pygame.mask.from_surface(self.asteroid_model)

        # ROCKET MASK
        self.rocket_mask = pygame.mask.from_surface(self.asteroid_model)
        self.rocket_mask_pos = self.pos
        self.mask_image = self.rocket_mask.to_surface()

        # SPACE KEY
        self.space_pressed = False


    def tick(self):
        # Physics
        self.vel -= self.gravity # Velocity has to fight with gravity
        self.vel *= 0.8 # Velocity increases slower and decreases when button released

        self.vel += self.acc  # Velocity increased with acceleration

        self.pos += self.vel  # Position changed proportionally to velocity
        self.acc *= 0 # acc set to 0

    def draw(self):
        self.game.screen.blit(self.asteroid_model, self.pos)