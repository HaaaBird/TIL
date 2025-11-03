# 진법 변환
# 10진수 -> 2진수 변환
def decimal_to_binary(N):
    print("######################################")
    print("10진수 -> 2진수 변환")
    print("기본 아이디어: 2로 나눈 나머지를 result.append()")
    print("역순으로 들어감으로 result.revere 처리 후 출력")
    target = N
    result = []
    print(f"시작 숫자: {target}")
    while target != 0:
        result.append(target % 2)
        target //= 2
    result.reverse()
    print("연산 결과: ", "".join(map(str, result)))
    print()
    return "".join(map(str, result))


def binary_to_decimal(N):
    print("######################################")
    print("2진수 -> 10진수 변환")
    print("기본 아이디어: 2진법 자릿수에 1이 있으면 2^자릿수")
    num_len = len(N)
    result = 0
    print(f"시작 숫자: {N}(이진법)")
    for s_char in N: # 문자열 입력 들어음 iterable
        if s_char == "1":
            result += 2 ** (num_len - 1)
        num_len -= 1
    print("연산 결과:", result)
    print()

def use_default_function():
    N = 150
    print("######################################")
    print("내장 함수 이용한 변환")
    print(f"변환 기본 타입: {type(bin(N))}")
    print("기본 숫자: ", N)
    print(f"2진수: bin(N) {bin(N)}")
    print(f"16진수: hex(N) {hex(N)}")


def bit_calculation():
    print("######################################")
    print("비트 연산이 기본적으론 가장 빠른 연산")
    print("수행 예")
    print()
if __name__ == "__main__":
    
    decimal_num = decimal_to_binary(8)
    binary_to_decimal(decimal_num)
    use_default_function()
    print(bin(0b1111 ^ 0b1101))
    
