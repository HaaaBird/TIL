# swea_1954.py
# 달팽이

T = int(input())

for case in range(1, T+1):
    N = int(input())
    # 방향설정. 동 -> 남 -> 서 -> 북
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    matrix = [[0] * N for _ in range(N)]
    ni = 0
    nj = -1 # 초기값 설정. 0에서 시작
    d_idx = 0

    for i in range(N*N):
        d_idx = d_idx % 4 # 현재 i % 4해서 방향 선택 반복되도록
        ni += di[d_idx] # 이동
        nj += dj[d_idx]
        matrix[ni][nj] = i+1
        n_ni = ni+di[d_idx]
        n_nj = nj+dj[d_idx]
        # 다음 칸을 미리 확인. 방향 결정 코드
        if n_ni == N or n_nj == N or matrix[n_ni][n_nj] != 0: # 현재 방향 진행시 벽에 부딛침 or 이미 채워진 칸이라면
            d_idx += 1 # 방향 전환
    print(f"#{case}")
    for arr in matrix:
        for value in arr:
            print(value, end=" ")
        print()
