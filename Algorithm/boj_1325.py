# boj_1325.py
import sys

input = sys.stdin.readline
def dfs(s_num):
    global result

    stack = [s_num]
    depth = 1

    while len(stack) != 0:
        now = stack.pop()
        depth += 1
        if tree.get(now):
            for child in tree[now]:
                stack.append(child)
    result.append((depth, i))


N, M = map(int, input().split())
tree = {}
for _ in range(M):
    A, B = map(int,input().split())
    if tree.get(B):
        tree[B].append(A)
    else:
        tree.update({B:[A]})
result = []
for i in range(1, N + 1):
    dfs(i)

result.sort(key=lambda x:(x[0], x[1]),reverse=True)
result_nums = []
max_val = result[0][0]
for i in range(N):
    if result[i][0] >= max_val:
        result_nums.append(result[i][1])
    else:
        break
result_nums.sort()
print(*result_nums)