import pygame
import math

#Игра жизнь (можете загуглить), рисуем левой кнопкой мышки, старт правой кнопкой мыши

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class GameOfLife:

    def __init__(self, width, height, cell_size, fps):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.fps = fps

        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_lines(self): #Рисует линии
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def create_grid(self): #Массив поля
        grid = []
        for i in range(0, self.cell_height):
            grid.append([])
            for j in range(0, self.cell_width):
                grid[i].append(0)
        return grid

    def draw_grid(self, grid): #Закрашиваем клетки
        for i in range(0, self.cell_height):
            for j in range(0, self.cell_width):
                if (grid[i][j] == 1):
                        pygame.draw.rect(self.screen, BLACK, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))

    def get_neighbours(self, grid): #Возвращаем количество соседей
        cellNeig = {}
        for i in range(0, self.cell_height):
            for j in range(0, self.cell_width):
                cellNeig[(i, j)] = 0
                count_neig = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if (i + k < 0 or i + k == self.cell_height or j + l < 0 or j + l == self.cell_width or k == 0 and l == 0):
                            continue
                        elif (grid[i + k][j + l] == 1):
                            count_neig += 1
                cellNeig[(i, j)] = count_neig

        return cellNeig

    def get_next_generation(self, cellNeig, grid): #Возвращаем следующее поколение
        for i in range(0, self.cell_height):
            for j in range(0, self.cell_width):
                    if (grid[i][j] == 0 and cellNeig[(i, j)] == 3):
                        grid[i][j] = 1
                    elif(grid[i][j] == 1 and (cellNeig[(i, j)] == 3 or cellNeig[(i, j)] == 2)):
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        return grid



    def run(self):
        pygame.init()
        pygame.mixer.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("GameOfLife")
        self.screen.fill(WHITE)
        grid = self.create_grid()
        running = True
        flag = False
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        grid[math.ceil(event.pos[1] / self.cell_size) - 1][math.ceil(event.pos[0] / self.cell_size) - 1] = 1
                        self.draw_grid(grid)
                    if event.button == 3:
                        flag = True
            if (flag):
                self.screen.fill(WHITE)
                cellNeig = self.get_neighbours(grid)
                grid2 = self.get_next_generation(cellNeig, grid)
                self.draw_grid(grid2)
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.fps)
        pygame.quit()

game = GameOfLife(640, 640, 10 ,30)
game.run()



