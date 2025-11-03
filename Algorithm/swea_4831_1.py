# 전기버스
"""
그리디로 풀면 됨.

현재 위치 -> 갈 수 있는 가장 먼 충전소
로 이동 하는 형태로 반복.
마지막 충전소에서 도착지 갈 수 있으면 충전 횟수 출력
마지막 충전소에서 도착지 갈 수 없으면 0 출력
"""
T = int(input())
for case in range(1, T + 1):

    K, N, M = map(int, input().split())
    queue = list(map(int, input().split())) + [N]
    head = 0
    now_position = 0
    charge_cnt = 0
    success = False
    l_K = K
    while True:
        if now_position == N:
            success = True
            break
        if now_position + l_K >= queue[head]:
            # 연료 사용 및 이동
            l_K -= queue[head] - now_position
            now_position = queue[head]
            head += 1
        elif now_position + l_K < queue[head]:
            # 못갈경우
            # 충전하면 갈 수 있는가?
            if now_position + K >= queue[head]:
                l_K = K
                charge_cnt += 1
            else:
                break

    if success:
        print(f"#{case} {charge_cnt}")
    else:
        print(f"#{case} 0")

