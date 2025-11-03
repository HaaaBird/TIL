# boj_27434.py
# 팩토리얼

N = int(input())

all_sum = 1

while N > 0:
    all_sum = all_sum * N
    N -= 1

print(all_sum)