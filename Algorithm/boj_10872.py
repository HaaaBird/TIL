# boj_10872.py
# 팩토리얼

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * (factorial(n - 1))


if __name__ == "__main__":
    N = int(input())
    a = factorial(N)
    print(a)