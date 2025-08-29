# boj_16953.py
# A -> B

"""
단순 BFS로 문제 풀 수 있을거 같긴 한데
수의 범위가 문제가. 10^9승까지 얘가 버텨 줄까?
그나마 시간제한 2초니까 일단 BFS로 문제 풀어 보면

처음 주어진 숫자를 큐에 넣고
다음 숫자를 계속 APPEND 하면서 탐색하는데, 해당 값이 타겟값보다 크면 APPEND 안하고, 작거나 같으면 넣기
NOW 가 TARGET 과 같으면 스탑하고 탐색 깊이를 리턴
"""

from collections import deque


N, target = map(int, input().split())

depth = 1
queue = deque([(N, depth)])
success = False

while len(queue) != 0:
    now, depth = queue.popleft()
    if now == target:
        success = True
        break
    # 1번 조건 2 곱하기
    a = now * 2
    b = now * 10 + 1
    if b <= target:
        queue.append([b, depth + 1])
    if a <= target:
        queue.append([a, depth + 1])

if success:
    print(depth)
else:
    print(-1)
