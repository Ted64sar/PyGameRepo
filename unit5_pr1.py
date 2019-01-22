import pygame
import os

pygame.init()
running = True
screen = pygame.display.set_mode((600, 600))
x = 0
v = 20  # пикселей в секунду
fps = 60
clock = pygame.time.Clock()

fullname = os.path.join('data', 'cursor.png')
image = pygame.image.load(fullname)
image = pygame.transform.scale(image, (50, 50))
screen.blit(image, image.get_rect())
pygame.display.update()


class Cursor:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def get_coords(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def render(self):
        screen.blit(image, (self.x, self.y))


cursor = Cursor(image.get_rect())
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            cursor.get_coords(pygame.mouse.get_pos())
    if pygame.mouse.get_focused():
        pygame.mouse.set_visible(False)
        cursor.render()
    pygame.display.flip()
pygame.quit()
