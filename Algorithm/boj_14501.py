# boj_14501.py
# 상담

N = int(input())
date_arr = []
value_arr = []
for _ in range(N):
    A, B = map(int,input().split())
    date_arr.append(A)
    value_arr.append(B)

select = [[date_arr[0], value_arr[0]]]
for i in range(1, N):
    now_val = []
    max_val = 0

    while True:
        change_cnt = 0
        single_list = []
        for j in range(len(select)):
            if len(select[j]) != 1:
                if select[j][0] == 1: # 날짜가 다 지났다면 돈으로 환산
                    now_val.append(select[j][1])
                    select.pop(j)
                    change_cnt += 1
                    break
                else:
                    select[j][0] -= 1
        if change_cnt == 0:
            break
        for j in rnage(len(select)):

    if len(now_val) != 0:
        max_val = max(now_val)
        select.append([max_val])
    select.append([date_arr[i], value_arr[i] + max_val])

result = 0
# for i in range(len(select)):
#     if select[i][0] == 1:
#         result = max(result, select[i][1])
print(select)
print(result)




