# swea_1952.py
# 수영장

def backT(a, n_price):
    global result
    if len(a) == 12:
        result = min(result, n_price)
        return
    if result < n_price:
        return
    for i in range(3):
        if i == 0:
           a.append(i)
           backT(a, n_price + (price_list[0] * arr[len(a)-1]))
           a.pop()
        elif i == 1:
            a.append(i)
            backT(a, n_price + price_list[1])
            a.pop()
        elif i == 2:
            if len(a) + 3 <= 12:
                a.append(i)
                a.append(i)
                a.append(i)
                backT(a, n_price + price_list[2])
                a.pop()
                a.pop()
                a.pop()
            elif (len(a) + 2) == 12:
                a.append(i)
                a.append(i)
                backT(a, n_price + price_list[2])
                a.pop()
                a.pop()
            else:
                a.append(i)
                backT(a, n_price + price_list[2])
                a.pop()





T = int(input())
for case in range(1, T + 1):
    price_list = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = 10 ** 10
    backT([], 0)
    if result < price_list[3]:
        print(f"#{case} {result}")
    else:
        print(f"#{case} {price_list[3]}")