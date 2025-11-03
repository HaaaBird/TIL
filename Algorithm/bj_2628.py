def max_distance(in_list):
    result = 0
    for i in range(len(in_list)-1):
        now_val = in_list[i+1] - in_list[i]
        if result < now_val:
            result = now_val
    return result

x, y = map(int, input().split())
T = int(input())
x_cut_list = [0]
y_cut_list = [0]

for case in range(T):
    mod, point = map(int, input().split())
    if mod == 0 :
        y_cut_list.append(point)
    else:
        x_cut_list.append(point)
        

x_cut_list.append(x)
y_cut_list.append(y)
x_cut_list.sort()
y_cut_list.sort()

max_x = max_distance(x_cut_list)
max_y = max_distance(y_cut_list)

print(max_x * max_y)