# boj_1676.py
# 팩토리얼 0의 개수
"""
0의 수를 센다 -> 2x5를 찾는거라고 봐야함.
더 정확히는, 5의 개수를 찾는다고 봐도 크게 문제될건 없을듯?
5는 항상 부족한데 비해 2는 분해하면 나옴.
"""

N = int(input())
cnt = 0
for i in range(1, N + 1):
    if i % 5 == 0:
        temp = i
        while temp % 5 == 0:
            temp //= 5
            cnt += 1

print(cnt)

def power(n):
    if n == 0:
        return 1
    else:
        return n * power(n - 1)


print(power(N))