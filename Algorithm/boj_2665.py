from heapq import heappop, heappush
import sys
input = sys.stdin.readline
def find(si, sj):
    INF = 10**21
    dists = [[INF] * N for _ in range(N)]
    pq = [(0, si, sj)]
    while len(pq) != 0:
        dist, i, j = heappop(pq)
        if dists[i][j] < dist:
            continue
        for k in range(4):
            ni = i + delta[k][0]
            nj = j + delta[k][1]
            if 0 <= ni < N and 0 <= nj < N:
                new_dist = dist
                if matrix[ni][nj] == 0:
                    new_dist += 1
                if dists[ni][nj] <= new_dist:
                    continue
                heappush(pq, (new_dist, ni, nj))
                dists[ni][nj] = new_dist
    return dists

N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
a = find(0, 0)
print(a[N-1][N-1])



