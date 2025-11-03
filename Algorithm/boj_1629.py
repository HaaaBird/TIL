# boj_1629.py
# 곱셈


"""
문제 자체는 간단한데 실버1일 리가 없다.
뭔가 있다.

분할 정복을 이용한 거듭제곱 풀이 방식이 있다.

2^16승을 일반 계산 통밥으로 때리면
2^2 를 16번 해야 한다. 이러면 메모리 많이 먹고 접근 시간도 복잡하다.

지수법칙 : a^(n+m) = a^n * a^m
모듈러 성질 : (a*b)%c = (a%c * b%c)%c
"""

import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

result = A
if B % 2 == 0: # 짝수인가?
    b1 = B
else:
    b1 = B - 1
result = A
for i in range(2):
    b1 = b1 // 2
    if b1 == 0:
        break
    else:
        result = ((result % C) ** 2) % C

if B % 2 != 0:
    print((A * result) % C)
else:
    print(result)
