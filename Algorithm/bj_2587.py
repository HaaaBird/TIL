# bj_2587.py
arr = []
all_sum = 0
for i in range(5):
    input_num = int(input())
    arr.append(input_num)
    all_sum += input_num

arr.sort()
print(int(all_sum/5))
print(arr[2])

