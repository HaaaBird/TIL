def marge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        marge_sort(left_half)
        marge_sort(right_half)

        left_ind = 0
        right_ind = 0
        alist_ind = 0
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                arr[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                arr[alist_ind] = right_half[right_ind]
                right_ind += 1
            alist_ind += 1
        while left_ind < len(left_half):
            arr[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1
        while right_ind < len(right_half):
            arr[alist_ind] = right_half[right_ind]
            right_ind += 1
            alist_ind += 1






def marge_sort_2(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        marge_sort(left_half)
        marge_sort(right_half)


        left_idx = 0
        right_idx = 0
        arr_idx = 0
        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] <= right_half[right_idx]:
                arr[arr_idx] = left_half[left_idx]
                left_idx += 1
            else:
                arr[arr_idx] = right_half[right_idx]
                right_idx += 1
            arr_idx += 1










if __name__ == "__main__":
    arr = [3,2,6,9]
    marge_sort(arr)
    print(arr)