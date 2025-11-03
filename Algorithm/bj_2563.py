# bj_2563.py

cp_size = 10
matrix = [[0] * 100] * 100

N = int(input())
cp_arr = []
for case in range(N):
    cp_arr.append(list(map(int, input().split())))

for arr in cp_arr:
    for ya in range(arr[1], arr[1]+cp_size):
        for xa in range(arr[0], arr[0]+cp_size):
            matrix[ya][xa] += 1
    result = 0

for y in range(100):
    for x in range(100):
        if matrix[y][x] > 10:
            result += 1
print(result)
###뭐가 문제인지 몰겠다. 내일 다시 보자