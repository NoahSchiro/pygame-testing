import pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 500
BLACK = 0,0,0
WHITE = 255,255,255

# Window set-up
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity")
FPS = 60
clock = pygame.time.Clock()

rectSize = 30     
dy = 1              # Object velocity
gravity = 0.05      # Object acceleration


rect = pygame.Rect(WIDTH/2, HEIGHT/2, rectSize, rectSize)


while 1:

    # Checks to see if user exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Capped FPS
    clock.tick(FPS)

    # Resets the screen every tick
    WIN.fill(BLACK)

    # Draws rectangle with current position
    pygame.draw.rect(WIN, WHITE, rect)

    # Adjusts position based on velocity (dy)
    rect.y += dy
    # Adjusts velocity based on acceleration (gravity)
    dy += gravity

    # Changes direction of dy if object hits bounds of window
    if rect.y >= HEIGHT - rectSize or rect.y <= 0:
        
        # When it hits a surface we also want 
        # to take some of it's energy away
        dy *= -0.7

    
    
    

    pygame.display.update()