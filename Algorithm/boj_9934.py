# boj_9934.py
# 완전 이진 트리
"""

상근이가 도시를 중위탐색으로 순회하였음으로
순회한 순서 배열이 있으면 이거를 가지고 트리맵 구성이 가능하다.
완전 이진 트리라는걸 가정하고 풀면 된다.
"""

def in_order(i, n):
    global idx, tree
    if n < i:
        return
    in_order(i * 2, n)
    tree[i] = arr[idx]
    idx += 1
    in_order(i * 2 + 1, n)



K = int(input())
tree = [0] * 2**K
arr = list(map(int, input().split()))
idx = 0
in_order(1, len(tree)-1)

for d in range(K):
    s = 2**d              # ← 1**d 가 아니라 2**d
    e = 2**(d + 1)        # ← min(...) 필요 없음. 그냥 2**(d+1)
    print(*tree[s:e])