# boj_7568.py
# 덩치

from collections import deque
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

"""
그룹을 리스트로 만들고, 거기 속한 원소 하나랑 비교.
만약 우열을 가릴 수 있으면 우열 가린 데로.

없으면 해당 그룹에 소속되도록
"""


result = deque([[(matrix[0][0], matrix[0][1])]])

for i in range(1, N):
    flag = False
    for j in range(len(result)):
        now = result[j]
        if (now[0][0] <= matrix[i][0] and now[0][1] < matrix[i][1]) or (now[0][0] < matrix[i][0] and now[0][1] <= matrix[i][1]): # 현재 요소가 더 크면
            result.insert(j, [(matrix[i][0], matrix[i][1])])
            flag = True
            break
        elif (now[0][0] >= matrix[i][0] and now[0][1] > matrix[i][1]) or (now[0][0] > matrix[i][0] and now[0][1] >= matrix[i][1]): # 현재 요소가 더 작으면
            continue
        else:
            result[j].append((matrix[i][0], matrix[i][1]))
            flag = True
            break
    if flag is False:
        result.append([(matrix[i][0], matrix[i][1])])
cnt_list = [0] * (N + 1)

for i in range(len(result)):
    cnt_list[i+1] += len(result[i])

for i in range(N):
    for j in range(len(result)):
        if (matrix[i][0], matrix[i][1]) in result[j]:
            print(sum(cnt_list[:j+1]) + 1, end=" ")
            break