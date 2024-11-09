import pygame
import math

pygame.init()

#DISPLAY
WIDTH = 1920
HEIGHT = 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

#Declaring the Colors
SunRGB = (255, 191, 0)
MercuryRGB = (160, 160, 160)
VenusRGB = (255, 255, 167)
EarthRGB = (40, 122, 184)
MarsRGB = (193, 68, 14)
JupiterRGB = (216, 170, 130)
SaturnRGB = (255, 204, 102)
UranusRGB = (102, 204, 255)
NeptuneRGB = (30, 105, 150)

class Planet:
    AU = 146.6e6 * 1000
    G = 6.674228e-11
    
    #1 AU = 100 px
    SCALE = 200 / AU   

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
        
        
class GravitationalForce:
    def __init__(self, mass1, mass2, distance):
        self.mass1 = mass1
        self.mass2 = mass2
        self.distance = distance
    
    def calculate_force(self):
        force = (self.G * self.mass1 * self.mass2 / (self.distance * self.distance))
    
    
def main():
    run = True
    clock = pygame.time.Clock()
    
    #Declaring the SUN
    sun = Planet(0,0, 40, SunRGB, 1.989e30)
    sun.sun = True
    
    #Declaring the Planets
    mercury = Planet(0.387 * Planet.AU, 0, 8, MercuryRGB, 3.3011e23)
    venus = Planet(0.72 * Planet.AU, 0, 14, VenusRGB, 4.8675e24)
    earth = Planet(1 * Planet.AU, 0, 16, EarthRGB, 5.972e24)
    mars = Planet(1.524 * Planet.AU, 0, 12, MarsRGB, 0.64171e24)
    jupiter = Planet(2.2 * Planet.AU, 0, 24, JupiterRGB, 1.8982e27) 
    saturn = Planet(2.582 * Planet.AU, 0, 18, SaturnRGB, 5.683e26)
    uranus = Planet(3 * Planet.AU, 0, 17, UranusRGB, 8.681e25)
    neptune = Planet(3.4 * Planet.AU, 0, 17, NeptuneRGB, 1.024e26)
    
    
    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]    
    
    while run:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()
    
main()



        
        