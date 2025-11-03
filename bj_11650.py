# bj_11650.py

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

sorted_arr = sorted(arr, key=lambda x: (x[0], x[1]))

for xy in sorted_arr:
    print(xy[0],xy[1])
