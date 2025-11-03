# 문자열 폭발
"""
스택 쓰는게 힌트.
글자가 100만개 이하니까 값 받아두고
하나씩 stack 하다가 폭발 문자열 만나면 터트려야 할듯?
"""

from collections import deque
import sys
input = sys.stdin.readline
arr = deque(list(input().strip()))
result = []
target = list(input().strip())
target_len = len(target)

for i in range(len(arr)):
    result.append(arr.popleft())
    if result[len(result)-target_len:] == target:
        for _ in range(len(target)):
            result.pop()

if len(result) != 0:
    print("".join(map(str, result)))
else:
    print("FRULA")
