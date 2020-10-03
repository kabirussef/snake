import pygame, random
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 196, 0))

apple_pos = (random.randint(0,590), random.randint(0,590))
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1] - 10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1] - 10)

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
