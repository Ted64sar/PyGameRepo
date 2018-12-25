import pygame
[n, k] = list(map(int, input().split()))
pygame.init()

size = width, height = n*k*2, n*k*2
screen = pygame.display.set_mode(size)

for i in range(0, k):
    Rect = ((i*n, i*n), ((k-i)*2*n, (k-i)*2*n))
    if k >= 3:
        if i % 3 == 2:
            color = (255, 0, 0)
        if i % 3 == 1:
            color = (0, 255, 0)
        if i % 3 == 0:
            color = (0, 0, 255)
    elif k == 2:
        if i == 0:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)
    else:
        color = (255, 0, 0)

    pygame.draw.ellipse(screen, color, Rect, n)

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()