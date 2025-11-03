# swea_5102.py
# 노드의 거리

"""
V개의 노드 개수와
방향성이 없는 E개의 간선 정보
가 주어진다.

주어진 출발 노드에서
최소 몇 개의 간선
을 지나면

도착 노드

에 갈 수 있는지 알아내는 프로그램을 만드시오.

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.
"""
import pprint
T = int(input())
for case in range(1, T + 1):
    V, E = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    tree = {}
    for n1, n2 in matrix:
        if tree.get(n1):
            tree[n1].append(n2)
        else:
            tree.update({n1:[n2]})
        if tree.get(n2):
            tree[n2].append(n1)
        else:
            tree.update({n2:[n1]})

    queue = [(S, 0)]
    visits = {S}              # 방문은 정수 노드만 기록 (튜플 X)
    answer = 0

    while len(queue) != 0:
        now = queue.pop(0)    # now = (node, dist)
        dist = now[1]

        if now[0] == G:
            answer = now[1]
            break

        # 키가 없을 수도 있으니 get(..., []) 사용해서 KeyError 방지
        for nxt in tree.get(now[0], []):
            if nxt not in visits:
                visits.add(nxt)             # 큐에 넣을 때 방문 처리
                queue.append((nxt, dist + 1))

    print(f"#{case} {answer}")
