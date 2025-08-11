# boj_24479.py
# 알고리즘 수업 - 깊이 우선 탐색1


def dfs(adj, R):
    visits = [R]
    while True:
        if len(adj[R]) == 0:
            break
        else:
            dfs(adj, adj[R])
    return visits

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
adj = [[] for _ in range(N + 1)]


for item in arr:
    adj[item[0]].append(item[1])
    adj[item[1]].append(item[0])

result = dfs(adj, R)
print(result)