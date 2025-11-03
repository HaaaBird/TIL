# boj_15655.py
# N과 M(6)

"""
문제
N개의 자연수와 자연수 M이 주어졌을 때,
아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
N개의 자연수는 모두 다른 수이다.

N개의 자연수 중에서 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

조합으로 풀라는 뜻.
"""

def backt(arr, start, n, m):
    global in_arr
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start, n):
        if in_arr[i] not in arr:
            arr.append(in_arr[i])
            backt(arr, i, n, m)
            arr.pop()

N, M = map(int, input().split())
in_arr = list(map(int, input().split()))
in_arr.sort()
backt([], 0, N, M)