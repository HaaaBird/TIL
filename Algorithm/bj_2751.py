import sys
input = sys.stdin.readline

T = int(input())
arr = []
for case in range(T):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)