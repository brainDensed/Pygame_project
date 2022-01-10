import pygame
import os
WIDTH,HEIGHT = 900,500
#making a window to display with certain width and height
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#Naming the game "Shooter Arena"
pygame.display.set_caption("Shooter Arena")
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
#making a verticle line(rectangle) at the middle of the window
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
FPS = 60
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#loading pygame spaceship
yellow_Spaceship_image = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_Spaceship_image, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
red_Spaceship_image = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_Spaceship_image, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

#Visual Function
def draw_window(red,yellow,red_bullets,yellow_bullets):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(yellow_spaceship,(yellow.x,yellow.y))
    WIN.blit(red_spaceship,(red.x,red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()

#yellow player movement
def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x + 10 - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL + 5 > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL - 5 < HEIGHT - SPACESHIP_HEIGHT - 15:
        yellow.y += VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL < BORDER.x - 35:
        yellow.x += VEL

#red player movement
def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + 5:
        red.x -= VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL + 5> 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL - 5< HEIGHT - SPACESHIP_HEIGHT - 15:
        red.y += VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL - 10< WIDTH + 15 - SPACESHIP_WIDTH:
        red.x += VEL

#bullets handling or counting bullets in this function
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

#main function
def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red_bullets = []
    yellow_bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width - 15, yellow.y + 7.5 +  yellow.height//2 - 2, 10 , 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x - 10, red.y + 7.95 + red.height//2 - 2, 10 , 5)
                    red_bullets.append(bullet)
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow, red_bullets, yellow_bullets)
    pygame.quit()
if __name__ == "__main__":
    main()
