


# 广度优先
import copy
from collections import deque
from settings import *


  # 上、 右 、下 、左
from functools import lru_cache


def migong_wide(x1, y1, x2, y2):     # Right
    """ 广度优先 算法 """
    global _matrix
    matrix = copy.deepcopy(_matrix)
    q = deque()
    q.append((x1, y1, -1))
    matrix[x1][y1] = 2
    traceback = []
    while len(q) > 0:
        cur_node = q.popleft()
        traceback.append(cur_node)
        if cur_node[:-1] == (x2, y2):
            path = []
            i = len(traceback) - 1
            while i >= 0:
                path.append(traceback[i][:-1])
                i = traceback[i][2]
            # path.reverse()
            # for i,v in enumerate(path): # 打印路径
            #     print(i, v)
            return True, path
        for d in Dirs_func:
            next_x, next_y = d(cur_node[0], cur_node[1])
            # print(f"next_x, next_y= {next_x, next_y}")
            if matrix[next_x][next_y] == 0:
                q.append((next_x, next_y, len(traceback) - 1))
                matrix[next_x][next_y] = 2
    else:
        print("There is no way")
        return False, None


def set_matrix(x, y, val):
    """ 设置 矩阵元素 索引 """
    global _matrix
    if x in range(0, len(_matrix)):
        if y in range(0, len(_matrix[0])):
            _matrix[x][y] = val
        else:
            raise("y out of range!")
    else:
        raise("x out of range!")


def get_matrix(x, y):
    """ 获取矩阵元素 索引 """
    global _matrix
    if x in range(0, len(_matrix)):
        if y in range(0, len(_matrix[0])):
            return _matrix[x][y]
        else:
            raise ("y out of range!")
    else:
        raise ("x out of range!")

# @lru_cache(maxsize = len(_matrix[0]) * len(_matrix))
# def charge_pos(x, y):


def matrix_init(size):
    """ 矩阵初始化 """
    global _matrix
    global SIZE
    SIZE = size
    _matrix = [[0 for i in range(0, size[0], matrix_cell_size)] for i in range(0, size[1], matrix_cell_size)]
    # _matrix = [[0 for i in range(0, 640, 5)] for i in range(0, 396, 5)]
    print(f"len row = {len(_matrix[0])},  len matrix = {len(_matrix)}")

    for k, li in enumerate(_matrix):
        li[0], li[-1] = 1, 1
        if k in [0, len(_matrix) - 1]:
            for k, ele in enumerate(li):
                li[k] = 1


# 矩阵转坐标
def cell_xy(row, col):
    """ 矩阵转坐标 """
    if row in range(0, len(_matrix)):
        if col in range(0, len(_matrix[0])):
            y = row * matrix_cell_size
            x = col * matrix_cell_size
            return x, y
        else:
            raise("col out of range!")
    else:
        raise("row out of range!")


# 坐标转矩阵
def xy_cell(x, y):
    """ 坐标转矩阵 """
    if x in range(0, SIZE[0]):
        if y in range(0, SIZE[1]):
            col = x //  matrix_cell_size
            row = y //  matrix_cell_size
            return row, col
        else:
            raise ("y out of range!")
    else:
        raise ("x out of range!")


def get_routes(x1, y1, x2, y2):
    """ 获取路径 """
    print(f"x1, y1, x2, y2 = {x1, y1, x2, y2}")
    res = migong_wide(x1, y1, x2, y2)
    print(f"res = {res}")
    if res[0]:
        return res[1]
    else:
        raise("There is no way")


if __name__ == '__main__':
    matrix_init((640, 396))
    print(f"_matrix[0] = {_matrix[0]}, len = {len(_matrix)}")

    routes = get_routes(9, 17, 200, 600)
    print(routes)




















# 深度优先
def migong_deep(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    _matrix[x1][y1] = 2
    while len(stack) > 0:
        cur_node = stack[-1]
        if cur_node == (x2, y2):
            print("到达终点，")
            for i ,v in enumerate(stack):
                print(i, v)
            return True
        for d in dirs:
            next_node = d(*cur_node)
            if _matrix[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                _matrix[next_node[0]][next_node[1]] = 2
                break
        else:
            stack.pop()
    else:
        print("There is no way")
        return False
