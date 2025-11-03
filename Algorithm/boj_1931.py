# boj_1931.py
# 회의실 배정

"""
종료 시간 순의로 정렬
첫 번째 활동을 선택하고
선택한 활동의 종료시간보다 빠른 시작 시간 가지면 죄다 제거
남은 활동들에
"""
import sys
input = sys.stdin.readline
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x:(x[1], x[0]))

cnt = 0
last_end_time = 0
for i in range(N):
    if last_end_time <= meetings[i][0]:
        cnt += 1
        last_end_time = meetings[i][1]
print(cnt)