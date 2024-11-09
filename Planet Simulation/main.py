import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")
YELLOW = (255, 191, 0)

class Planet:
    AU = 146.6e6 * 1000
    G = 6.674228e-11
    
    #1 AU = 100 px
    SCALE = 250 / AU   

    # 1 Day
    TIMESTEP = 3600*24 
    
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.x_vel = 0
        self.y_vel = 0
        
        self.sun = False
        self.distanceToSun = 0
        self.orbit = []
        
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win,self.color, (x,y), self.radius) 
        
        
        
def main():
    run = True
    clock = pygame.time.Clock()
    
    sun = Planet(0,0, 30, YELLOW, 1.989e30)
    sun.sun = True
    
    planets = [sun]
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()
    
main()



        
        