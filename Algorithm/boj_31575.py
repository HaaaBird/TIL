# boj_31575.py
# 도시와 비트코인

"""

문제
전날에 비해 비트코인의 시세가 백만원이나 오른 어느 아침,
진우는 거래소에 가서 비트코인을 매도하려고 한다.
현재 비트코인의 시세가 점점 떨어지고 있기 때문에 진우는 최대한 빨리 거래소에 가야 한다.

도시는 가로
$N$, 세로
$M$ 크기의 격자 모양으로 이루어졌다.
진우는 북서쪽 끝에 있고 거래소는 남동쪽 끝에 있다.
도시의 일부 구역은 공터 또는 도로라서 진우가 지나갈 수 있지만,
어떤 구역은 건물이 있어서 진우가 갈 수 없다.

진우는 최대한 빨리 거래소에 가야 하므로,
동쪽(오른쪽) 또는
남쪽(아래쪽)으로만 이동하여 거래소로 도착할 수 있어야 한다.
진우를 도와 거래소로 갈 수 있는지 구하는 프로그램을 작성하여라. 진
우의 현재 위치가 거래소일 수 있다.

입력
첫 번째 줄에 도시의 가로 크기
$N$과 세로 크기
$M$ (
$1 \le N, M \le 300$)이 주어진다.

두 번째 줄부터
$M$개의 줄에는 도시의 형태를 나타내는
$N$개의 정수가 공백을 사이에 두고 주어진다. 각 칸이 1인 경우 진우가 갈 수 있는 칸을 의미하고 0인 경우 진우가 갈 수 없는 칸을 의미한다.

왼쪽 위의 끝 칸과 오른쪽 아래의 끝 칸은 모두 1이다.

출력
첫 번째 줄에 진우가 거래소로 갈 수 있으면 Yes를, 그렇지 않으면 No를 출력한다.

그냥 dfs로 검색해서 찾으면 됨. 첫 줄에서 출발 가능
"""
delta = [(0, 1), (1, 0)]
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
end = (N-1, M-1)
success_flag = False

stack = [(0,0)]
visit = set()
while len(stack) != 0:
    ii, jj = stack.pop()
    visit.add((ii, jj))
    if ii == N - 1 and jj == M - 1:
        success_flag = True
        break
    for k in range(2):
        ni = ii + delta[k][0]
        nj = jj + delta[k][1]
        if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 1 and (ni, nj) not in visit:
            stack.append((ni, nj))
            visit.add((ni, nj))

if success_flag:
    print("Yes")
else:
    print("No")