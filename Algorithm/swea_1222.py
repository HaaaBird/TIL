# swea_1222.py
# 계산기1

T = 10
for case in range(1, T + 1):
    N = int(input())
    arr = input()
    result = []
    stack = []
    idx = 0
    while True:
        if idx == N:
            while len(stack) != 0:
                result.append(stack.pop())
            break
        if arr[idx].isnumeric(): # 숫자면
            result.append(int(arr[idx]))
            idx += 1
        elif not arr[idx].isnumeric() and len(stack) == 0 :
            stack.append(arr[idx])
            idx += 1
        else:
            result.append(stack.pop())
            stack.append(arr[idx])
            idx += 1
    stack = []
    idx = 0
    while idx != N:
        if type(result[idx]) == int:
            stack.append(result[idx])
            idx += 1
        else:
            last_num = stack.pop()
            first_num = stack.pop()
            stack.append(last_num + first_num)
            idx += 1
    print(f"#{case} {stack[0]}")
