# swea_2112.py
# 보호필름

"""
시간이 생각보다 길다
당장 떠오르는건 백트래킹 써서 모든 경우 다 조사해보는 방법 정도가 떠오르긴 한데

나머지 도식화해서 이쁘게 푸는건 떠오르지가 않는다.

백트래킹으로 풀면

일단 기본 입출력 하고

기본 검사해서 pass 면 0 출력
안되면 첫번째 줄부터 그냥 깡으로 백트래킹 해 보자. 이거 말곤 떠오르는게 없다.

"""

import copy


def test(d, w, k):
    for j in range(w):
        flag = False
        if k <= 1:
            continue
        prev = matrix[0][j]
        cnt = 1
        for x_idx in range(1, d):
            if matrix[x_idx][j] == prev:
                cnt += 1
                if cnt >= k:
                    flag = True
                    break
            else:
                prev = matrix[x_idx][j]
                cnt = 1
        if flag:
            continue
        else:
            return False
    return True


def backt_A(start, r_cnt):
    global cnt
    # 만약 이미 답을 찾았는데 깊이가 더 깊다면 더 볼 필요 없음.
    if r_cnt >= cnt:
        return
    elif test(D, W, K):
        if r_cnt < cnt:
            cnt = r_cnt
        return
    for floor in range(start, D):
        matrix[floor] = [0] * W
        backt_A(floor + 1, r_cnt + 1)
        matrix[floor] = c_matrix[floor]
        matrix[floor] = [1] * W
        backt_A(floor + 1, r_cnt + 1)
        matrix[floor] = c_matrix[floor]


T = int(input())
for case in range(1, T + 1):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]
    c_matrix = copy.deepcopy(matrix)
    cnt = K
    backt_A(0, 0)
    print(f"#{case} {cnt}")
