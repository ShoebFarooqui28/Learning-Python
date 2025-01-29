import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trignometric Functions")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 200
FONT = pygame.font.SysFont("CMU Serif Roman", 36)

def drawUnitCircle(theta):
    WIN.fill(BLACK)
    
    # Draw the unit circle
    pygame.draw.circle(WIN, WHITE, CENTER, RADIUS, 2)
    
    # Draw the x and y axes
    pygame.draw.line(WIN, WHITE, (CENTER[0] - RADIUS - 20, CENTER[1]), (CENTER[0] + RADIUS + 20, CENTER[1]), 2)
    pygame.draw.line(WIN, WHITE, (CENTER[0], CENTER[1] - RADIUS - 20), (CENTER[0], CENTER[1] + RADIUS + 20), 2)
    
    text1 = FONT.render("2π", True, WHITE)
    text_rect1 = text1.get_rect(center=(CENTER[0] + RADIUS + 40, CENTER[1]))
    WIN.blit(text1, text_rect1)
    
    text2 = FONT.render("π/2", True, WHITE)
    text_rect2 = text2.get_rect(center=(CENTER[0], CENTER[1] - RADIUS - 40))
    WIN.blit(text2, text_rect2)
    
    text3 = FONT.render("π", True, WHITE)
    text_rect3 = text3.get_rect(center=(CENTER[0] - RADIUS - 40, CENTER[1]))
    WIN.blit(text3, text_rect3)
    
    text4 = FONT.render("π3/4", True, WHITE)
    text_rect4 = text4.get_rect(center=(CENTER[0], CENTER[1] + RADIUS + 40))
    WIN.blit(text4, text_rect4)
    
    # Calculate the point on the Unit Circle
    x = CENTER[0] + RADIUS * math.cos(math.radians(theta)) # Adjacent
    y = CENTER[1] - RADIUS * math.sin(math.radians(theta)) # Opposite
    
    # Draw the point on the unit circle
    pygame.draw.line(WIN, RED, CENTER, (x, y), 2)
    pygame.draw.circle(WIN, BLUE, (int(x), int(y)), 5)
    
    
    pygame.display.flip()
    
def main():
    theta = float(input("Enter the angle theta (in degrees): "))
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        drawUnitCircle(theta)
                
        pygame.display.update()
    
    pygame.quit()
    sys.exit()
    
main()