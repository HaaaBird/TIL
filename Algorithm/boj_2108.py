# boj_2108.py
# 통계학
import math
"""
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline


N = int(input())
all_sum = 0
cnt_arr = [0] * 8001

max_ = -4001
min_ = 4001

for i in range(N):
    input_val = int(input())
    all_sum += input_val # 누적합 구하기
    cnt_arr[input_val+4000] += 1 # 카운팅 리스트 갱신
    max_ = max(max_, input_val)
    min_ = min(min_, input_val)

# 중앙값 구하기
count = 0
mid = None
for i in range(8001):
    count += cnt_arr[i]
    if count >=(N // 2 + 1):
        mid = i - 4000
        break

mode_idx = cnt_arr.index(max(cnt_arr)) # 최빈값 중 가장 왼쪽 idx
mode_cnt = max(cnt_arr)
mode = 0
if cnt_arr.count(mode_cnt) == 1:
    mode = mode_idx-4000
else:
    for i in range(mode_idx+1, 8001):
        if cnt_arr[i] == mode_cnt:
            mode = i-4000
            break

# 답
print(round(all_sum/N)) # 평균
print(mid) # 중앙값
print(mode) # 최빈값
print(max_ - min_) # 범위