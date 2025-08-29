# swea_16533.py
# 노드의 합


def post_order(node_idx):
    if node_idx > N:
        return 0
    # 왼쪽부터 탐색
    if left[node_idx] == 0:
        left[node_idx] = post_order(node_idx * 2)
        left_data = left[node_idx]
    else:
        left_data = left[node_idx]
    if right[node_idx] == 0:
        right[node_idx] = post_order((node_idx * 2) + 1)
        right_data = right[node_idx]
    else:
        right_data = right[node_idx]
    return left_data + right_data

T = int(input())
for case in range(1, T + 1):
    N, M, L = map(int, input().split())
    parents = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for _ in range(M):
        node_idx, data = map(int, input().split())
        p = node_idx // 2 # 부모 노드의 인덱스
        parents[node_idx] = p
        if node_idx % 2 == 0: # 짝수 인덱스로 왼쪽 노드에 들어감
            left[p] = data
        else:
            right[p] = data
    result = post_order(L)
    print(f"#{case} {result}")






