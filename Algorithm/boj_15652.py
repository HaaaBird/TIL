# boj_15652.py
# N 과 M(4)

"""
같은 수를 여러번 골라도 됨.
그러면 49번 알고리즘에서, 나를 고른걸 따지지 않게 만들면 되는거 아닌가
"""


def backtrack(start):
    if len(result_list) == M:
        print(" ".join(map(str, result_list)))
        return
    for i in range(start, N + 1):
        result_list.append(i)
        backtrack(i)
        result_list.pop()


N, M = map(int, input().split())
result_list = []
backtrack(1)
