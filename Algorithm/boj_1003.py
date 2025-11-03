# boj_1003.py
# 피보나치 함수

import sys
input = sys.stdin.readline

def fibo(num):
    global zero_cnt, one_cnt
    if num == 0:
        zero_cnt += 1
        return 0
    elif num == 1:
        one_cnt += 1
        return 1
    else:
        return fibo(num-1) + fibo(num-2)



T = int(input())
for _ in range(1, T + 1):
    zero_list = [1, 0, 1, 1, 2, 3, 5, 8] # 0~7
    one_list = [0, 1, 1, 2, 3, 5, 8, 13] # 0~7
    in_num = int(input())
    if in_num < 8:
        print(zero_list[in_num], one_list[in_num])
    else:
        for k in range(7, in_num):
            zero_list.append(zero_list[k] + zero_list[k-1])
            one_list.append(one_list[k] + one_list[k-1])
        print(zero_list[-1], one_list[-1])
