# swea_4839.py
# 이진탐색

def b_search(page, target):
    start = 1
    end = page
    s_cnt = 0
    while True:
        s_cnt += 1
        mid = int((end + start) / 2)
        if mid == target:
            break
        elif mid > target:
            end = mid
        elif mid < target:
            start = mid
    return s_cnt


T = int(input())

for case in range(1, T + 1):
    P, A, B = map(int, input().split())
    a_result = b_search(P, A)
    b_result = b_search(P, B)

    if a_result < b_result:
        print(f'#{case} A')
    elif a_result > b_result:
        print(f'#{case} B')
    elif a_result == b_result:
        print(f'#{case} 0')
