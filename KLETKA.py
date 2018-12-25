import pygame
[w, n] = list(map(int, input().split()))
a = w // n
pygame.init()

size = width, height = w,w

screen = pygame.display.set_mode(size)
if n%2 == 1:
    screen.fill((255, 255, 255))
    c = (0, 0, 0)
else:
    c = (255, 255, 255)
for i in range(0, n):
    if i % 2 == 0:
        for j in range(0, n, 2):
            Rect = ((a * i, a * j), (a, a))
            pygame.draw.rect(screen, c, Rect)
    else:
        for j in range(0, n, 2):
            Rect = ((a * i, a * (j + 1)), (a, a))
            pygame.draw.rect(screen, c, Rect)


pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()