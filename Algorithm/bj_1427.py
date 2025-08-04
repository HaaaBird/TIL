# bj_1427.py


start_num = input()
result = []
for i in start_num:
    result.append(i)
result.sort(reverse=True)
result_str = ''.join(map(str, result))
print(result_str)

