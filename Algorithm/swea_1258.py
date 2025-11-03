# swea_1258.py
# 행렬 찾기


"""
일단 매트릭스 다 받아오고
동일한 크기로 방문행렬 만들고
만약 0 이 아니면 델타써서 ㄱ자로 이동
직선 이동하며 컬럼 수 세고
직각이동하며 행 수 센다

둘 다 0에 부딛치면 델타 방향 바꾸고
다 탐색했다면 크기 (크기, 행, 열) 값으로 리스트에 넣어서 저장한다.
마지막에 SORT 해서 X[0] X[1]로 정렬하고 순서대로 출력
"""


delta = [(0, 1), (1, 0)]
T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0 and visit[i][j] == 0: # 0이 아니면, 뭔가 들어 있다면
                d = 0 # 방향 시작은 0
                ni = i
                nj = j
                col_cnt = 1
                row_cnt = 1
                while True:
                    ni += delta[d][0]
                    nj += delta[d][1]
                    if d == 0:
                        if nj >= N or matrix[ni][nj] == 0:
                            d += 1
                            nj -= 1
                        else:
                            col_cnt += 1
                    elif d == 1:
                        if ni >= N or matrix[ni][nj] == 0:
                            break
                        else:
                            row_cnt += 1
                for ii in range(i, ni):
                    for jj in range(j, nj+1):
                        visit[ii][jj] = 1
                result.append([row_cnt * col_cnt, row_cnt, col_cnt])
    result.sort(key=lambda x:(x[0], x[1]))
    print(f"#{case} {len(result)}", end= " ")
    for arr in result:
        print(arr[1], arr[2], end=" ")
    print()


