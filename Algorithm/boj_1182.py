# boj_1182.py
# 부분수열의 합

import sys
input = sys.stdin.readline

def my_solve(N,S,arr):
    cnt = 0
    for i in range(1 << N):
        n_arr = []
        for j in range(N):
            if i & (1 << j):
                n_arr.append(arr[j])
        if len(n_arr) == 0:
            pass
        else:
            if sum(n_arr) == S:
                cnt += 1
    print(cnt)
def use_library(N,S,arr):
    import sys
    from itertools import combinations
    cnt = 0
    for i in range(1, N+1):
        comb = combinations(arr,i) # 1~N 개의 원소를 가지는 조합을 뽑아줌
        for j in comb:
            if sum(j) == S:
                cnt += 1
    print(cnt)
if __name__ == "__main__":
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    my_solve(N,S,arr)




# 부분수열 리스트를 다 받아오고
# 비트 연산 통해서 가능한 부분집합 다 만들기
# 가능한 부분집합에 sum 값이 S에 해당하는 거 카운트


