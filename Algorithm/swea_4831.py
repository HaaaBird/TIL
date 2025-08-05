# swea_4831.py
# 전기버스

T = int(input())

for case in range(T):
    K, N, M = map(int, input().split()) # K는 한번에 이동 가능한 거리, N은 총 길이(0에서 출발), M은 충전소 수
    charge_arr = [0] + list(map(int, input().split())) + [N] # 시작위치, 종료위치 더하기
    arrive_flag = False
    p = 0
    c_cnt = 0

    while True:
        target_idx = None
        for idx in range(len(charge_arr)): # 현재 위치에서 갈 수 있는 주유소, 혹은 목적지를 순차적으로 찾음
            move_range = p + K
            if move_range >= charge_arr[idx]: # 이동가능하다면, target, idx 둘 다 갱신
                target = charge_arr[idx]
                target_idx = idx
            else: # 해당 주유소까지 도착이 불가하면 break 해 for 문 탈출
                break
        # for 문 탈출 이후
        if target_idx is None: # 도달 가능한 곳이 없다면 while 문 break.
            break # 기본 arrive_flag 가 False기 때매 자동으로 0 출력하고 케이스 종료
        elif charge_arr[target_idx] == N: # 도착한 곳이 최종 목적지라면
            arrive_flag = True # arrive_flag = True 로 전환하고 while문 탈출
            break
        else:
            p = charge_arr[target_idx] # 현재 위치 갱신
            charge_arr = charge_arr[target_idx+1:] # 도달 가능한 주유소 리스트 재갱신
            c_cnt += 1 # 충전회수 ++1
    if arrive_flag is True:
        print(f"#{case+1} {c_cnt}")
    else:
        print(f"#{case+1} 0")

