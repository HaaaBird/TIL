# boj_10814.py
# 나이순 정렬
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    age, name = input().split()
    arr.append((int(age), name, i))

arr.sort(key=lambda x:(x[0],x[2]))

for age, name, i in arr:
    print(age, name)