import random
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

grid_size = 75
cells = np.zeros((grid_size,grid_size),dtype=int)

#states: 0 = OFF, 1 = ON (add state 2 - signaling)

# Setting initial conditions

# Random initialization
for row in range(grid_size):
    for col in range(grid_size):
        cells[row,col] = random.randint(0, 1)

# Blinker at arbitrary position (test)
# cells[24,24:24+3]=1

def copy_matrix(mat):
    copy = np.zeros(mat.shape)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            copy[i,j]=mat[i,j]
    return copy

#Get and return state of cells in Moore neighborhood of cell at the specified position (row,col)
def get_neighbors(cells, row, col):
    global grid_size
    neighbors = np.zeros(8)  # Moore neighborhood with a toroidal grid
    neighbors[0] = cells[row, (col - 1) % grid_size]
    neighbors[1] = cells[row, (col + 1) % grid_size]
    neighbors[2] = cells[(row - 1) % grid_size, col]
    neighbors[3] = cells[(row + 1) % grid_size, col]
    neighbors[4] = cells[(row - 1) % grid_size, (col - 1) % grid_size]
    neighbors[5] = cells[(row - 1) % grid_size, (col + 1) % grid_size]
    neighbors[6] = cells[(row + 1) % grid_size, (col - 1) % grid_size]
    neighbors[7] = cells[(row + 1) % grid_size, (col + 1) % grid_size]
    return neighbors


def update_cells(data):
    global cells, grid_size
    temp = copy_matrix(cells)
    for row in range(grid_size):
        for col in range(grid_size):
            #get neighbors
            neighbors = get_neighbors(cells,row,col) #passing in position of cell in question
            #count number of neighbors that are on
            nborsON = int(sum(neighbors==1))
            #update states of each cell based on rules
            if cells[row,col]==1 and nborsON<2: #isolation
                temp[row, col]=0
            elif cells[row,col]==1 and (nborsON==2 or nborsON==3): #statis
                temp[row, col] = 1
            elif cells[row,col]==1 and nborsON>3: #crowding
                temp[row, col] = 0
            elif cells[row,col]==0 and nborsON==3: #reproduction
                temp[row,col]=1
    mat.set_data(temp)
    cells = temp #apply changes to grid
    return [cells]


fig, ax = plt.subplots()
mat = ax.matshow(cells, cmap='binary')
ani = animation.FuncAnimation(fig, update_cells, interval=50,
                              save_count=50)
plt.show()
