import pygame
import os
WIDTH,HEIGHT = 900,500
#making a window to display with certain width and height
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#Naming the game "Shooter Arena"
pygame.display.set_caption("Shooter Arena")
WHITE = (255,255,255)
BLACK = (0,0,0)
#making a verticle line(rectangle) at the middle of the window
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)
FPS = 60
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
VEL = 5
#loading pygame spaceship
yellow_Spaceship_image = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_Spaceship_image, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
red_Spaceship_image = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_Spaceship_image, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
def draw_window(red,yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(yellow_spaceship,(yellow.x,yellow.y))
    WIN.blit(red_spaceship,(red.x,red.y))
    pygame.display.update()
#yellow player movement
def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - SPACESHIP_HEIGHT:
        yellow.y += VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL < BORDER.x - 35:
        yellow.x += VEL
#red player movement
def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + 5:
        red.x -= VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL < HEIGHT - SPACESHIP_HEIGHT:
        red.y += VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH + 15 - SPACESHIP_WIDTH:
        red.x += VEL
#main function or gameplay function
def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        draw_window(red,yellow)
    pygame.quit()
if __name__ == "__main__":
    main()