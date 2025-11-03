# swea_5201.py
# 컨테이너 운반
"""

트럭당 컨테이너 1개씩만 가져갈 수 있으니까.
일단 크기순으로 오름차순 하고
만약 물건을 옮길 수 있으면 트럭에 물건 달아서 보내고 끝
"""

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    p_arr = list(map(int, input().split()))
    t_arr = list(map(int, input().split()))
    p_arr.sort()
    t_arr.sort()

    total = 0
    while len(t_arr) != 0 and len(p_arr) != 0:
        if t_arr[-1] >= p_arr[-1]:
            t_arr.pop()
            total += p_arr.pop()
        else:
            p_arr.pop()
    print(f"#{case} {total}")