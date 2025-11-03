# swea_16287.py
# 반복문자 지우기


T = int(input())

for case in range(1, T + 1):
    in_str = input()
    stack = []

    for i in range(len(in_str)):
        if len(stack) == 0:
            stack.append(in_str[i])
        elif stack[-1] == in_str[i]:
            stack.pop()
        else:
            stack.append(in_str[i])
    print(f"#{case} {len(stack)}")