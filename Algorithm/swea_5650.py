# swea_5650.py
# 핀볼게임


"""
nxn 크기의 핀볼판에서 게임함
각도 변환 블록은 5개, 윔홀 6~10번 번호를 가짐. 블랙홀은 -1
벽 만나면 방향 전환

삼각형은 만나는 방향 따라 봐야함
웜홀 만나면 다른 웜홀로 이동
핀볼 만나면 게임 종료 / 출발 위치로 돌아와도 게임 종료

게임판 위에서 출발 위치와 진행 방향을 임의 결정 가능 -> 완전 탐색 하라는 뜻

게임판 크기 N은 5~100
파이썬 15초. 그냥 완탐 돌려도 크게 문제 없어보임.


그래프로 문제 풀긴 어려워 보임

단순히 생각해 보면

1. 각 도형별로 함수를 하나씩 뺀다.
2. 완전탐색을 돌다 만나는 숫자와 방향을 해당 함수에 넣는다.
3. 함수는 해당 방향과 숫자에 따른 방향을 준다.
4. VISIT 함수까진 필요 없고, 시작 위치는 기억해두고, 현재 위치가 다시 시작 위치에 왔는지를 판단한다.
5. 함수에 진입할 때 마다 글로벌에 점수를 카운트 해서 돌려준다.

만들 순서는?
1. 기본 데이터 입출력을 받아오고
2. 이중 FOR 문 + 4개 방향까지 해서 총 3중 FOR문에 WHILE 넣은 형태로 구현한다.

"""
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 좌 우 상 하

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    wormholes = {}
    # 5:[(i,j), (i, j)]
    # 웜홀 탐색해서 별도 딕셔너리로
    for i in range(N):
        for j in range(N):
            if 6 <= matrix[i][j] <= 10:
                if wormholes.get(matrix[i][j]):
                    wormholes[matrix[i][j]].append((i, j))
                else:
                    wormholes.update({matrix[i][j]: [(i, j)]})

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:  # 시작위치는 빈 공간에서 시작
                for d in range(4):
                    i_add, j_add = direction[d]  # 시작 방향값
                    ni, nj = i, j
                    now_score = 0
                    while True:
                        ni += i_add
                        nj += j_add
                        if nj < 0 or nj == N or ni < 0 or ni == N:  # 벽에 박았을 경우
                            ni -= i_add
                            nj -= j_add  # 위치 원상복귀
                            now_score += 1  # 점수 증가
                            j_add *= -1  # 방향전환
                            i_add *= -1  # 방향전환

                        elif ni == i and nj == j:
                            break
                        ########## 1번 !!!!!!!!
                        elif matrix[ni][nj] == 1:
                            now_score += 1  # 점수 증가
                            if i_add == -1 or j_add == 1:
                                ni -= i_add
                                nj -= j_add  # 위치 원상복귀
                                i_add *= -1  # 우 상 충돌이면 180도
                                j_add *= -1
                            elif i_add == 1:  # 하 충돌이면 우로
                                i_add = 0
                                j_add = 1
                            else:  # 좌 충돌이면 상으로
                                i_add = -1
                                j_add = 0
                        ########### 2번
                        elif matrix[ni][nj] == 2:
                            now_score += 1  # 점수 증가
                            if i_add == 1 or j_add == 1:
                                ni -= i_add
                                nj -= j_add  # 위치 원상복귀
                                i_add *= -1  # 하, 우 충돌이면 그냥 방향 180도 전환
                                j_add *= -1
                            elif i_add == -1:  # 상 충돌이면 우회전
                                i_add = 0
                                j_add = 1
                            else:  # 좌 충돌이면 하로
                                i_add = 1
                                j_add = 0
                        ### 3번
                        elif matrix[ni][nj] == 3:
                            now_score += 1  # 점수 증가
                            if i_add == 1 or j_add == -1:
                                ni -= i_add
                                nj -= j_add  # 위치 원상복귀
                                i_add *= -1  # 좌, 하 충돌이면 그냥 방향 180도 전환
                                j_add *= -1
                            elif i_add == -1:  # 상 충돌이면 좌회전
                                i_add = 0
                                j_add = -1
                            else:  # 우 충돌이면 하로
                                i_add = 1
                                j_add = 0
                        ### 4번
                        elif matrix[ni][nj] == 4:
                            now_score += 1  # 점수 증가
                            if i_add == -1 or j_add == -1:
                                ni -= i_add
                                nj -= j_add  # 위치 원상복귀
                                i_add *= -1  # 상, 우 충돌이면 그냥 방향 180도 전환
                                j_add *= -1
                            elif i_add == 1:  # 하 충돌이면 좌회전
                                i_add = 0
                                j_add = -1
                            else:  # 좌 충돌이면 상로
                                i_add = -1
                                j_add = 0
                        ### 5번
                        elif matrix[ni][nj] == 5:
                            ni -= i_add
                            nj -= j_add  # 위치 원상복귀
                            now_score += 1  # 점수 증가
                            i_add *= -1
                            j_add *= -1
                        elif 6 <= matrix[ni][nj] <= 10:  # 5:[(i,j), (i, j)]
                            pairs = wormholes[matrix[ni][nj]]
                            for pair in pairs:
                                if pair == (ni, nj):
                                    pass
                                else:
                                    ni = pair[0]
                                    nj = pair[1]
                        elif matrix[ni][nj] == -1:
                            break
                        if ni == i and nj == j:
                            break

                    max_score = max(max_score, now_score)

    print(max_score)
