# swea_1946.py
# 간단한 압축 풀기

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    words = [list(map(str, input().split())) for _ in range(N)]
    result = []
    for word in words:
        result.append(word[0] * int(word[1]))
    result = "".join(result)
    last_start = len(result) - len(result) % 10
    print(f"#{case}")
    for i in range(0, len(result)-10, 10):
        print(result[i:i+10])
    print(result[last_start:])