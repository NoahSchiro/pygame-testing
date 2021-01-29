import pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 500
BLACK = 0,0,0
WHITE = 255,255,255

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity")
FPS = 120
clock = pygame.time.Clock()

rectSize = 30
dy = -3        # Object velocity
dx = 5
gravity = 0.03    # Object acceleration


rect = pygame.Rect(0, HEIGHT - rectSize - 1, rectSize, rectSize)

while 1:

    # Checks to see if user exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Capped FPS
    clock.tick(FPS)
    WIN.fill(BLACK)

    pygame.draw.rect(WIN, WHITE, rect)
    rect.y += dy
    dy += gravity
    rect.x += dx

    if rect.y >= HEIGHT - rectSize or rect.y <= 0:
        dy *= -0.75

    if rect.x >= WIDTH - rectSize or rect.x <= 0:
        dx *= -0.75
    
    

    pygame.display.update()