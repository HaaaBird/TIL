# boj_1874.py
# 스택 수열

import sys
input = sys.stdin.readline

N = int(input())
target = [int(input()) for _ in range(N)]


s_list = list(reversed(range(1,N+1)))

stack = [0]
work_stack = []
result = []

success = False
stack.append(s_list.pop())
work_stack.append("+")
target_idx = 0

while True:
    if stack[-1] == target[target_idx]:
        stack.pop()
        work_stack.append("-")
        target_idx += 1
    elif target[target_idx] < stack[-1]:
        break
    elif target_idx == N:
        success = True
        break
    else:
        stack.append(s_list.pop())
        work_stack.append("+")
if success:
    print("YES")
else:
    print("No")