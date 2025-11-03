# boj_15829.py
# 해싱

N = int(input())
in_str = list(input().strip())

hash_num = 0
for idx, s_chr in enumerate(in_str):
    n_num = ((ord(s_chr) - 96) * pow(31, idx))
    hash_num += n_num

print(hash_num % 1234567891)