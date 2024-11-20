import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
PANEL = pygame.display.set_mode((WIDTH, HEIGHT))

def handleEvents(object, space, clickCount, line):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, object, clickCount, line

        if event.type == pygame.MOUSEBUTTONDOWN:
            object, clickCount, line = launchObject(object, space, clickCount, line)

        if event.type == pygame.MOUSEMOTION and clickCount == 1:
            if line:
                line[1] = pygame.mouse.get_pos()

    return True, object, clickCount, line

def createBoundaries(space, width, height):
    rects = [
        [(width / 2, height - 10), (width, 20)],
        [(width / 2, 10), (width, 20)],
        [(10, height / 2), (20, height)],
        [(width - 10, height / 2), (20, height)]
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.color = (48, 25, 52, 255)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

def createBall(space, radius, mass, position):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.elasticity = 1
    shape.friction = 0.5
    space.add(body, shape)
    return shape

def createBlocks(space, width, height):
    RED = (220, 20, 60, 1)
    rects = [
        [(500, height - 120), (40, 200), RED, 100],
        [(600, height - 120), (40, 200), RED, 100],
        [(700, height - 120), (40, 200), RED, 100],
        [(800, height - 120), (40, 200), RED, 100],
        [(900, height - 120), (40, 200), RED, 100],
            ]

    for pos, size, color, mass in rects:
        body = pymunk.Body()
        body.position = pos
        shape =  pymunk.Poly.create_box(body, size)
        shape.color = color
        shape.mass = mass
        shape.elasticity = 0.4
        shape.friction = 0.5
        
        space.add(body, shape)
    
    
def launchObject(object, space, clickCount, line):
    pressedPos = pygame.mouse.get_pos()

    if clickCount == 0:
        object = createBall(space, 30, 10, pressedPos)
        clickCount += 1
        line = [pressedPos, pressedPos]

    elif clickCount == 1:
        if object:
            object.body.body_type = pymunk.Body.DYNAMIC
            line[1] = pygame.mouse.get_pos()
            angle = calculateAngle(line[0], line[1])
            distance = calculateDistance(line[0], line[1])

            if distance > 0:
                fz = distance * -100 
                fx = math.cos(angle) * fz
                fy = math.sin(angle) * fz

                object.body.body_type = pymunk.Body.DYNAMIC
                object.body.apply_impulse_at_local_point((fx, fy), (0, 0))

                print(f"Impulse applied: fx={fx:.2f}, fy={fy:.2f}, angle={angle:.2f}, distance={distance:.2f}")

        clickCount += 1
        line = None

    elif clickCount == 2:
        if object:
            space.remove(object, object.body)
            object = None
        clickCount = 0

    return object, clickCount, line

def calculateDistance(p1, p2):
    return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)

def calculateAngle(p1, p2):
    return math.atan2((p2[1] - p1[1]), p2[0] - p1[0])

def physicsSpace(window):
    space = pymunk.Space()
    space.gravity = (0, 981)
    drawOptions = pymunk.pygame_util.DrawOptions(window)
    return space, drawOptions

def draw(space, window, drawOptions, line):
    window.fill("white")

    if line:
        pygame.draw.line(window, "black", line[0], line[1], 3)

    space.debug_draw(drawOptions)
    pygame.display.update()

def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    space, drawOptions = physicsSpace(window)
    object = None
    clickCount = 0
    line = None
    createBoundaries(space, width, height)
    createBlocks(space, width, height)

    while run:
        run, object, clickCount, line = handleEvents(object, space, clickCount, line)
        draw(space, window, drawOptions, line)
        space.step(dt)
        clock.tick(fps)
        pygame.display.set_caption(f"Physics Simulation FPS : {clock.get_fps():.0f}")

    pygame.quit()

run(PANEL, WIDTH, HEIGHT)
