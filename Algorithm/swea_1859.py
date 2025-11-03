# swea_1859.py
# 백만 장자 프로젝트

# pop 한 다음, 이전 가격보다 비싸보다 같으면 이게 best price.
# 만약, pop 한 것이 best 보다 싸면 profit 에 이득 추가
T = int(input())
for case in range(1, T + 1):
    N = int(input())
    stack = list(map(int, input().split()))
    profit = 0
    best_price = 0
    while len(stack) != 0:
        now = stack.pop()
        if now < best_price:
            profit += best_price-now
        elif now >= best_price:
            best_price = now
    print(f"#{case} {profit}")
