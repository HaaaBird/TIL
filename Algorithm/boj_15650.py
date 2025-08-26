# boj_15650.py
# N과 M (2)

import sys
input = sys.stdin.readline

def subset(a, k, n, m):
    global result_list
    if k == n:
        if sum(a) == m:
            arr = []
            for i in range(n):
                if a[i]:
                    arr.append(i + 1)
            result_list.append(arr)
    else:
        a[k] = 0
        subset(a, k+1, n, m)
        a[k] = 1
        subset(a, k+1, n, m)
if __name__ == "__main__":
    result_list = []
    N, M = map(int, input().split())
    a = [0] * N   # 선택 여부를 기록할 배열
    subset(a, 0, N, M)
    result_list.sort()
    for arr in result_list:
        print(" ".join(map(str, arr)))

