import pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 500
BLACK = 0,0,0
WHITE = 255,255,255

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Totally not pong")
FPS = 120
clock = pygame.time.Clock()

class Paddle(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        self.points = 0

class Ball(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.speed = 15
        self.dx = -1
        self.dy = 1


paddleSpeed = 4

paddle1 = Paddle()
paddle1.rect.x = 10
paddle1.rect.y = HEIGHT/2

paddle2 = Paddle()
paddle2.rect.x = WIDTH - 10 - 10
paddle2.rect.y = HEIGHT/2

pong = Ball()
pong.rect.x = WIDTH / 2
pong.rect.y = HEIGHT / 2

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1,paddle2,pong)

def draw_screen():
    WIN.fill(BLACK)
    all_sprites.draw(WIN)
    pygame.display.update()

while 1:

    # Checks to see if user exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Capped FPS
    clock.tick(FPS)

    # Checks for key presses to move the paddles
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y -= paddleSpeed
    if key[pygame.K_s]:
        paddle1.rect.y += paddleSpeed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += paddleSpeed
    if key[pygame.K_UP]:
        paddle2.rect.y -= paddleSpeed

    # Moves the ball at set speed
    pong.rect.x += pong.dx
    pong.rect.y += pong.dy

    # Pong collision detection
    if pong.rect.y >= HEIGHT - 10 or pong.rect.y <= 0:
        pong.dy *= -1
    
    if pong.rect.x >= WIDTH - 10 or pong.rect.x <= 0:
        pong.rect.y = HEIGHT / 2
        pong.rect.x = WIDTH / 2
    
    # Paddle collision detection
    if paddle1.rect.y >= HEIGHT - 75:
        paddle1.rect.y = HEIGHT - 75
    if paddle1.rect.y <= 0:
        paddle1.rect.y = 0
    if paddle2.rect.y >= HEIGHT - 75:
        paddle2.rect.y = HEIGHT - 75
    if paddle2.rect.y <= 0:
        paddle2.rect.y = 0
    
    # Pong/paddle collision detection
    if paddle1.rect.colliderect(pong):
        pong.dx *= -1.0
        print(pong.dx)
    if paddle2.rect.colliderect(pong):
        pong.dx *= -1.0
        print(pong.dx)

    # Win detection
    #if pong.rect.x <= 0:
        #Win statement for player 2
    #if pong.rect.x >= WIDTH - 10:
        #Win statement for player 1

    draw_screen()