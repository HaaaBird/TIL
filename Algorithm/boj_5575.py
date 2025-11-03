# boj_5575.py

for _ in range(3):
    arr = list(map(int, input().split()))
    end = (arr[3] * 3600) + (arr[4] * 60) + arr[5]
    start = (arr[0] * 3600) + (arr[1] * 60) + arr[2]
    work_sec = end - start

    work_h = work_sec // 3600
    work_sec %= 3600
    work_m = work_sec // 60
    work_sec %= 60
    print(work_h, work_m, work_sec)
