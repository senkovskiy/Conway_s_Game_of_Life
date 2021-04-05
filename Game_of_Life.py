import numpy as np
import copy

def cut_grid(grid):
    live_cells = np.nonzero(grid)
    left = min(live_cells[0])
    right = max(live_cells[0])
    top = min(live_cells[1])
    bottom = max(live_cells[1])
    result = grid[left:right+1, top:bottom+1]
    return result

def new_cells(cells):
    grid = np.array(cells)
    grid_pad = np.pad(grid, 2)
    new_grid = copy.deepcopy(grid_pad) #make a deep cppy of the grid_pad
    
    print(grid_pad, '\n')
    for x in range(1, grid_pad.shape[0]-1): 
        for y in range(1, grid_pad.shape[1]-1):  #run over all cells, exept outer ones
            cell = grid_pad[x][y]
            naighbours = [grid_pad[x-1][y-1], grid_pad[x-1][y], 
                          grid_pad[x-1][y+1], grid_pad[x][y-1],
                          grid_pad[x][y+1], grid_pad[x+1][y-1],
                          grid_pad[x+1][y], grid_pad[x+1][y+1]]
            naighbour_count = sum(naighbours)
            if cell == 1: 
                if naighbour_count == 2 or naighbour_count == 3:
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = 0
            else:
                if naighbour_count == 3:
                    new_grid[x][y] = 1
    
    new_cells = cut_grid(new_grid).tolist()
    return new_cells

def get_generation(cells, generations):
    print('generations = ', generations, '\n')
    while generations:
        cells = new_cells(cells)
        generations-=1
    return cells
