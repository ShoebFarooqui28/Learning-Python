import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()

WIDTH, HEIGHT = 1000,600
PANEL = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulation")

def handleEvents(shape):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            launchObject(shape)
            
    return True


def createBoundaries(space, width, height):
    rects = [   
        [(width/2, height - 10), (width, 20)],
        [(width/2, 10), (width, 20)],
        [(10, height/2), (20, height)],
        [(width - 10, height/2), (20, height)] 
    ]
    
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.color = (48, 25, 52, 255)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)
        
        
def createBall(space, radius, mass):
    body = pymunk.Body()
    body.position = (WIDTH / 2, HEIGHT / 2)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (106, 90, 205, 255)
    shape.elasticity = 1
    shape.friction = 0.5
    space.add(body, shape)
    return shape


def launchObject(shape):
    shape.body.apply_impulse_at_local_point((10000, 0), (0, 0)) 
        
            
def physicsSpace(window):
    space = pymunk.Space()
    space.gravity = (0, 981)
    
    drawOptions = pymunk.pygame_util.DrawOptions(window)
    
    return space, drawOptions
    
    
def draw(space, window, drawOptions):
    window.fill("white")
    space.debug_draw(drawOptions)
    pygame.display.update()
    
    
def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    
    space, drawOptions = physicsSpace(window)
    ball = createBall(space, 30, 100)
    createBoundaries(space, width, height)
    
    while run:
        run = handleEvents(ball)
        draw(space, window, drawOptions)
        space.step(dt)
        clock.tick(fps)
        
    pygame.quit()

run(PANEL, WIDTH, HEIGHT)
