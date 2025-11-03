# swea_16811.py
# 당근 포장하기

"""
일단 값을 cnt_list 로 입력 받은 다음에

만약 답이 나온다면
백트래킹 써서 3등분 하는 문제인가?
"""


def backT(start, arr, no_zero_arr, N):
    global global_min_max
    # 처음에 들어가서 박스 사이즈(먹어치울 당근 크기 영역) 선택
    # 조건 들어가는건 박스 사이즈. 박스 하나에 넣을 사이즈를 기준으로 3개 박스 다 채울때까지 재귀
    if len(arr) == 3:
        if sum(arr) != sum(no_zero_arr):
            return
        global_min_max = min(global_min_max, max(arr) - min(arr))
        return

    for i in range(1, len(no_zero_arr)):
        carrot_num = 0
        for j in range(start, start + i):
            if j >= len(no_zero_arr):
                return
            carrot_num += no_zero_arr[j]
        if N // 2 < carrot_num:
            return
        arr.append(carrot_num)
        backT(start + i, arr, no_zero_arr, N)
        arr.pop()

def main_function():
    global global_min_max
    T = int(input())
    for case in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        c_arr = [0] * (N + 1)
        no_zero_arr = []
        for val in arr:
            c_arr[val] += 1

        for val in c_arr:
            if val != 0:
                no_zero_arr.append(val)
        backT(0, [], no_zero_arr, N)
        if global_min_max == 10 ** 9:
            print(f"#{case} -1")
        else:
            print(f"#{case} {global_min_max}")


if __name__ == "__main__":
    global_min_max = 10 ** 9
    main_function()
