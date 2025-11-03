# swea_1242.py
# 암호코드 스캔
import sys
sys.stdin = open("input.txt", "r")
binary_code_dict = {
    (3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4, (1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8, (3, 1, 1, 2): 9
}
hex_to_binary = {
    "0": [0, 0, 0, 0], "1": [0, 0, 0, 1], "2": [0, 0, 1, 0], "3": [0, 0, 1, 1], "4": [0, 1, 0, 0],
    "5": [0, 1, 0, 1], "6": [0, 1, 1, 0], "7": [0, 1, 1, 1], "8": [1, 0, 0, 0], "9": [1, 0, 0, 1],
    "A": [1, 0, 1, 0], "B": [1, 0, 1, 1], "C": [1, 1, 0, 0], "D": [1, 1, 0, 1], "E": [1, 1, 1, 0], "F": [1, 1, 1, 1]
}


def get_thickness(in_arr):
    # 테스트용 t_arr = [0,0,0,0,1,1,1,1,0,0,0,0,1,1] 1, 두께 2
    # 이 함수의 목적은 지금 들어온 숫자를 디코딩할때 필요한 굵기를 리턴해주기 위한 함수
    # 배수 숫자 하나 return 하면 됨.
    in_arr = tuple(in_arr)
    if binary_code_dict.get(in_arr,[]) or binary_code_dict.get(in_arr) == 0:
        return 1
    multiple = None
    for chk_mul in [2, 3, 5, 7]:
        pass_cnt = 0
        for s_num in in_arr:
            if s_num % chk_mul == 0:
                pass_cnt += 1
            else:
                break
        if pass_cnt == 4:
            multiple = chk_mul
            break
    multiple_cnt = 1
    new_arr = list(in_arr[:])  # 1차원 배열이라 얕은 복사 떠도 됨
    repeat_cnt = 0
    while True:
        repeat_cnt += 1
        for i in range(len(new_arr)):
            new_arr[i] = new_arr[i] // multiple
        new_arr = tuple(new_arr)
        if binary_code_dict.get(new_arr) or binary_code_dict.get(new_arr) == 0:
            return multiple_cnt * multiple
        else:
            multiple_cnt += 1
            new_arr = list(new_arr)


def streak_count_list_return(in_arr, mod):
    result = []
    start = None
    binary_len = 1
    if mod == 1:
        start = in_arr[-1]
        for i in range(len(in_arr)-2, -1, -1): # 역방향 순회
            if len(result) == 4:
                break
            if start == in_arr[i]:
                binary_len += 1
            else:
                result.append(binary_len)
                binary_len = 1
                start = in_arr[i]
    else:
        start = in_arr[0]
        for i in range(1, len(in_arr)):
            if len(result) == 4:
                break
            if start == in_arr[i]:
                binary_len += 1
            else:
                result.append(binary_len)
                binary_len = 1
                start = in_arr[i]
    if len(result) < 4:
        result.append(binary_len)
    if mod == 1:#
        return list(reversed(result))
    else:
        return result


def check_code(arr):
    global visit
    # 첫 번째 수 찾아서 두꼐 확인하기
    arr = list(arr)
    c_arr = arr[:]
    b_arr = []
    in_data = []  # 최종결과값 저장할 리스트 return 대상
    for s_hex in c_arr:
        b_arr += hex_to_binary[s_hex]

    while len(b_arr) >= 56:
        while True:  # 0이 아닌 첫번째 수 찾기
            if len(b_arr) == 0:
                break
            if b_arr[-1] == 0:
                b_arr.pop()
            else:
                break
        if len(b_arr) < 56:  # 크면 중단하고 나와야 함.
            break
        # 0이 아닌 첫번째 수 나옴.
        # 그러면 일단 당장 14자리 잘라서 두께 확인
        thick_test_arr = b_arr[len(b_arr) - 56:]
        # 끝 숫자 패턴 추출 연속된 숫자 수 확인
        length_chk = streak_count_list_return(thick_test_arr, 1)
        thickness = get_thickness(length_chk)  # 두께 확인
        # 두께값이 나왔으면 이번 코드 길이만큼 코드 잘라서 해석
        n_arr = b_arr[len(b_arr) - 56 * thickness:]
        del b_arr[len(b_arr) - 56 * thickness:]

        if tuple(n_arr) in visit:
            continue
        visit.add(tuple(n_arr))
        n_decimal_list = []
        even = 0
        odd = 0
        for i in range(0, len(n_arr), 7 * thickness):
            decode_tuple = []
            streak = streak_count_list_return(n_arr[i:i + 7 * thickness], 0)
            for j in streak:
                decode_tuple.append(j // thickness)
            decode_tuple = tuple(decode_tuple)
            decode_num = binary_code_dict[decode_tuple]
            n_decimal_list.append(decode_num)

        for i in range(1, 8):
            if i % 2 == 0:  # 짝수
                even += n_decimal_list[i - 1]
            else:
                odd = odd + (n_decimal_list[i - 1] * 3)
        if (even + odd + n_decimal_list[-1]) % 10 == 0:
            in_data.append(sum(n_decimal_list))

    return sum(in_data)


T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [input().strip().upper() for _ in range(N)]
    visit = set()
    out_visit = set()
    total_score = 0
    for arr in matrix:
        if arr in out_visit:
            continue
        out_visit.add(arr)
        for idx in range(M):
            if arr[idx] != "0":
                a = check_code(arr)
                total_score += a
    print(f"#{case} {total_score}")
