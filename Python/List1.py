import time
import random
"""
list 1장 코드 내용
1. 버블 정렬 
2. 카운팅 정렬

"""
def bubble_sort():
    # 첫 번째 원소부터 인접 원소끼리 자리 교환하며 맨 마지막 까지 이동하는 정렬 방법.
    # O(n^2)인 만큼, 실제 정렬에 사용이 자주되는 것은 아님.
    # 다만 코드가 간단하고 쉬운 만큼, 알고 있는 것이 좋음
    start_time = time.time()
    # 0~1000 사이 값을 가지는 랜덤 정수가 1000개 든 배열 생성 
    arr = [random.randint(0,1000) for _ in range(1000)] 
    N = len(arr)
    work_count = 0
    print("0~1000 사이 랜덤 정수, 길이 1000개짜리 배열")
    print("기존 배열: ", arr[:15])
    
    for i in range(N - 1, 0, -1): # 역순으로 i를 생성 1사이클 시 가장 큰 값이 맨 뒤로 가게 됨.
        for j in range(i): # i 한번당 1씩 감소하는 크기의 range 
            if arr[j] > arr[j+1]: # j가 j+1보다 더 크면
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                # 파이썬에선 아래 코드로도 동작하나, 다른 언어에선 지원 안함.
                # arr[j], arr[j+1] = arr[j+1], arr[j]
                work_count += 1
    end_time = time.time()

    print("버블 정렬 후 배열: ", arr[:15])
    print("정렬에 걸린 시간: ", end_time - start_time)
    print("for 문 실행 횟수: ", work_count)
    print("#################################")
    print()

def counting_sort():
    # Direct Access Table 개념. 꽤 중요한 내용
    # 현업에서 직접 자료구조를 다루던, 해시나 DB index 등 간접적으로 다루게 됨
    start_time = time.time()
    # 0~1000 사이 값을 가지는 랜덤 정수가 1000개 든 배열 생성 
    arr = [random.randint(0,1000) for _ in range(1000)] 
    N = len(arr)
    work_count = 0
    print("0~1000 사이 랜덤 정수, 길이 1000개짜리 배열")
    print("기존 배열: ", arr[:15])
    cnt_list = [0] * (1000+1) #0~1000 사이 값이 생성됨. 해당하는 크기의 cnt list 생성
    # arr 순회하며 카운팅
    for value in arr:
        cnt_list[value] += 1
        work_count += 1
    # 자리 보정
    for i in range(1, len(cnt_list)):
        cnt_list[i] = cnt_list[i] + cnt_list[i-1]
        work_count += 1
    
    result_list = arr[:] # 정렬된 값이 들어갈 리스트
    for i in range(len(arr)-1, -1, -1):
        # 왜 뒤에서 부터? 정렬 안정성 
        # 정수, 문자열 같이 단일 속성 값을 정렬할 경우엔 앞에서 정렬해도 상관 x
        # 예를 들어서 좌표, x,y 1,2로 되어 있는데 y는 정렬되어 있다면 만약 앞에서 부터 접근하면 다 뒤집힘.
        cnt_list[arr[i]] -= 1
        result_list[cnt_list[arr[i]]] = arr[i]
        work_count += 1

    end_time = time.time()

    print("버블 정렬 후 배열: ", result_list[:15])
    print("정렬에 걸린 시간: ", end_time - start_time)
    print("for 문 실행 횟수: ", work_count)
    print("#################################")
    print()

def exaustive_search():
    # 완전 탐색
    # 완전 탐색을 한다 -> 모든 경우의 수를 다 확인한다.
    # 모든 경우의 수 개념? -> 순열 개념.
    # 순열: 서로 다른 것 들 중 몇개를 뽑아서 한줄로 나열함. nPr로 표기
    # nPr 예시: 5명 중 1,2등을 뽑는 경우
    # 5P2 = 5! ÷ (5 - 2)! = 20 (n! / (n-2))
    """
    구현: for 문 중첩은 r에 의해 결정. 현재 경우는 r이 2라 중첩
    실제 현업에선 어떻게? 라이브 코드를 수정해 for문을 추가할 수 없으니 순열 라이브러리 생성해서 사용
    단순 시뮬레이션, 경로탐색, 게임 로직(좀 많이 멍청하고 수동적인AI) 등에서 
    할 수 있는 행동 리스트를 죄다 뽑아서(순열을 생성해) 처리하는 경우가 종종 있음.
    """
    items = ['A', 'B', 'C', 'D', 'E']
    result = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j:  # 같은 요소 중복 방지
                result.append((items[i], items[j]))

    print(f"총 개수: {len(result)}")
    for r in result:
        print(r)

def greedy_algorithm():
    """
    그리디(Greedy) 기법은 딱 정해진 공식이 있는 건 아님.
    여러 개의 턴으로 쪼개어 동작하는 시뮬레이션 환경에서,
    각 턴마다 '당장 가장 유리해 보이는 선택'을 수행하는 방식.

    전역 최적해를 절대 보장하지 않음.
    매우 근시안적인 알고리즘이며, 보통 근사해(Approximation)를 제공.

    그럼에도 현업에서 자주 쓰임.
    - 꼭 최적해가 필요 없는 경우
    - 문제 구조가 단순하거나, 영향도가 크지 않은 경우

    통상적으로 개발자 자기가 짠 알고리즘이 뭔가 답은 내는데 이론적으로 최적해를 보장 안하거나
    이 알고리즘이 최적해인지 보장하는걸 따지기 귀찮을때
    "그리디 알고리즘" 이라고 표현해서 반영함. 

    나중 가면 A*, 다익스트라, 프림, 크루스칼 등
    전체 맵 또는 전체 상태 공간을 고려해 최적화를 보장하는 알고리즘을
    다루게 될 예정.
    """
    # 그리디 기법을 이용한 Baby gin 문제 풀이
    num = 112233 
    c = [0] * 12

    for i in range(6):
        c[num % 10] += 1
        num //= 10

    i = 0
    tri = run = 0
    while i < 10:
        if c[i] >= 3: # count값이 3개 이상이면 triplet
            c[i] -= 3 # 요소 삭제
            tri += 1  # 트리플랫 변수 증가
        
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사. 카운트 변수 왼편(작은수)부터 접근하기 때매 뭐 따질거 없음)
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1        
            run += 1
            continue # run 도달하면 컨티뉴
        i += 1 
    if run + tri == 2 : print("Baby Gin")
    else: print("Lose")
    """
    이 코드가 왜 그리디인가? 
    
    1. 더 이상 탐색할 것이 없어도 계속 탐색함
    112233 이란 값을 넣으면 run 두번 카운트 하고난 후로는 리스트가 텅 비기 때매 더 이상 연산을 할 이유가 없으나
    계속해서 i를 갱신하며 텅 빈 리스트를 순회하며 조건문을 비교함. 
    """



if __name__ == "__main__":
    
    # bubble_sort()
    # counting_sort()
    # greedy_algorithm()

    pass

