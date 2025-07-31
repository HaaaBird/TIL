def up_stream_function(array, now_x_point):
    y_distance = 0
    while True:
        if array[y_distance][now_x_point] == 1:
            y_distance += 1
        else:
            break
    return y_distance

def forward_function(array, now_y_point):
    pass

T = int(input())
array = []
array_size = 0
column_list = []
for case in range(T):
    column_list.append(list(map(int, input().split())))
    if  array_size < max(column_list[-1]):
        array_size = max(column_list[-1])
column_list = sorted(column_list, key=lambda x: x[0])

total_m2 = 0
x_ = column_list[0][0]
y_ = column_list[0][1]

for col in range(1,len(column_list)):  
    if col[1] > start_y:
        m2 = m2 + (col[0] - start_x) * start_y 
        x_ = col[0]
        y_ = col[1]
        
        if y_ == array_size:
            m2 = m2 + 1















# # 행렬 만들기
# for i in range(array_size):
#     array.append([0]*array_size)

# # 기둥 그리기

# for column in column_list:
#     for y in range(column[1]):
#         array[y][column[0]-1] = 1


# # approach_left
# # get letf start point
# left_start_point = [0,0]
# for i in range(array_size):
#     if array[0][i] == 1:
#         left_start_point = [0,i]