
arr = [0,4,1,3,1,2,4,1]
idx_arr = [0] * (max(arr) + 1)
result_arr = [0] * len(arr)

for val in arr:
    idx_arr[val] += 1

for idx in range(1, len(idx_arr)):
    idx_arr[idx] = idx_arr[idx] + idx_arr[idx-1]

# for val in reversed(arr):
for val in arr:
    idx_arr[val] -= 1
    result_arr[idx_arr[val]] = val

print(result_arr)