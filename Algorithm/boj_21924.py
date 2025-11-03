# boj_21924.py
# 도시 건설
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def prim(start_node):
    queue = [(0, start_node)]
    MST = [0] * N  # 방문 여부확인 리스트
    min_result = 0

    while len(queue) != 0:
        dist, node = heappop(queue)
        if MST[node] == 1:  # 이미 방문했으면 다음으로
            continue
        # 방문 처리
        MST[node] = 1
        min_result += dist

        for next_dist, next_node in graph[node]:
            if MST[next_node] == 1:
                continue
            heappush(queue, (next_dist, next_node))
    return min_result, sum(MST)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
w_sum = 0

for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    w_sum += w
    graph[a].append((w, b))
    graph[b].append((w, a))
min_val, MST_sum = prim(0)
if MST_sum != N:
    print(-1)
else:
    print(w_sum - min_val)