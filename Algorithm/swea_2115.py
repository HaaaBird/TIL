
def get_value(arr, M):
    max_value = 0
    c = len(arr)
    for i in range(1, 1<<c):
        t_honey = 0
        t_value= 0
        for j in range(c):
            if i & (1<<j):
                t_honey += arr[j]
                t_value += arr[j] ** 2
        if t_honey <= M:
            max_value = max(max_value, t_value)
    return max_value


T = int(input())
for case in range(1, T+1):
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    values = []
    for i in range(N):
        for j in range(N-M+1):
            value = get_value(matrix[i][j:j+M],C)
            values.append((value, i, j))
    
