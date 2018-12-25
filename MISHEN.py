import pygame

[n, k] = list(map(int, input().split()))
pygame.init()

size = width, height = n * k * 2, n * k * 2
screen = pygame.display.set_mode(size)
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]

c2 = ([(0, 0, 255), (0, 255, 0), (255, 0, 0)][::-1])[0:(k % 3)]

c1 = c2

for i in range(k // 3):
    for j in range(3):
        c1.append(colors[j])
# c1.reverse()
for i in range(k):
    Rect = ((i * n, i * n), ((k - i) * 2 * n, (k - i) * 2 * n))
    color = c1[i]
    pygame.draw.ellipse(screen, color, Rect, n)

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()
