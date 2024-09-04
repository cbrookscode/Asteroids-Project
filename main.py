from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
import sys
from player import Player
import pygame


def main():

    asteroids = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

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

        for objects in asteroids:
            if objects.is_collision(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for sprites in drawable:
            sprites.draw(screen)

        pygame.display.flip()


        #limit frame rate to 60 fps
        dt = clock.tick(60)

if __name__=="__main__":
    main()