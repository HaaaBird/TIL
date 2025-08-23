# marge_sort.py


def marge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        marge_sort(left_arr) # 길이가 2인 리스트가 될 때 까지 4~9번줄을 순회하게 됨
        marge_sort(right_arr) # 여기까지가 분할 코드

        left_idx = 0
        right_idx = 0
        arr_idx = 0
        # 정복 및 합성 코드
        # 분할한 left, right 간 요소 값을 비교해서 한 단계 상위 arr에 삽입.
        while left_idx < len(left_arr) and right_idx < len(right_arr):
            if left_arr[left_idx] > right_arr[right_idx]:
                arr[arr_idx] = right_arr[right_idx]
                right_idx += 1
            else:
                arr[arr_idx] = left_arr[left_idx]
                left_idx += 1
            arr_idx += 1

        while left_idx < len(left_arr):
            arr[arr_idx] = left_arr[left_idx]
            left_idx += 1
            arr_idx += 1

        while right_idx < len(right_arr):
            arr[arr_idx] = right_arr[right_idx]
            right_idx += 1
            arr_idx += 1



if __name__ == "__main__":
    start_arr = [6, 3, 9, 2]
    marge_sort(start_arr)
    print(start_arr)

    pass


a = 3
b = 5
if a > b:
    print(True)
else:
    print(False)