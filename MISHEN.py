import pygame
[n, k] = list(map(int, input().split()))
pygame.init()

size = width, height = n*k*2, n*k*2
screen = pygame.display.set_mode(size)

for i in range(0, k):
    Rect = ((i*n, i*n), ((k-i)*2*n, (k-i)*2*n))

    pygame.draw.ellipse(screen, color1 , Rect, n)

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()