# swea_16289.py
# 배열 최소 합

"""
NxN 배열에 숫자가 들어있다.
한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다.
단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
예를 들어 다음과 같이 배열이 주어진다.

2 1 2
5 8 5
7 2 2

이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.
"""


def get_min_sum(i, N, s):
    # 초기 i 는 0, 10, 0
    global min_v  # 초기값 10,000
    if i == N:  #
        if min_v > s:
            min_v = s
    elif min_v < s:  # 중간 합계가 최소합보다 크면
        return
    else:
        for j in range(i, N):  # i 번 부터 N까지 for 문 순회하며 자리 바꿔보기
            p[i], p[j] = p[j], p[i]  # 자리교환
            get_min_sum(i + 1, N, s + matrix[i][p[i]])  # i+1자리 결정
            p[i], p[j] = p[j], p[i]  # 원상복구


if __name__ == "__main__":
    T = int(input())
    for case in range(1, T + 1):
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(N)]
        p = [i for i in range(N)]  # P[i] : i에서 고른 열 번호
        print(p)
        min_v = 10000
        get_min_sum(0, N, 0)
        print(f"#{case} {min_v}")
