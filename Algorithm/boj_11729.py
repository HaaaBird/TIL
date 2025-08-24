# boj_11729.py
# 하노이의 탑

"""
이 문제는 해야 하는 일이 결정되어 있다.
n = 1 1->3
n = 2 1->2, 1->3, 2->3
n = 3 1->3, 1->2, 3->2, 1->3, 2->1, 2->3, 1->3

"""


def hanoi(n, a, b, c, out):
    if n == 1:
        out.append(f"{a} {c}")
        return
    hanoi(n - 1, a, c, b, out)
    out.append(f"{a} {c}")
    hanoi(n - 1, b, a, c, out)


N = int(input())
moves = []
hanoi(N, 1, 2, 3, moves)
print(len(moves))
for move in moves:
    print(move)
