import random
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.signal as signal

# Initialize grid of cells
grid_size = 75
cells = np.zeros((grid_size,grid_size),dtype=int)

# States: 1 = ABSENT, 2 = PRESENT, 3 = PRESENT & SIGNALING

# Setting initial conditions
# Random initialization of cell states
for row in range(grid_size):
    for col in range(grid_size):
        cells[row,col] = random.randint(1, 3)

# Initialize kernel
# random kernel
kernel = np.zeros((3,3),dtype=int)
for row in range(kernel.shape[0]):
    for col in range(kernel.shape[1]):
        kernel[row,col] = random.randint(1, 3)
print(kernel)

def update_cells(data):
    global cells, grid_size, kernel
    temp = np.matrix.copy(cells) #copy cells grid to do synchronous update of cell states
    conv = signal.convolve2d(cells, kernel, mode='same')
    for row in range(grid_size):
        for col in range(grid_size):
            #update states of each cell based on rules (arbitrary rules for now...)
            #does the state of the cell in the previous time step matter?
            result = conv[row,col]
            if result>=9 and result<24:
                temp[row, col]=1
            elif result>=24 and result<48:
                temp[row, col] = 2
            elif result>=48 and result<=81:
                temp[row, col] = 3
    mat.set_data(temp)
    cells = temp #apply changes to grid
    return [cells]

fig, ax = plt.subplots()
mat = ax.matshow(cells, cmap='binary')
ani = animation.FuncAnimation(fig, update_cells, interval=50,
                              save_count=50)
plt.show()
