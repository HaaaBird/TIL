# boj_1929.py
# 소수 구하기
import sys

import math

M, N = map(int, input().split())
is_prime = [False, False] + [True] * (N - 1)
limit = int(math.sqrt(N))


for p in range(2, limit + 1):
    if is_prime[p]:
        start = p * p
        is_prime[start:N+1:p] = [False] * (((N - start) // p) + 1)

out = []
for x in range(max(M, 2), N + 1):
    if is_prime[x]:
        out.append(str(x))

for num in out:
    print(num)