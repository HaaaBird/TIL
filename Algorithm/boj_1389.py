# boj_1389.py
# 케빈 베이컨
"""
생각 나는건 bfs 써서 푸는데
백트래킹으로 가지치기 조건 잘 달면 6초 짜리 가능할듯?
관계 5000개정도면 뭐
"""

from collections import deque
def bfs(start, depth):
    global minimum, result
    queue = deque([(start, depth)])
    visit = {start}
    n_depth = 0
    while len(queue) != 0:
        ns, nd = queue.popleft()
        n_depth += nd
        if n_depth > minimum:
            break
        for friend in graph[ns]:
            if friend not in visit:
                queue.append((friend, nd + 1))
                visit.add(friend)

    minimum = min(minimum, n_depth)
    if n_depth <= minimum:
        result.append((start, n_depth))


N, M = map(int, input().split())
graph = {}
minimum = 10 ** 9
result = []
for _ in range(M):
    a, b = map(int, input().split())
    if graph.get(a):
        graph[a].append(b)
    else:
        graph.update({a: [b]})
    if graph.get(b):
        graph[b].append(a)
    else:
        graph.update({b: [a]})

for i in range(1, N + 1):
    bfs(i, 0)

result.sort(key=lambda x: (x[1], x[0]))
print(result[0][0])
