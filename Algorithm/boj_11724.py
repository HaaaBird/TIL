# boj_11724.py
# 연결 요소의 개수


"""
문제
방향 없는 그래프가 주어졌을 때,
연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.


# 그냥 DFS 로 간선 순회하면서 visit()을 업데이트 해 보고
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = {}
all_set = set()
for _ in range(M):
    a, b = map(int, input().split())
    all_set.add(a)
    all_set.add(b)
    if tree.get(a):
        tree[a].append(b)
    else:
        tree.update({a:[b]})
    if tree.get(b):
        tree[b].append(a)
    else:
        tree.update({b:[a]})

for i in range(1, N + 1):
    if not tree.get(i):
        tree[i] = []

# DFS 코드
visit = set()
cnt = 0
for node in range(1, N + 1):
    if node not in visit:
        cnt += 1
        stack = [node]
        visit.add(node)
        while len(stack) != 0:
            now = stack.pop()
            neighbors = tree.get(now, [])
            for item in neighbors:
                if item not in visit:
                    visit.add(item)  # push 전에 방문 처리
                    stack.append(item)

print(cnt)