# boj_25501.py
# 재귀의 귀재

"""
재귀를 통해 펠린드롬을 검출해야 한다

"""

def is_pal(word, start, end):
    global cnt
    cnt += 1
    if end <= start:
        return 1
    elif word[start] != word[end]:
        return 0
    else:
        return is_pal(word, start + 1, end -1)


T = int(input())
for case in range(1, T + 1):
    cnt = 0
    word = input()
    a = is_pal(word, 0, len(word)-1)
    print(a, cnt)
