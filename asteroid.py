import pygame
from constants import *
from circleshape import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return

        log_event("asteroid_split")
        
        split_angle = random.uniform(20, 50)

        new_velocity1 = pygame.Vector2.rotate(self.velocity, split_angle)
        new_velocity2 = pygame.Vector2.rotate(self.velocity, -split_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_ast1.velocity = new_velocity1 * 1.2
        new_ast2.velocity = new_velocity2 * 1.2
