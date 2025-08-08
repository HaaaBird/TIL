# boj_1874.py
# 스택 수열

import sys

input = sys.stdin.readline

N = int(input())
target = [int(input()) for _ in range(N)]

stack = []
result = []
work_stack = []

flag = False
s_list = list(reversed(range(1,N+1)))

stack.append(s_list.pop())
work_stack.append("+")
next_push = 1

while True:

    if len(target) == len(result):
        flag = True
        break

    target_num = target[len(result)]
    if target_num > next_push: # 이미 지나간 스택에 있다면, 숫자가 같힌 수라면
        break # 종료하고 fail

    if len(stack) == 0:
        stack.append(s_list.pop())
        work_stack.append("+")
        next_push += 1

    if stack[-1] == target_num:
        result.append(stack.pop())
        work_stack.append("-")
    else:
        stack.append(s_list.pop())
        work_stack.append("+")
        next_push += 1

if not flag:
    print("NO")
else:
    for work in work_stack:
        print(work)
