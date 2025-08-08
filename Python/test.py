# bit = [0, 0, 0, 0]
# for i in range(2):
#   bit[0] = i
#   for j in range(2):
#     bit[1] = j
#     for k in range(2):
#       bit[2] = k
#       for l in range(2):
#         bit[3] = l
#         print(bit)

# N = 4
# for i in range(1 << N):  # 0부터 15까지
#     bit = [(i >> j) & 1 for j in reversed(range(N))]
#     print(bit)


arr = [3,7,7,1,5,4]
n = len(arr)

for i in range(1<<n): # 64, 혹은 2**len(n) 으로 안쓰고 비트 연산 형태로 쓰는 이유는 
    # 비트를 이용한 부분집합 찾겠다는 묵시적인 표현. 컴하하하들 은 알아먹는다고
    for j in range(n):
        if i & (1<<j): 
            # 일반적인 AND 연산처럼 값을 결합하는 게 아니라,
            # i의 j번째 비트가 켜져 있는지를 검사하겠다는 뜻.
            # 예를 들어 i = 3 (10진수) → 이진수로 011
            # j = 2이면 (1 << 2) → 100 (2진수)
            # 즉, i의 2번째 비트(세 번째 자리)가 1인지 확인하는 것.
            # 이 경우 i & (1 << 2) = 011 & 100 = 000 → 결과는 0(False)
            print(arr[j], end=", ") # 해당하는 bit 가 켜져 있으면 arr[j]를 print, 
    print()
print()