#boj_3052.py
# 나머지

cnt_arr = [0] * 43
for _ in range(10):
    cnt_arr[int(input()) % 42] += 1

a_cnt = 0

for i in cnt_arr:
    if i != 0:
        a_cnt += 1

print(a_cnt)