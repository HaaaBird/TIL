# swea_5203.py
def is_babygin(cnt):
    # triplet
    for v in cnt:
        if v >= 3:
            return True
    # run
    for i in range(8):
        if cnt[i] and cnt[i+1] and cnt[i+2]:
            return True
    return False

T = int(input())
for case in range(1, T + 1):
    nums = list(map(int, input().split()))
    c1 = [0]*10
    c2 = [0]*10
    ans = 0

    for i, x in enumerate(nums):
        if i % 2 == 0:
            c1[x] += 1
            if i >= 4 and is_babygin(c1):
                ans = 1
                break
        else:
            c2[x] += 1
            if i >= 5 and is_babygin(c2):
                ans = 2
                break

    print(f"#{case} {ans}")
