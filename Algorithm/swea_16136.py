# swea_16136.py
# 회문


def is_palindrome(arr):
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True

    pass


T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(str, input().strip())) for _ in range(N)]

    result = None
    # 행 방향 회문 검색
    for word in matrix:
        for i in range(0, N - M + 1):  # 단어 길이 - 회문 길이
            if is_palindrome(word[i:i + M]):
                result = "".join(word[i:i + M])
                break

    if result is None:
        # 열 방향 회문 검색
        for j in range(N):
            col_word = [matrix[i][j] for i in range(N)]
            for j in range(0, N - M + 1):
                if is_palindrome(col_word[j:j + M]):
                    result = "".join(col_word[j:j + M])
                    break

    print(f"#{case} {result}")
