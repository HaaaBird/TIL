# swea_1251.py
# 하나로
from heapq import heappop, heappush
import math


def cal_cost(sx, sy, ex, ey):
    x_ = abs(sx - ex)
    y_ = abs(sy - ey)
    temp = math.hypot(x_, y_)
    return E * (temp ** 2)


def prim(start_node):
    queue = [(0, start_node)]
    MST = [0] * N
    result = 0

    while len(queue) != 0:
        n_weight, n_node = heappop(queue)
        if MST[n_node] == 1:
            continue
        MST[n_node] = 1
        result += n_weight

        for i in range(N):
            if MST[i] == 1:
                continue
            n_cost = cal_cost(x_list[n_node], y_list[n_node], x_list[i], y_list[i])
            heappush(queue, (n_cost, i))
    return result


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    a = prim(0)
    print(f"#{case} {int(round(a, 0))}")
