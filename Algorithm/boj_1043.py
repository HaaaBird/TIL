# boj_1043.py
# 거짓말

"""
n, m 크기가 50 이하라 완전탐색 해도 1250000 수준이라 그냥 돌려도 된다.
"""

can_lie = set()
cannot_lie = set()
start_cl_len = 0
start_cnl_len = 0
N, M = map(int, input().split())
know_list = list(map(int, input().split()))
party_list = [list(map(int, input().split())) for _ in range(M)]
result = 0

if len(know_list) == 1:
    print(M)
else:
    while True:
        for i in range(1, len(know_list)):
            cannot_lie.add(know_list[i])

        for party in party_list:
            t_set = set(party[1:])
            # 아는 사람이 섞여 있으면 해당 인물들 모두 거짓말 하면 안됨.
            if len(t_set & cannot_lie) != 0:
                for j in range(1, len(party)):
                    cannot_lie.add(party[j])
            else:
                for j in range(1, len(party)):
                    can_lie.add(party[j])
        can_lie = can_lie - cannot_lie

        if start_cl_len == len(can_lie) and start_cnl_len == len(cannot_lie):
            break
        else:
            start_cl_len = len(can_lie)
            start_cnl_len = len(cannot_lie)

        for party in party_list:
            t_set = set(party[1:])
            # 아는 사람이 섞여 있으면 여기선 거짓말 못함
            if len(t_set & cannot_lie) == 0:
                result += 1

    print(result)
