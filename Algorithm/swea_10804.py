# swea_10804.py
# 문자열의 거울상

mapping = {
    'b':'d',
    'd':'b',
    'p':'q',
    'q':'p'
}

T = int(input())
for case in range(1, T + 1):
    word = list(input())
    result = len(word) * ["a"]
    for i in range(len(word)):
        result[len(result) - i - 1] = mapping.get(word[i])
    print("".join(result))