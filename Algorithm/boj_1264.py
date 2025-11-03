# boj_1264.py
# 모음의 개수

arr = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
while True:
    in_str = input()
    if in_str == "#":
        break
    cnt = 0

    for s_char in in_str:
        if s_char in arr:
            cnt += 1
    print(cnt)