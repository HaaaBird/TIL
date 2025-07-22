a = int(input())
b = input()

for digit in reversed(b):   # 역순으로 돌기
    print(a * int(digit))
print(a * int(b))  # 마지막 전체 곱 출력
