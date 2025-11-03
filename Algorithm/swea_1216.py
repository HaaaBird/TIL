# swea_1216.py
# 회문2

import sys
sys.stdin = open("input.txt", "r")


def is_pal(word):
    for i in range(len(word)//2):
        if word[i] != word[-i - 1]:
            return False
    return True

N = 10
TEST_100 = 100

for case in range(1, N + 1):
    a_ = int(input())
    matrix = [list(input().strip()) for _ in range(TEST_100)]
    max_len = 0
    # 열 방향으로 탐색
    # 긴 것부터 찾으면 괜히 여러번 할 필요 없음
    for i in range(TEST_100):
        for j in range(TEST_100):
            pal_len = 0
            for word_len in range(TEST_100, 1, -1):
                if j + word_len > TEST_100:
                    continue
                else:
                    if is_pal(matrix[i][j:j+word_len]):
                        pal_len = max(pal_len, word_len)
                        break
            max_len = max(max_len, pal_len)

    for j in range(TEST_100):
        for i in range(TEST_100):
            pal_len = 0
            for word_len in range(TEST_100, 1, -1):
                if i + word_len > TEST_100:
                    continue
                else:
                    vertical_word = "".join(matrix[x][j] for x in range(i, i + word_len))
                    if is_pal(vertical_word):
                        pal_len = max(pal_len, word_len)
                        break
            max_len = max(max_len, pal_len)

    print(f"#{a_} {max_len}")