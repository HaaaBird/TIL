# boj_15651.py
# N 과 M(3)

"""
같은 수를 여러번 골라도 됨.

for i in range(N):
backtrack(i)
"""

def backt1(arr, n, m):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1, N+1):
        arr.append(i)
        backt1(arr, n, m)
        arr.pop()

N, M = map(int,input().split())
backt1([], N, M)