# swea_10804.py
# 문자열의 거울상


mapping = {
    "q":"p",
    "p":"q",
    "d":"b",
    "b":"d"
}

T = int(input())

for case in range(1, T + 1):
    in_str = list(input())
    result = ["a"] * len(in_str)
    for i in range(len(in_str)):
        result[len(in_str)-i-1] = mapping.get(in_str[i])
    print(f"#{case} {''.join(result)}")