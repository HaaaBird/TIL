# boj_15650.py
# N과 M (2)

"""
이번 문제의 경우 중복순열을 뺀다는 조건이 들어간다.
오름차순을 유지해라 -> 조합 문제로 풀어라

즉 1,2
2,1 이런거 하지 않는다는 뜻.

그러면
이전에 선택해 본거 하지 말라
4 2의 경우
첫 자리가 1이면 2,3,4 다 가능
첫 자리가 2이면 3, 4 가능
첫 자리가 3이면 4만 가능
4까지 오면 할거 없음

"""

def backtracking(arr, start, n, m):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start, N+1):
        arr.append(i)
        start += 1
        backtracking(arr, start, n, m)
        arr.pop()
N, M = map(int, input().split())
arr = []
backtracking(arr, 1, N, M)