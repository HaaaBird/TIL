# bj_1747.py
# 소수, 팰린드롬

def is_prime_num(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def is_palindrome(x):
    digit_count = 0
    x_copy = x
    while x_copy > 0:
        x_copy //= 10
        digit_count += 1
    for i in range(1,digit_count):
        l_num = x // 10**(digit_count - i)
        r_num = x % 10**i
        if l_num == r_num:
            x = x - l_num * 10**(digit_count-i) - r_num


