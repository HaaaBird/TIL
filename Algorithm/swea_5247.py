# swea_5247.py
# 연산
from collections import deque

def find(start_num, cnt):
    queue = deque([(start_num, cnt)])
    visited = {start_num}
    while len(queue) != 0:
        nn, n_c = queue.popleft()
        if nn == M:
            return n_c
        for i in range(4):
            if i == 0 and nn + 1 < 1_000_001 and (nn + 1) not in visited:
                queue.append((nn + 1, n_c + 1))
                visited.add(nn+1)
            elif i == 1 and nn - 1 < 1_000_001 and (nn - 1) not in visited:
                queue.append((nn - 1, n_c + 1))
                visited.add(nn-1)
            elif i == 2 and nn * 2 < 1_000_001 and (nn * 2) not in visited:
                queue.append((nn * 2, n_c + 1))
                visited.add(nn*2)
            elif i == 3 and nn - 10 < 1_000_001 and (nn - 10) not in visited:
                queue.append((nn - 10, n_c + 1))
                visited.add(nn - 10)


T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    min_result = find(N, 0)
    print(f"#{case} {min_result}")
