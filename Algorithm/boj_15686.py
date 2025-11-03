# boj_15686.py
# 치킨배달

"""

시간 제한이 빡빡하다. 여기서 bfs 쓰면 안됨
그냥 for 문 두번 돌리면서 치킨집 위치 찾고, 그거 가지고 모든 집의 모든 치킨집 거리를 계산해서 가지고 있는다.
백트래킹 써서 치킨집 하나 빠질때마다 모든 집의 최소 치킨집 거리 합이 어찌 되는지 확인해본다.
최소값을 가지치기 조건 쓰면 될듯?
"""


def backT(pf_arr, start):
    global min_result
    n_min = 0
    if len(pf_arr) == M:  # 다 골랐다면 최소값 추정
        for s_house in h_list:
            s_house_min = 10**9
            for i in pf_arr:
                s_house_min = min(s_house_min, s_house[i])
            n_min += s_house_min
            if n_min > min_result:
                return
        min_result = min(min_result, n_min)
        return

    for ch in range(start, len(c_list)):
        pf_arr.append(ch)
        backT(pf_arr, ch+1)
        pf_arr.pop()


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

c_list = []  # (i,j)
h_list = []  # [cd1, cd2, cd3. # 치킨집의 인덱스 길이만큼의 리스트를 h_list[n] 이 가지도록 해야 한다.
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:  # 치킨집이면
            c_list.append((i, j))

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:  # 집을 만나면
            # 모든 치킨집과의 거리 계산
            n_cd_list = []
            for c in c_list:
                temp = abs(c[0] - i) + abs(c[1] - j)
                n_cd_list.append(temp)
            h_list.append(n_cd_list)

pf_arr = []
min_result = 10**9
backT(pf_arr,0)
print(min_result)
