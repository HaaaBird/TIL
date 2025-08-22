# swea_4751.py
# 다솔이의 다이아몬드 장식

import pprint
T = int(input())
for case in range(1, T + 1):
    word = input()
    fl = '..#..' + '.#..' * (len(word) - 1)
    sl = '.#.#.' + '#.#.' * (len(word) - 1)
    tl = f'#.{word[0]}.#'
    if len(word) != 1:
        for i in range(1, len(word)):
            tl += f'.{word[i]}.#'
    print(fl)
    print(sl)
    print(tl)
    print(sl)
    print(fl)