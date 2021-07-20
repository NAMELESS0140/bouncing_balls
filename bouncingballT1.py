import pygame, sys
from pygame.locals import*

pygame.init()

RESOLUTION = (800,600)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)

FPS = 60
fpsClock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (128,0,128)
BGCOLOR = WHITE

DISPLAYSURF.fill(BGCOLOR)

x=400
y=300
Vx=60
Vy=60
r=50
t_c = 0
t0 = 0

while(True):
    # event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    t = pygame.time.get_ticks()
    t_c = t-t0
    t0 = t
    to_top = y
    to_bottom = 600-y
    to_left = x
    to_right = 800-x
    DISPLAYSURF.fill(BGCOLOR)
    if(to_top<=50 or to_bottom <=50):
        Vy*=-1
    if(to_left<=50 or to_right<=50):
        Vx*=-1
    x+=Vx*t_c/1000
    y+=Vy*t_c/1000
    pygame.draw.circle(DISPLAYSURF,BLUE,(x,y),r) 
    pygame.display.update()
    fpsClock.tick(FPS)

