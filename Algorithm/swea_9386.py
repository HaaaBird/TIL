# swea_9386.py
# 연속한 1의 개수

def solve_use_str():
    in_val = input()
    c_max = 0
    # 2중 for 문. 다음 원소도 1인지 확인하는 코드
    for i in range(len(in_val)):
        # 선택된 놈이 1이면
        if in_val[i] == "1":
            now_c = 0
            for j in range(i, len(in_val)):
                if in_val[j] == "1":
                    now_c += 1
                else:
                    break
            if now_c > c_max: c_max = now_c
    return c_max


if __name__ == "__main__":
    T = int(input())
    for case in range(T):
        N = int(input())
        print(f"#{case+1} {solve_use_str()}")