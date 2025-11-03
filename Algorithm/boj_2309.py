# boj_2309.py
# 일곱 난쟁이

import sys
input = sys.stdin.readline
N = 9
arr = [int(input()) for _ in range(N)]
result = None
for i in range(1<<N):
    t_arr = []
    for j in range(N):
        if i & (1<<j):
            t_arr.append(arr[j])
    if sum(t_arr) == 100 and len(t_arr) == 7:
        result = t_arr
        break
for item in result:
    print(item)