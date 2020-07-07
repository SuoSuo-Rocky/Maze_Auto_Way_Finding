


# 导入pygame 及常量库
import pygame
from pygame.locals import *
# 导入精灵类
from sprite_repo import Sprite_Fact
# 导入 获取路径 方法
from find_way import matrix_init, get_routes
# 导入 索引 与 坐标相互转化的  方法
from find_way import xy_cell, cell_xy


SIZE = WIDTH, HEIGHT = 640, 396
FPS = 60

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello__施伟")
clock = pygame.time.Clock()
# 创建字体对象 
font = pygame.font.SysFont(None, 60, )
# 创建精灵类
panda = Sprite_Fact()
# panda.load("img/size_80.png", 80, 80, 4)
# panda.load("img/222.jpg", 80, 80, 4)
panda.load("img/size_80_02.png", 80, 80, 4)
pygame.key.set_repeat(FPS)

change_li = {pygame.K_UP: (3, 0, -2),
             pygame.K_RIGHT: (2, 2, 0),
             pygame.K_DOWN: (0, 0, 2),
             pygame.K_LEFT: (1, -2, 0)}
# 初始化 矩阵
matrix_init(SIZE)

# res = get_routes(10, 10, 36, 36)
# print(res)

START_POS = None      # 起始 方格位置
END_POS = None        # 终点 方格 位置
# auto_move_switch = False   # 移动开关
delay_fps = 3        # 移动延迟
delay = delay_fps     # 延迟 计数变量
ROUTES = []           # 移动路径
old_dot = None      # 前一位置 坐标点
dir_dict = {(0, -1): (3, 0, -1), \
            (1,  0): (2, 1, 0), \
            (0,  1): (0, 0, 1), \
            (-1, 0): (1, -1, 0)}

running = True
# 主体循环
while running:
    # 1. 清屏
    screen.fill((25, 102, 173))
    current_time = pygame.time.get_ticks()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: exit()
    for k in range(pygame.K_UP, pygame.K_LEFT + 1):
        if keys[k]:
            panda.direction, panda.vel.x, panda.vel.y = change_li[k]
            panda.is_move = True
            break
    else:
        panda.vel.x = panda.vel.y = 0
        if not panda.auto_move_switch:
            panda.is_move = False

    # 边界检测
    if panda.rect.centerx <= 9:
        panda.rect.centerx = 10
    if panda.rect.centerx >= SIZE[0] - 12:
        panda.rect.centerx = SIZE[0] - 13
    if panda.rect.bottom <= 9:
        panda.rect.bottom = 10
    # if panda.rect.top <= 0:
    #     panda.rect.top = 1
    if panda.rect.bottom > SIZE[1]:
        panda.rect.bottom = SIZE[1] - 1

    # 设置起始移动 矩阵坐标
    START_POS = xy_cell(*panda.rect.midbottom)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # 获取 鼠标 点击坐标， 有新的目标啦！
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                # 设置终止坐标
                END_POS = xy_cell(*event.pos)
                ROUTES = get_routes(*START_POS, *END_POS)
                panda.routes = ROUTES
                panda.auto_move_switch = True
                panda.is_move = True
                # print("dfdfd")
    # pygame.draw.line(screen, pygame.Color("red"), (SIZE[0] // 2, 0), (SIZE[0] // 2, SIZE[1]), 1)

    # 判断到达终点 ， 关闭移动开关
    if START_POS == END_POS:
        panda.auto_move_switch = False
        panda.is_move = False

    if panda.auto_move_switch and ROUTES:
        # delay -= 1
        # if delay == 0:
        # panda.rect.midbottom = cell_xy(*ROUTES[-1])
        dot = cell_xy(*panda.routes.pop())
        # panda.goto(*dot)
        # print(f'midbottom = {panda.rect.midbottom}--- dot = {dot}')
        off = pygame.Vector2(dot) - pygame.Vector2(old_dot)
        offset_vec = (int(off.x), int(off.y))
        # print(f'offset_vec = {offset_vec}')
        if offset_vec in list(dir_dict):
        #     print(f"dir = {panda.direction}")
            panda.direction, panda.vel.x, panda.vel.y = dir_dict[offset_vec]

        # if :
            # delay = delay_fps



    panda.update(current_time, 80)
    panda.move()
    old_dot = panda.rect.midbottom
    # 绘制精灵
    panda.draw(screen)

    # 3.刷新
    pygame.display.update()
    clock.tick(FPS)



