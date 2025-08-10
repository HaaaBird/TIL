# swea_1221.py
# GNS
#
import sys
sys.stdin = open("input.txt", "r")

num_map = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4,
           "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
revers_map = {v:k for k, v in num_map.items()}

T = int(input())
for case in range(1, T+1):
    case_no, word_len = map(str, input().split())
    word_len = int(word_len)
    in_words = list(map(str, input().split()))
    temp_words = [num_map[word] for word in in_words]
    temp_words.sort()
    in_words = [revers_map[word] for word in temp_words]
    print(case_no)
    print(" ".join(in_words))
