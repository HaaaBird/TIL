# swea_5202.py
# 화물 도크

"""
스케줄링 문제
1. 종료 시간이 빠른 순서대로 정렬
2. 첫 번쨰 활동 선택
3. 남은 활동의 종류시간보다 빠른 시작시간을 모두 제거
4. 남은 선택들 반복
"""

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x:x[1])

    work_cnt = 0
    last_work_end = 0
    for i in range(N):
        if arr[i][0] >= last_work_end:
            work_cnt += 1
            last_work_end = arr[i][1]
    print(f"#{case} {work_cnt}")