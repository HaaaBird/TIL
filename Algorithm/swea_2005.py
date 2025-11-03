# swea_2005.py
# 파스칼의 삼각형


# N의 크기가 작다. 1~10
# 깡으로, 완전탐색으로 풀어도 무관하다.

# 파스칼의 삼각형 규칙은 시작과 끝은 1이다.
# 실질적인 연산이 필요한 배열은 시작과 끝을 제외한, 행 번호 -2한 값이 1 이상인 열 부터 연산값이 들어간다.
# 그러면 i -2 > 0 을 물어보고, 작으면 1 * i 을 출력하고 마지막 출력 리스트를 갱신하게 한다.
# 만약 크다면 이전 리스트를 순회하면서 계산을 하고, 이 앞뒤에 1을 더해서 푼다.

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    last = []
    print(f"#{case}")
    for i in range(1, N + 1):
        result = []
        if i - 2 <= 0:
            result = [1 for i in range(i)]
            last = result
            print(" ".join(map(str, result)))
        else:
            result.append(1)
            for j in range(len(last)-1):
                result.append(last[j] + last[j+1])
            result.append(1)
            last = result
            print(" ".join(map(str, result)))

