# marge_sort.py


def marge_sort(in_arr):
    if len(in_arr) != 1:
        mid = len(in_arr) // 2
        left_arr = in_arr[:mid]
        right_arr = in_arr[mid:]
        marge_sort(left_arr)
        marge_sort(right_arr)

        if left_arr > right_arr:
            left_arr, right_arr = right_arr, left_arr



if __name__ == "__main__":
    start_arr = [6, 3, 9, 2]
    marge_sort(start_arr)

    pass
