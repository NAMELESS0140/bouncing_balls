import pygame, sys, numpy
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

class ball:
    x=0
    y=0
    r=0
    color=WHITE
    Vx=0
    Vy=0
    to_top = 0
    to_bottom = 0
    to_left = 0
    to_right = 0
    def __init__(self,a,b,c,d,e,f):
        self.x=a
        self.y=b
        self.r=c
        self.color=d
        self.Vx=e
        self.Vy=f
    def move(self,time): # time = Δt
        self.x+=self.Vx*time/1000
        self.y+=self.Vy*time/1000
        self.to_top = self.y
        self.to_bottom = 600-self.y
        self.to_left = self.x
        self.to_right = 800-self.x        
        pygame.draw.circle(DISPLAYSURF,self.color,(self.x,self.y),self.r) 
    def ifHitWall(self):
        if(self.to_top<=self.r or self.to_bottom <=self.r):
          self.Vy*=-1
        if(self.to_left<=self.r or self.to_right<=self.r):
          self.Vx*=-1
    def ifCollide(self,other):
        if(numpy.sqrt(numpy.square(self.x-other.x) + numpy.square(self.y-other.y)) <= self.r+other.r):
            return True
        else:
            return False
    def changeAfterCollide(self,other):
        s=(self.Vx*(self.x- other.x)+ self.Vy*(self.y- other.y))/numpy.square(self.x-other.x)+numpy.square(self.y-other.y)
        self.Vx=self.Vx-s*(self.x-other.x)
        self.Vy=self.Vy-s*(self.y-other.y)

b1=ball(200,300,100,BLUE,60,60)
b2=ball(600,300,50,RED,-60,60)

t_c = 0
t0 = 0

while(True):
    # event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    t = pygame.time.get_ticks()
    t_c = t-t0 # Δt
    t0 = t

    DISPLAYSURF.fill(BGCOLOR)
    b1.ifHitWall()
    b2.ifHitWall()
    if(b1.ifCollide(b2)==True):
        b1.changeAfterCollide(b2)
        b2.changeAfterCollide(b1)
    b1.move(t_c)
    b2.move(t_c)
    pygame.display.update()
    fpsClock.tick(FPS)
