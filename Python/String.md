# 1. 문자열
## 1.1 코드체계
- 문자에 대응되는 숫자를 정함
  - A를 메모리에 저장하려면? 메모리는 숫자밖에 못 다룸.
  - 그러면 특정 숫자를 글자에 맵핑시켜 두면 됨.
- 대표적 코드 체계 ASCII(American Standard Code for Information Intercharge)
  - 8bit 단위 전송인데 7bit만 씀. 1개는 패러티 라 부르는 오류 검출자.
  - 128문자 중 33개의 출력 불가한 제어 문자와 공백, 95개의 출력 가능한 문자로 이루어짐
- 확장 아스키 코드 -> 패러티도 날리고 8비트 모두 사용
- 유니코드 - 미국 외 다른 나라에서도 쓰려고 만든거. 이모지도 유니코드
  - 기본 32비트 체계인데 21비트까지 정보를 담음. 나머지는 비어 있음. 
  - 16진법을 기본으로 쓰는 체계
## 1.2 문자열
- 문자들이 순서대로 나열된 데이터
- 문자열의 분류
  - Length-Controlled 문자열
    - 문자열의 길이정보를 함께 저장해서 그 길이만큼 문자 데이터를 읽는 방식
    - Java, Python, 네트워크 패킷에 사용됨
  - Delimited 문자열
    - 문자열의 끝을 나타내는 특정한 구분자(Delimiter)가 있어 구분자가 나올때 까지 문자열로 인식함
| Length-controlled | 5 | H | E | L | L | O |
| --- |--- |--- |--- |--- |--- |--- |
| Delimited | H | E | L | L | O | \0 |
- 파이썬의 str 클래스
- 길이 외 다른 정보도 저장
  - pyObject_HEAD: 모든 python 객체가 상속하는 공통 구조
  - length: 문자열 길이
  - hash: 문자열의 hash값으로 딕셔너리 키로 쓸때 사용됨
  - interned: 같은 문자열을 관리하는 플래그
  - kind: 문자열 인코딩의 크기
  - data: 문자열이 저장된 실제 메모리 주소를 가리키는 포인터
  - 그럼 아래처럼 class 선언 되어 있느냐? 아님
```python
# 예상
class str():
    def __init__(self):
        self.length
        self.hash
        self.interned
        self.kind
        self.data
# 실제는 C로 선언된 걸 파이썬에서 가져다 쓰는 것이라 내부 파이썬에서 직접 그 구조를 확인할 수 없다.
# hash, length 등은 객체 생성 시 같이 세팅되므로 호출 시 시간복잡도 O(1)로 바로 얻을 수 있다.
```
- C언어에서 문자열
  - 문자열은 문자들의 **배열**형태로 구현된 응용 자료형
  - 문자배열에 문자열을 저장할 때 항상 마지막에 끝을 표시하는 null 문자 필요('\0').
    - char arr[] = "abc" // char ary[] = {'a', 'b', 'c', '\0'};
  - 문자열 처리에 필요한 연산을 함수 형태로 제공함
    - strlen(), strcpy(), strcmp()
- Java에서 문자열
  -  문자열 데이터를 저장, 처리해주는 클래스를 제공함
  -  String Class
     -  String str = "abc"; // 또는 String str = new String("abc")
  -  문자열 처리에 필요한 연산을 연산자, 메소드 형태로 제공함
     -  +, length(), replace(), split(), substring()
-  Python3 에서의 문자열
-  텍스트 데이터의 취급 방법이 통일되어 있음.
   -  python2 와 달리 바이트 배열 문자열과 Unicode구분이 없음
   -  유니코드 기반이라 어떤 언어나 기호도 동일한 방식으로 처리함
   -  문자열 기호
      -  '홑따옴표', "쌍따옴표", '''홑따옴표 3개''', """ """
   - 연산
     - + 연결(Concatenation)
       - 문자열 + 문자열 이어붙여주는 연산
       - 반복: 문자열 * 수 수만큼 문자열 반복
 - 문자열은 데이터 순서가 구본되는 시퀀스 자료형으로 분류됨.
   - 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있음
 - 문자열 클래스에서 제공되는 메소드
   - replace(), split(), isalpha(), find()
 - 문자열은 튜플과 같이 요소값을 변경할 수 없음(immutable)
```python
# 1. 인덱스를 사용할 수 있음
a = 'abc'
print(a[1]) # "b"

# 2. 요소값을 변경할 수 없음
b = 'abc'
b[1] = 'c' # //TypeError: 'str' object does not support item assignment
```
- C, Java, Python 문자열 차이
  - C는 ASCII로 저장. 한글 출력 가능하나 콘솔에서 다시 랜더링
  - java는 유니코드 utf=16, 2byte로 저장
  - python은 utf-8로
```C
char * name = "홍길동";
int count = strlen(name);
printf("%d", count) // 6이 출력
```
```java
String name = "홍길동";
System.out.println(name.length()); // 3이 출력
```
```python
name = "홍길동"
print(len(name)) # 3
```
- Python에서의 문자열 입력
  - input() 함수로 읽기

## 1.3 연습문제
## 1.4 연산
- 문자열 뒤집기
```python
# 문자열을 역순으로 재정의
s = "reverse this string"
s = s[::-1] # sgnirts siht esreveR

# 리스트로 변환 후 다시 문자열로
s = "abcd"
s = list(s)
s.reverse()
s = ''.join(s)
print(s) # dcba
```
- 회문
  - 기러기 토마토 스위스 해체해와 같이 똑바로 읽어도 거꾸로 읽어도 동일한 문장이나 낱말
  - 문자열 길이의 반만 비교하면 됨.
해 체 해 <- 문자열 길이 3, 3//2 -> 1 1회 반복
```python
def is_palindrome(txt):
    for i in range(len(txt)//2):
        if txt[i] != txt[len(txt) - i]:
            return False
    return True
```
- 문자열 비교
  -  == 연산과 is 연산
  -  == 는 값을 비교. is는 객체의 정체성을 비교. 같은 주소에 있는 객체인지를 비교
  -  == 는 내부적으로 __eq__() 메서드를 호출
```python
s1 = 'abc'
s2 = 'abc'
print(s1 == s2) # True
print(s1 is s2) # True 왜? interning. 아까 str 형 설명할때 나온 내용. 파이썬이 재사용성을 높이기 위해서 일정 문자들은 이미 만들어두고 그거 참조하게 함
h1 = "Hello World"
h2 = "Hello World"
print(h1 is h2) # False -> 띄어쓰기 들어가면 보통 interning이 깨짐

s3 = 'def'
s4 = s1 
s5 = s1[:2] + 'c' # ab + c
print(s4 == s5) # True s4는 s1이 참조하는 주소를 할당받은거고, s1의 주소에 있는 값끼리 비교라 True
print(s4 is s5) # False 객체 동일성이 다름.
```
- C 와 Java는?
  - C는 strcmp() 함수를 이용해 문자열의 내용을 비교
  - Java는 ==로 객체 주소(참조)를 비교. is연산자
  - equals()메서드로 내용을 비교 ==
- 사전에서의 순서 비교
  - 비교 연산자 사용. 유니코드를 이용해서 비교함
```python
def my_strcmp(s1, s2):
    if s1 < s2:
        return -1 # s1이 s2 보다 사전 순서상 앞
    elif s1 > s2:
        return 1 # s1이 s2보다 사전 순서상 뒤
    else:
        return 0 # 내용이 같음
```
- 문자열 숫자를 숫자로 변환
- 1. 문자열을 숫자로 변환하는 예시
```python
a = int(1,2,3)
b = float('3.14')
c = int('A0', 16) # 문자열 A0을 16진법으로 해석해 변환

# 2. 숫자를 문자열로 변환하는 예시
a = str(123)
b = str(3.14)
```
# 2. 패턴 매칭
## 2.1 고지식한 패턴 검색
- 고지식한 알고리즘 Brute Force
  - 단순한 방법
  - 본문 문자열을 처음부터 끝까지 순회하며 패턴 내의 문자열을 찾는 것
```python
target = list("TTAT")
arr = list("TTTTAACCA")

for i in range(0, len(arr) - len(target) + 1, 1):
  if arr[i:i+len(target)] == target:
    return True
return False
```
## 2.2 KMP 알고리즘
## 2.3 보이어-무어 알고리즘
## 2.4 문자열 암호화