# boj_2096.py
# 내려가기

"""
행 방향으로 돌려서 봤을때, 각 행이 가질 수 있는 값의 경우는 2 3 2개씩.
이중 최대, 최소 2가지로 열방향 진행하면서 값을 확인하면 될듯?

"""
import sys
input = sys.stdin.readline
N = int(input())

if N == 1:
    r_arr = list(map(int, input().split()))
    print(max(r_arr), min(r_arr))
else:
    for i in range(N):
        n_arr = list(map(int, input().split()))
        if i == 0:
            last_max = [n_arr[0], n_arr[1], n_arr[2]]
            last_min = [n_arr[0], n_arr[1], n_arr[2]]
        else:

            # 최대 수열 갱신
            l0 = max(last_max[0] + n_arr[0], last_max[1] + n_arr[0])
            l1 = max(last_max[0] + n_arr[1], last_max[1] + n_arr[1], last_max[2] + n_arr[1])
            l2 = max(last_max[1] + n_arr[2], last_max[2] + n_arr[2])

            m0 = min(last_min[0] + n_arr[0], last_min[1] + n_arr[0])
            m1 = min(last_min[0] + n_arr[1], last_min[1] + n_arr[1], last_min[2] + n_arr[1])
            m2 = min(last_min[1] + n_arr[2], last_min[2] + n_arr[2])

            last_max[0] = l0
            last_max[1] = l1
            last_max[2] = l2

            # 최소 수열 갱신
            last_min[0] = m0
            last_min[1] = m1
            last_min[2] = m2

    print(max(last_max), min(last_min))

