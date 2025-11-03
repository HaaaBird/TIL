# boj_5717.py
# 상근이와 친구들]

while True:
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        break
    else:
        print(M + F)