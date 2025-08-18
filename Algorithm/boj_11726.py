# boj_11726.py
# 2×n 타일링

"""

2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

"""

N = int(input())
result_list = [0,1,2,3,5,8]
if len(result_list)-1 >= N:
    print(result_list[N] % 10007)
else:
    last_1 = result_list[-2]
    last = result_list[-1]
    for i in range(N-5):
        temp = last
        last += last_1
        last_1 = temp
    print(last % 10007)