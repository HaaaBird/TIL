# boj_1697.py
# 숨바꼭질

"""

문제
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점
N(0 ≤ N ≤ 100,000)에 있고,
동생은 점
K(0 ≤ K ≤ 100,000)에 있다.

수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

그냥 bfs로 풀어야 하는 문제같긴 한데
x-1, x+1, x*2 3개다 큐에 넣어서 탐색 가야 햘듯?
"""

N, K = map(int, input().split())
queue = [(N, 0)]
visit = {N}
head = 0
result = 0

while head < len(queue):
    now, dist = queue[head]
    visit.add(now)
    if now == K:
        result = dist
        break
    head += 1
    now_can = [now-1, now+1, now*2]
    for k in range(3):
        if 0 <= now_can[k] < 100_001 and now_can[k] not in visit:
            queue.append((now_can[k], dist + 1))
print(result)