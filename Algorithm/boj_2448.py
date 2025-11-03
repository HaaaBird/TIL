# boj_2448.py
# 별 찍기 11

def star(n, s):
    if n == 0:
        return
    if n - s == 3:
        for i in range(1, n * 2):
            if i % 6 != 0:
                matrix[n-1][i-1] = "*"
            else:
                matrix[n-1][i-1] = " "
        star(n, s+1)
    elif n - s == 2:
        for i in range(1, n * 2):
            if i % 6 == 0:
                pass
            elif i % 2 == 1:
                pass
            else:
                matrix[n - 2][i - 1] = "*"
        star(n, s+1)
    else:
        for i in range(1, n * 2):
            if i % 6 == 0:
                pass
            elif i % 3 == 0:
                matrix[n - 3][i - 1] = "*"
        star(n-3, s-5)


N = int(input())
matrix = [[" "] * (N * 2 - 1) for _ in range(N)]
p_check = N - 3

star(N, p_check)

for arr in matrix:
    print("".join(map(str,arr)))
