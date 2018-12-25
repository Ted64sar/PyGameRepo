import pygame
x = int(input())
y = int(input())

pygame.init()

size = width, height = x, y

screen = pygame.display.set_mode(size)
pygame.draw.line(screen, (255, 255, 255), (0, 0), (x, y), 5)
pygame.draw.line(screen, (255, 255, 255), (x, 0), (0, y), 5)

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()