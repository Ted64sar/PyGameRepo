import pygame
x = int(input())
y = int(input())

pygame.init()

size = width, height = x, y

screen = pygame.display.set_mode(size)
Rect=(1, 1, x - 2, y - 2)
pygame.draw.rect(screen, (255, 0, 0), Rect)

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()