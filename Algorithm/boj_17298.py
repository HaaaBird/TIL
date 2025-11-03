import sys
n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
stack = [0]


for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
        stack.append(i)

while stack:
    ans[stack.pop()] = -1

for i in range(n):
    print(str(ans[i]) + " ")