# swea_1215.py
# 회문 1

def is_pal(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True


if __name__ == "__main__":
    N = 10
    for case in range(N):
        M = int(input())
        arr = [list(input().strip()) for _ in range(8)]
        pal_cnt = 0

        for i in range(8):
            for j in range(8 - M + 1):
                # 가로 검사
                horizontal_word = "".join(arr[i][j:j + M])
                if is_pal(horizontal_word):
                    pal_cnt += 1

        for j in range(8):
            for i in range(8 - M + 1):
                # 세로 검사
                vertical_word = "".join(arr[x][j] for x in range(i, i + M))
                if is_pal(vertical_word):
                    pal_cnt += 1

        print(f"#{case+1} {pal_cnt}")
