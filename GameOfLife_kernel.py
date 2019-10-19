import random
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.signal as signal

grid_size = 75
cells = np.zeros((grid_size,grid_size),dtype=int)

#states: 1 = ABSENT, 2 = PRESENT

# Setting initial conditions
# Random initialization
for row in range(grid_size):
    for col in range(grid_size):
        cells[row,col] = random.randint(0, 1) #random.randint(1, 3)

#initialize kernel (random for now)
kernel = np.ones((3,3),dtype=int)
kernel[1,1] = 0 #game of life kernel

# random kernel
# for row in range(kernel.shape[0]):
#     for col in range(kernel.shape[1]):
#         kernel[row,col] = random.randint(0, 1)

def update_cells(data):
    global cells, grid_size, kernel
    temp = np.matrix.copy(cells) #copy cells grid to do synchronous update of cell states
    conv = signal.convolve2d(cells, kernel, mode='same')
    for row in range(grid_size):
        for col in range(grid_size):
            # #update states of each cell based on rules
            nborsON = conv[row,col]
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
