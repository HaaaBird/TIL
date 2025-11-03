# boj_1774.py
# 우주신
import math
def get_dist(si, sj, ti, tj):
    return math.hypot(pow(si, ti), pow(sj, tj))

def connect(start_node)
    MST = [0] *


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
gods = []

for _ in range(N):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    gods.append([i, j])

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append((0, B))
    graph[B].append((0, A))

