# boj_10775.py
# 공항
"""
cnt_list 로 받은다음
값 정리하면 될거같은데
"""
N = int(input())
P = int(input())
cnt_list = [0] * (N + 1)

for _ in range(P):
    cnt_list[int(input())] += 1
result = 0
zero_cnt = 0
p_cnt = 0
for i in range(1, N + 1):
    p_cnt += cnt_list[i]
    if cnt_list[i] == 1:
        result += 1
    elif cnt_list[i] == 0:
        zero_cnt += 1
    elif cnt_list[i] > 1:
        result += 1
        num = cnt_list[i] - 1
        if zero_cnt == 0:
            pass
        elif num >= zero_cnt:
            result += zero_cnt
            zero_cnt = 0
        else:
            result += zero_cnt - num
            zero_cnt -= num
    if p_cnt >= N:
        break
print(result)
