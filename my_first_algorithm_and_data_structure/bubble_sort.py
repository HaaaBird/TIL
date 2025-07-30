def bubble_sort_break():
    in_list = [2,4,5,6,7,31,455,21,2]
    count = 0    
    for i in range(len(in_list) - 1): 
        swap = True
        for j in range(len(in_list)-1):
            count += 1
            if in_list[j] > in_list[j+1]:
                temp = in_list[j]
                in_list[j] = in_list[j+1]
                in_list[j+1] = temp    
                swap = False
        if swap:
            return in_list, count
    return in_list, count
        

def bubble_sort_all():
    in_list = [2,4,5,6,7,31,455,21,2]
    count = 0
    for i in range(len(in_list) - 1): 
        for j in range(len(in_list)-1):
            count += 1
            if in_list[j] > in_list[j+1]:
                temp = in_list[j]
                in_list[j] = in_list[j+1]
                in_list[j+1] = temp    
    return in_list, count

def bubble_sort_test_main():
    pass





if __name__ == "__main__":
    a, count_0 = bubble_sort_all()
    b, count_1 = bubble_sort_break()
    print("최적화 안한 코드 결과:", a, count_0)
    print("최적화 좀 한 코드 결과:", b, count_1)