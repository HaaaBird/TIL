# swea_16126.py 숫자카드


# T = int(input())
T = 1
for case in range(T):

    # N = int(input()) # 카드 장수
    N = 5
    # num = int(input())
    num = 49679
    c = [0] * 10
    for i in range(N):
        c[num % 10] += 1
        num //= 10
    for i in reversed(range(10)):
        if c[i] == max(c):
            print(f"#{case+1} {i} {c[i]}")
            break