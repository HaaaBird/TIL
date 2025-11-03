from heapq import heappop, heappush


def dijkstra(start_node):
    pq = [(0, start_node)]  # 시작 노드 기준으로 누적 거리, 노드 번호
    dists = [INF] * V  # 시작할땐 정점까지의 최저값. 시작은 무한대
    dists[start_node] = 0  # 노드 시작점 초기화

    while len(pq) != 0:
        dist, node = heappop(pq)  # 최소값 빼기
        if dists[node] < dist:# 이미 더 작은 값으로 온 적이 있으면 버린다.
            continue
        for next_dist, next_node in graph[node]:# 다음 노드로 가기 위한 누적 거리 계산
            new_dist = dist + next_dist  # 새 거리 + 현재까지 누적거리
            if dists[next_node] <= new_dist:# 이미 작거나 같은 가중치로 온 적이 있으면 continue
                continue
            dists[next_node] = new_dist # 누적거리와 새로운 노드들 pq에 저장해주고 dists 에 갱신
            heappush(pq, (new_dist, next_node))
    return dists


INF = int(21e8)  # 무한대를 가정(문제의 최대)
V, E = map(int, input().split())
start_node = 0  # 시작점 노드. 문제에 따라 다름.
graph = [[] for _ in range(V)]  # 인접 리스트로 구현.

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))  # 우선순위큐에서 뺄려고 . 단 주의사항은 단방향

# 출발지로부터 모든 최단거리를 나오게

result = dijkstra(0)
print(result)
