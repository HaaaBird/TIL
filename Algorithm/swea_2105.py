# swea_2105.py
# 디저트 카페




"""


친구들과 디저트 카페 투어를 할 계획이다.

[Fig. 1]과 같이 한 변의 길이가
N인
정사각형 모양을 가진 지역에 디저트 카페가 모여 있다.


원 안의 숫자는 해당 디저트 카페에서 팔고 있는 디저트의 종류를 의미하고
카페들 사이에는 대각선 방향으로 움직일 수 있는 길들이 있다.
디저트 카페 투어는 어느 한 카페에서 출발하여
[Fig. 2]와 같이 대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 한다.


디저트 카페 투어를 하는 도중 해당 지역을 벗어나면 안 된다.
또한, 친구들은 같은 종류의 디저트를 다시 먹는 것을 싫어한다.
즉, [Fig. 3]과 같이 카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안 된다.

[Fig. 4]와 같이 하나의 카페에서 디저트를 먹는 것도 안 된다.
[Fig. 5]와 같이 왔던 길을 다시 돌아가는 것도 안 된다.

친구들과 디저트를 되도록 많이 먹으려고 한다.
디저트 가게가 모여있는 지역의 한 변의 길이 N과 디저트 카페의 디저트 종류가 입력으로 주어질 때,
임의의 한 카페에서 출발하여 대각선 방향으로 움직이고
서로 다른 디저트를 먹으면서 사각형 모양을 그리며 다시 출발점으로 돌아오는 경우,
디저트를 가장 많이 먹을 수 있는 경로를 찾고, 그 때의 디저트 수를 정답으로 출력하는 프로그램을 작성하라.
만약, 디저트를 먹을 수 없는 경우 -1을 출력한다.


항상 정사각형, 길이는 N
중복 디저트 없음. visit같은걸로 중복 체크 해 줘야함.
항상 대각선 움직임의 결과로 직사각형 가능. 내 위치로 돌아와야 함.
자기 자리 뺑뺑이 불가능

델타 탐색 문제로도 풀이 가능.

탐색 하는 영역은
첫 줄 처음, 끝 빼고
둘째줄은 전부

i 기준 N-2는 불가능.
"""


di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
T = int(input())
for case in range(1, T + 1):
    max_value = 0
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-2):
        for j in range(1, N-1):
            for a in range(1, N):
                for b in range(1, N):
                    moves = [a,b,a,b]
                    ni = i
                    nj = j
                    go_flag = True
                    visit = set()
                    for k in range(4):
                        if go_flag is not True:
                            break
                        else:
                            for _ in range(moves[k]):
                                ni += di[k]
                                nj += dj[k]
                                if ni < 0 or ni >= N or 0 > nj or nj >= N:
                                    go_flag = False
                                    break
                                elif matrix[ni][nj] in visit:
                                    go_flag = False
                                    break
                                else:
                                    visit.add(matrix[ni][nj])
                    if go_flag:
                        max_value = max(max_value, len(visit))
    if max_value == 0:
        print(f"#{case} -1")
    else:
        print(f"#{case} {max_value}")