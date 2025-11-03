# boj_7581.py
# Cuboids


"""
직육면체 계산 문제
가로 세로 높이 부피 값이 주어지는데 이 중에서 빈칸 있으면 해당 부분 채우기
"""


import sys

while True:
    a,b,c,d = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    elif a == 0:
        a = d // (b*c)
    elif b == 0:
        b = d // (a * c)
    elif c == 0:
        c = d // (a * b)
    elif d == 0:
        d = a * b * c

    print(a,b,c,d)