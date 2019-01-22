import pygame
import os

pygame.init()
running = True
screen = pygame.display.set_mode((300, 300))
x = 0
v = 20  # пикселей в секунду
fps = 60
clock = pygame.time.Clock()

fullname = os.path.join('data', 'creature.png')
image = pygame.image.load(fullname)
#image = pygame.transform.scale(image, (50, 50))
screen.blit(image, image.get_rect())
pygame.display.update()


class hero_blin:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def give_coords(self):
        return self.x, self.y

    def get_coords(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def render(self):
        screen.blit(image, (self.x, self.y))


hero = hero_blin(image.get_rect())
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x, y = hero.give_coords()
                y = y - 10
                hero.get_coords([x, y])
            if event.key == pygame.K_DOWN:
                x, y = hero.give_coords()
                y = y + 10
                hero.get_coords([x, y])
            if event.key == pygame.K_RIGHT:
                (x, y) = hero.give_coords()
                x = x + 10
                hero.get_coords([x, y])
            if event.key == pygame.K_LEFT:
                x, y = hero.give_coords()
                x = x - 10
                hero.get_coords([x, y])
        hero.render()
        pygame.display.flip()

pygame.quit()