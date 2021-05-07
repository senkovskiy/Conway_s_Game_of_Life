import numpy as np
import copy
from matplotlib import pyplot as plt
#from IPython import display
import time
import matplotlib.animation as animation

cells1 = [[1,0,0],
         [0,1,1],
         [1,1,0]]

glider_gun =\
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

X = np.zeros((50, 70))
X[1:10,1:37] = glider_gun
cells = X

def plot(name):
    plt.imshow(name, interpolation='none')
    plt.draw()
    display.display(plt.gcf())
    time.sleep(0)
    display.clear_output(wait=True)

def get_generation(cells, generations):
    for _ in range(generations):
        cells = Cell(cells)
        cells = cells.new_cells()
    return cells

class Cell:

    def __init__(self, cells):
        self.cells = np.array(cells)

    def summ_neighbours(self, grid, i, j):
        neighbours = [grid[i - 1][j - 1], grid[i - 1][j],
                      grid[i - 1][j + 1], grid[i][j - 1],
                      grid[i][j + 1], grid[i + 1][j - 1],
                      grid[i + 1][j], grid[i + 1][j + 1]]
        return sum(neighbours)

    def cut_grid(self, grid):
        live_cells = np.nonzero(grid)
        left = min(live_cells[0])
        right = max(live_cells[0])
        top = min(live_cells[1])
        bottom = max(live_cells[1])
        result = grid[left:right + 1, top:bottom + 1]
        return result

    def new_cells(self):
        grid = np.array(self.cells)
        grid = np.pad(grid, 2)
        new_grid = copy.deepcopy(grid)

        for x in range(1, grid.shape[0] - 1):
            for y in range(1, grid.shape[1] - 1):
                cell = grid[x][y]
                neighbours_count = self.summ_neighbours(grid, x, y)
                if cell == 1:
                    if neighbours_count == 2 or neighbours_count == 3:
                        new_grid[x][y] = 1
                    else:
                        new_grid[x][y] = 0
                else:
                    if neighbours_count == 3:
                        new_grid[x][y] = 1
        new_cells = self.cut_grid(new_grid).tolist()
        return new_cells

fig = plt.figure()

def animate(i):
    generations = 1+i
    return [plt.imshow(get_generation(cells, generations))]

anim = animation.FuncAnimation(
                               fig,
                               animate,
                               frames = 100,
                               interval = 5)
plt.show()
