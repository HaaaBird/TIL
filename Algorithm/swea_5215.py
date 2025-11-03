# swea_5215.py
# 햄부기 다이어트



def backT(in_set, n_score, n_cal, start):
    global result
    if n_cal > L:
        return
    elif len(in_set) > 1 and n_cal <= L and result < n_score:
        result = n_score
    for i in range(start, N):
        if i not in in_set:
            in_set.add(i)
            backT(in_set, n_score + parts_list[i][0], n_cal + parts_list[i][1], i)
            in_set.remove(i)
T = int(input())
for case in range(1, T + 1):
    N, L = map(int, input().split())
    parts_list = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    backT(set(), 0, 0, 0)

    print(f"#{case} {result}")
