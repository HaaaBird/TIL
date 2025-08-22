# boj_1260.py
# DFS 와 BFS


"""
문제
그래프를 DFS로 탐색한 결과와
BFS로 탐색한 결과를
출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는
정점 번호가 작은 것을 먼저 방문
하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에
정점의 개수 N(1 ≤ N ≤ 1,000),
간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V
가 주어진다.

다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를,
그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.
"""


def BFS(graph, start):
    queue = [start]
    visits = {start}   # FIX: set(start) -> {start}
    result = []

    head = 0           # pop(0) 대신 포인터로 큐 소진
    while head < len(queue):
        now = queue[head]
        head += 1
        result.append(now)
        for next_node in graph[now]:
            if next_node not in visits:
                visits.add(next_node)   # FIX: now -> next_node
                queue.append(next_node)
    return result


def DFS(graph, start):
    stack = [start]
    visit = set()
    result = []

    while len(stack) != 0:
        now = stack.pop()
        if now in visit:
            continue
        visit.add(now)
        result.append(now)
        for nxt in reversed(graph[now]):
            if nxt not in visit:
                stack.append(nxt)
    return result


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

for child_list in graph:
    child_list.sort()

a = DFS(graph, V)
b = BFS(graph, V)
print(" ".join(map(str, a)))
print(" ".join(map(str, b)))
