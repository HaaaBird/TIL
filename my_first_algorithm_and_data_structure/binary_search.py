from bisect import bisect_left

def binary_search(in_list, n):
    start = 0
    last = len(in_list)-1
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
    test_list = list(range(100))
    search_idx, work_count = binary_search(test_list,42)
    print(search_idx, work_count)

def bisect_test():
    sorted_fruits = ['apple', 'banana', 'orange', 'plum']
    result = bisect_left(sorted_fruits, 'kiwi')
    print(result)

if __name__ == "__main__":
    b_searh_main()
    print()
    bisect_test()