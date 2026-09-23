import pygame,os
pygame.font.init()

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invader Game!")

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)

FPS = 60

VEL = 5 #player velocity
BULLET_VEL = 7
MAX_BULLETS = 3

SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

#To customize the event
YELLOW_HIT = pygame.USEREVENT +1 
RED_HIT = pygame.USEREVENT +2

YELLOW_SPACESHIP_IMAGE= pygame.image.load(os.path.join('Assets','yellow_spaceship.png'))
RED_SPACESHIP_IMAGE= pygame.image.load(os.path.join('Assets','red_spaceship.png'))
SPACE_IMAGE= pygame.image.load(os.path.join('Assets','space.png'))

YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SPACE=pygame.transform.scale(SPACE_IMAGE,(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):

    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)

    red_health_text = HEALTH_FONT.render('Health:'+str(red_health),1,WHITE)
    WIN.blit(red_health_text,(700,10))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)


    yellow_health_text= HEALTH_FONT.render('Health:'+str(yellow_health,1,WHITE))
    WIN.blit(yellow_health_text,(10,10))
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)

    pygame.display.update()

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL #move right

        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x-=BULLET_VEL #move left

        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)