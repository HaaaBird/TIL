# boj_1062.py
# 가르침

"""
비트마스킹 문제.
k 가 5보다 작으면 0 출력

5보다 크면, 마스킹 해야 하는 문자열만 추출
시작 번호는 97부터

기본으로 5개 문자열 비트 체크 해두고
백트래킹으로 마스킹 해야 하는 문자열 하나씩 추가하고 or 연산해서
"""

default = ['n','t','i','c']
visited = set(default)
visited.add('a')
num = 1

for c in default:
    num += (1 << (ord(c) - 97))

N, M = map(int, input().split())
if N < 5:
    print(0)
else:
    candidate = []
    for _ in range(M):
        word = list(map(str, input().strip()))
        for c in word:
            if c not in visited:
                n_num = 1 << (ord(c) - 97)
                candidate.append(n_num)
                visited.add(n_num)
    print(candidate)
