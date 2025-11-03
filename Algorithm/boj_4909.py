# boj_4909.py
import math

while True:
    arr = list(map(float, input().split()))
    arr.pop(arr.index(max(arr)))
    arr.pop(arr.index(min(arr)))
    sum_all = 0
    for i in range(4):
        sum_all += arr[i]

    result = sum_all / 4

    if result == 0:
        print()

    elif result.is_integer():
        print(int(result))

    else:
        print(result)
