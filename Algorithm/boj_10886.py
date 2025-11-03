# boj_10886.py
# 0 = not cute / 1 = cute

N = int(input())
score = 0
for _ in range(N):
    score += int(input())

if score / N > 0.5:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")