# swea_16135.py
# 문자열 비교



T = int(input())
for case in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())

    str1_len = len(str1)
    str2_len = len(str2)

    find_flag = False

    for i in range(str2_len - str1_len + 1):
        if str2[i:i+str1_len] == str1:
            find_flag = True
            break
    if find_flag:
        print(f"#{case} 1")
    else:
        print(f"#{case} 0")