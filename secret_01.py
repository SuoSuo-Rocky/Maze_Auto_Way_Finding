


# suosuo = [
#     [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
#     [1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1],
#     [1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1],
#     [1 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,1],
#     [1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,1],
#     [1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1],
#     [1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1],
#     [1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,1],
#     [1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
#     [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1]
# ]


suosuo = [[0 for i in range(128)] for i in range(80)]



for k, li in enumerate(suosuo):
    li[0] , li[-1] = 1, 1
    if k in [0, len(suosuo) - 1]:
        for k, ele in enumerate(li):
            li[k] = 1

print(f"len first = {len(suosuo[0])},-------- len all = {len(suosuo)}")


print(suosuo)


  # 上、 右 、下 、左
dirs = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
]

# 深度优先
def migong_deep(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    suosuo[x1][y1] = 2
    while len(stack) > 0:
        cur_node = stack[-1]
        if cur_node == (x2, y2):
            print("到达终点，")
            for i ,v in enumerate(stack):
                print(i, v)
            return True
        for d in dirs:
            next_node = d(*cur_node)
            if suosuo[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                suosuo[next_node[0]][next_node[1]] = 2
                break
        else:
            stack.pop()
    else:
        print("There is no way")
        return False

# 广度优先
from collections import deque

def migong_wide(x1, y1, x2, y2):     # Right
    q= deque()
    q.append((x1, y1, -1))
    suosuo[x1][y1] = 2
    traceback = []
    print(f"q = {q}")
    while len(q) > 0:
        cur_node = q.popleft()
        traceback.append(cur_node)
        if cur_node[:-1] == (x2, y2):
            path = []
            i = len(traceback) - 1
            while i >= 0:
                path.append(traceback[i][:-1])
                i = traceback[i][2]
            path.reverse()
            for i,v in enumerate(path):
                print(i, v)
            return True
        for d in dirs:
            next_x, next_y = d(cur_node[0], cur_node[1])
            if suosuo[next_x][next_y] == 0:
                q.append((next_x, next_y, len(traceback) - 1))
                suosuo[next_x][next_y] = 2
    else:
        print("There is no way")
        return False


# migong_wide(10, 10, 2, 2)
migong_wide(9, 17, 60, 20)
# migong_deep(9, 17, 60, 20)

# migong_deep(10, 10, 2, 2)
