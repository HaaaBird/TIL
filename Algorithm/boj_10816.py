# boj_10816.py
# 숫자 카드
import sys
import time
import random

input = sys.stdin.readline


def get_sample_data():
    N = random.randint(99_000, 100_000)
    N_list = [random.randint(1, 100_000) for _ in range(N)]
    M = random.randint(99_000, 100_000)
    M_list = [random.randint(1, 100_000) for _ in range(M)]
    return N, N_list, M, M_list


def counting_solve(N, c_arr, M, s_arr):
    start_time = time.time()
    cnt_arr = [0] * 20_000_001
    result = []
    for i in range(N):
        cnt_arr[c_arr[i] + 10_000_000] += 1
    for i in range(M):
        result.append(cnt_arr[s_arr[i] + 10_000_000])
    end_time = time.time()
    print("카운팅: ",round(end_time - start_time,5))
    return round(end_time - start_time, 5)


def dictionary_solve(N, c_arr, M, s_arr):
    start_time = time.time()
    cnt_dict = {}
    for i in range(N):
        if cnt_dict.get(c_arr[i]) is None:
            cnt_dict.update({c_arr[i]: 1})
        else:
            cnt_dict[c_arr[i]] += 1
    result = []
    for i in range(M):
        if cnt_dict.get(s_arr[i]) is None:
            result.append(0)
        else:
            result.append(cnt_dict[s_arr[i]])
    end_time = time.time()

    print("딕셔너리: ",round(end_time - start_time,5))
    return round(end_time - start_time,5)


if __name__ == "__main__":
    N, c_arr, M, s_arr = get_sample_data()
    print("초기 N, M: ", N, M)
    c_result = counting_solve(N, c_arr, M, s_arr)
    d_result = dictionary_solve(N, c_arr, M, s_arr)
    print((1 - c_result/d_result) * 100)