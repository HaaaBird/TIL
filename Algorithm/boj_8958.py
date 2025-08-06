# boj_8958.py
# ox퀴즈

N = int(input())

for _ in range(N):
    input_str = input()
    score = 0
    bonus = 1
    for s_char in input_str:
        if s_char == "O":
            score += bonus
            bonus += 1
        else:
            bonus = 1
    print(score)