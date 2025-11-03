for case in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(2, N-2):
        if max(arr[i-2:i+3]) == arr[i]: # 내가 가장 높을 때, 조망권은 확보된다
            another = arr[i-2:i] + arr[i+1:i+3]
            result += arr[i] - max(another)
    print(f"#{case+1} {result}")
