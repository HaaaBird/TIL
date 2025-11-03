# swea_1231.py
# 중위 순회

def inorder(tree, start, n):
    if start > n:
        return
    else:
        inorder(tree, start*2, n)
        print(tree[start], end="")
        inorder(tree, start*2 + 1, n)


T = 10
for case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    for _ in range(N):
        operation = list(input().split())
        tree[int(operation[0])] = operation[1]
    print(f"#{case} ", end="")
    inorder(tree, 1, N)
    print()
