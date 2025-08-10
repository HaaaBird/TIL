# boj_10989.py
# 수 정렬하기3
import sys
input = sys.stdin.readline

if __name__ == "__main__":

    cnt_arr = [0] * 10001
    N = int(input())
    for i in range(N):
        cnt_arr[int(input())] += 1

    for i in range(len(cnt_arr)):
        if cnt_arr[i] == 0:
            pass
        else:
            for _ in range(cnt_arr[i]):
                print(i)

