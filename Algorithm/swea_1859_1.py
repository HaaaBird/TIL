# swea_1859_1.py
# 백만 장자 프로젝트

"""
뒤에서부터 스택으로 뺴와서
최고 가격보다 싸면 이득
최고 가격보다 비싸면 얘가 새로운 최고가
"""

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    stack = list(map(int, input().split()))
    result = 0
    best_price = 0
    while len(stack) != 0:
        today_price = stack.pop()
        if today_price > best_price:
            best_price = today_price
        else:
            result += best_price - today_price
    print(f"#{case} {result}")