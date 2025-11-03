# swea_5644.py
# 무선 충전

"""
파이썬 15초. 시간 길다.


5
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
…

// 총 테스트 케이스 개수 T=5
// 첫 번째 테스트 케이스: M=20, A=3
// 사용자A의 이동 정보
// 사용자B의 이동 정보
// AP 1의 정보 (4, 4), C1=1, P1=100
// AP 2의 정보 (7, 10), C2=3, P2=40
// AP 3의 정보 (6, 3), C3=2, P3=70
// 나머지는 sample_input.txt 참조
1. 맵에 그리기

이게 보면 p가 1일때는 십자가 그리고
p가 2부터는 십자가 더하기 사각형 그리기라서 해야하는건

십자가 세로축 거리는 c * 2 + 1

for i in range(c * 2 + 1)
    range_control = min(i, 2 * c - i)
    for j in range(
    아무튼 이런식으로

"""
from pprint import pprint

def charger_install():
    for charger in charger_list:
        x, y, c, p = charger
        x -= 1
        y -= 1
        for i in range(-c, c+1):
            ni = y + i
            for j in range(c, -c-1, -c):
                if 0 <= i < N and 0 <= j < N:
                    matrix[i][j].append(p)
    # 충전기 설치 후 리스트 재정비
    for i in range(N):
        for j in range(N):
            matrix[i][j].sort()



T = int(input())
for case in range(1, T + 1):
    N = 10
    M, A = map(int, input().split())
    user_a = list(map(int, input().split()))
    user_b = list(map(int, input().split()))
    matrix = [[[] for _ in range(N)] for _ in range(N)]
    charger_list = [list(map(int, input().split())) for _ in range(A)]
    charger_install()
    pprint(matrix)
