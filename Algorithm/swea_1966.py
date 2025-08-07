# swea_1966.py
# 숫자를 정렬하자

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    c = [0] * (max(arr)+1)
    for val in arr:
        c[val] += 1
    for i in range(1,len(c)):
        c[i] = c[i-1] + c[i]
    arr_copy = arr[:]
    for val in arr_copy:
        c[val] -= 1
        arr[c[val]] = val

    print(f"#{case}", end=" ")
    for val in arr:
        print(val, end=" ")
    print()



