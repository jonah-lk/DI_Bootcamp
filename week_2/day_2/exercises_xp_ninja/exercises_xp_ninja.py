from random import random
import os, copy, time

class GameOfLife:
    def __init__(self, width, height, bias):
        self.width = width
        self.height = height
        self.grid = [[False if random() < bias else True for _ in range(0, width)] for _ in range(height)]
        self.game_over = self.game_over_check()

    def game_over_check(self):
        empty_count = 0

        for row in self.grid:
            if 1 not in row:
                empty_count += 1

        game_over = empty_count == self.height

        return game_over
    
    def draw_cells(self):
        display = ''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                display += '*' if self.grid[i][j] else ' '
            display += '\n'
        print(display)

    def neighbours_list(self, cell):
        row, column = cell
        neighbours = []
        row_range = range(max(0, row - 1), min(self.height, row + 2))
        column_range = range(max(0, column - 1), min(self.width, column + 2))
        for i in row_range:
            for j in column_range:
                if row == i and column == j:
                    continue
                else:
                    neighbours.append(self.grid[i][j])
        return neighbours
        # prev row i - 1, j - 1 | i - 1, j | i - 1, j + 1
        # same row     i, j - 1 |          | i    , j + 1
        # next row i + 1, j - 1 | i + 1, j | i + 1, j + 1

    def play(self):
        while not self.game_over:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

            new_grid = copy.deepcopy(self.grid)
            self.draw_cells()
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    neighbours = self.neighbours_list((i, j))
                    if (self.grid[i][j] and (neighbours.count(True) in [2, 3])) or (not self.grid[i][j] and neighbours.count(True) == 3):
                        new_grid[i][j] = True
                    else:
                        new_grid[i][j] = False
            self.grid = copy.deepcopy(new_grid)
            self.game_over = self.game_over_check()
            time.sleep(1)

    def regenerate(self, bias):
        self.grid = [[False if random() < bias else True for _ in range(0, self.width)] for _ in range(self.height)]
        self.game_over = self.game_over_check()

game = GameOfLife(40, 40, 0.75)
game.play()