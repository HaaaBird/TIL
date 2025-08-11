# boj_2164.py
# 카드2

from collections import deque

N = int(input())
arr = deque(list(reversed(range(1, N+1))))

while len(arr) != 1:
    arr.pop()
    arr.appendleft(arr.pop())
print(arr[0])