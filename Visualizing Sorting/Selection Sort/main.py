import pygame
import random
pygame.init()

# Constants
WIDTH, HEIGHT = 1500, 500
BLACK = 0,0,0
WHITE = 255,255,255

# Window set-up
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort")
FPS = 1000
clock = pygame.time.Clock()

# Intializes a list of the values to be sorted
values = []
for i in range(WIDTH):
    values.append(random.randint(0, int(HEIGHT)))

# Function to draw the current state of the our values list
def draw_lines(a_list):
    for index in range(0, len(a_list)):
        pygame.draw.line(WIN, WHITE, [index+1, HEIGHT], [index+1, HEIGHT-a_list[index-1]])



# Selection sort stuff
n = len(values)
i = 0

while 1:

    # Capped FPS
    clock.tick(FPS)

    # Resets the screen every tick
    WIN.fill(BLACK)

    # Checks to see if user exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # If i is greater than or equal 
    # to the length of the array,
    # don't do selection sort stuff
    if(i < n):

        # Assume that i is the smallest element
        jMinimum = i

        # Test against elements after i to find the smallest
        for j in range(i+1, n):

            # If this element is less, then it's the new minimum
            if(values[j] < values[jMinimum]):

                jMinimum = j
        
        if(jMinimum != i):
            print("debug")
            values[i], values[jMinimum] = values[jMinimum], values[i]

    i += 1
    
    # Draw each line
    draw_lines(values)

    

    pygame.display.update()