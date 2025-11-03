# swea_5097.py
# 회전

"""
N개의 숫자로 이루어진 수열이 주어진다.
맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때,
수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.
"""

if __name__ == "__main__":
    T = int(input())
    for case in range(1, T + 1):
        N, M = map(int, input().split())
        arr = list(map(int, input().split()))
        for _ in range(M):
            temp = arr.pop(0)
            arr.append(temp)
        print(f"#{case} {arr[0]}")



