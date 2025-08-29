# boj_15650.py
# N과 M (2)

"""
이번 문제의 경우 중복순열을 뺀다는 조건이 들어간다.

즉 1,2
2,1 이런거 하지 않는다는 뜻.

그러면

해당 숫자를 골랐는지 안골랐는지 기억하는 배열을 갱신하면서 문제를 풀면 된다.


"""
def backtrack(arr, k, n, m):
    global result_list
    if k == n:
        if sum(arr) == m:
            array = []
            for i in range(n):
                if arr[i] == 1:
                    array.append(i+1)
            result_list.append(array)
    else:
        arr[k] = 1
        backtrack(arr, k + 1, n, m)
        arr[k] = 0
        backtrack(arr, k + 1, n, m)


result_list = []
N, M = map(int, input().split())
arr = [0] * N
backtrack(arr, 0, N, M)
for n_arr in result_list:
    print(" ".join(map(str, n_arr)))
