# swea_1231.py
# 중위 순회

def inorder(node, tree):
    if node < len(tree):
        inorder(node * 2, tree)
        print(tree[node][0], end ="")
        inorder(node * 2 + 1, tree)


T = 10
for case in range(1, T + 1):
    N = int(input())
    tree = [[] for _ in range(N + 1 )]
    for _ in range(N):
        arr = list(map(str, input().split()))
        if len(arr) == 4:
            tree[int(arr[0])] = [arr[1], int(arr[2]), int(arr[3])]
        elif len(arr) == 3:
            tree[int(arr[0])] = [arr[1], int(arr[2])]
        else:
            tree[int(arr[0])] = [arr[1]]
    visit = set()
    print(f"#{case} ", end="")
    inorder(1, tree)
    print()