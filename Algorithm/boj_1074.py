# boj_1074.py
# Z

"""
재귀 써서 전체 중에 몇번째 탐색인지를 다음 재귀로 넘긴다.
그렇게 해서 N = 1 까지 시킨다.
"""


def find_position(N, R, C, step):
    if N == 0:
        return step
    length = 2**N
    half = length // 2
    # 상체인가 하체인가 판단 전체 길이 // 2 한거보다 작으면 상체
    ni = 0
    nj = 0
    if R < half and C < half: # 1번 순서
        step += 4 ** (N - 1) * 0
        ni = R
        nj = C
    elif R < half and C >= half: # 2번 순서
        step += 4 ** (N - 1) * 1
        ni = R
        nj = C - half
    elif R >= half and C < half: # 3번 순서
        step += 4 ** (N - 1) * 2
        ni = R - half
        nj = C
    elif R >= half and C >= half: # 4번 순서
        step += 4 ** (N - 1) * 3
        ni = R - half
        nj = C - half
    return find_position(N - 1, ni, nj, step)


N, R, C = map(int, input().split())
print(find_position(N, R, C, 0))