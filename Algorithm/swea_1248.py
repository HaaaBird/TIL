def find_lca(parent, a, b):
    # a의 모든 조상 저장
    ancestors = set()
    while a:
        ancestors.add(a)
        a = parent[a]
    # b의 조상 중 가장 먼저 나오는 a의 조상 찾기
    while b:
        if b in ancestors:
            return b
        b = parent[b]
    return None

def subtree_size(children, root):
    size = 1
    for child in children[root]:
        size += subtree_size(children, child)
    return size

T = int(input())
for case in range(1, T+1):
    V, E, node1, node2 = map(int, input().split())
    edges = list(map(int, input().split()))

    parent = [0] * (V + 1)
    children = [[] for _ in range(V + 1)]

    for i in range(0, len(edges), 2):
        p = edges[i]
        c = edges[i+1]
        parent[c] = p
        children[p].append(c)

    lca = find_lca(parent, node1, node2)
    size = subtree_size(children, lca)

    print(f"#{case} {lca} {size}")
