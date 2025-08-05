# boj_4153.py
# 직각삼각형

while True:
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] == 0:
        break
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print("right")
    else:
        print("wrong")