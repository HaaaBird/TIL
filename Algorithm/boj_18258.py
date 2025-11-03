# boj_18258.py
# 큐2

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

queue = deque([])
for i in range(N):
    order = list(input().split())
    if order[0] == "push":
        queue.append(order[1])
    elif order[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif order[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
