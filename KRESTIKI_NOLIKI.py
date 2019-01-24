import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return (y, x)
        else:
            return None

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                Rect = (
                (j * self.cell_size + self.left, i * self.cell_size + self.top), (self.cell_size, self.cell_size))
                Rect1 = ((j * self.cell_size + self.left + 1, i * self.cell_size + self.top + 1),
                         (self.cell_size - 2, self.cell_size - 2))
                c = [(0, 0, 0), (255, 0, 0), (0, 0, 255)]
                pygame.draw.rect(screen, (255, 255, 255), Rect, 1)
                pygame.draw.rect(screen, c[self.board[i][j]], Rect1, 0)

    def on_click(self, cell_coords):

        self.board[cell_coords[0]][cell_coords[1]] = (self.board[cell_coords[0]][cell_coords[1]] + 1) % 2
        '''
        print(cell_coords)

        for i in range(self.width):
            self.board[cell_coords[0]][i] = (self.board[cell_coords[0]][i] + 1) % 2
        for j in range(self.height):
            self.board[j][cell_coords[1]] = (self.board[j][cell_coords[1]] + 1) % 2
        '''


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def cross(self):


    def zero(self):



screen = pygame.display.set_mode((700, 700))
board = Board(10, 10)
board.set_view(100, 100, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()
