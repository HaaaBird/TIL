# swea_16286.py
# 괄호검사


brk_map = {
    ")":"(",
    "}":"{"
}
open_brk = ["(", "{"]
close_brk = [")", "}"]

T = int(input())
for case in range(1, 1 + T):
    in_str = input()
    flag = True
    stack = []

    for i in range(len(in_str)):
        if in_str[i] in open_brk:
            stack.append(in_str[i])
        elif in_str[i] in close_brk:
            if len(stack) == 0: # 스택이 비어있는데 닫는 괄호가 나옴
                flag = False
                break
            elif brk_map[in_str[i]] != stack[-1]: # 마지막 스택과 다른 괄호가 나옴
                flag = False
                break
            else: # 정상
                stack.pop()
    if len(stack) != 0: # 스택에 뭐가 남아있음.
        flag = False
    if flag:
        print(f"#{case} 1")
    else:
        print(f"#{case} 0")




