# boj_1922.py
# 네트워크 연결

from heapq import heappop, heappush


def prim(start_node):
    MST = [0] * N  # 방문 처리 할 노드
    min_result = 0  # 리턴할 최소 가중치 합
    queue = [(0, start_node)]

    while len(queue) != 0:
        now_weight, now_node = heappop(queue)
        if MST[now_node] == 1:
            continue
        MST[now_node] = 1  # 방문 처리
        min_result += now_weight  # 가중치 부여

        for i_weight, i_node in graph[now_node]:
            if MST[i_node] == 1:  # 이미 방문한 노드라면
                continue
            heappush(queue, (i_weight, i_node))
    return min_result


N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((w, v))
    graph[v].append((w, u))

result = prim(0)
print(result)
