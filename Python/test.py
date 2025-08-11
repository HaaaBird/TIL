target = list("TTT")
arr = list("TTTTAACCA")

for i in range(0, len(arr) - len(target) + 1, 1):
    if arr[i:i+len(target)] == target:
        print(True)
        break