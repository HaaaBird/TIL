N, M = map(int, input().split())
numbers = [int(input()) for _ in range(N)]

def check(arr, M):
    result_list = []
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            cnt += 1
        else:
            if cnt > 1 and cnt >= M:
                result_list.append((i-cnt, i))
            cnt = 1
    return result_list

# Please write your code here.
while True:
    pop_list = check(numbers, M)
    change_cnt = 0
    for si, se in pop_list:
        for i in range(si, se):
            numbers[i] = -1
            change_cnt += 1
    temp = []
    for i in range(len(numbers)):
        if numbers[i] == -1:
            continue
        temp.append(numbers[i])

    numbers = temp
    if change_cnt == 0:
        break

print(len(numbers))
for num in numbers:
    print(num)
