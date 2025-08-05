# swea_1945.py
# 간단한 소인수분해



T = int(input())
for case in range(1, T+1):
    N = int(input())
    p_nums = [2,3,5,7,11]
    p_nums_power = [0] * 5

    # for 문을 이용해 소수 부분 iter 진행
    # while 문 통해 해당 값 % 소수가 !=일때까지 while 진행

    for i in range(len(p_nums)):
        while N % p_nums[i] == 0:
            N = N // p_nums[i]
            p_nums_power[i] += 1
    result = " ".join(map(str, p_nums_power))
    print(f"#{case} {result}")



