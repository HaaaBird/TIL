# swea_4837.py
# 2일차 부분집합 합 구하기

T = int(input())
arr = [1,2,3,4,5,6,7,8,9,10,11,12] # 기본 배열
result_dict = {} #
for i in range(13): # 0~12까지 idx 배열 생성. 1~12 다 더한 값이 78
    result_dict.update({i:[0]*79}) # 0번 idx 감안해 79개 생성

# 비트연산 배열 50번 사용할 것임으로 시작하자마자 불러오기
for i in range(1 << 12):
    cnt = 0
    s_sum = 0
    for j in range(12):
        if i & (1 << j):
            cnt += 1
            s_sum += arr[j]
    result_dict[cnt][s_sum] += 1

for case in range(1, T + 1):
    N, K = map(int, input().split())
    print(f"#{case} {result_dict[N][K]}")