# boj_1916.py
# 최소비용 구하기
from heapq import heappop, heappush


def dijkstra(start_node):
    pq = [(0, start_node)]  # 가중치, 시작 노드
    INF = 10 ** 9  # 처음 들어갈 가중치. 최소거리 구하는거니 최대값 넣는거
    dists = [INF] * N  # 각 노드들에 대한 가중치 초기화
    dists[start_node] = 0  # 시작 노드에 대해서는 거리 0으로 막아서 갱신 못하게 처리

    while len(pq) != 0:
        dist, node = heappop(pq)
        if dists[node] < dist:  # 이미 갱신했던 노드라면 넘어가기
            continue
        for next_dist, next_node in graph[node]:  # 현재 노드에서 갈 수 있는 노드 확인
            new_dist = next_dist + dist  # 다음 노드 거리는 출발지로부터 누적된 거리값이 넘어가게
            if dists[next_node] < new_dist:
                continue  # 이미 갱신된 노드라면 넘어가기
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    return dists


N = int(input())
M = int(input())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((w, b))

start, end = map(int, input().split())

result = dijkstra(start - 1)
print(result[end - 1])
