import datetime
import sys
from random import randint

import pygame
from pygame.math import Vector2


class Rocket(object):

    def __init__(self, game):
        self.game = game
        self.size = game.screen.get_size()

        self.pos = Vector2((self.size[0] / 2), (self.size[1] / 2)) # Position
        self.vel = Vector2(0, 0)  # Velocity
        self.acc = Vector2(0, 0)  # Acceleration
        self.acc_value = 4.0
        self.gravity = Vector2(0, -2)

        # ROCKET
        self.rocket_img = pygame.image.load("/Users/jakubmierzynski/Desktop/Pygame/rocket.png")
        self.rocket_model = pygame.transform.scale(self.rocket_img, (100, 100))
        self.rotated_model = pygame.transform.rotate(self.rocket_model, -90)
        self.rocket_rect = self.rotated_model.get_rect()
        self.rocket_mask = pygame.mask.from_surface(self.rotated_model)

        # self.rocket_rect = self.rocket_model.get_rect()
        # self.rocket_mask = pygame.mask.from_surface(self.rocket_model)

        # ROCKET MASK
        self.rocket_mask = pygame.mask.from_surface(self.rocket_model)
        self.rocket_mask_pos = self.pos
        self.mask_image = self.rocket_mask.to_surface()

        # SPACE KEY
        self.space_pressed = False

    def add_acc(self, force):
        self.acc += force

    def steering(self):
        # Input
        pressed = pygame.key.get_pressed()
        # space_pressed = False

        # Should be once pressed not hold, but doesnt work. Probably tick issue

        if pressed[pygame.K_SPACE] and self.space_pressed is False:
            self.add_acc(Vector2(0, -self.acc_value))
            self.space_pressed = True

    def tick(self):
        self.space_pressed = False
        self.steering()

        # Physics
        self.vel -= self.gravity # Velocity has to fight with gravity
        self.vel *= 0.8 # Velocity increases slower and decreases when button released

        self.vel += self.acc  # Velocity increased with acceleration

        self.pos += self.vel  # Position changed proportionally to velocity
        self.acc *= 0 # acc set to 0

    def draw(self):
        self.game.screen.blit(self.rotated_model, self.pos)