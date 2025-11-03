# boj_20168.py
from heapq import heappop, heappush
def find(start_node):
    pq = [(0, 0, start_node)] # 거리, 누적거리, 노드
    INF = 10**21
    dists = [INF] * N
    dists[start_node] = 0

    while pq:
        dist, s_dist, node = pq.pop()
        if dists[node] < s_dist or s_dist > C:
            continue
        for new_dist, new_node in graph[node]:
            m_dist = max(new_dist, dist)
            ss_dist = new_dist + s_dist # 누적합 신규
            if dists[new_node] < ss_dist or ss_dist > C:
                continue
            pq.append((m_dist, ss_dist, new_node))
            dists[new_node] = m_dist
        pq.sort(key=lambda x:(x[0], x[1]))
    return dists



N, M, A, B, C = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,w = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((w, b))
    graph[b].append((w, a))


a = find(A - 1)
print(a[B - 1])
print(a)
