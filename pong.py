import pygame
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_PINK = (255,150,196)
COLOR_WHITE = (255, 255, 255)

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption('Pink Pong')

    while True:
        window.fill(COLOR_PINK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
        
# Rect: rectangular sprite with collisions
# by default, a positive ball_x will make the ball go right
# positive ball_y will make the ball go down (ball acceleration)
    paddle1_rect = pygame.Rect(30, 0, 7, 100)
    paddle2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

    p1_move = 0
    p2_move = 0

    ball_rectangle = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)

    ball_speedx = random.randint(2,4) * 0.1
    ball_speedy = random.randint(2,4) * 0.1

    if random.randint(1,2) == 1:
        ball_speedx *= -1
    if random.randint(1,2) == 1:
        ball_speedy *= -1
    
    pygame.draw.rect(window, COLOR_WHITE, paddle1_rect)
    pygame.draw.rect(window, COLOR_WHITE, paddle2_rect)

    pygame.draw.rect(window, COLOR_WHITE, ball_rectangle)
    
    pygame.display.update()

if __name__ == '__main__':
    main()