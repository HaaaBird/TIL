# swea_4874.py
# Forth


T = int(input())
for case in range(1, T + 1):
    arr = input().split()
    stack = []
    flag = True
    for i in range(len(arr)):
        if arr[i].isnumeric():
            stack.append(int(arr[i]))
        elif arr[i] == ".":
            break
        else:
            try:
                if arr[i] == "+":
                    f_n = stack.pop()
                    s_n = stack.pop()
                    stack.append(f_n + s_n)
                elif arr[i] == "-":
                    f_n = stack.pop()
                    s_n = stack.pop()
                    stack.append(f_n - s_n)
                elif arr[i] == "/":
                    f_n = stack.pop()
                    s_n = stack.pop()
                    stack.append(f_n / s_n)
                elif arr[i] == "*":
                    f_n = stack.pop()
                    s_n = stack.pop()
                    stack.append(f_n * s_n)
            except Exception:
                flag = False
                break

    if flag:
        print(f"#{case} {stack[0]}")
    else:
        print(f"#{case} error")