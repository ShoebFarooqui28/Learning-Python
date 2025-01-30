import pygame
import math
import sys

pygame.init()

# CONSTANTS
WIDTH = 1000
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trigonometric Functions Visualization")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)  # Sine
GREEN = (0, 255, 0) # Cosine
YELLOW = (255, 255, 0) # Tangent

CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 150
FONT = pygame.font.SysFont("CMU Serif", 30)

# Unit Circle Function
def drawUnitCircle(theta):
    WIN.fill(BLACK)

    # Unit Circle
    pygame.draw.circle(WIN, WHITE, CENTER, RADIUS, 2)

    # Axis
    pygame.draw.line(WIN, WHITE, (CENTER[0] - RADIUS - 20,CENTER[1]),(CENTER[0] + RADIUS + 20,CENTER[1]), 2)
    pygame.draw.line(WIN, WHITE, (CENTER[0], CENTER[1] - RADIUS - 20),(CENTER[0], CENTER[1] + RADIUS + 20), 2)

    # Angles
    angles = {
        "2π" : (CENTER[0] + RADIUS + 30,CENTER[1] - 5),
        "π": (CENTER[0] - RADIUS - 45, CENTER[1] - 5),
        "π/2" : (CENTER[0] - 15, CENTER[1] - RADIUS - 50),
        "π/4" : (CENTER[0] - 15, CENTER[1] + RADIUS + 30),
    }  
    for text, position in angles.items():
        text_surface = FONT.render(text, True, WHITE)
        WIN.blit(text_surface, position)

    # Trigonometric Points
    x = CENTER[0] + RADIUS * math.cos(math.radians(theta))
    y = CENTER[1] - RADIUS * math.sin(math.radians(theta))
    
    # Hypotenuse 
    pygame.draw.line(WIN, YELLOW, CENTER, (x, y), 2)
    

    # Sine (y) Line & Cosine (x) Line (forming the triangle)
    pygame.draw.line(WIN, BLUE, (x, y), (CENTER[0], y), 2)  # Sine line
    pygame.draw.line(WIN, GREEN, (x, y), (x, CENTER[1]), 2)  # Cosine line

    pygame.draw.circle(WIN, BLUE, (CENTER[0], y), 5)  # Sine point
    pygame.draw.circle(WIN, GREEN, (x, CENTER[1]), 5)  # Cosine point
    pygame.draw.circle(WIN, YELLOW, (x,y), 5) # Tangent point

    # Display 
    angle_text = FONT.render(f"Angle: {theta}°", True, WHITE)
    coord_text = FONT.render(f"x: {math.cos(math.radians(theta)):.2f}, y: {math.sin(math.radians(theta)):.2f}", True, WHITE)
    WIN.blit(angle_text, (20, 20))
    WIN.blit(coord_text, (20, 50))
    
    pygame.display.update()

# Main Function  
def main():
    theta = 45 # Start at 45 degrees
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        # Control the angle with left and right arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            theta = (theta - 2) % 360  # Decrement angle (wrap around 360)
        if keys[pygame.K_RIGHT]:
            theta = (theta + 2) % 360  # Increment angle (wrap around 360)

        drawUnitCircle(theta)

    pygame.quit()
    sys.exit()

main()