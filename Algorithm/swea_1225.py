# swea_1225.py
# 암호 생성

T = 10

for case in range(1, T + 1):
    tc = int(input())
    arr = list(map(int, input().split()))
    flag = True

    while flag is True:
        for i in range(1, 6):
            now = arr.pop(0)
            if now - i <= 0:
                now = 0
                arr.append(now)
                flag = False
                break
            else:
                arr.append(now - i)
        if flag is False:
            break
    print(f"#{tc} {' '.join(map(str, arr))}")
