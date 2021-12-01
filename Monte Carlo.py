import pygame , sys
from pygame.locals import *

import random
import math as m

pygame.init()
pygame.display.set_caption("Pi Approximation (Monte Carlo)")


clock = pygame.time.Clock()


r = 350
stroke = 1
black = (0,0,0,1)
white = (255, 255, 255,1)
cyan =  (224,255,255,1)
blue =  (0,0,255,1)
green = (0, 255,0,1)
r1= 2

recordpi = 0
total = 0
circle =0

screen = pygame.display.set_mode((2*r  , 2*r) , 0 , 64)

screen.fill(black)

def draw ():
    pygame.draw.rect(screen, white, [0,0,2*r,2*r] , 2 )
    pygame.draw.circle(screen,white,(r,r),r,stroke)
    pygame.display.flip()

def loop():
    frame_count = 0
    while True:
        global total , circle ,recordpi
        for i in range (10):
            x = random.uniform(0,2*r)
            y = random.uniform(0,2*r)
            dist = (x-r)**2+(y-r)**2
            if dist < r**2 :
                pygame.draw.circle(screen,green,(x,y),r1)
                circle += 1
            else:
                pygame.draw.circle(screen,blue,(x,y),r1)
            total +=1
            pi = 4 * (circle/total)
            recodif = abs(m.pi-recordpi)
            dif = abs(m.pi- pi)
            if recodif > dif :
                recodif =dif
                recordpi =pi
            error = abs(m.pi-recordpi)/m.pi *100
            print("pi =", recordpi ,",", "error =" , error)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        frame_count += 1
        filename = "./pngs/screen_%04d.png" % ( frame_count )
        pygame.image.save( screen, filename )
        pygame.display.update()
        clock.tick(60)


draw()
loop()
