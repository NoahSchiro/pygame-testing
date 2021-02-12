import pygame
from pygame import gfxdraw
import datetime
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")
FPS = 120
clock = pygame.time.Clock()

# Circle stuff
tau = 2 * 3.14
rect = [(WIDTH/2)-250,(HEIGHT/2)-250,500,500]
startAngle = -90
secondStopAngle = 0
minuteStopAngle = 0
hourStopAngle = 0

while 1:
    # Window framerate
    clock.tick(FPS)
    
    # Checks to see if user exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # Clears screen
    WIN.fill(BLACK)

    # Time stuff
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    # Seconds
    pygame.gfxdraw.arc(WIN, 400, 400, 300, startAngle, secondStopAngle, RED)

    # Minutes
    pygame.gfxdraw.arc(WIN, 400, 400, 310, startAngle, minuteStopAngle, GREEN)

    # Hours
    pygame.gfxdraw.arc(WIN, 400, 400, 320, startAngle, hourStopAngle, BLUE)

    secondStopAngle = (now.second * 6) - 90
    minuteStopAngle = (now.minute * 6) - 90
    hourStopAngle   = (now.hour * 30)  - 90
    

    pygame.display.update()