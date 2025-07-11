import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def split(self):
        self.kill()  # Remove the asteroid from the game
        # Logic to split the asteroid into smaller ones
        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius / 2
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = self.velocity.rotate(30)
            new_asteroid2.velocity = self.velocity.rotate(-30)
            return new_asteroid1, new_asteroid2

    def update(self, dt):
        self.position += self.velocity * dt