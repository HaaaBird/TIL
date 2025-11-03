# swea_6190.py
# 정곤이의 단조 증가하는 수


"""

정곤이는 자신이 엄청난 수학자임을 증명하기 위해,
어떤 규칙 만족하는 수를 찾아보기로 했다.

그 규칙은 단조 증가하는 수인데, 각
숫자의 자릿수가 단순하게 증가하는 수를 말한다.

어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.
예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
양의 정수 N 개 A1, …, AN이 주어진다.
 1 ≤ i < j ≤ N 인 두 i, j에 대해,
 Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.

두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.


[출력]

문제 이해 자체를 잘못했다.
단조 증가하는 수가 AI x AK니까 계산해보고 단조 증가 안하면 버리는 식으로 계산을 했어야 함.
값이 오름차순으로 주어지니까 반대로 정렬해서 백트래킹으로 시도

중단 조건은 어차피 오름차순 정렬이기 때매 중간에 한번이라도 계산 성공해서 갱신했다면 더 이상 볼거 없음
바로 숫자 둘 다 빼버려야 함.
"""
def MCT_check(num):
    num = str(num)
    cnt = 1
    for i in range(1, len(num)):
        if int(num[i-1]) <= int(num[i]):
            cnt += 1
        else:
            break
    if len(num) == cnt:
        return True
    else:
        return False
def backtracking_search(a, start, N):
    global answer
    if len(a) == 2:
        n_result = int(arr[a[0]]) * int(arr[a[1]])
        pf = MCT_check(n_result)
        if pf:
            answer = max(answer, n_result)
            return True
        return
    for i in range(start, N):
        if i not in a:
            a.append(i)
            b = backtracking_search(a, i, N)
            if b:
                a.pop()
                return
            a.pop()


T = int(input())
for case in range(1, T + 1):
    answer = -1
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    backtracking_search([], 0, N)
    print(f"#{case} {answer}")

