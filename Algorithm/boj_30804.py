# boj_30804.py
# 과일 탕후루
import sys
input = sys.stdin.readline
"""
과일의 종류가 9개니까
cnt list 쓰고
앞, 뒤로 뺴면서 cnt_list에 0이 8개 될때까지 반복
그냥 덱 써서 쉽게 가자
"""

N = int(input())
arr = list(map(int, input().split()))

kinds = set()

start = 0
last = 0
last_len = 1
max_len = 0
for i in range(N):
    if len(kinds) == 0:
        start = i
        kinds.add(arr[i])
    elif i + 1 == N:
        if arr[i] in kinds:
            max_len = max(max_len, i - start + 1)
        else:
            max_len = max(max_len, i-1 - start + 1)

    elif len(kinds) == 1:
        kinds.add(arr[i])
        last_len = 1

    elif arr[i] in kinds:
        if arr[i - 1] == arr[i]:
            last_len += 1
        else:
           last_len = 1
    elif arr[i] not in kinds:
        dist = i - start
        max_len = max(max_len, dist)
        start = i - last_len
        kinds = {arr[i-1], arr[i]}

print(max_len)


