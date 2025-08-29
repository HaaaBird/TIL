# boj_15654.py
# N과 M (5)

def backtrack(a_list, n, m):
    if len(a_list) == m:
        result = []
        for idx in a_list:
            result.append(arr[idx])
        print(" ".join(map(str, result)))

    else:
        for i in range(n):
            if i not in a_list:
                a_list.append(i)
                backtrack(a_list, n, m)
                a_list.pop()



N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
zero_arr = []
backtrack(zero_arr, N, M)