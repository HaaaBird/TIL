T = int(input())

for case in range(T):
    N = int(input())
    arr = list(map(int,input().split()))

    arr.sort(reverse=True)
    work_count = 0
    print(f"#{case + 1}", end= " ")
    while work_count != 10:
        if work_count % 2 == 0:
            print(f"{arr.pop(0)}", end=" ")
        else:
            print(f"{arr.pop(-1)}", end=" ")
        work_count += 1
    print()
