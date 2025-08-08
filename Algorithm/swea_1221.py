# swea_1221.py
# GNS
#
# import sys
# sys.stdin = open("input.txt", "r")

num_map_1 = {"ZRO":0,"ONE":1,"TWO":2,"THR":3,"FOR":4,
             "FIV":5,"SIX":6,"SVN":7,"EGT":8, "NIN":9}
num_map_2 = {v: k for k, v in num_map_1.items()}
T = int(input())

for _ in range(1, 1 + T):
    case_no, N = map(str, input().split())
    N = int(N)

    arr = list(map(str, input().split()))
    earth_arr = [num_map_1.get(arr[i]) for i in range(N)]
    earth_arr.sort()
    result_word = []
    print(case_no)
    for val in earth_arr:
        result_word.append(num_map_2[val])
    print(" ".join(result_word))