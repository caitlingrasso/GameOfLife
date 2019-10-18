import random
import numpy as np
from pygameWindow import PYGAME_WINDOW
import time

pygameWindow_size = 500 #size of pygame window
pygameWindow = PYGAME_WINDOW(pygameWindow_size)

cell_size = 10
n = pygameWindow_size/cell_size #number of cells = grid size/cell_size
cells = np.zeros((n,n))

#states: 0 = OFF, 1 = ON (add state 2 - signaling)

# Setting initial conditions

# Random initialization
for row in range(n):
    for col in range(n):
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
def getNeighbors(cells, row, col):
    neighbors = np.zeros(8)  # Moore neighborhood with a toroidal grid
    neighbors[0] = cells[row, (col - 1) % n]
    neighbors[1] = cells[row, (col + 1) % n]
    neighbors[2] = cells[(row - 1) % n, col]
    neighbors[3] = cells[(row + 1) % n, col]
    neighbors[4] = cells[(row - 1) % n, (col - 1) % n]
    neighbors[5] = cells[(row - 1) % n, (col + 1) % n]
    neighbors[6] = cells[(row + 1) % n, (col - 1) % n]
    neighbors[7] = cells[(row + 1) % n, (col + 1) % n]
    return neighbors

while True:
    pygameWindow.Prepare()
    pygameWindow.Draw_Grid(cells, cell_size)
    #copy matrix for synchronous updates
    temp = copy_matrix(cells)
    for row in range(n):
        for col in range(n):
            #get neighbors
            neighbors = getNeighbors(cells,row,col) #passing in position of cell in question
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
    cells = temp #apply changes to grid
    pygameWindow.Reveal()
    # time.sleep(0.5)