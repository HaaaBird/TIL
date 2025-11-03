import sys 
T = int(sys.stdin.readline()) #input으로 하면 시간초과

arr = []
for case in range(T):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        arr.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "empty":
        if len(arr) != 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
        
        