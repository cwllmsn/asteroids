import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fill the screen with black
        updateable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit(0)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()
