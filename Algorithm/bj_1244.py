def reverse_swicth(input_val):
    return int(not(input_val))

switch_num = int(input())
switch_list = [None] + list(map(int, input().split()))
switch_ok = False

user_num = int(input())

for user in range(user_num):
    gender, switch_idx = map(int, input().split())

    if gender == 1: #남자. idx가 배수값에 해당하는 스위치 상태 뒤집기. 2 -> 2,4,6 ...
        for i in range(switch_idx, len(switch_list), switch_idx):
            switch_list[i] = reverse_swicth(switch_list[i])

    else: # 여자. idx 값 중심으로 대칭 구간 찾아서 전체 전환
        left = switch_idx
        right = switch_idx
        while True:
            l = left - 1
            r = right + 1
            if l <= 0 or r > switch_num:
                break
            elif switch_list[l] != switch_list[r]:
                break
            left = l
            right = r
        for i in range(left, right+1):
            switch_list[i] = reverse_swicth(switch_list[i])

# 20개씩 출력
for i in range(1, switch_num + 1):
    print(switch_list[i], end=" ")
    if i % 20 == 0:
        print()