# boj_1541.py
# 잃어버린 괄호

"""
문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다.
그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고,
가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고,
5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다.


마이너스로 뭉텅이 만들어 던지는게 가장 이득이다.

list 두개 만들어 놓고, 숫자를 검사하다
마이너스 부호를 만나면 이후 숫자는 다 마이너스 처리해도 된다,



15 + 34 - 22 - (15 + 30) 하면 최소기 때문. 마이너스 부호 한번 나오면 뒤는 다 마이너스임.
그럼 자릿수를 어떻게 인식하느냐

문자열을 한 글짜씩 읽어오고,이게 만약 isnum? 이면 temp에 붙여서 저장하다가 부호 나오면 temp -> str -> int
"""


if __name__ == "__main__":
    equation = input() + "+"
    plus_list = []
    minus_list = []
    temp_num = []
    plus_flag = True
    for s_char in equation:
        if s_char.isdigit():
            temp_num.append(s_char)
        elif plus_flag and s_char == "+":
            temp = "".join(map(str, temp_num))
            temp_num = []
            plus_list.append(int(temp))
        elif plus_flag and s_char == "-":
            plus_flag = False
            temp = "".join(map(str, temp_num))
            temp_num = []
            plus_list.append(int(temp))
        else:
            temp = "".join(map(str, temp_num))
            temp_num = []
            minus_list.append(int(temp))

    print(sum(plus_list) - sum(minus_list))