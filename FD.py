import pygame
from pygame.locals import * 

pygame.init() 

clock = pygame.time.Clock()
wh = 840
ww = 850
bg = pygame.image.load("./bg.png")
gr = pygame.image.load("./ground.png")
fps = 60
gs = 0
gss = 4


screen = pygame.display.set_mode((ww,wh))
pygame.display.set_caption("Flapy nader")


run = True
while run:
    
    screen.blit(bg,(0,0))
    screen.blit(gr,(gs,wh-150))
    clock.tick(fps)
    gs -= gss
    if abs(gs) > 35:
        gs = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()

