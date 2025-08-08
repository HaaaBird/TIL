# swea_1989.py
# 초심자의 회문 검사


def is_pal(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i- 1]:
            return False
    return True


T = int(input())
for case in range(1, T + 1):
    in_str = input()
    print(f"#{case} {int(is_pal(in_str))}")
