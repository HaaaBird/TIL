# swea_1926.py
# 간단한 369 게임
N = int(input())
for i in range(1, N + 1):
    num = i
    clap_cnt = 0
    while num > 0:
        digit = num % 10
        if digit in (3,6,9):
            clap_cnt += 1
        num //= 10
    if clap_cnt == 0:
        print(i, end= " ")
    else:
         print("-" * clap_cnt, end=" ")

