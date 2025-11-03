# boj_1197.py
# 최소 스패닝 트리
"""
프림으로 풀어 보자
1. 임의의 정점에서 시작
2. 지금까지 선택한 정점 집합과 연결되는 간선 중 가장 짧은 간선을 선택
3. 그 간선으로 연결된 새로운 정점을 추가
4. 모든 정점이 포함될 때 까지 반복


일단 자료 입력받아서 무향 그래프니까 양방향으로 리스트 만들어서 관리
"""
import heapq
import sys
input = sys.stdin.readline


def prim(start, graph, N):
    visited = [False] * (N + 1)
    pq = []
    total_cost = 0

    heapq.heappush(pq, (0, start))
    while len(pq) != 0:
        cost, now = heapq.heappop(pq)
        if visited[now]:
            continue
        visited[now] = True
        total_cost += cost
        for next_cost, nxt in graph[now]:
            if not visited[nxt]:
                heapq.heappush(pq, (next_cost, nxt))
    return total_cost


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
graph = [[] for _ in range(V + 1)]
for u, v, w in edges:
    graph[u].append((w, v))  # 가중치, 정점
    graph[v].append((w, u))

print(prim(1, graph, V))
