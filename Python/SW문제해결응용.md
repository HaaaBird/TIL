# 1. 진법
- 2진수, 8진수, 10진수, 16진수
  - 10진수: 사람이 사용하는 진수
  - 2진수: 컴퓨터가 사용하는 진수
  - 8진수, 16진수: 2진수를 가독성 있게 표현하기

| 2진수 | 8진수 | 10진수 | 16진수 |
| --- | --- | --- | --- |
| 1010 1000 | 250 | 168 | A8 | 

- 왜 16진수를 쓰는가?
  - 2진수 -> 10진수로 하면 **사람은 이해 하는데** 컴퓨터가 인식하긴 느림
## 1.1 구현
- 10진수를 다른 진법으로 바꾸어보자
- 원하는 타 진법의 수로 나누어준 뒤 나머지를 거꾸로 읽음
- 2진법 예제 149 -> b(10010101)
| 나눌 숫자 | 수 | 나머지 |
| ---- | ---- | ---- |
| 2 | 149 | 1 |
| 2 | 74 | 0 |
| 2 | 37 | 1 |
| 2 | 18 | 0 |
| 2 | 9 | 1 |
| 2 | 4 | 0 |
| 2 | 2 | 0 |
| 2 | 1 |  |
```python
hex_map = {
    0:0,1:1,2:2,3:3,4:4,5:5,
    6:6,7:7,8:8,9:9,10:"A",11:"B",
    12:"C", 13:"D", 14:"E", 15:"F",
}
hex_map_reverse = {
    "0":0, "1":1, "2":2, 3:3, "4":4, "5":5, "6":6, 7:7,
    "8":8, "9":9, "A":10, "B":1,"C":12, "D":13, "E":14, "F":15,
}

def decimal_to_another(n, m):
    b_num = []

    while n > 0:
        remain = hex_map[n % m]
        b_num.append(remain)
        n = n // m
    return list(reversed(b_num))

def another_to_decimal(a_num_str, formation):
    pow = 0
    decimal = 0
    for s_char in reversed(a_num_str):
        decimal += hex_map_reverse[s_char] * (formation ** pow)
        pow += 1
    return decimal

print(*decimal_to_another(28, 16)) # 1 C
print(hex(28)) # 0x1c
print(another_to_decimal("1C", 16)) # 28
```

# 2. 완전탐색
## 2.1 반복과 재귀
- 반복과 재귀는 유사한 작업을 수행한다.
- 반복은 수행하는 작업이 완료될 때 까지 계속 반복한다
  - 루프(for while 구조)
  - **반복문은 코드를 n 번 반복 가능**
- 재귀는 주어진 문제의 해를 구하기 위해 동일함녀서 더 작은 문제의 해를 이용하는 방법
  - 하나의 큰 문제를 해결할 수 있는(해결하기 쉬운) 다 작은 문제로 쪼개고 결과들을 결합
  - 재귀호출은 n중 반복문과 동일한 효과
```python
# 1,2,3으로 만들 수 있는 두 자릿수 만들기
for i in range(1,4):
    for j in range(1,4):
        print(i, j)
# 중첩 for 문을 방지해야 한다면 재귀를 써야 한다.

def run(level):
    if level == N:
        print(path)
        return
    for i in range(1, N+1):
        path.append(i)
        run(level + 1)
        path.pop()
        




```
## 2.2 순열

## 2.3 완전탐색
## 2.4 연습 문제
## 2.5 실습 문제