# swea_5208.py
# 전기버스 2
"""
연료 만땅 넣었을 떄 이동 가능한 거리가 계속 바뀐다.
"""
def backT(charge_cnt, now_p, N):
    global result
    if now_p == N - 1:
        result = min(result, charge_cnt)
        return
    if charge_cnt >= result:
        return

    for i in range(1, arr[now_p] + 1):
        if now_p + i <= N:
            backT(charge_cnt + 1, now_p + i, N)



T = int(input())
for case in range(1, 1 + T):
    arr = list(map(int, input().split()))
    N = arr[0]
    result = 10 ** 9
    start_charge = arr[1]
    arr = arr[1:]

    backT(0, 0, N)
    print(f"#{case} {result - 1}")

