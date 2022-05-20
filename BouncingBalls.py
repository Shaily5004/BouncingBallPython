# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:39:11 2022

@author: Shaily
"""

import pygame 
pygame.init()
canvas=pygame.display.set_mode((500,500))
pygame.display.set_caption("Bouncing ball")
font = pygame.font.Font(None, 34)


bgimage=pygame.image.load("bg.jpg").convert()
canvas.blit(bgimage,[0,0])
ball1posx=350
ball1posy=451
ball2posx=150
ball2posy=49
ball1=pygame.draw.circle(canvas, (0,255,0),(ball1posx,ball1posy), 20,0)
ball2=pygame.draw.circle(canvas, (120,255,200),(ball2posx,ball2posy), 20,0)
flag1=1
flag2=1

velocity=[1,-1]
carryOn = True
clock=pygame.time.Clock()
while carryOn:
   
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False
     
   
    bgimage=pygame.image.load("bg.jpg").convert()
    canvas.blit(bgimage,[0,0])
    
   #Code for ball1 movement
    
    ball1posy = ball1posy-flag1
    
    
    if ball1posy<50 :
        ball1posy=50
        flag1=-1 * flag1
    
    if ball1posy>450:
       ball1posy=450
       flag1=-1 * flag1
       
     #Code for ball2 movement   
        
    ball2posy = ball2posy+flag1 
    if ball2posy<50 :
         ball2posy=50
         flag2=-1 * flag2
     
    if ball2posy>450:
        ball2posy=450
        flag2=-1 * flag2
        
    
    
    ball1=pygame.draw.circle(canvas, (0,255,0),(ball1posx,ball1posy), 20,0)
    ball2=pygame.draw.circle(canvas, (120,255,200),(ball2posx,ball2posy), 20,0)         
    clock.tick(60)
    pygame.display.flip()    
    pygame.display.update()
pygame.quit()        
                          


