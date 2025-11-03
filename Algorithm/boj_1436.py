# boj_1436.py
# 영화감독 숌

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
num = 666
while cnt < N:
    if "666" in str(num):
        cnt += 1
        num += 1
    else:
        num += 1
print(num-1)