# boj_15649.py
# N과 M(1)

"""

백트래킹 연습문제

백트래킹은 재귀 써서 틀렸을때 다시 돌아가는 기능을 적극적으로 활용하는 프로그래밍 기법.
진입조건과 중단조건을 확실하게 해서 가야 함.


1~N 까지 자연수 중 중복 없이 m개를 고른 수열을 만드는 문제.

중복 없이 m개 -> 1,2 2,1 가능

그러면 이 선택을 어케하냐?
어차피 중복만 없으면 됨.

1을 골랐다. 두번째 숫자로 2,3,4 가능
하여튼 아무거나 지금 고른 숫자 외 다른걸 고르게 해라.

그러면 이걸 동작순서대로 적어보면

맨 앞 숫자 한개를 고르고
또 하나 잡아본다.
근데 그게 이미 있으면 pass
아니면 추가.
추가했더니 길이가 같다 -> 출력하고


"""


def backtrack1(arr, n, m):

    if len(arr) == m:
        print(*arr)
    else:
        for i in range(1, N + 1):
            if i not in arr:
                arr.append(i)
                backtrack1(arr, n, m)
                arr.pop()

N, M = map(int, input().split())
arr = []
backtrack1(arr, N, M)