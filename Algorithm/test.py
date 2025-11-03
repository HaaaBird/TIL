import math

N = int(input())

for _ in range(N):
    a1, b1, r1, a2, b2, r2 = map(int, input().split())
    d = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

    if a1 == a2 and b1 == b2 and r1 == r2:
        print(-1)
    elif d < r1 + r2:
        print(2)
    elif d == r1 + r2:
        print(1)
    elif a1 == a2 and b1 == b2 and r1 != r2:
        print(0)

