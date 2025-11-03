# boj_12851.py
# 숨바꼭질2

"""
bfs로 이동 가능한 영역 다 탐색하고
도달하면 가지치기?
"""
from collections import deque
N, K = map(int, input().split())
best_time = 10 ** 9
queue = deque([(N, 0)])
work_set = set()
while len(queue) != 0:
    x, nt = queue.popleft()
    if x == K: # 만났다면
        print(nt)
        if best_time > nt:
            best_time = nt
    if nt > best_time:
        continue
    for j in range(3):
        if j == 0:
            nx = x + 1
            if 0 <= nx < 100000 and (x, nx) not in work_set:
                queue.append((nx, nt + 1))
                work_set.add((x, nx))
        elif j == 1:
            nx = x - 1
            if 0 <= nx < 100000 and (x, nx) not in work_set:
                queue.append((nx, nt + 1))
                work_set.add((x, nx))
        else:
            nx = x * 2
            if 0 <= nx < 100000 and (x, nx) not in work_set:
                queue.append((nx, nt + 1))
                work_set.add((x, nx))

print(best_time)
