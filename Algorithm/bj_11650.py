N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

sort_list = sorted(arr, key=lambda x:(x[1],x[0]))
for xy in sort_list:
    print(xy[0], xy[1])
