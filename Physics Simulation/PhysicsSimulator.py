import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()

WIDTH, HEIGHT = 1000,800
PANEL = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulation")

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def physicsSpace(window):
    space = pymunk.Space()
    space.gravity = (0, 981)
    
    drawOptions = pymunk.pygame_util.DrawOptions(window)
    
    return space, drawOptions
    
    
def draw(space, window, drawOptions):
    window.fill("white")
    space.debug_draw(drawOptions)
    
    
def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    
    space, drawOptions = physicsSpace(window)
    
    while run:
        run = handleEvents()
        
        draw(space, window, drawOptions)
        space.step(dt)
        clock.tick(fps)
        
    pygame.quit()
    
run(PANEL, 1,1)
        
    


