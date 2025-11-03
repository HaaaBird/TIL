# swea_1234.py
# 비밀번호

for case in range(1, 11):
    N, num = input().split()
    nums = list(map(int, str.strip(str(num))))
    stack = []

    for char in num:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    print(f"#{case} {''.join(stack)}")