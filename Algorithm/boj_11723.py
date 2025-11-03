# boj_11723.py
# 집합


"""
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
"""
import sys
input = sys.stdin.readline

T = int(input())
my_set = set()
works = [list(map(str, input().split())) for _ in range(T)]

for work in works:
    if len(work) == 1:
        if work[0] == "all":
            my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        elif work[0] == "empty":
            my_set = set()
    else:
        if work[0] == "add":
            my_set.add(int(work[1]))
        elif work[0] == "remove":
            my_set.discard(int(work[1]))
        elif work[0] == "check":
            if int(work[1]) in my_set:
                print(1)
            else:
                print(0)
        elif work[0] == "toggle":
            if int(work[1]) in my_set:
                my_set.remove(int(work[1]))
            else:
                my_set.add(int(work[1]))
