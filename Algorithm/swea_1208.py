# swea_1208.py
# Flatten

# 인덱스 읽어온 것을 카운트 정렬한 리스트를 만들고
# 상자 옮길때도 카운트 정렬을 사용해서 넣고 빼고 하기.
# 한번 옮길때마다 소팅 새로하면 비용이 너무 큼
T = 10
for case in range(1, T + 1):
    dump_num = int(input())
    arr = list(map(int, input().split()))

    c = [0] * 101
    for value in arr:
        c[value] += 1

    for _ in range(dump_num):
        # 최댓값 찾기
        for high in range(100, -1, -1):
            if c[high] > 0:
                c[high] -= 1
                c[high - 1] += 1
                break

        # 최솟값 찾기
        for low in range(101):
            if c[low] > 0:
                c[low] -= 1
                c[low + 1] += 1
                break

    # 결과 계산
    for high in range(100, -1, -1):
        if c[high] > 0:
            max_height = high
            break
    for low in range(101):
        if c[low] > 0:
            min_height = low
            break

    print(f"#{case} {max_height - min_height}")
