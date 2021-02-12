import pygame
import random
pygame.init()

# Constants
WIDTH, HEIGHT = 750, 500
BLACK = 0,0,0
WHITE = 255,255,255

# Window set-up
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort")
FPS = 100
clock = pygame.time.Clock()

# Intializes a list of the values to be sorted
values = []
for i in range(WIDTH):
    values.append(random.randint(0, int(HEIGHT)))

# Function to draw the current state of the our values list
def draw_lines(a_list):
    for index in range(0, len(a_list)):
        pygame.draw.line(WIN, WHITE, [index+1, HEIGHT], [index+1, HEIGHT-a_list[index-1]])



# Bubble sort stuff
n = len(values)
i = 0
j = 0

while 1:

    # Capped FPS
    clock.tick(FPS)

    # Resets the screen every tick
    WIN.fill(BLACK)

    # Checks to see if user exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    print(i, j)

    

    if i < n:
        j += 1
        if j >= n-i-1:
            j = 0
            i += 1
    else:
        break

    if values[j-1] > values[j]:
        values[j-1], values[j] = values[j], values[j-1]
    
    
    # Draw each line
    draw_lines(values)

    

    pygame.display.update()