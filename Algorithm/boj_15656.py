# boj_15656.py
# N과 M(6)

"""
문제
N개의 자연수와 자연수 M이 주어졌을 때,
아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
N개의 자연수는 모두 다른 수이다.

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.

순열 문제네
"""
import sys
input = sys.stdin.readline
def backt(arr, n, m):
    global in_arr
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n):
        arr.append(in_arr[i])
        backt(arr, n, m)
        arr.pop()

N, M = map(int, input().split())
in_arr = list(map(int, input().split()))
in_arr.sort()

backt([], N, M)

