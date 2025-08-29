# swea_1232.py
# 사칙연산
"""

중위 순회 하면 계산할 수 있음.
값을 걍 받아서 ㄱ

"""

operator = ["+", "-", "/", "*"]


def calculate(n1, n2, o):
    if o == "+":
        return n1 + n2
    elif o == "-":
        return n1 - n2
    elif o == "/":
        return n1 // n2
    elif o == "*":
        return n1 * n2


def postorder(start):
    n_val = val[start]
    if n_val in operator:
        n1 = postorder(left[start])
        n2 = postorder(right[start])
        return calculate(n1, n2, n_val)
    else:
        return int(n_val)


T = 10
for case in range(1, T + 1):
    N = int(input())
    val = [""] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        arr = list(input().split())
        idx = int(arr[0])
        val[idx] = arr[1]
        if len(arr) == 4:
            left[idx] = int(arr[2])
            right[idx] = int(arr[3])
    print(f"#{case} {postorder(1)}")
