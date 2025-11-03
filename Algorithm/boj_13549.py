# boj_13549.py
# 숨바꼭질3

from heapq import heappop, heappush
def find(start_node, target):
    pq = [(0, start_node, 0)]
    INF = 10**9
    dists = [INF] * 100_500
    dists[start_node] = 0

    while len(pq) != 0:
        dist, node, jump = heappop(pq)
        if dists[node] < dist:
            continue

        for next_dist, next_node, next_jump in [(dist + 1, node - 1, 0), (dist + 1, node + 1, 0), (dist + 1, node * 2, 1)]:
            new_dist = next_dist + dist
            if new_dist < 0 or next_node > 100_499 or dists[next_node] <= new_dist:
                continue
            heappush(pq, (new_dist, next_node, jump + next_jump))
            dists[next_node] = new_dist
    return dists



start, target = map(int, input().split())
a = find(start, target)

print(a)

for i in enumerate