# swea_5174.py
# subtree

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

    print(tree_dict)