# swea_1232.py
# 사칙연산
"""
임의의 이진 트리라고 했지 이게 완전 이진트리라고 한게 아님.
따라서 index 잘 잡으면서 가야함.

그래서
값을 저장할 values = [] 가 하나 필요함. 인덱스에 해당하는 값이 들어가게
그리고 해당 인덱스의 왼쪽, 오른쪽 자식이 누구인지 기록할
left
right 가 필요함

그러면 값을 받아와서
자식이 있는, 연산자라면
left[arr[3]
"""

operator = ["+", "-", "*", "/"]

def calculater(n1, n2, o):
    if o == "+":
        return n1 + n2
    elif o == "-":
        return n1 - n2
    elif o == "*":
        return n1 * n2
    elif o == "/":
        return n1 // n2

def postorder(start):
    global tree_values, left_idx_list, right_idx_list
    if start < N+1 and start != 0:
        left = postorder(left_idx_list[start])
        right = postorder(right_idx_list[start])
        if tree_values[start] in operator: # 연산자라면
            return calculater(left, right, tree_values[start])
        return tree_values[start]
    else:
        return 0


T = 10
for case in range(1, T + 1):
    N = int(input())
    tree_values = [0] * (N + 1)
    left_idx_list = [0] * (N + 1)
    right_idx_list = [0] * (N + 1)
    for _ in range(N):
        arr = list(input().split())
        if len(arr) == 4: # 연산자일때
            tree_values[int(arr[0])] = arr[1]
            left_idx_list[int(arr[0])] = int(arr[2])
            right_idx_list[int(arr[0])] = int(arr[3])
        else:
            tree_values[int(arr[0])] = int(arr[1])
    result = postorder(1)
    print(f"#{case} {result}")