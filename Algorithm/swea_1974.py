# swea_1974.py
# 스도쿠 검증

# 대각방향으로 순회하며 행/열 검사
# % 연산 통해서 박스도 검산
# 델타로 +, box 배열 빼서 접근하면서 검색하도록. 검색 세트 자체는 총 9회 순회하게.
T = int(input())

for case in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    pass_flag = True
    for i in range(9):
        cnt_arr = [0] * 10
        for x in range(9):
            cnt_arr[matrix[i][x]] += 1 # 행 단위로 순회하며 모든 요소 cnt_list 에 업데이트
            cnt_arr[matrix[x][i]] += 1 # 열 단위 순회하며 요소 cnt_list 에 업데이트
            r1 = i // 3 # 모듈러 연산. 행 단위 반복 규칙
            r2 = i % 3
        # 박스 단위 순회 연산
        for bi in range(0+r1*3,3+r1*3):
            for bj in range(0+r2*3,3+r2*3):
                cnt_arr[matrix[bi][bj]] += 1
        if set(cnt_arr[1:]) != {3}:
            pass_flag = False
            break
    print(f"#{case} {int(pass_flag)}")
