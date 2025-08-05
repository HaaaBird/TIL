# swea_6485.py
# 삼성시의 버스 노선


T = int(input())

for case in range(1, T + 1):
    # 입력단부분
    N = int(input())
    bus_array = []
    # 버스 노선 읽어오기
    for _ in range(N):
        bus_array.append(list(map(int, input().split())))
    P = int(input())
    result_stop = []
    # 결과 출력할 버스 정류장 읽어오기
    for _ in range(P):
        result_stop.append(int(input()))

    # 반복문. 각각의 버스 범위에 해당하는
    bus_stops = [0] * 5001 # 버스정류장 5000 개(count 변수로 쓸 것)

    # 해당하는 버스정류장 idx 카운팅
    for bus in bus_array:
        for i in range(bus[0], bus[1]+1):
            bus_stops[i] += 1
    # 출력
    print(f"#{case}", end=" ")
    for stop in result_stop:
        print(bus_stops[stop], end= " ")
    print()
