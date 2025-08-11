def move_zeros(arr):
    zero_idx = 0
    for idx, val in enumerate(arr):
        if val != 0:
            arr[zero_idx] = val
            if zero_idx != idx:
                arr[idx] = 0
            zero_idx += 1


arr = [8,0,3,0,12]
move_zeros(arr)
print(arr)