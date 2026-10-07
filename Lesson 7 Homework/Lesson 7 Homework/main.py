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

BLUE_SPACESHIP=pygame.transform.scale(BLUE_SHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
GREEN_SPACESHIP=pygame.transform.scale(GREEN_SHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
SPACE=pygame.transform.scale(SPACE_IMAGE,(WIDTH,HEIGHT))

def draw_window(green,blue,green_bullets,blue_bullets,green_health,blue_health):

    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)

    green_health_text = HEALTH_FONT.render('Health:'+str(green_health),1,WHITE)
    WIN.blit(green_health_text,(700,10))
    WIN.blit(GREEN_SPACESHIP,(green.x,green.y))

    for bullet in green_bullets:
        pygame.draw.rect(WIN,GREEN,bullet)


    blue_health_text= HEALTH_FONT.render('Health:'+str(blue_health),1,WHITE)
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
            
def blue_handle_movement(keys_pressed,blue):

    if keys_pressed[pygame.K_a] and blue.x - VEL > 0: #LEFT
        blue.x-=VEL

    if keys_pressed[pygame.K_d] and blue.x + VEL + blue.width < BORDER.x: #RIGHT
        blue.x+=VEL

    if keys_pressed[pygame.K_w] and blue.y - VEL > 0: #UP
        blue.y-=VEL

    if keys_pressed[pygame.K_s] and blue.y + VEL + blue.height < HEIGHT: #DOWN
        blue.y+=VEL

def green_handle_movement(keys_pressed,green):

    if keys_pressed[pygame.K_LEFT] and green.x - VEL > BORDER.x + BORDER.width: #LEFT
        green.x-=VEL

    if keys_pressed[pygame.K_RIGHT] and green.x + VEL + green.width< WIDTH: #RIGHT
        green.x+=VEL

    if keys_pressed[pygame.K_UP] and green.y - VEL > 0: #UP
        green.y-=VEL

    if keys_pressed[pygame.K_DOWN] and green.y + VEL + green.height < HEIGHT: #DOWN
        green.y+=VEL

def draw_winner(text):

    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(5000)

def main():

    green = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    green_bullets = []
    green_health = 10

    blue = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    blue_bullets = []
    blue_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_z and len(blue_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(blue.x, blue.y, 10, 5)
                    blue_bullets.append(bullet)

                if event.key == pygame.K_m and len (green_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(green.x, green.y, 10, 5)
                    green_bullets.append(bullet)

            if event.type == GREEN_HIT:
                green_health-=1

            if event.type == BLUE_HIT:
                blue_health-=1

        winner_text=""
        if green_health < 1:
            winner_text = "Blue WINS!"

        if blue_health < 1:
            winner_text = "Green WINS!"

        if winner_text !="":
            draw_winner(winner_text)
            break

        keys_pressed=pygame.key.get_pressed()

        blue_handle_movement(keys_pressed,blue)

        green_handle_movement(keys_pressed,green)

        handle_bullets(blue_bullets,green_bullets,blue,green)

        draw_window(green,blue,green_bullets,blue_bullets,green_health,blue_health)

    main()

if __name__=="__main__":
    main()