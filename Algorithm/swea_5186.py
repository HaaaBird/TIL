# swea_5186.py
# 이진수2

T = int(input())


for case in range(1, T + 1):
    N = float(input())
    result = []
    while N:
        if len(result) > 13:
            break
        N = N * 2
        if N >= 1:
            result.append(1)
            N -= 1
        else:
            result.append(0)
    if len(result) > 13:
        print(f"#{case} overflow")
    else:
        print(f"#{case}","".join(map(str, result)))