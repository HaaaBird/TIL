# boj_28278.py
# 스택2
import sys

input = sys.stdin.readline

stack = []
N = int(input())

for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 3:
        print(len(stack))
    elif order[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
