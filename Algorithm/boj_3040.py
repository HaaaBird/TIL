# boj_3040.py
# 백설공주와 일곱 난장이

"""
9개 숫자 중 100이 되는 조합을 찾으시오인데
백트래킹 쓰면 금방 될거같은데
"""


def backT(arr):
    global result
    if len(result) == 7:
        return
    if len(arr) == 7:
        n_sum = []
        for idx in arr:
            n_sum.append(a[idx])
        if sum(n_sum) == 100:
            result = n_sum[:]

    for i in range(9):
        if len(result) == 7:
            return
        if i not in arr:
            arr.append(i)
            backT(arr)
            arr.pop()



a = [int(input()) for _ in range(9)]
result = []
backT([])
for num in result:
    print(num)
