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
        
    def attraction(self, otherBody):
        #Taking in the planets x and y cords
        otherBody_x = otherBody.x
        otherBody_y = otherBody.y
        
        # Measuring the x and y distance between sun and the planet
        distance_x = otherBody_x - self.x
        distance_y = otherBody_y - self.y
        
        # Measuring the direct distance from sun to planet
        distance =  math.sqrt((distance_x ** 2) + (distance_y ** 2))
        
        if otherBody.sun:
            self.distanceToSun = distance
        
        # Attraction of Gravity
        force = self.G * self.mass1 * otherBody.mass / distance ** 2 
        
        # Measuring the angle theta from sun to planet
        theta = math.atan2(distance_y, distance_x)
        
        force_x = math.cos(theta) * force
        
        force_y = math.sin(theta) * force
        
        return force_x, force_y
    
    def update_position(self, planets):
        totalForce_x = totalForce_y = 0
        for planet in planets:
            if self == planet:
                continue
            
            fx, fy = self.attraction(planet)
            totalForce_x =+ fx
            totalForce_y =+ fy
            
            self.x_vel += totalForce_x / self.mass * self.TIMESTEP
            self.y_vel += totalForce_y / self.mass * self.TIMESTEP
            
            self.x += self.x_vel * self.TIMESTEP
            self.y += self.y_vel * self.TIMESTEP
            
            self.orbit.append((self.x, self.y))
            
            
            
            
        
        
        
        
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



        
        