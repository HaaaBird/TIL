hex_map = {
    0:0,1:1,2:2,3:3,4:4,5:5,
    6:6,7:7,8:8,9:9,10:"A",11:"B",
    12:"C", 13:"D", 14:"E", 15:"F",
}
hex_map_reverse = {
    "0":0, "1":1, "2":2, 3:3, "4":4, "5":5, "6":6, 7:7,
    "8":8, "9":9, "A":10, "B":1,"C":12, "D":13, "E":14, "F":15,
}

def decimal_to_another(n, m):
    b_num = []

    while n > 0:
        remain = hex_map[n % m]
        b_num.append(remain)
        n = n // m
    return list(reversed(b_num))

def another_to_decimal(a_num_str, formation):
    pow = 0
    decimal = 0
    for s_char in reversed(a_num_str):
        decimal += hex_map_reverse[s_char] * (formation ** pow)
        pow += 1
    return decimal

print(*decimal_to_another(28, 16)) # 1 C
print(hex(28)) # 0x1c
print(another_to_decimal("1C", 16)) # 28