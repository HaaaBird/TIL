# swea_11092.py
# 최대 최소의 간격


T = int(input())

for case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    # for 문 갱신하며 최대값, 최소값 idx 저장.

    max_idx = arr[0]
    max_val = 0
    min_idx = arr[0]
    min_val = 11

    for i in range(len(arr)):
        # 최대값 갱신조건. 가장 오른쪽 idx 를 찾기 위해 크거나 같다로 조건 설정
        if arr[i] >= max_val:
            max_val = arr[i]
            max_idx = i
        # 최소값은 가장 먼저 나오는 조건임으로 작다로 조건 설정
        if arr[i] < min_val:
            min_val  = arr[i]
            min_idx = i
    result = max_idx - min_idx
    print(f"#{case+1} {abs(max_idx - min_idx)}")
