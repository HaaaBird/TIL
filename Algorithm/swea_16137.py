# swea_16137.py
# 글자수

T = int(input())

for case in range(1, T + 1):
    cnt_dict = {}
    str1 = input()
    str2 = input()

    for s_char in str1:
        cnt_dict[s_char] = 0
    max_cnt = 0
    for s_char in str2:
        if cnt_dict.get(s_char) != None:
            cnt_dict[s_char] += 1
            if cnt_dict[s_char] > max_cnt:
                max_cnt = cnt_dict[s_char]
    print(f"#{case} {max_cnt}")
