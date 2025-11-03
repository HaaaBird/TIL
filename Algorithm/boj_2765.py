# boj_2765.py
# 자전거
import sys

pi = 3.1415927
inch = 1
feet = 12 * inch
mile = 5280 * feet
cnt = 1

for line in sys.stdin:
    A, B, C = map(float, line.split())
    circle = A * pi

    d = (((circle * B) / 12) / 5280)
    mph = (d / C) * 3600

    print(f"Trip #{cnt}: {round(d,2):.2f} {round(mph,2):.2f}")
    cnt += 1