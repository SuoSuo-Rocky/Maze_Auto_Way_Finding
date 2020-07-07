import pygame
from pygame.locals import *

matrix_cell_size = 2     # 矩阵单元尺寸
move_size = 2            # 一次移动的尺寸
_matrix = [[0,], [0, ]]  # 矩阵数据
SIZE = None              # 窗体尺寸


Dirs_func = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
]

Move_Dir_Dict = {pygame.K_UP: (3, 0, -move_size),
             pygame.K_RIGHT: (2, move_size, 0),
             pygame.K_DOWN: (0, 0, move_size),
             pygame.K_LEFT: (1, -move_size, 0)}