# swea_16297.py
# 토너먼트 카드 게임

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    left = arr[:N//2]
    right = arr[N//2:]
    print(left)
    print(right)