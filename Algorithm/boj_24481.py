# boj_24481.py
# 깊이 우선 탐색

import sys
input = sys.stdin.readline

N,M,start = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(M)]
depth = [0] * (N + 1)
tree = {}
for a, b in nodes:
    if tree.get(a):
        tree[a].append(b)
    else:
        tree.update({a:[b]})
    if tree.get(b):
        tree[b].append(a)
    else:
        tree.update({b:[a]})

for key in tree.keys():
    tree[key].sort(reverse=True)


stack = [start]
visit = {start}

now_depth = 0

while len(stack) != 0:
    now = stack.pop()
    depth[now] = now_depth
    now_depth += 1
    child = tree.get(now,[])
    if child is None:
        pass
    else:
        for node in child:
            if node not in visit:
                stack.append(node)
                visit.add(node)


for a in range(1, len(depth)):
    if a == start:
        print(0)
    elif depth[a] == 0:
        print(-1)
    else:
        print(depth[a])