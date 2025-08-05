# bj_1747.py
# 소수, 팰린드롬

def is_prime_num(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def is_palindrome(x):