# bj_2750.py

N = int(input())
arr = []
for case in range(N):
    arr.append(int(input()))
arr.sort()

for i in arr:
    print(i)