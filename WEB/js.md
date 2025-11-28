# 1. 변수
## 1.1 변수 작성 규칙
- 식별자(변수명) 작성 규칙
  - 반드시 문자, $, _ 시작
  - 대소문자 구분
  - 예약어 사용 불가(for, if 등)
  - 의미가 드러나는 이름을 사용해 데이터의 의미를 명확히 설명(userName, phoneNumber)
- 식별자(변수명)Naming Convention
  - 카멜 케이스(camelCase)
    - 변수, 객체, 함수에 사용
  - 파스칼 케이스(PascalCase)
    - 클래스, 생성자에 사용
  - 대문자 스네이크 케이스(SNAKE_CASE)
    - 상수(constants)에 사용
## 1.2 변수 선언 키워드
- 1. let
  - 재할당이 필요한 변수를 선언할 때 사용
- 2. const
  - 재할당이 불가능한 상수를 선언할 때 사용
- 3. var
  - 재선언/재할당 가능, 다만 현재는 호이스팅 문제로 사용을 권장하지 않음

- let
  - 블록 스코프(block scope)를 가지는 지역 변수를 선언
    - 재할당 가능
    - 재선언 불가능
```javascript
let number = 10 // 1. 선언 및 초기값 할당
number = 20  // 2. 재할당
let number = 40 // 3. 재선언 불가능이라 이거 하면 오류남
```
- const
  - 블록스코프를 가지는 지역 변수를 사용
    - 재할당 불가능
    - 재선언 불가능
```javascript
const number = 10 // 1. 선언 및 초기값 할당
number = 20 // 2. 재할당 불가능 오류남
const number = 30 // 3. 재선언 불가능 오류남
```
- 블록 스코프(block scope)
  - if, for 함수 등의 중괄호 내부를 가리킴
  - 블록스코프를 가지는 변수는 블록 바깥에서 접근 불가
```javascript
let x = 1
if (x == 1){
    let x = 2
    console.log(x) // 블록 안쪽에서 지역변수 x가 새로 선언. 2 출력
}
console.log(x) // 블록 밖에 있는 x를 사용
```
- 어떤 변수 선언 키워드를 사용해야 할까?
  - **const를** 기본으로 사용할 것
    - 코드의 의도 명확화
      - 해당 변수가 재할당되지 않을 것임을 명확히 표현
      - 개발자들에게 변수의 용도와 동작을 더 쉽게 이해할 수 있게 해줌
    - 버그 예방
      - 의도치 않은 변수 값 변경으로 인한 버그를 예방
      - 큰 규모의 프로젝트나 팀 작업에서 중요
    - 필요한 경우에만 let으로 전환(재할당이 필요한 경우)
      - let을 사용하는 것은 해당 변수가 의도적으로 변경될 수 있음을 명확히 나타냄
      - 코드의 유연성을 확보하면서도 const의 장점을 최대 활용 가능
# 2. DOM
- 웹 브라우저에서의 JavaScript 
  - 웹 페이지에서 동적인 기능을 담당
1. HTML script 태그
```html
<body>
    <script>
        console.log('hello')
    </script>
</body>
```
2. js확장자 파일
```html
// hello.js
<body>
    <script src="hello.js"></script>
</body>
```
## 2.1 문서 구조
- Document Structure
  - HTML 문서는 여러 상자가 중첩된 구조로 볼 수 있음
  - 브라우저가 문서를 표현하기 위해 사용하는 데이터 구조는 우측 이미지와 같은 모양
  - 각 상자는 객체이며 개발자는 이 객체와 상호작용하여 어떤 HTML 태그를 나타내는지, 어떤 콘텐츠가 포함되어 있는지 등을 알아낼 수 있음
  - 이 표현을 객체 모델(Document Object Model), DOM이라고 부름
- DOM(Document Object Model)
  - 웹 페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
  - 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함
- DOM API
  - 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작할 수 있도록 페이지 요소들을 객체 형태로 제공하며 관련된 다른 메서드(Method)도 함께 제공
  - HTML 구조와 내용을 조작하는 명령어 모음
## 2.2 Document 객체
- 웹 페이지를 나타내는 DOM트리 최상위 객체
- HTML 문서의 모든 콘텐츠에 접근하고 조작할 수 있은 진입점
- DOM에서 모든 요소, 속성, 텍스트는 하나의 객체
- 모두 document 객체의 하위 객체로 구성됨
## 2.3 DOM Tree
- HTML 태그를 나태나는 elements의 node는 문서의 구조를 결정
- 이들은 다시 자식 node를 가질 수 있음(ex: document.body)
- DOM 핵심
  - 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에에서 접근하고 조작할 수 있는 방법을 제공하는 API

# 3. DOM 선택
- 웹 페이지를 동적으로 만들기 == 웹 페이지를 조작하기
  - 조작 순서
    - 1. 조작하고자 하는 요소를 선택(또는 탐색)
    - 2. 선택된 요소의 콘텐츠 또는 속성을 조작
## 3.1 선택 메서드
- document.querySelector(selector)
  - 요소 한 개 선택
  - 제공한 선택자(selector)와 일치하는 첫 번째 요소를 하나 선택
  - 제공한 선택자를 만족하는 첫 번째 element 객체를 반환(없으면 null)
- document.querySelectorAll(selector)
  - 요소 여러개 선택
  - 제공한 선택자와 일치하는 여러 element를 선택
  - 제공한 선택자를 만족하는 NodeList를 반환
# 4. DOM 조작
- 1. 속성(attribute) 조작
  - 1.1 클래스 속성 조작
  - 1.2 일반 속성 조작
- 2. HTML 콘텐츠 조작
- 3. DOM 요소 조작
- 4. 스타일 조작
## 4.1 속성 조작
- 1. 클래스(Class)속성 조작
  - 스타일링 및 상태 제어를 위한 클래스 목록을 동적으로 추가/제거
- 2. 일반 속성(Attribute)조작
  - id, href 등 요소의 모든 HTML 속성 값을 직접 설정/조회
- 클래스 속성 조작
  - classList property
    - 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
  - classList 메서드
    - element.classList.add()
      - 지정한 클래스 값을 추가
    - element.classList.remove()
      - 지정한 클래스 값을 제거
    - element.classList.toggle()
      - 클래스가 존재한다면 제거하고 false를 반환(존재하지 않으면 클래스를 추가하고 true를 반환)
- 일반 속성 조작 메서드
  - Element.getAttribute()
    - 해당 요소에 지정된 값을 반환(조회)
  - Element.setAttribute(name, value)
    - 지정된 요소의 속성값을 설정
    - 속성이 이미 있으면 기존 값을 갱신(그렂히 않으면 지정된 이름과 값으로 새 속성이 추가)
  - Element.removeAttribute()
    - 요소에서 지정된 이름을 가진 속성을 제거
## 4.2 HTML 콘텐츠 조작
- textContent property
  - 요소의 텍스트 콘텐츠를 표현
- html 콘텐츠 조작 실습
```javascript
const h1Tag = document.querySelector('.heading')
console.log(h1Tag.textContent)
```
## 4.3 DOM 요소 조작
- document.createElement(tagName)
  - 작성한 tagName의 HTML 요소를 생성하여 반환
- Node.appendChild()
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
  - 추가된 Node 객체를 반환
- Node.removeChild()
  - DOM에서 자식 Node를 제거
  - 제거된 Node를 반환
## 4.4 Style 조작
- style property
  - 해당 요소의 모든 style속성 목록을 포함하는 속성
# 5. 참고
# 5.1 DOM 속성 확인 Tip
- 개발자도구 - Elements - Properties
- 선택한 해당 요소의 모든 DOM 속성 확인 가능
# 5.2 용어 정리
- Node
  - DOM의 기본 구성 단위
  - DOM트리의 각 부분은 Node라는 객체로 표현됨
    - Document Node -> HTML문서 전체를 나타내는 노드
    - Element Node -> HTML 요소를 나태내는 노드(예를 들어 <p>)
    - Text Node -> HTML 텍스트(Element Node 내의 텍스트 컨텐츠를 나타냄)
    - Attribute Node -> HTML 요소의 속성을 나태나는 노드
- NodeList  
  - DOM 메서드를 사용해 선택한 Node의 목록
    - 배열과 유사한 구조
    - index로만 각 항목에 접근 가능
    - JavaScript의 배열 메서드 사용 가능
    - querySeletcorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음
      - DOM이 나중에 변경되더라도 이전에 이미 선택한 NodeList값은 변하지 않음
- Element
  - DOM 트리에서 HTML의 요소를 나태내는 특별한 유형의 Node
    - Node의 하위 유형
    - 예를 들어 <p>, <div>, <span>, <body> 등의 HTML 태그들이 Element 노드를 생성
    - Node의 속성과 메서드를 모두 가지고 있으며 추가적으로 요소 특화된 기능
      - className, innerHTML, id 등 등을 가지고 있음
    - 모든 Element는 Node지만, 모든 Node가 Element인 것은 아님
- Parsing
  - 브라우저가 문자열을 해석해 DOM Tree로 만드는 과정(구문 분석, 해석)
# 5.3 호이스팅
- 변수 선언문이 코드의 최상단으로 끌어올려지는듯한 현상
  -  var로 선언된 변수는 선언 위치와 상관없이 최상단에 선언된것 처럼 동작, 할당 전까진 undefined 값을 가짐
```javascript
console.log(name) // undifined 
var name = '홍길동' // 선언, 할당
// 위 코드랑 똑같이 동작
var name
console.log(name) // undifiend
var name = '홍길동'
```

# 1. 데이터 타입
- 원시 자료형(Primitive type)
  - 값 자체가 변수에 직접 저장되는 자료형
  - 불변(immutable)이며, 변수 간 할당 시 값이 복사
  - Number, String, Boolean, null, undefined
- 참조 자료형(Reference type)
  - 데이터가 저장된 메모리의 주소가 변수에 저장되는 자료형
  - 가변(Mutable)이며, 변수 간 할당 시 주소가 복사
  - Objects(Object, Array, Function)
- 원시 자료형
  - 변수에 할당될 때 값이 복사됨
  - 변수간에 서로 영향 x
```javascript
const a = 'bar'
console.log(a) //bar

a.toUpperCase() // a를 대문자로 바꾸는건데 안바뀜. 왜냐면 이건 메서드라 반환하는건데 변수에 할당된게 아님.
console.log(a) // bar

let a = 10
let b = a
b = 20
console.log(a) // 10
console.lob(b) // 20
```
- 참조 자료형
  - 객체를 생성하면 객체의 메모리 주소를 변수에 할당
  - 변수 간에 서로 영향을 미침
```javascript
const obj1 = {name:'Alice', age:2000}
const obj2 = obj1

obj2.age = 1
console.log(obj1.age) // 40
console.log(obj2.age) // 40
```
## 1.1 원시 자료형
- Number
  - 사칙연산 및 나머지 연산 가능
  - 문자열과 + 연산 시 숫자가 문자열로 자동 형 변환되어 연결
  - 정수와 실수 구분이 없고 모든 숫자를 단일 타입으로 처리
```javascript
const a = 13
const b = -5
const c = 3.14
const d = 2.998e8 // 2.998 * 10^8 -> 299,800,000
const e = Infinity
const f = -Infinity
const g = NaN // Not a Number
```
- String
  - 텍스트 데이터를 표현하는 자료형
  - + 연산자를 사용해 문자열끼리 결합
  - 뺄셈, 곱셈 나눗셈 불가
```javascript
const firstName = 'Tony'
const lastName = 'Stark'
const fullName = firstName + lastName
```
- Template literals(템플릿 리터럴)
  - 내장된 표현식을 허용하는 향상된 문자열 작성 방식
  - BackTick(``, 백틱)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할수도, JavaScript의 변수를 문자열 안에 바로 연결할 수 있음
  - 표현식은 $와 중괄호{expression} 표기
  - ES6+부터 사용 가능
```javascript
const age = 100
const message = `홍길동은 ${age} 세 입니다.`
console.log(message) // 홍길동은 100세 입니다.
```
- null
  - 프로그래머가 의도적으로 '값이 없음' 을 나타낼 때 사용
```javascript
let a = null
console.log(a) // null
```
- undefined
  - 시스템이나 javascript 엔진이 값이 할당되지 않음 을 나타낼 때 사용
```javascript
let b
console.log(b) // undifined
```
- Boolean
  - 참과 거짓을 나타내는 논리적인 자료형
  - 조건문 또는 반복문에서 Boolean 이 아닌 데이터 타입은 자동 형 변환 규칙에 따라 true 또는 false로 변환
| 데이터 타입 | false | true |
| ------ | ------ | ------ |
| undifined | 항상 false | x |
| null | 항상 false | x |
| Number | 0, -1, NaN | 나머지 모든 경우 |
| String | ''(빈 문자열) | 나머지 모든 경우 |

# 2. 연산자
- 할당 연산자
  - 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
  - 단축 연산자 지원

```javascript
let a = 0
a += 10
console.log(a) // 10

a -= 3
console.log(a) // 7

a *= 10
console.log(a) // 70

a %= 7
console.log(a) // 0
```
- 증가 & 감소 연산자
  - 증가 연산자 ++
    - 피연산자를 증가(1더함) 시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환
  - 감소 연산자 --
    - 피연산자를 1뺌 시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환
  - 코드 가독성 때매 a += 1 같은 명시적 표현 더 권장
```javascript
let x = 3
const y = x++ //후치연산자. x를 y에 대입하고 하나 올림
console.log(x, y) // 4 3

let a = 3
const b = ++a // 전치연산자 a에 1을 더하고 b에 할당
console.log(a, b) // 4 4
```
- 동등 연산자(==)
  - 두 피연산자가 같은 값으로 평가되는지 비교한 후 Boolean 값을 반환
  - 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
  - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
```javascript
console.log(1 == 1) // true
console.log('hello' == 'hello') // true
console.log('1'== 1) // true
cosole.log(0 == false) // true
```
- 일치 연산자(===)
  - 두 피연산자의 값과 타입이 모두 같은 경우에 true반환
  - 엄격한 비교, 암묵적 타입변환 없음
  - 왠만하면 이거 쓰면 됨
```javascript
console.log(1===1) // true
console.log('1' === 1) // false
console.log(0 === false) // false
```
# 3. 조건문
- if
```javascript
const name = 'customer'
if (name === 'admin') {
  console.log('관리자 하이')
} else if (name === 'customer') {
  console.log('고객 하이')
}
```
- 삼항 연산자
  - 간단한 조건부 로직을 간결하게 표현할 때 유용
  - 복잡한 로직이나 대다수의 경우엔 가독성이 떨어질 수 있음으로 적잘한 사용에서 사용할 것
  - condition
    - 평가할 조건(true, false)
  - expression1
    - 조건이 true일 경우 반환
  - expression2 
    - 조건이 false일 경우 반환할 값 또는 표현식
```javascript
const age = 20
const message = (age > 19) ? '성인' : '미성년자'
console.log(message) // 성인

```
# 4. 반복문
- 반복문 종류
  - while
  - for 
  - for ... in
  - for ... of
- while
  - 조건문이 참이면 문장을 계속해서 수행
```javascript
let i = 0
while (i < 6) {
  console.log(i)
  i += 1
}
```
- for
  - 특정한 조건이 거짓으로 판별될 때 까지 반복
```javascript
for (let i=0; i < 6; i++) {
  console.log(i)
}
```
## 4.1 for ... in
- 객체의 열거 가능한(enumerable) 속성(property)의 키(key)에 대해 반복
```javascript
const fruits = { a:'apple', b:'banana'}
for (const property in fruits) {
  console.log(property) // a, b
  console.log(fruits[property]) // apple, banana
}
```
## 4.2 for ... of
- 반복 가능한(iterable) 객체(배열, 문자열)의 값에 대해 반복
```javascript
const numbers = [0, 1, 2, 3]
for (const number of numbers) {
  console.log(number) // 0, 1, 2, 3
}
```
## 4.3 for ... in 과 for ... of
- for...in
```javascript
// Array
const arr = ['a', 'b', 'c']
for (const elem in arr) {
  console.log(elem) // 0 1 2
}

// Object
const capitals = {
  korea:'서울',
  japan:'도쿄',
  china:'베이징',
}
for (const capital in capitals) {
  console.log(capital) // korea, japan, china
}
```
- for ... of
```javascript
const arr = ['a', 'b', 'c']
for (const elem of arr) {
  console.log(elem) // a b c
}

// Object
const capitals = {
  korea:'서울',
  japan:'도쿄',
  china:'베이징',
}
for (const capital of capitals) {
  console.log(capital)
  // TypeError: capitals is not iterable 
}
```
- 배열 반복과 for ... in
  - 객체의 관점에서 보면 배열의 인덱스도 '정수 형태의 이름을 가진 열거 가능한 속성'
  - for ... in 은 정수가 아닌 이름과 속성을 포함하여 열거 가능한 모든 속성을 반환
  - 내부적으로 for ... in 은 배열의 반복자가 아닌 속성 열거를 사용하기 때문에 특정 순서에 따라 인덱스를 반환하는 것을 보장할 수 없음
    - 따라서 for in은 인덱스의 순서가 중요하면 사용하지 않음
    - 배열에서는 for문, for...of를 사용
  - 객체 관점에서 배열의 인덱스는 정수 이름을 가진 속성이기 때문에 인덱스가 출력됨(순서 보장x)
- 반복문 사용 시 const 사용 여부
  - for 문
    - for(let i = 0; i < arr.length; i++) {} 의 경우에 최초 할당한 i를 재할당 하며 사용하기 때문에 const 를 사용하면 에러 발생
  - for ... in for ... of 
    - 재할당이 아니라 매 반복마다 다른 속성 이름이 변수에 지정되는 것으로 const 를 사용해도 에러 안남
    - 단 const 특징에 따라 블록 내부에서 변수를 수정할 수 없음
# 5. 함수
- 참조 자료형에 속하며 모든 함수는 Function object
## 5.1 함수 정의 
```javascript
function name ([param[, param, [..., parma]]]) {
  statements
  return value
}
```
- function 키워드
- 함수의 이름
- 함수의 매개변수
- 함수의 body 를 구성하는 statements
- return 문이 없거나 return 뒤에 값이 없으면 함수는 undefined를 반환
- 함수 정의 방법 2개
  - 선언식 (function declaration)
  - 표현식(function expression)
```javascript
// 선언식
function funcName() {
  statements
}
function add(num1, num2) {
  return num1 + num2
}
add(1,2) // 3
// 표현식
const funcName = function() {
  statments
}
const sub = function(num1, num2) {
  return num1 - num2
}
sub(2, 1) //1
```
- 함수 선언식 특징
  - 호이스팅 됨
  - 코드의 구조와 가독성 부분에서 강점
- 함수 표현식 특징
  - 호이스팅 되지 않음
  - 변수 선언만 호이스팅, 함수 할당은 실행 시점
- 함수 이름이 없는 익명 함수 사용 가능
```javascript 
sub(2, 1) // ReferenceError: Cannot access 'sub' befor initialization

const sub = function(num1, num2) {
  return num1- num2
}
```
- 함수 표현식을 권장하는 이유
  - 예측 가능성
    - 호이스팅 영향이 없음. 코드 실행 흐름이 더 명확하게 예측 가능
  - 유연성
    - 변수에 할당됨으로 함수를 값으로 다루기 쉬움
  - 스코프 관리
    - 블록 스코프를 가지는 let이나 const와 함께 사용하여 더 엄격한 스코프 관리 가능
## 5.2 매개변수
1. 기본 함수 매개 변수
2. 나머지 매개 변수
- 1. 기본 함수 매개변수(Default function parameter)
  - 함수 호출 시 인자를 전달하지 않거나 undefined를 전달할 경우, 지정된 기본값으로 매개변수를 초기화
```javascript
const greeting = function(name = 'Alice') {
  return `Hi ${name}`
}
greeting() // Hi Alice
```
- 나머지 매개변수(Rest paratmeter)
  - 정해지지 않은 개수의 인자들을 배열로 모아서 받는 방법
  - 작성 규칙
    - 함수 저으이 시 나머지 매개변수는 하나만 작성할 수 있음
    - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함
```javascript
const myFunc = function(param1, param2, ...restParams) {
  return [param1, param2, restParams]
}
console.log(myFunc(1,2,3,4,5)) // [1,2,[3,4,5]]
console.log(myFunc(1,2)) // [1,2,[]]
```
- 매개변수와 인자 개수가 불일치 할 때
  - 누락된건 undefined로 할당
```javascript
const theeArgs = function(param1, param2, param3) {
  return [param1, param2, param3]
}
threeArgs() // [undefined, undefined, undefined]
```
- 인자가 초과하면?
  - 초과 입력한건 사용하지 않음
```javascript
const noArgs = function() {
  return 0
}
noArgs(1) // 0
```
## 5.3 spread syntax
- 전개 구문
- 배열이나 문자열처럼 반복 가능한(iterable)항목들을 개별 요소로 펼치는 것
- 전개 대상에 따라 역할이 다름
  - 배열이나 객체의 요소를 개별적인 값으로 분리하거나 다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가하는 등
- 전개 구문 활용처
  - 1. 함수와의 사용
    - 함수 호출 시 인자 확장
    - 
## 5.4 화살표 함수 표현식

# 6. 참고
## 6.1 NaN 예시
## 6.2 null & undefined
## 6.3 화살표 함수 심화  

기존까진 form 기능을 통해 서버에 API를 날렸는데
이제는 axios 를 통해서 서버에 요청을 날릴거임.

form 을 가져올 수 있는 id를 지정하고, 