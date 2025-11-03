# swea_4408.py

"""
새로운 선의
시작점이 기존 선의 시작보다 높고
도착점이 기존 선의 도착보다 낮음

시작점이 기존 선의 시작보다 낮고
도착점이 기존 선의 도착보다 낮음.


튜플 형태로 값을 받아서
교차점이 생기면 해당 그룹에 묶이는거.



"""

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    cr_list = [list(map(int, input().split())) for _ in range(N)]
    chk_list =[set() for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            # j가 같은 행끼리 움직이는 경우
            if cr_list[j][0] % 2 == cr_list[j][1] % 2:
                # 구간 어디던 사이에 있다면
                if cr_list[i][0] < cr_list[j][0] < cr_list[i][1] or cr_list[i][0] < cr_list[j][1] < cr_list[i][1]:
                    chk_list[i].add(j) #그룹정보 추가
            #j가 교차해서 이동하는 경우
            else:
                if cr_list[i][0] > cr_list[j][0] and cr_list[i][1] < cr_list[j][1]:
                    chk_list[i].add(j)  # 그룹정보 추가
                elif cr_list[i][0] < cr_list[j][0] and cr_list[i][1] > cr_list[j][1]:
                    chk_list[i].add(j)  # 그룹정보 추가

    result = 0
    while len(chk_list) != 0:
        target = chk_list[0]
        chk_list = [x for x in chk_list if x != target]
        result += 1
    print(f"#{case} {result}")

