# swea_4013.py
# 특이한 자석

"""
자석이 한칸 회전시킨다 할때, 옆에 놈의 2,6번 극성이 다를 경우, 옆에놈도 움직인다.
근데 하나 움직이고, 하나 움직이는게 아니라 한번에 다 움직이게 해야 한다.
즉 한번에 움직일 수 있는 자석의 수는 최대 3개이고, 없을 수 있다.

그럼 순서를 정리해보면

1번을 돌렸더니 2번이 돌아갈 수 있다면 돌리지 말고 옆을 본다
3번을 봤더니 2번이 돌아가면 돌아갈 수 있다면 옆을 봐서 4번을 본다.
4번을 봤더니 얘는 안돌아가겠다 싶으면
1,2,3 을 지금 돌린다. 이 순서대로 돌리는 로직을 짜 주면 된다.

그래서 최종 결과를 보고 답을 출력하면 된다.
"""

def rotate(d, arr):
    if d == -1: # 반시계방향
        pass
    else:
        pass

def rotate_check(emn, mn):
    if emn > mn: # 영향받는 기어가 원래 기어 오른쪽에 있는 경우
        if magnet[mn][2] != magnet[emn][6]:
            return True
        else:
            return False
    else:
        if magnet[emn][2] != magnet[mn][6]:
            return True
        else:
            return False

d_map = {
    0:[1],
    1:[0,1],
    2:[1,3],
    3:[2]
}

T = int(input())
for case in range(1, T + 1):
    K = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    order = [list(map(int, input().split())) for _ in range(K)]

    for idx in range(len(order)):
        m_num = order[idx][0] - 1
        direction = order[idx][1]

        stack = [(m_num, direction)]
        visit = [(m_num, direction)] #

        while len(stack) != 0:
            mn, d = stack.pop()
            effect_m = d_map[mn]

            for emn in effect_m:
                if (emn, d * -1) not in visit:
                    c_result = rotate_check(emn, mn)
                    if c_result:
                        stack.append((emn, d*-1))
                        visit.append((emn, d*-1))

        for work in visit:
            magnet[0] = rotate(work[1], magnet[0])
        print(visit)




