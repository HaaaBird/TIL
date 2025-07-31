T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    anser_arr = []
    # min search
    for idx in range(len(arr)-M+1):
        anser_arr.append(sum(arr[idx:idx+M]))

    print(f"#{case+1}",(max(anser_arr)) - (min(anser_arr)))