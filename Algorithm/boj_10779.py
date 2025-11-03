# 쇠막대기

arr = list(input().strip())
result = 0
stack = []
for i in range(len(arr)):
    if arr[i] == "(":
        stack.append(arr[i])
    else:
        if arr[i-1] == "(": #레이저를 만났던 거라면
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)