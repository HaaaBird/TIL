# swea_5174.py
# subtree


def per_order_traversal(tree_dict, target):
    count = 1
    if target in tree_dict:
        for child in tree_dict[target]:
            count += per_order_traversal(tree_dict, child)
    return count

T = int(input())
for case in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree_dict = {}

    for i in range(0, len(arr), 2):
        if tree_dict.get(arr[i]) is None:
            tree_dict[arr[i]] = [arr[i+1]]
        else:
            tree_dict[arr[i]].append(arr[i+1])

    sub_tree_size = per_order_traversal(tree_dict, N)
    print(f"#{case} {sub_tree_size}")