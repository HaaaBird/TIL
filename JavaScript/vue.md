# 1. Froutend Development
- 웹사이트와 웹어플리케이션 사용자 인터페이스(UI)와 사용자 경험(UX)을 만들고 디자인하는것
- HTML, CSS, JavaScript 등을 활용해 사용자가 직접 상호작용 하는 부분을 개발
## 1.1 Client-side Frameworks
- 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 Javascript 기반 프레임워크
- Client-side-frameworks 가 필요한 이유
  - 단순히 무언가를 읽는 공간에서 무언가를 하는 곳으로 변화
    - 사용자는 이제 웹에서 문사만을 읽는 것이 아닌 음악을 스트리밍 하고, 영화를 보고, 지구 반대편 사람들과 텍스트 및 영상 채팅을 통해 즉시 통ㅅ니
    - 현대적인 웹 어플리케이션 개발이 필요
    - JavaScript기반으 Client-Side Frameworks 가 등장하면서 매우 동적인 대화형 어플리케이션 구축이 더 쉬워짐
  - 다루는 데이터가 다양해짐
    - 친구가 이름을 바꾸면?
      - 모든 곳이 다 바뀜(친구 목록, 타임라인 등등)
      - 애플리케이션의 기본 데이터를 안정적으로 추적하고 업데이트(랜더링, 추가, 삭제)하는 도구가 필요
      - 애플리케이션의 상태가 변경될 때 마다 ui가 일관성 있게 업데이트되어야 함
- Vanilla JS만으로는 간단하지 않음
  - 불필요한 코드의 반복
- Client-side frameworks의 필요성
  - 동적이고 반응적인 웹 어플리케이션 개발
    - 실시간 데이터 업데이트
  - 코드 재사용성 증가
    - 컴포넌트 기반 아키텍처
    - 모듈화된 구조
  - 개발 생산성 향상
    - 강력한 개발 도구 지원
## 1.2 SPA
- Single Page Application
  - 단일 페이지에서 동작하는 웹 어플리케이션
  - 하나의 html 파일 위에서 javascript가 필요한 부분만 교체하며 진짜 페이지 이동 없이 동작
  - 하나의 앱 처럼 빠르고 부드러운 사용자 경험
- Signle Page Application 작동 원리
  - 최초 로드 시, 어플리케이션에 필요한 주요 리소스를 다운로드
  - 페이지 갱신에 대해 필요한 데이터만을 비동기적 전달 받아 화면의 필요한 부분만 동적으로 갱신
    - AJAX와 같은 기술을 사용해 필요한 데이터만 비동기적으로 로드
    - 페이지 전체를 다시 로드할 필요 없이 필요한 데이터만 서버로부터 가져와서 화면에 표시
  - JavaScript를 사용하여 클라이언트 측에서 동적으로 콘텐츠를 생성하고 업데이트
    - CSR 방식

## 1.3 CSR
- Client Side Rendering
  - 클라이언트에서 콘텐츠를 렌더링 하는 방식
- 작동 원리
  - 사용자가 웹사이트에 요청을 보냄
  - 최소한의 HTML, JS파일을 클라이언트에게 전달
  - 브라우저가 JS를 실행해 동적으로 페이지 콘텐츠를 생성
  - 필요한 데이터는 API를 통해 서버로부터 비동기적으로 가져옴
- 작동 예시
  - 클라이언트는 서버로부터 최소한의 HTML 페이지와 어플리케이션 실행에 필요한 JS만 응답 받음
  - JS를 이용해 DOM을 업데이트해 페이지를 랜더링
  - 서버는 더 이상 HTML을 제공하지 않고 요청에 필요한 데이터만 응답
  - Google Maps, FaceBook, Instagram 등의 서비스 페이지에서 페이지 갱신 시 새로고침이 없음
- CSR과 SPA의 장점
  - 빠른 페이지 전환
    - 페이지가 처음 로드된 후에는 필요한 데이터만 가져오고, JS는 전체 페이지를 새로 고칠 필요 없이 페이지의 일부를 다시 렌더링 할 수 있음.
    - 서버로 전송되는 데이터 양을 최소화
  - 사용자 경험
    - 새로고침이 발생하지 않아 네이티브 앱과 비슷한 경험
  - Frontend와 Backend의 명확한 분리
    - FE는 UI렌더링, 사용자 상호 작용 처리 담당, BE는 데이터 및 API제공
    - 대규모 어플리케이션 개발이 더 쉽고 유지 가능
- 단점
  - 느린 초기 로드 속도
    - 전체 페이지를 보기 전에 지연 느낌, js가 다운, 구문분석 실행 될때까지 기다려야 함
  - SEO문제
    - 페이지를 나중에 그림으로 검색에 잘 노출되지 않음
    - 검색엔진이 읽을 HTML에 콘텐츠가 없기 때문
# 2. Vue
- 사용자 인터페이스 구축을 위한 JS프레임워크
# 3. Vue tutorial
- Vue를 사용하는 방법
  - CDN 방식
  - NPM 방식
## 3.1 Vue Application 생성
- vue 사용을 위한 CDN 작성
```vue
<script src="https://unpkg.com/vue@3/dist/vue.global.js">
</script>
<script>
  const { createApp } = Vue
  // 1. CDN으로 불러온 전역 Vue 객체를 불러와 구조분해할당 무넙ㅂ으로 createApp 함수를 할당
  const app = createApp({
    setup() {} 
    // 3. Root Component. crateApp 함수에는 객체가 전달됨. 모든 App에는 다른 컴포넌트들을 하위 컴포넌트로 포함할 수 있는 Root(최상위) 컴포넌트가 필요(현재는 단일 컴포넌트)
  }) // 2. 모든 vue 어플리케이션은 createApp함수로 새 Application instance를 생성하는걸로 시작
  app.mount('#app') // Mounting the App(앱 연결) html요서에 Vue Application instance를 연결. 각 앱인스턴스에 대해 mount는 한번만 호출 가능
</script>
```
## 3.2 반응형 상태
- ref() 반응형 상태(데이터)를 선언하는 함수(Declaring Reactive State)
  - .value 속성이 있는 ref객체로 wrapping 하여 반환하는 함수
  - ref로 선언된 변수의 값이 변경되면, 해당 값을 사용하는 탬플릿에서 자동으로 업데이트
  - 인자는 어떤 타입도 가능
  - ref 함수는 반응형을 가지는 참조 변수를 만드는 것

```vue
<script>

  const { createApp, ref} = Vue
  const app = createApp({
    setpu() {
      const message = ref('Hello vue!')
      console.log(message) // ref 객체
      console.log(message.value) // Hello vue!
    }
  })

</script>
```
## 3.3 Vue 기본 구조

# 4. 참고
## 4.1 ref 객체
## 4.2 Ref Unwrap 주의사항
## 4.3 SEO
## 4.4 CSR과 SSR

# 1. Template Syntax
