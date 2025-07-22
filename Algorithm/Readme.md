
- 마지막에 안하고 간거: bj_1244 적다말고, 나머지도 다 덜적음.

# 알고리즘 
## 이론 정리
### 1. Brute force 알고리즘
작성일자: 2025-07-21
- 무식한 힘으로도 해석 가능. 완전탐색 알고리즘
- 관련문제 백준 [백준 2669](bj_2635.py)
#### 1.1 개요
- 알고리즘의 가장 기본적인 접근 방법은 해가 있을 것으로 예상되는 영역을 모두 탐색하는것. 브루스 포스가 이런 알고리즘



## 문제풀이
### 스위치 끄고 켜기 bj_1244.py
- 작성일자: 2025-07-21
- [백준 1244](https://www.acmicpc.net/problem/1244)
- [내 코드](bj_1244.py)
- 남자는 배수 배열 뒤집기.
    - ```python
        for i in range(switch_idx, len(switch_list), switch_idx):
            switch_list[i] = reverse_swicth(switch_list[i])
      ```
    - 배수 단위로 range 범위 지정해주고(시작위치, 끝, step을 idx 번호로) 해당하는 부분 다 반전하도록 로직 구성
- 여자는 idx 값 대칭 찾기
    - 중심위치를 잡고, 그 위치에서 -1, +1 되는 값을 본다
    - 그 값이 동일하지 않거나 범위에서 벗어나면 break
    - 같으면 while 탈출하지 않고 범위 계속 탐색
    - break 되어 나오면 범위 전체 다 한방에 뒤집기
    ```python
        left = switch_idx
        right = switch_idx
        while True:
            l = left - 1
            r = right + 1
            if l <= 0 or r > switch_num:
                break
            elif switch_list[l] != switch_list[r]:
                break
            left = l
            right = r
        for i in range(left, right+1):
            switch_list[i] = reverse_swicth(switch_list[i])
    ```

    - 해맨 부분
        - 너무 복잡하게 하려고 했다. 결국 범위를 잡아서 한번에 반복문을 돌리는게 제일 똑똑한 방법인데, 그냥 구간 적용해서 한번 넘어갈때마다 반전시키려고 했던걸로. 
        - 변수명 너무 길게 했다. 그냥 짧게 이해갈수 있게 기호로 표시하는게 훨씬 덜 햇갈린다.
        - 틀린코드
        ```python
        else: # 여자. idx 값 중심으로 대칭 구간 찾아서 전체 전환
        add_range = 1
        center_change = False
        while True:
            left_ = switch_idx - add_range
            right_ = switch_idx + add_range
            
            if left_ <= 0 or right_ > len(switch_list)-1:
                break
            elif switch_list[left_] != switch_list[right_]:
                break
            ### 여기까진 맞는데
            else: # 여기서 바보짓. 그냥 한번에 범위잡아서 반전시켜야 하는데, 이걸 이상하게 해서 틀림.
                switch_list[left_] = reverse_swicth(switch_list[left_])
                switch_list[right_] = reverse_swicth(switch_list[right_])
                if center_change == True: # center_change 도 필요없는 값
                    pass
                else:
                    switch_list[switch_idx] = reverse_swicth(switch_list[switch_idx])
                    center_change = True
                add_range = add_range + 1
        ```
### 3자릿수 곱셈 bj_2588.py
- 작성일자: 2025-07-21
- [백준 1244](https://www.acmicpc.net/problem/2588)
- [내 코드](bj_2588.py)
- 큰 내용이 있는 문제는 아님.
- 다만 풀때, 변수 타입 지정이 별도로 없는 파이썬 환경 주의해서 풀 것.
```python
reversed(list) # <- 이 함수 기억하고 있을 것 알고리즘 할 때 자주 쓸 듯.
```
### 종이자르기 bj_2628
- 작성일자: 2025-07-22
- [백준 1244](https://www.acmicpc.net/problem/2628)
- [내 코드](bj_2628.py)
- 문제 이해가 중요.
- 실제 가상 공간에서 종이 자르는 그런 계산 할 필요 없음
    - 종이자르는 행동이 가져오는 수학적 특징만 고려해도 문제는 풀림. 

- 종이자르는 행동이 무엇이냐?
    - 종이자르는 행동이 중간에 끊어지지 않음. 무조건 끝까지 다 짤림.
    - 그러면 x 축에서 자른 가장 긴 구간, y축에서 나온 가장 긴 구간이 나오게 되는거고, 이 두 구간을 곱한게 가장 큰 종이.
    - 그리고, 잘리는 포인트는 계속 변한다 하더라도, 결국 순서대로 정렬이 필요.

### 수 이어가기 bj_2635
- 작성일자: 2025-07-22
- [백준 1244](https://www.acmicpc.net/problem/2635)
- [내 코드](bj_2635.py)
- 첫 번째 수가 주어지고, 두번째 수는 0~첫번째 수
- 세번째부터는 1-2값이 들어가고, 이 길이가 가장 긴 조합을 찾아내는 문제.
    - 브루스 포스 알고리즘이라 분류가 들어가긴 하는데, 사실 엄격하게 들어간건 아니고 그냥 일반적인 완전탐색 문제라고 생각해도 큰 차이는 없는듯. 
- 배열 구조와 인덱싱에 대한 이해만 있어도 금방 풀었음.

### 직사각형 네개의 합집합의 면적 구하기 bj_2669
- 작성일자: 2025-07-22
- [2669](https://www.acmicpc.net/problem/2669)
- [내 코드](bj_2669.py)
- 문제설명
    - 리스트 4개가 넘어오고, 각각 직사각형을 만들 수 있는 최소정보가 담겨있음.
    - 직사각형의 위치가 겹치기도 하니, 이에 대한 전체면적 구하는 문제
- 풀이
    - 0으로 된 2차원 배열공간을 만들고, 직사각형이 들어가는 위치는 1을 채운다
    - 그 배열공간 안에 있는 1의 수를 센다
- 특이사항
    - 리스트 만들때 리스트 컴프리핸션 쓰면 멋있어 보인다.
    - 2차원 배열에서 좌표값은 Y, X 로 구성된다. 리스트 안에 리스트를 넣는거라 반대다. 
    ```python
    array_size = 100
    array = [[0]*array_size for _ in range(array_size)]

    # 이건 아래 식과 같다.
    array = []
    for i in range(array_size):
        array[i] = [0]*array_size
    ```
    - 결국 사고력 싸움. 이 문제를 보고, 2차원 공간을 만들어 푼다는 개념만 나오면 금방 품.

### 주사위 쌓기 bj_2116
- 작성일자: 2025-07-22
- [2669](https://www.acmicpc.net/problem/2116)
- [내 코드](bj_2116.py)
- 문제설명. 랜덤한 수량(최대 3만개)의 주사위를 쌓는거. 주사위의 눈금 위치는 합쳐서 7이 되는 일반적인 주사위가 아니라, 랜덤한 값 순서대로 제공되지만, 서로 짝이 맞추어지는 위치값은 제공됨.
- 1번 주사위의 눈금값 == 2번 주사위의 눈금값이 항상 일치해야 함. 
- 전역변수 위치 잘 볼껏. nameError