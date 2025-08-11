# swea_3143.py
# 빠른 문자열 타이핑


T = int(input())
for case in range(1, T + 1):
    A, B = map(str, input().split())
    cnt = 0
    cnt += A.count(B)
    A = A.replace(B, '')
    cnt += len(A)
    print(f'#{case} {cnt}')