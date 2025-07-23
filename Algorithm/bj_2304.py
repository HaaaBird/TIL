

T = int(input())

max_column = [0,0]
column_list = []
for case in range(T):

    column_list.append(list(map(int, input().split())))
    if column_list[-1][1] > max_column[1]:
        max_column = column_list[-1]

column_list = sorted(column_list, key=lambda x: x[0])
max_col_idx = column_list.index(max_column)

left_list = column_list[:max_col_idx+1]
right_list = column_list[max_col_idx:]

m2 = max_column[1]
x_ = left_list[0][0]
y_ = left_list[0][1]

for col in left_list:
    if col[1] > y_:
        m2 = m2 + (col[0] - x_) * y_ 
        x_ = col[0]
        y_ = col[1]

x_ = right_list[-1][0]
y_ = right_list[-1][1]
for col in reversed(right_list):
    if col[1] >= y_:
        m2 = m2 + (x_ - col[0]) * y_ 
        x_ = col[0]
        y_ = col[1]

print(m2)