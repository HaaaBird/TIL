# swea_4836.py
# 색칠하기

T = int(input())

for case in range(T):
    N = int(input())
    square_list = []
    matrix = [[0 for _ in range(10)] for i in range(10)]
    for i in range(N):
        square_list.append(list(map(int, input().split())))
    
    # paint
    for bp in square_list:
        # y movement
        color = bp[4]
        for y in range(bp[1], bp[3]+1):
            for x in range(bp[0], bp[2]+1):
                matrix[y][x] += color

    purple_count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            if matrix[y][x] == 3:
                purple_count += 1
    print(f"#{case+1} {purple_count}")