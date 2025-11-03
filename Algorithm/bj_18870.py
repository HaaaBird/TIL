# bj_18870.py
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

comp_map = {}
sort_arr = sorted(set(arr))

for idx, value in enumerate(sort_arr):
    comp_map[value] = idx

for i in arr:
    print(comp_map[i], end= " ")
