from bisect import bisect_left

def binary_search(in_list, n):
    start = 0
    last = len(in_list)
    search_count = 0

    while True:
        search_count += 1
        mid = (last + start) // 2
        if in_list[mid] == n:
            return mid, search_count
        else:
            if in_list[mid] < n:
                start = mid + 1
            else:
                last = mid -1
def b_searh_main():
    test_list = [1,2,3,54,5,231,123]
    test_list = sorted(test_list)
    print(test_list)
    search_idx, work_count = binary_search(test_list,231)
    print(search_idx, work_count)

def bisect_test():
    sorted_fruits = ['apple', 'banana', 'orange', 'plum']
    result = bisect_left(sorted_fruits, 'kiwi')
    print(result)

if __name__ == "__main__":
    b_searh_main()
    print()
    bisect_test()