import pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 500
BLACK = 0,0,0
WHITE = 255,255,255

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Totally not pong")
FPS = 60
clock = pygame.time.Clock()


playerWidth = 10
playerHeight = 100
dy = 3


player1 = pygame.draw.rect(WIN, WHITE, (0 + 20, HEIGHT/2, playerWidth, playerHeight))

player2 = pygame.draw.rect(WIN, WHITE, (WIDTH - 20 - playerWidth, HEIGHT/2, playerWidth, playerHeight))


while 1:

    # Checks to see if user exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Capped FPS
    clock.tick(FPS)
    WIN.fill(BLACK)

    pygame.draw.rect(WIN, WHITE, player1)
    pygame.draw.rect(WIN, WHITE, player2)

    if

    pygame.display.update()