# boj_2839.py
# 설탕 배달

"""

가능하면 5로 나누어 보고 몫을 더하고 나머지를 갱신한다.

"""
# 0~ 14까지 미리 구한 값.
arr = [-1, -1, -1, 1, -1, 1, 2, -1, 2, 3, 2, 3, 4, 3, 4]
N = int(input())

if 14 >= N: # 이미 구한 값 중에 답이 있으면
    print(arr[N])
else:
    for i in range(1, N - 13):
        now_weight = 14 + i
        case1 = arr[now_weight - 3] + 1
        case2 = arr[now_weight - 5] + 1
        result = min(case2, case1)
        arr.append(result)
    print(arr[-1])