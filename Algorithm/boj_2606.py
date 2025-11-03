# boj_2606.py
# 바이러스

# 그냥 인접행렬 구해서 풀면 될듯?


N = int(input())
V = int(input())
tree = [[] for _ in range(101)]

for _ in range(V):
    idx, val = map(int, input().split())
    tree[idx].append(val)
    tree[val].append(idx)

# 100 이하의 양의 정수니까 간선 뭐 그리 많지 않겠지 뭐. dfs로 풀자

stack = [1]
visits = {1}
while len(stack) != 0:
    now = stack.pop()
    visits.add(now)
    if len(tree[now]) != 0:
        for i in range(len(tree[now])):
            if tree[now][i] not in visits:
                stack.append(tree[now][i])


print(len(visits)-1)
