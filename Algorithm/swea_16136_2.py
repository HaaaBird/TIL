# swea_16136_2.py
# 회문

def is_pal(line):
    for i in range(len(line)//2):
        if line[i] != line[len(line) - i - 1]:
            return False
    return True


T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    result = None

    matrix = [list(map(str, input().strip())) for _ in range(N)]
    for i in range(M):
        for j in range(0, N - M + 1):
            ver_word = []
            for c in range(M):
                ver_word.append(matrix[i][j+c])
            if is_pal(ver_word):
                result = ver_word
                break
    if result is None:
        for i in range(0, N - M + 1):
            for j in range(M):
                word = []
                for c in range(M):
                    word.append(matrix[i+c][j])
                if is_pal(word):
                    result = word
                    break

    print(f"#{case} {''.join(result)}")