# swea_5432.py
# 쇠막대기 자르기 (스택 활용)

T = int(input())
for case in range(1, T + 1):
    works = input().strip()
    stack = []
    result = 0

    for i in range(len(works)):
        if works[i] == "(":
            stack.append(works[i])
        else: # 레이저거나 막대의 끝
            stack.pop() # 일단 한개 날린다. 레이저던, 쇠막대 끝이던
            if works[i-1] == "(": # 만난게 레이저면
                result += len(stack) #스택에 쌓여있는 ( 수만큼 막대기가 생긴다.
            else: # 레이저가 아니고 다른 막대의 끝이라면
                result += 1
    print(f'#{case} {result}')