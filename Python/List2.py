# List2
import time
from pprint import pprint

def get_two_dimensional_array_use_list_comprehension():
    """
    리스트 컴프리핸션을 왜 쓰냐? 파이썬에서 빠름. 내부 로직이 C로 직접적으로 동작하게 부분이라
        for 문 중첩해서 쓰는것보다 아주 약간 더 빠름.
        코드 길이도 짧아져서 보기 편함
        있어보임

    쓰면 안되는 이유
        파이썬에만 있는 문법인지라 언어 섞어써야 하는 환경에서 리스트 컴프리핸션 쓰면 가독성이 떨어짐
        비 파이썬 개발자들이 처음 보고 뭔지 모르겠어서 싫어함.
        
    for _ in range(5): -> 일 때,  _ 는 반복문의 할당 임시 변수를 쓰지 않겠다는 묵시적인 파이썬 문법
    """
    # [0,0,0,0,0] 이 있는 배열을 리스트컴프리핸션 두번 써서 생성하는 예시
    arr_1 = [[[0] for _ in range(5)]for _ in range(5)]

    # 속도 비교 코드
    N = 1000
    start_time = time.time()
    t_arr_1 = []
    for _ in range(N):          # 바깥쪽 리스트(행)
        row = []
        for _ in range(N):      # 안쪽 리스트(열)
            row.append(0)     # 각 칸에 [0] 추가
        t_arr_1.append(row)
    end_time = time.time()
    for_time = end_time - start_time
    print("##################################")
    print("2중for문, 리스트 컴프리핸션 속도 비교")
    print("##################################")
    print(" ")
    print(f"2중for문: ", for_time)

    start_time = time.time()
    t_arr_2 = [[0 for _ in range(N)] for _ in range(N)]
    end_time = time.time()
    l_c_time = end_time - start_time
    print(f"리스트 컴프리핸션: ", l_c_time)
    print(100 - (l_c_time/for_time * 100), '% 만큼 속도 차이 발생(음수일 경우 for 문이 더 빠름)')
    print("##################################")
    print(" ")
    # 항상 빠른건 아니나 대부분의 경우 리스트 컴프리핸션이 조금 더 빠름
    # N값이 크면 클수록 리스트컴프리핸션이 빠른 경우가 많음.
    # 다만 for문 동작도 매우 빠른 편. 실무에서 이걸로 속도 따지는 경우는 많지 않다고.
    
def zigzag_traversal():
    """
    지그재그 순회. 일반 순회는 간단해서 넘어가고
    이거 c++로 구현하는게 c++반 분반 시험 문제였음.
    문제 풀거나 프로그램 만들때 가끔 쓰이니 기억하는게 좋음. 
    """
    arr = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    n = 3
    for i in range(n):
        for j in range(n):
            print(arr[i][j + (n-1-2*j) * (i%2)], end=" ")
        print(" ")
    
def delta():
    """
    델타(Delta) 기법:
    2차원/3차원 그리드에서 인접한 칸을 탐색할 때,
    이동 방향을 좌표 변화량(Δx, Δy) 배열로 정의해 반복 처리하는 방식.
    
    시뮬레이션, BFS/DFS 탐색, 게임 범위 연산 등에 자주 사용.
    예: 게임에서 스플래시 공격 범위, 지도에서 인접 지역 탐색 등.
    자주 쓰이는 기본적인 기법
    """
    # 십자모양 순회하는 코드 예시
    arr = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    N = len(arr)
    di = [0,1,0,-1] # delta 맵 방향을 여기서 결정
    dj = [1,0,-1,0]

    for i in range(N):
        for j in range(N):
            for d in range(len(di)): # 맵을 어떻게 순회할지 순서를 결정하는 변수 d
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N:
                    print(arr[ni][nj], end= " ")
            print(" ")

def delta_2():
    """
    k값 범위만큼 순회하며 합계가 가장 큰 경우를 찾는
    델타 코드 만들기
    파리잡기 등
    """
    arr = [[1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15],
           [16,17,18,19,20],
           [21,22,23,24,25]]
    max_v = 0
    k = 2
    N = len(arr)
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    for i in range(N):
        for j in range(N):
            s = arr[i][j] # 중심위치
            for d in range(4):
                for c in range(1, k+1):
                    ni = i + di[d] * c
                    nj = j + dj[d] * c
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
    print(max_v)
    """
    구성 요약

    for i <- 행 방향 변수
        for j <- 열 방향 변수
            for d <- di, dj와 같은 방향 제어 행렬 관리 변수
                for c <- 거리 제어 변수
                if <- 에러 방지 조건문
                    실행

    의 4중 for 문 + if문으로 구성
    패턴 이해하고 외워두기
    """
def transposing():
    """
    전치 행렬 만드는 코드 패턴
    """
    print("##################")
    print("전치 행렬 만들기")
    print(" ")
    print("전치 전 행렬")
    arr = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
    pprint(arr)

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    print(" ")
    print("전치 처리 후")
    pprint(arr)
    print("###################")
    print(" ")

def use_bit_calcul_to_make_subset():
    """
    집합 a = [1,2,4,6] 일때, 
    2개 원소, 합이 5인 부분집합이 있는가? 있다면 몇개 있는가?
    에 대한 일반해 구하는 방법이 없음. 부분적으로, 
    배열 패턴상 가능한 경우가 있을 수 있으나, 일반해 구하는 방법은 없음.

    따라서, 결국 그냥 모든 부분집합을 몽땅 만들어 풀어야 하는 경우가 대부분.
    그 때 비트 연산을 이용하면 빠르게 해당 값을 구할 수 있음. 
    """
    
    arr = [1,2,3]
    n = len(arr)

    for i in range(1 << n): 
        # 1을 n만큼 왼쪽으로 비트 쉬프트 시키겠다는 뜻 
        # 2**n 과 동일한 연산이나, 비트 연산을 하겠다는 묵시적인 표현으로 가장 외곽 for문에 저런식으로 적음.
        for j in range(n):
            if i & (1 << j): # 현재 순회중인 bit연산 부분집합 i값과 j만큼 1을 쉬프트 했을때, 둘 다 1인가?
                # i 와 2**j 의 동일성을 따지는게 아님. 예를 들어
                # i = 3 이면 이진수로는 011 이고
                # j = 1 이면 1을 1번 왼쪽 쉬프트 010임
                # 011
                # 010 임으로 둘째자리가 둘다 1로 같으니 Pass
                
                print(arr[j], end=" ") # 1이라면 arr의 j번째 요소 출력
        print()
    print()

def binary_search():
    
    
    
    
    pass



if __name__ == "__main__":

    # get_two_dimensional_array_use_list_comprehension()
    # zigzag_traversal()
    # delta_2()
    # transposing()
    use_bit_calcul_to_make_subset()
   
   
   
   
   
   
   
   
    pass