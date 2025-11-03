# boj_1463.py
# iq검사
import sys
input = sys.stdin.readline
# 0~6까지 이미 구해둔 답
arr = [0,0,1,1,2,3,2]
X = int(input())

if 6 >= X:
    print(arr[X])
else:
    for i in range(7, X+1):
        case1 = arr[i-1] + 1 # 1을 빼는 경우
        if i % 2 == 0: # 2로 나누어지는 경우
            case2 = arr[i//2] + 1
        else:
            case2 = 100000000000000
        if i % 3 == 0: # 3로 나누어지는 경우
            case3 = arr[i//3] + 1
        else:
            case3 = 100000000000000
        min_val = min(case3, case1, case2)
        arr.append(min_val)
    print(arr[-1])
