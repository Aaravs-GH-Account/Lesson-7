import pygame,os
pygame.font.init()

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invader Game!")

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)

FPS = 60

VEL = 5 #player velocity
BULLET_VEL = 7
MAX_BULLETS = 3

SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

#To customize the event
BLUE_HIT = pygame.USEREVENT +1 
GREEN_HIT = pygame.USEREVENT +2

BLUE_SHIP_IMAGE= pygame.image.load(os.path.join('Assets','blue_ship.png'))
GREEN_SHIP_IMAGE= pygame.image.load(os.path.join('Assets','green_ship.png'))
SPACE_IMAGE= pygame.image.load(os.path.join('Assets','space.png'))

BLUE_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(BLUE_SHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
GREEN_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(GREEN_SHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SPACE=pygame.transform.rotate(pygame.transform.scale(SPACE_IMAGE,(WIDTH,HEIGHT)),90)

def draw_window(green,blue,green_bullets,blue_bullets,green_health,blue_health):

    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)

    green_health_text = HEALTH_FONT.render('Health:'+str(green_health),1,WHITE)
    WIN.blit(green_health_text,(700,10))
    WIN.blit(GREEN_SPACESHIP,(green.x,green.y))

    for bullet in green_bullets:
        pygame.draw.rect(WIN,GREEN,bullet)


    blue_health_text= HEALTH_FONT.render('Health:'+str(blue_health,1,WHITE))
    WIN.blit(blue_health_text,(10,10))
    WIN.blit(BLUE_SPACESHIP,(blue.x,blue.y))

    for bullet in blue_bullets:
        pygame.draw.rect(WIN,BLUE,bullet)

    pygame.display.update()

def handle_bullets(blue_bullets,green_bullets,blue,green):
    
    for bullet in blue_bullets:
        bullet.x += BULLET_VEL #move right

        if green.colliderect(bullet):
            pygame.event.post(pygame.event.Event(GREEN_HIT))
            blue_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            blue_bullets.remove(bullet)

    for bullet in green_bullets:
        bullet.x-=BULLET_VEL #move left

        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            green_bullets.remove(bullet)
        elif bullet.x < 0:
            green_bullets.remove(bullet)