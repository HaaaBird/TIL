# boj_15651.py
# N 과 M(3)

"""
같은 수를 여러번 골라도 됨.
그러면 49번 알고리즘에서, 나를 고른걸 따지지 않게 만들면 되는거 아닌가
"""

def backtrack(arr, k, n, m):
    global result_list
    if sum(arr) == m:
        array = []
        for j in range(n):
            if arr[j]:
                for k in range(arr[j]):
                    array.append(j + 1)
        print(" ".join(map(str, array)))
        return
    else:
        for i in range(n):
            arr[i] += 1
            backtrack(arr, k, n, m)
            arr[i] -= 1

N, M = map(int, input().split())
arr = [0] * N
result_list = []
backtrack(arr, 0, N, M)