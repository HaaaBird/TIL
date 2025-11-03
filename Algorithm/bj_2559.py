# bj_2559.py
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp_list = list(map(int, input().split()))

stack_num = 0
stack_list = [0]

for i in temp_list:
    stack_num += i
    stack_list.append(stack_num)
max_val = -float('inf')
for i in range(len(stack_list)-K):
    if (max_val < stack_list[i+K] - stack_list[i]):
        max_val = stack_list[i+K] - stack_list[i]

print(max_val)