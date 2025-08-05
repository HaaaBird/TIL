# boj_1181.py
# 단어 정렬

n = int(input())

words = [str(input()) for i in range(n)]

words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    print(i)