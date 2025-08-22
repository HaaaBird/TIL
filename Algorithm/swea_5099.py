# swea_5099.py
# 피자 굽기

"""
N개의 피자를 동시에 구울 수 있는 화덕이 있다.
피자는 치즈가 모두 녹으면 화덕에서 꺼내며,
치즈의 양은 피자마다 다르다.

1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때,
치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.

주어진 조건에 따라 피자를 구울 때,
화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.

- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.

- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고,
화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다.
이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고,
바로 그 자리에 남은 피자를 순서대로 넣는다.

while 문 돌려서 계속 회전시키고.
리스트 한 바퀴 돌면서 c//2 연산
"""

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    pizza_list = [[i+1, arr[i], 0] for i in range(len(arr))]
    last = 0
    pizza_cnt = M
    oven = [[0,0] for _ in range(N)]
    while pizza_cnt != 0:
        now = oven.pop(0)
        now[1] //= 2
        if now[1] == 0: # 빈 칸이라면면
            if len(pizza_list) != 0: # 넣을 피자가 있다면
                oven.append(pizza_list.pop(0)) # 피자 넣기
            else:
                oven.append(now) # 빈 칸 그대로 넣기
                pizza_cnt -= 1
        else:
            oven.append(now)
            last = now[0]
    print(f"#{case} {last}")


