# def backt(start, q_cnt):
#     global result
#     if q_cnt == N:
#         result += 1
#         return
#
#     for i in range(start, min(N, start + 1)):
#         for j in range(N):
#             if ((i - j) in used_d1) or ((i + j) in used_d2):
#                 continue
#             used_d1.add(i - j)
#             used_d2.add(i + j)
#             backt(start + 1, q_cnt + 1)
#             used_d1.remove(i - j)
#             used_d2.remove(i + j)
#         return
#
#
# N = int(input())
# result = 0
# used_d1, used_d2 = set(), set()
# for j in range(N // 2):
#     used_d1.add(0 - j)
#     used_d2.add(0 + j)
#     backt(1, 1)
#     used_d1.clear()
#     used_d2.clear()
# count_left = result
# result = 0
#
# count_mid = 0
# if N % 2 == 1:
#     used_d1.add(0 - (N // 2))
#     used_d2.add(0 + (N // 2))
#     backt(1, 1)
#     count_mid = result
#     result = 0
#
# print(count_left * 2 + count_mid)

def check(row, col):
    # 행 단위로 내려가기 때문에 위쪽만 보면 됨.
    # 1. 같은 열에 놓은 적이 있는가?
    for i in range(row):
        if visit[i][col]:
            return False
    # 2. 좌상단 대각에 놓은 적이 있는가?
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if visit[i][j]:
            return False
        i -= 1
        j -= 1
    # 3. 우상단 대각에 놓은 적이 있는가?
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if visit[i][j]:
            return False
        i -= 1
        j += 1

    return True


def recur(row):
    global answer
    if row == N:  # N개의 행을 모두 보았다면 종료
        answer += 1
        return
    # 한 행마다 모든 열을 다 봐야 함. 한개 행에 대해서 모든 열 다 체크
    for col in range(N):
        if visit[row] and check(row, col) is False:  # 같은 열을 못 고르도록 가지치기
            # 대각선까지 모두, 유망하지 않은 경우 모두 삭제(가로, 세로, 대각선) 가로는 알아서 없어짐
            continue
        # 해당 컬럼을 선택함
        visit[row] = col
        recur(row + 1)
        visit[row][col] = 0


N = 12
answer = 0  # 가능한 정답 수
visit = [0] * N
recur(0)

print(answer)


from collections import deque