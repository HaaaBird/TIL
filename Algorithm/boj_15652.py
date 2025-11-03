# boj_15652.py
# N 과 M(4)

"""
같은 수를 여러번 골라도 됨.
근데 비내림차순 조건 -> 유사 조합 문제로 풀라는 것. 중복은 한번만 허용해라
"""

def backt(arr, start, n, m):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start, n):
        arr.append(i+1)
        backt(arr, i, n, m)
        arr.pop()


N, M = map(int, input().split())
backt([], 0, N, M)