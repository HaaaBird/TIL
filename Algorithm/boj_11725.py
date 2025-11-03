# boj_11725.py
# 트리의 부모 찾기

"""

이진 트리인지 뭔지가 없다. 걍 양방향 트리라고 가정하고
일단 트리 형태로 값을 받아오고
1에서부터 내려가면서 자식, 부모 정보를 기록한다.

"""
import sys
input = sys.stdin.readline
N = int(input())
tree = {}

for _ in range(N-1):
    a, b = map(int, input().split())
    if tree.get(a):
        tree[a].append(b)
    else:
        tree.update({a:[b]})
    if tree.get(b):
        tree[b].append(a)
    else:
        tree.update({b:[a]})

stack = [1]
parent = [0] * (N + 1)
while len(stack) != 0:
    now = stack.pop()
    if tree.get(now):
        for idx in tree[now]:
            if parent[idx] == 0:
                stack.append(idx)
                parent[idx] = now
for i in range(2, len(parent)):
    print(parent[i])