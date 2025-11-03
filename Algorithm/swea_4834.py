T = int(input())

for case in range(T):
    N = int(input())
    arr = [int(my_int) for my_int in input()]
    idx_list = [0] * 10

    for i in arr:
        idx_list[i] += 1

    if idx_list.count(max(idx_list)) == 1:
        print(f"#{case+1} {idx_list.index(max(idx_list))} {max(idx_list)}")
    else:
        result_num = 0
        for i in range(len(idx_list)):
            if idx_list[i] == max(idx_list) and result_num < i:
                result_num = i
        print(f"#{case+1} {result_num} {max(idx_list)}")
