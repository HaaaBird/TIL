# boj_1259.py
# 펠린드롬 수

def is_pal(arr):
    for i in range(0, len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            return "no"
    return "yes"



while True:
    in_arr = list(input())

    if in_arr == ["0"]:
        break
    else:
        print(is_pal(in_arr))