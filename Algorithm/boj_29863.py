# boj_29863.py
# Arno's Sleep Schedule

A = int(input())
B = int(input())

if A > B: B += 24
print(B - A)