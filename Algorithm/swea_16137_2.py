# swea_16137_2.py

T = int(input())

for case in range(1, T + 1):
    str1 = input()
    str2 = input()
    char_dict = {}
    max_cnt = 0
    for s_char in str1:
        char_dict[s_char] = 0
    for s_char in str2:
        if char_dict.get(s_char) == None:
            pass
        else:
            char_dict[s_char] += 1
            max_cnt = max(max_cnt, char_dict[s_char])

    print(f"#{case} {max_cnt}")

