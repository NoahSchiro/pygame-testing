import pygame
from rocket import Rocket
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 500
BLACK = 0,0,0
WHITE = 255,255,255

# Basic window setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket")
FPS = 120
clock = pygame.time.Clock()

# Defining a rectangle and rectangel velocity
rectSize = 30
rect = pygame.Rect(WIDTH/2, HEIGHT/2, rectSize, rectSize * 2)
dx = 0
dy = 0

# Defining individual forces
thrust = 0
gravity = 0.03

# Defining total forces
yForces = gravity + thrust
xForces = 0

while 1:

    # Capped FPS
    clock.tick(FPS)
    WIN.fill(BLACK)

    # Checks to see if user exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        
        # Checks for keypresses
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                dy *= -0.3

    # Draw the rocket
    pygame.draw.rect(WIN, WHITE, rect)
    
    # Move rocket based on dy
    rect.y += dy

    # Change dy based on yForces
    #dy += yForces

    # Move Rocket based on dx
    rect.x += dx

    # Change dx based on xForces
    #dx += xForces

    if rect.y >= HEIGHT - rectSize * 2 or rect.y <= 0:
        dy *= -0.75

    if rect.x >= WIDTH - rectSize or rect.x <= 0:
        dx *= -0.75
    
    

    pygame.display.update()