l_rainbow_set = set()
u_rainbow_set = set()


N = int(input())
in_str = list(map(str, input().strip()))

for char in in_str:
    if char.islower():
        l_rainbow_set.add(char)
    else:
        u_rainbow_set.add(char)

if len(l_rainbow_set) == 7 and len(u_rainbow_set) != 7:
    print("yes")
elif len(l_rainbow_set) != 7 and len(u_rainbow_set) == 7:
    print("YES")
elif len(l_rainbow_set) == 7 and len(u_rainbow_set) == 7:
    print("YeS")
else:
    print("NO!")