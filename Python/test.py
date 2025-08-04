def cal_sum_1(n):
    return n * (n+1) // 2


def cal_sum_2(n):
    a = 0
    for i in range(1, n+1):
        a += i

    return  a


print(cal_sum_1(101))
print(cal_sum_2((101)))