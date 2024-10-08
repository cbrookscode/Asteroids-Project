from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from shot import Shot
import sys
from player import Player
import pygame


def main():

    asteroids = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for sprites in updatable:
            sprites.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.is_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for sprites in drawable:
            sprites.draw(screen)

        pygame.display.flip()


        #limit frame rate to 60 fps
        dt = clock.tick(60) / 1000

if __name__=="__main__":
    main()