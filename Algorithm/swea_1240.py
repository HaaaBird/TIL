# swea_1240.py
# 단순 2진 코드

"""
일단 매트릭스에서 암호 구분하는건
줄 단위로 읽어와서 줄 단위로 sum 때려보면 됨. 0이면 pass
0이 아니면 암호 있는 행

그러면 해당 행에서 암호가 어디부터인지 어떻게 알지?
마지막 1을 찾는다.
암호코드는 뭘 하던 마지막 숫자는 1이다. 따라서 마지막 1에서 부터 56개 인덱싱 해서 잘라오면 그게 암호코드다.


암호유효성검사는
짝수 * 3 + 홀수 해서 10의 배수 되면 됨.
이걸 문자열로 읽어와서 확인 시간 넘친다.

바코드 형태라서 여러번 주어지는거지 이거 그냥 하나만 읽으면 된다.

"""
dict_key = {
    (0,0,0,1,1,0,1):0,
    (0,0,1,1,0,0,1):1,
    (0,0,1,0,0,1,1):2,
    (0,1,1,1,1,0,1):3,
    (0,1,0,0,0,1,1):4,
    (0,1,1,0,0,0,1):5,
    (0,1,0,1,1,1,1):6,
    (0,1,1,1,0,1,1):7,
    (0,1,1,0,1,1,1):8,
    (0,0,0,1,0,1,1):9
}

def check():
    pass

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    code_arr = []
    matrix = [list(map(int, input().strip())) for _ in range(N)]
    for arr in matrix:
        if sum(arr) != 0:
            code_arr = arr
            break
    for ri in range(M-1, -1, -1):
        if code_arr[ri] == 1:
            code_arr = code_arr[ri - 56 + 1 : ri + 1]
            break
    cnt = 0
    change_num = []
    even = 0
    odd = 0
    for i in range(0, 56, 7):
        a = tuple(code_arr[i:i+7])
        now_num = dict_key[a]
        if cnt % 2 != 0: # 홀수
            odd += dict_key[a]
        else:
            even = even + (now_num * 3)
        change_num.append(dict_key[a])
        cnt += 1
    if (even + odd) % 10 != 0:
        print(f"#{case} 0")
    else:
        print(f"#{case} {sum(change_num)}")