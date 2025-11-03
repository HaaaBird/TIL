# swea_20397.py
# 돌 뒤집기 게임
"""

동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고, 게임의 규칙은 다음과 같다.

i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
주어진 돌을 벗어나는 경우 뒤집기는 중지된다.

[입력]
첫 줄에 게임의 개수 T,
1<=T<=50,
다음 줄부터 게임별로 첫 줄에 돌의 수 N,
3<=N<=20,
뒤집기 횟수 M,
1<=M<=10
다음 줄에 N개 돌의 초기상태,

이후 M개의 줄에 걸쳐 i, j가 주어진다.
(  , 1<=i, j<=N)

[출력]
#과 게임번호, 빈칸에 이어 빈칸으로 구분된 돌의 상태를 출력한다.

# ij_map 에서 받은걸 하나씩 꺼내서 해당 위치만큼을 리스트  슬라이싱 한다.
# 팰린드롬 체크하는거 비슷하게 해서 각 수가 같으면 뒤집고, 다르면 넘어가게 한다.


"""


def diff_check(arr, work, N):
    i = work[0] - 1  # 시작위치
    j = work[1]  # 범위
    di = [-1, 1]

    for k in range(1, 1 + j):
        ni_m = i + di[0] * k
        ni_p = i + di[1] * k
        if 0 <= ni_m < N and 0 <= ni_p < N:
            if arr[ni_m] == arr[ni_p]:
                if arr[ni_m] == 0:
                    arr[ni_m] = 1
                    arr[ni_p] = 1
                else:
                    arr[ni_m] = 0
                    arr[ni_p] = 0
        else:
            break


T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ij_matrix = [list(map(int, input().split())) for _ in range(M)]

    for work in ij_matrix:
        diff_check(arr, work, N)
    print(f"#{case}", *arr)
