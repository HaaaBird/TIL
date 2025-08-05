# swea_16181.py
# baby gin

T = int(input())
for case in range(T):
    num = int(input())
    count_arr = [0] * 12
    num_arr = []

    # 입력받은 인자의 수를 카운트

    for i in range(6):
        count_arr[num % 10] += 1
        num //= 10

    tri = 0
    run_n = 0
    i = 0
    while i < 10:
        if count_arr[i] >= 3: # triplet 조건에 해당하면
            tri += 1
            count_arr[i] -= 3
            continue
        if count_arr[i] >= 1 and count_arr[ i +1] >= 1 and count_arr[ i +2] >= 1:
            count_arr[i] -= 1
            count_arr[i +1] -= 1
            count_arr[i +2] -= 1
            run_n += 1
            continue
        i += 1
    if run_n + tri == 2: print(f"#{case+1} 1")
    else: print(f"#{case+1} 0")
