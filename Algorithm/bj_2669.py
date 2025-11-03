array_size = 100
array = [[0]*array_size for _ in range(array_size)]
input_array = []

for i in range(4):
    x,y,xx,yy = (map(int, input().split()))
    for i in range(x, xx):
        for j in range(y, yy):
            array[j][i] = 1

result = 0
for i in range(array_size):
    for j in range(array_size):
        if array[i][j] == 1:
            result = result + 1 

print(result)

