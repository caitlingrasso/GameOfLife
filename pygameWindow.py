import pygame
import numpy as np

class PYGAME_WINDOW:
    def __init__(self,screen_size):
        pygame.init()
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode((screen_size, screen_size))

    def Prepare(self):
        self.screen.fill((255, 255, 255))
        pygame.event.get()

    def Reveal(self):
        pygame.display.flip()

    def Draw_Grid(self, grid, cell_size):
        on_color = (0,0,0) #black
        off_color = (255, 255, 255) #white
        for row in range(grid.shape[0]):
            for col in range(grid.shape[1]):
                if grid[row,col]==1: #ON
                    pygame.draw.rect(self.screen, on_color, (row*cell_size,col*cell_size,cell_size,cell_size))
                elif grid[row,col]==0: #OFF
                    pygame.draw.rect(self.screen, off_color, (row*cell_size,col*cell_size,cell_size,cell_size))