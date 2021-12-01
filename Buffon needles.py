from __future__ import division  
import pygame , sys
from pygame.locals import *
from pygame import gfxdraw
import random 
import math as m
import numpy as np 

clock = pygame.time.Clock()


stroke = 1 
black = (0,0,0,1)
white = (255, 255, 255,1)
cyan =  (224,255,255,1)
blue =  (0,0,255,1)
green = (0, 255,0,1)
l = 50.0
r = 500
n = 10
d = 2*r/(n-1)

np.set_printoptions(precision=0)
pygame.init()
pygame.display.set_caption("Pi Approximation (buffon needles problem)")
screen = pygame.display.set_mode((2*r+10 , r))
screen.fill(black)

def draw():
    for i in range(n):
        pygame.draw.line(screen, white, (i*d+5,0),(i*d+5,r), stroke)

    pygame.display.flip() 

def loop():
    frame_count = 0
    global l ,d,r
    hits = 0
    total =0
    recordpi = 0  
    while True:
        x = random.uniform(0, 2*r+5)
        y = random.uniform(0, r)
        angle =random.uniform(0, 2*m.pi)
        x2 = l*m.cos(angle)+x
        y2 = l*m.sin(angle)+y 
        a = [5.,116.,227,338.,449.,560.,671.,782.,893.,1005.]

        for i in a:
            if (i> x and i<x2)  or (i< x and i>x2) :
                pygame.draw.line(screen, green, (int(x),int(y)),(int(x2),int(y2)), stroke)
                hits += 1
                break 
            else:
                pygame.draw.line(screen, blue, (int(x),int(y)),(int(x2),int(y2)), stroke)
        total +=1 
        pi = (2*l*total)/(d*hits)
        recodif = abs(m.pi-recordpi)
        dif = abs(m.pi- pi)
        if recodif > dif :
            recodif =dif
            recordpi =pi
        error = abs(m.pi-recordpi)/m.pi *100  
        print("pi = ",recordpi,",","error = ",error)            
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        frame_count += 1
        filename = "./pngs/screen_%04d.png" % ( frame_count )
        #pygame.image.save( screen, filename )        
        pygame.display.update()
        clock.tick(60)
draw()
loop()

