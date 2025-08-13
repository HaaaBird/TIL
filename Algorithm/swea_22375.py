# swea_22375.py
# 스위치 조작


"""
N개의 전등이 설치되어 있다. 각 전등은 1번부터 N번까지 번호가 붙어있고,
i번 스위치를 조작하면 i번부터 N번까지의 전등의 켜짐/꺼짐 상태가 반대가 된다고 한다.
모든 전등의 현재 상태와 스위치 조작 후 상태가 주어지면 최소 몇 개의 스위치를 조작해야 하는지 알아내는 프로그램을 만드시오.

전등이 켜진 상태는 1, 꺼진 상태는 0으로 주어진다.
예를 들어 현재 상태 A가 0 0 0이고, 조작 후 상태 B가 0 1 0인 경우,

초기상태가  0 0 0 이므로,
2번 스위치를 조작해 0 1 1인 상태를 만들고,
3번 스위치를 조작해 0 1 0인 상태를 만들 수 있으므로, 최소 2번의 조작이 필요하다.

하나 조작하면 다 꺼진다는거니까.

그냥 for i in range(len())을 써서 처음부터 숫자를 본다
다르면 끄고 뒤에를 다 반전시킨다.

입력 범위 자체가 별로 길지도 않다. O(N) 문제라 대충 풀어도 풀린다.

[입력]
첫 줄에 테스트케이스 개수 T, 다음 줄 부터 케이스 별로 스위치 개수 N, 다음 두 줄에 조작 전 스위치 상태 Ai와 조작 후 상태 Bi가 각각 N개씩 주어진다.
(1<=T<=10, 1<=N<=100)
"""


def reverse(arr, i):
    for j in range(len(arr[i:])):
        if arr[i+j] == 0:
            arr[i+j] = 1
        else:
            arr[i+j] = 0


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    current = list(map(int, input().split()))
    target = list(map(int, input().split()))

    cnt = 0

    for i in range(N):
        if current[i] != target[i]:
            cnt += 1
            reverse(current, i)

    print(f"#{case} {cnt}")
