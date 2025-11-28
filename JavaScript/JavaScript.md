# 1. DOM
## 1.1 문서 구조
## 1.2 Document 객체
## 1.3 DOM Tree

# 2. DOM 선택
## 2.1 선택 메서드
```javascript
document.querySelector("p") // 태그 선택자
document.querySelector(".box") // 클래스 선택자
document.querySelector("#title") //id선택자
document.querySelector("input[type='text']") // 속성 선택자
document.querySelector("ul li") // ul 안에 있는 첫 번째 li
```
- 쿼리셀렉터로 잡아오는건 엔트리 전체. <p>반갑습니다</p>
- 그렇기 때매 이후에 조작하는건 그 엔트리에 대한 조작

# 3. DOM 조작
## 3.1 속성 조작
- 속성은 결국 클래스에 대한 속성 조작고, 그 외에 대한 것으로 구분하여 조작한다.
1. 클래스 속성 조작
   1. 스타일링 및 상태 제어를 위한 클래스 목록을 동적으로 추가/제거
```javascript
const h1Tag = document.querySelector('.heading') // 해딩 클래스를 기준으로 엔티티를 잡아옴
h1Tag.classList.add('red') // class 에 red 속성을 추가. <h1 class="heading red">
h1Tag.classList.remove('red') // class 에서 red 속성을 제거 <h1 class="heading">
h1Tag.classList.togle('red') // 없으면 추가, 있으면 제거
```
2. 일반 속성 조작
   1. id, href등 요소의 모든 HTML속성 값을 직접 설정/조회
```javascript
const aTag = document.querySelector('a')
aTag.getAttribute('href') // href에 달린 값 출력
aTag.setAttribute('href', 'https:\\www.naver.com') // href 속성에 있는 값을 오른쪽걸로 변경
aTag.removeAttribute('href') // aTag에 할당된 엔티티의 href 속성을 제거
```
## 3.2 HTML 콘텐츠 조작
- 글자 수정 하기

```javascript
const h1Tag = document.querySelector('.heading')
h1Tag.textContent = '내용 수정'
```
## 3.3 DOM 요소 조작
- querySelector로 잡아온 요소의 하위에 무엇을 추가하거나
- 아니면 아예 엔티티를 만들어버리는 기능들

```javascript
const newH1Tag = document.createElement('h1') // h1태그를 가진 요소를 생성<h1></h1>
const newDivTag = document.createElement('div') // div 태그를 가진 요소 생성
newDivTag.appendChild(newH1Tag) // div 하위에 h1태그 만들어둔걸 달아줌
```
## 3.4 Style 조작

# 4. 참고
## 4.1 DOM 속성 확인 Tip
## 4.2 용어 정리
## 4.3 세미콜론
## 4.4 var
## 4.5 호이스팅


# 1. 이벤트
## 1.1 Input 이벤트
- 요소의 value(값)이 변경될 때 발생
- 붙여넣기에도 반응하는 유효성 검사 가능
## 1.2 Keyup Event
- 키보드가 눌렀다가 올라올 때
- 특정 키(예: Enter키)에 대해서만 반응



# 1. 비동기
- 프로그램의 실행 흐름이 순차적으로 진행
- 동기(Synchronous) 코드 예시
```javascript
console.log('작업 시작')
const syncTask = function() {
    for (let i=0; i<100000; i++) {
        // 반복 실행 동안 잠시 대기
    }
    return '작업 완료'
}
const result = syncTask()
console.log(result)
console.log('작업 시작')
```
- 비동기
  - 특정 작업의 실행이 완료될 때 까지 기다리지 않고 다음 작업을 즉시 실행하는 방식
- 예시
  - 메일을 보내면 받은 편지함으로 넘어오지만 실제론 보내진건 아님.
  - 웹페이지를 띄우면 먼저 처리되는 이미지 부터 뜸
- 비동기 코드 예시
```javascript
console.log('작업 1 시작')
const asyncTask = function (callBack) {
    setTimeout(() => {
        callBack('작업 완료')
    }, 3000)
}

asyncTask((result)=>{
    console.log(result)
})

console.log('작업 2 시작')
```
- synchronous 특징
  - 시작 순서대로 처리
  - 앞의 작업이 먼저 끝나야만 다음 작업 시작 가능
  - 장점
    - 단순하고 예측 가능한 흐름
  - 단점
    - 시간이 오래걸리는 작업이 실행되면 해당 작업이 끝날때 까지 프로그램 전체가 멈춤
    - 시스템 자원의 낭비
- Asynchronous 특징
- 병렬적 수행
- 당장 처리를 완료할 수 없는 작업들은 백그라운드에서 실행되며 빨리 완료되는 작업부터 처리
- 장점
  - 시간이 오래걸리는 작업을 백그라운드에 위임해 효율성 증가
  - 프로그램이 멈추지 않아 사용자 경험 향상
- 단점
  - 작업의 시작 순서와 완료 순서가 다를 수 있어 복잡한 흐름과 결과값을 처리해야함으로 코드 복잡
# 2. JavaScript 와 비동기
- Single Thread언어 JavaScript로 병렬 처리를 한다는건 뭘까?
## 2.1 JavaScript Runtime
- JavaScript는 Single Thread임으로 비동기 처리를 할 수 있도록 도와주는 환경이 필요
- JavaScript가 동작할 수 있는 환경(Runtime)
  - 브라우저
  - Node.js
- 브라우저 환경에서의 JavaScript 비동기 처리 관련 요소
- JavaScript Engine의 Call Stack
  - 코드가 실행되면 함수 호출이 순서대로 쌓이는 작업 공간
  - 기본적인 Javascript의 Single Thread 작업 처리
- Web API
  - 시간이 걸리거나 언제 실행될 지 모르는 비동기 작업들을 처리하는 곳
  - 브라우저에서 제공하는 runtime 환경
- Task Queue
  - Web API에서 처리가 완료된 작업들이 줄을 서서 기다리는 대기열
- Event Loop
  - Call Stack이 비어있는지 계속해서 확인하며 Task Queue에서 가장 오래된 작업을 콜스택으로 보내는 역할
  - 

# 3. Ajax
- 비동기적인 웹 어플리케이션 개발을 위한 기술
  - XMLHttpRequest 기술을 사용해 복잡하고 동적인 웹페이지를 구성하는 방식
  - 브라우저와 서버 간의 데이터를 비동기적으로 교환하는 기술
  - Ajax를 사용하면 페이지 전체를 새로고침 하지 않아도 동적으로 데이터를 불러와 화면을 갱신할 수 있음
  - Ajax의 X는 원래 XML이였는데 지금은 JSON도 가능
- Ajax 목적
  - 1. 비동기 통신
    - 웹 페이지 전체를 새로고침 하지 않고 서버와 데이터를 주고받음
  - 2. 부분 업데이트
    - 전체 페이지가 다시 로드되지 않고 HTML 페이지 일부 DOM만 업데이트
    - 페이지의 일부분만 동적으로 갱산할 수 있어 사용자 경험이 향상
  - 3. 서버 부하 감소
    - 필요한 데이터만 요청함으로 서버 부하를 줄일 수 있음
- XHR 객체
  - JavaScript를 사용해 서버에 HTTP 요청을 할 수 있는 객체
  - 웹 페이지의 전체 새로고침 없이도 서버로부터 데이터를 가져오거나 보낼 수 있음
- 기존 기술과 차이
  - 1. 클라이언트에서 form을 체우고 이를 서버에 제출
  - 2. 서버는 요청 내용에 따라 데이터 처리 후 새로운 웹페이지를 작성해 응답으로 전달
    - 결과적으로 모든 요청에 따라 새로운 페이지를 응답받기 때문에 계속해서 새로고침이 발생
    - 기존 페이지와 유사한 내용을 가진 경우에도, 중복된 코드를 다시 전송받아 대역폭을 낭비하게 됨
  - 1. XHR 객체 생성 및 요청
  - 2. 서버는 새로운 페이지를 응답으로 만들지 않고 필요한 부분에 대한 데이터만 처리 후 응답
    - 새로운 페이지를 받는 것이 아닌 필요한 부분 일부를 수정
    - 서버에서 처리되던 데이터 처리 일부분이 이제는 클라이언트쪽에서 처리됨.
- 이벤트 핸들러는 비동기 프로그래밍의 한 형태
  - 이벤트가 발생할 때 마다 호출되는 함수(콜백 함수)를 제공하는 것
  - HTTP요청은 응답이 올 때 까지의 시간이 걸릴 수 있는 작업이라 비동기, 이벤트 핸들러를 XHR 객체에 연결해 요청의 진행상태 및 최종 완료에 대한 응답을 받음.
## 3.1 Axios
- 브라우저와 Node.js 환경에서 모두 사용할 수 있는, Promise 기반의 HTTP클라이언트 라이브러리
- Axios 정의 및 특징
  - 클라이언트와 서버 사이에 HTTP 요청을 만들고 응답을 처리하는데 사용되는 자바스크립트 라이브러리
  - 서버와 HTTP요청 응답을 간편하게 처리할 수 있도록 도와주는 도구
  - 브라우저를 위한 XHR 객체 생성
  - 간편한 API를 제공하면 Promise 기반의 비동기 요청을 처리
- Ajax를 활용한 클라이언트 서버 간 동작
  - XHR 객체 생성 및 요청
  - 응답 데이터 생성
  - JSON 데이터 응답
  - Promise 객체를 활용해 DOM 조작
- Axios 설치 및 사용
  - CDN 방식으로사용
  - axios 객체를 활용해 요청을 보낸 후 응답 데이터 promise 객체를 받음
  - 예시
```javascript
axios ({
    method:get,
    url: "https:\\api...
})
```
## 3.2 Axios 활용
## 3.3 Ajax 와 Axios


# 4. CallBack과 Promise
## 4.1 비동기 콜백
## 4.2 프로미스

# 5. 참고
## 5.1 비동기 처리와 사용자 경험
## 5.2 비동기 처리 주요 사례
## 5.3 비동기 처리 주의 사항