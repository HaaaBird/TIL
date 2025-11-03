# boj_28352.py
# 10!

def get_pow(num):
    if num == 1:
        return 1
    return num * get_pow(num-1)

a_f = get_pow(int(input()))
week_sec = 60*60*24*7

print(int(a_f/week_sec))