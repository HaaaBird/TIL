# swea_5432.py
# 쇠막대기 자르기

# 스택 구조 이용해서 괄호 죄다 잡아넣고
# 잡혀온 놈 거리가 1이면 레이저
#





T = int(input())

for case in range(1, 1 + T):
    works = input()
    left_count = 0
    result = 0
    ll_idx = None
    for i in range(len(works)):
        if works[i] == "(" and works[i+1] == ")":
            result += left_count
        elif works[i] == ")" and works[i-1] == "(":
            pass
        elif works[i] == ")" and works[i-1] != "(":
            left_count -= 1
            result += 1
        else:
            left_count += 1
    print(f"#{case} {result}")


