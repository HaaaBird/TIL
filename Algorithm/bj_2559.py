import sys
input = sys.stdin.readline

n, m = map(int, input().split())
temp_list = list(map(int, input().split()))
sum_list = [0]
sum = 0
temp_sum = []
for i in range(n):
    sum = sum + temp_list[i]
    sum_list.append(sum)

for i in range(n-m+1):
    temp_sum.append(sum_list[i+m] - sum_list[i])

print(max(temp_sum))