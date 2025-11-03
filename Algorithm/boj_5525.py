# BOJ 5525 - IOIOI
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()  # 개행 제거

ans = 0
cnt = 0
i = 0

while i < M - 2:              # 최소 3글자 필요
    if S[i:i+3] == 'IOI':
        cnt += 1              # "IOI" 1개 추가
        if cnt >= N:          # N개 연속이면 Pn 하나 성립
            ans += 1
        i += 2                # 겹침 허용 위해 2칸 전진
    else:
        cnt = 0               # 연속 끊김
        i += 1

print(ans)