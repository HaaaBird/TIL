# swea_50551.py
# 증가하는 사탕 수열

"""
그냥 3개겠다 일단 가능한가 불가능한가는
a <= b <= c로 판정 가능

이후 먹어야 하는 사탕 수는

하니씩 계산하면 될 것 같은데
c랑 b랑 같니? 같으면 1개 빼
b랑 a랑 같니? 같으면 1개 뺴
"""

T = int(input())
for case in range(1 ,T + 1):
    arr = list(map(int, input().split()))
    cnt = 0
    pass_flag = True
    if arr[1] >= arr[2]:
        cnt += (arr[1] - arr[2] + 1)
        arr[1] = arr[1] - (arr[1] - arr[2] + 1)
        if arr[1] <= 0:
            pass_flag = False
    if arr[0] >= arr[1]:
        cnt += (arr[0] - arr[1] + 1)
        arr[0] = arr[0] - (arr[0] - arr[1] + 1)
        if arr[0] <= 0:
            pass_flag = False
    if pass_flag:
        print(f"#{case} {cnt}")
    else:
        print(f"#{case} -1")