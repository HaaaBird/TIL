# Git  
    최종 수정일자: 2025-07-17 17:04
---
## 1. git 이란 무엇인가? 
git 은 리눅스 개발자가 만든 버전 관리 시스템  
## 2. 분산 개념
분산 관리 -> 원본을 서버에서 저장하고, 각 로컬 PC에 클론을 배치.  
작업자는 클론 기반으로 작업 및 수정  
## 3. PUSH, PULL  
클론을 기반으로 동작해서 로컬에 원본을 가져오고 올리는 작업  
PUSH: 로컬의 내용을 서버에 밀어올린다  
PULL: 서버에 있는 내용을 가져온다.  
## 4. git 의 영역
### 4.1 Working Directory 
- 실제로 내가 수정하고 있는 코드/파일들이 있는 공간(로컬)
- 물리적으로도 저장된 실제 파일
```bash
git status
```
### 4.2 Staging Area(idx)
- git add 하면 커밋할 후보 목록이 올라가는 대기 공간. add 했을때 스테이징 되는 공간(이름처럼)
- index라고도 부르나봄
### 4.3 Repository(.git 디렉토리)
- git commit 했을때 Staging Area의 내용이 저장되는 공간
- 모든 커밋의 변경이력이 저장됨.
- 진짜 버전관리 DB

## 5.Git 사용해보기
- vsc -> 터미널 기본설정을 **git bash** 로 바꿔주기
- 왜 바꾸나요? bash 가 리눅스 명령어 기반. 리눅스에서 쓰던, 윈도우에서 쓰던, 맥에서 쓰던 bash 쓰면 리눅스 명령어로 작업 가능
- vsc에서 내가 작업 할(git으로 관리 할) 프로젝트 폴더를 만들고, 열기
- 폴더 연 상태로 터미널에서
```bash
git init
```
- 그러면 터미널에 나오는 주소 끝에 master 라는게 나오면 성공(git에서 관리중이라는 뜻?)
### 5.1 Staging Area로 보내보기
- 앞서 말했듯, Add 동작을 해서 예비 저장소 개념인 Staging 공간으로 보내보자.
- GUI를 이용하던, CLI를 쓰던 새롭게 파일을 하나 만들어본다. 
```bash
touch Readme.md
```
- 내용 추가를 하던, 없어도 상관없다. 
```bash
git add Readme.md
```
- 이렇게 Staging Area에 새롭게 생성된 Readme.md파일을 보낸다

#### 질문. 진짜 엄격하게 파일이 복사된건가? 아니면 그냥 idx만 남긴건가? 
#### GPT한테 들은 답: blob(블롭)으로 저장한다.
- blob 이 뭐야? 
- blob 은 SHA-1 해시값.
- git add 파일명 -> 하게 될 경우 .git/object 에 저렇게 압축해서 때려박아두고
- Staging Area(.git/index)에는 걍 이 파일이 .git/objec 에 저장되어 있는 저 blob을 가리킨다는 참조만 기록(메타데이터만)
- SHA-1 Hash -> 파일 내용을 기반으로 만든 16진법, 40자짜리 해쉬키. 복원은 불가능. 다만 내용이 한글짜라도 바뀌면 hash값이 완전히 바뀌기 때문에 변경관리에 아주 큰 장점이 있음. 이 성격 이용하기 위해서 SHA-1 사용
### 5.2 Commit 을 해 보자
- git commit -m "commit name" 를 하면 처음엔 안됨. 
- git 관리자 설정이 된게 아니기 때문 config 설정 필요
```bash
git config --global user.email 메일주소@.com
git config --global user.name username
```
- 을 해 줘야 한다. 저기서 global, local 로 설정 가능
- global 을 하면 pc 전체, 어디서든 git을 썼을때 config 가 저 값으로 나감. 다시 설정할 필요 x 사용자 홈 디텍로리 기준으로 gitconfig 가 저장됨
- local로 하면 현재 git 으로 잡아둔 master 설정된 영역 내에서만 config 값으로 동작. 
### 5.3 commit 을 수정해보자.
- commit 된 내용도 수정 가능. 왜냐면 commit 을 한다는건 원본 파일 압축 + 변경 이력 등을 저장하는 과정. 
- amend 마지막 commit 을 수정해도 좋다. 아무튼 그렇다.
