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
            break
    return True


def createBall(space, radius, mass):
    body = pymunk.body()
    body.position = (WIDTH / 2, HEIGHT / 2)
    shape = pymunk.Circle(body, 10)
    shape.mass = mass
    shape.color = (106, 90, 205, 255)



def physicsSpace(window):
    space = pymunk.Space()
    space.gravity = (0, 981)
    
    drawOptions = pymunk.pygame_util.DrawOptions(window)
    
    return space, drawOptions
    
    
def draw(space, window, drawOptions):
    window.fill("white")
    space.debug_draw(drawOptions)
    pygame.display.update()
    
def run(window):
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
    
run(PANEL)
        
    


