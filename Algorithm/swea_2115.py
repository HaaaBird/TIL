# swea_2115.py
# 벌꿀 채취
# 문제 개념. 2명이 가로방향으로 꿀을 딴다.
# 이 때 꿀의 가격을 최대로 하는 조합을 찾아라
# 꿀의 가격은 수확한 꿀의 수랑 ** 2
# 꿀의 최대 수확량은 C



# 벌 통의 크기는 3~10 크기가 작다
# M또한 1~5 이며 N 이하다.
# 최대 양은 10 < 30
# 걍 완전탐색으로 풀어도 풀리는 문제다. 문제 크기가 작다.

# 완전탐색으로 푸는 법
# 먼저, 가능한 조합을 모두 구한다.

# 조합의 조합을 구하는 방법
# 어차피 result 또한 배열이니까, 해당 배열의 배열로 조합을 만들어 리스트 in list 형태로 값을 만들고
# 해당 배열을 get_value에 인자로 써서 get_value는 두 사람의 총 수익을 return 하도록 한다.
# 이후 그 가격을 max 와 비교해서 갱신하고, 최종적으로 모든 경우를 다 비교했다면 출력한다.

# 잘못품! 비트 연산도 필요 없음. 붙어있는 2개 고르면 되는거라.

def get_value(arr, C):
    n = len(arr)
    best = 0
    # 부분집합 비트마스크: 0..(1<<n)-1
    for i in range(1 << n):
        total = 0
        value = 0
        ok = True
        for j in range(n):
            if i & (1 << j):
                total += arr[j]
                if total > C:
                    ok = False
                    break
                value += arr[j] * arr[j]
        if ok and value > best:
            best = value
    return best


T = int(input())
for _ in range(1, T + 1):
    N, M, C = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # M크기에 맞는 조합 비트마스크 생성
    all_com = []
    for i in range(len(matrix)):
        for j in range(N - M + 1):
            now_arr = matrix[i][j:j + M]
            now_arr.sort(reverse=True)
            add_list = [get_value(now_arr, C), i, j, j + M]
            all_com.append(add_list)
    all_com.sort(reverse=True, key=lambda x:x[0])

    max_total = 0

    for i in range(len(all_com)):
        v1, r1, s1, e1 = all_com[i]
        for j in range(i + 1, len(all_com)):
            v2, r2, s2, e2 = all_com[j]

            # 같은 행이면 겹치면 안 됨
            if r1 == r2 and not (e1 <= s2 or e2 <= s1):
                continue  # 겹치면 패스

            total_value = v1 + v2
            if total_value > max_total:
                max_total = total_value

    print(max_total)
