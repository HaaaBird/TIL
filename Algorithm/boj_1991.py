# boj_1991.py
# 트리 순회


"이진 트리를 전위, 중위, 후위 순회하는 코드"

def per_order(tree, start, moves):
    now_child = tree[start]
    moves.append(start)
    if now_child[0] == "." and now_child[1] == ".":
        return
    else:
        if now_child[0] != ".":
            per_order(tree, now_child[0], moves)
        if now_child[1] != ".":
            per_order(tree, now_child[1], moves)

def in_order(tree, start, moves):
    now_child = tree[start]
    if now_child[0] == "." and now_child[1] == ".":
        moves.append(start)
        return
    else:
        if now_child[0] != ".":
            in_order(tree, now_child[0], moves)
        moves.append(start)
        if now_child[1] != ".":
            in_order(tree, now_child[1], moves)

def post_order(tree, start, moves):
    now_child = tree[start]
    if now_child[0] == "." and now_child[1] == ".":
        moves.append(start)
        return
    else:
        if now_child[0] != ".":
            post_order(tree, now_child[0], moves)
        if now_child[1] != ".":
            post_order(tree, now_child[1], moves)
        moves.append(start)



N = int(input())
tree = {}
for _ in range(N):
    arr = list(map(str, input().split()))
    tree[arr[0]] = (arr[1], arr[2])

moves = []
per_order(tree, "A", moves)
print("".join(map(str, moves)))

moves = []
in_order(tree, "A", moves)
print("".join(map(str, moves)))
moves = []
post_order(tree, "A", moves)
print("".join(map(str, moves)))