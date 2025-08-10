# boj_18110.py
# Solved.AC
import sys
input = sys.stdin.readline

def round_new(value):
    if value - int(value) >= 0.5:
        value = int(value) + 1
    else:
        value = int(value)
    return value

def cut(arr, target):
    sec_target = target
    for i in range(len(arr)):
        if arr[i] == 0:
            pass
        elif arr[i] >= target:
            arr[i] -= target
            break
        elif arr[i] < target:
            target -= arr[i]
            arr[i] = 0
    for i in range(len(arr)-1, 0, -1):
        if arr[i] == 0:
            pass
        elif arr[i] >= sec_target:
            arr[i] -= sec_target
            break
        elif arr[i] < sec_target:
            sec_target -= arr[i]
            arr[i] = 0
    return arr


N = int(input())
if N == 0:
    print(0)
else:
    arr = [0] * 31
    for i in range(N):
        arr[int(input())] += 1
    cut_range = round_new(N * 0.15)
    arr = cut(arr, cut_range)
    sum = 0
    for i in range(len(arr)):
        sum += arr[i] * i
    print(round_new(sum / (N-(cut_range*2))))
