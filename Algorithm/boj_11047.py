# boj_11047.py
# 동전 0

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0
while True:
    # 큰 동전 나누기 연산해서 해당 동전으로만 구성 가능한지 확인하고 가능하면 break
    # 안되면 작은 동전으로 내려감
    now_coin = coins.pop()
    if K % now_coin == 0:
        cnt += K // now_coin
        break
    elif K // now_coin == 0:
        pass
    else:
        cnt += K // now_coin
        K = K - (K//now_coin * now_coin)
print(cnt)
