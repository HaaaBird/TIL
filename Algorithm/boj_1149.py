# boj_1149.py
# RGB 거리

"""
다음 집의 색깔별 가격을 갱신하면서 가면 된다.
"""
import sys
input = sys.stdin.readline

N = int(input())

last_house = [0, 0, 0]
for i in range(N):
    r, g, b = map(int, input().split())
    if i == 0:
        last_house[0] = r
        last_house[1] = g
        last_house[2] = b
    else:
        l0 = min(r + last_house[1], r + last_house[2])
        l1 = min(g + last_house[0], g + last_house[2])
        l2 = min(b + last_house[0], b + last_house[1])
        last_house[0] = l0
        last_house[1] = l1
        last_house[2] = l2


print(min(last_house))
