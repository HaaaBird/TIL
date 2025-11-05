# 1. Database
- 데이터란?
  - 저장이나 처리를 위해 변환된 정보
- 데이터 처리 방법
  - 1. 파일(File)이용
    - 어디서나 쉽게 사용 가능
    - 구조적으로 관리 어려움
  - 2. Spreadsheet 이용
    - 테이블의 열과 행을 사용해 데이털르 구조적으로 관리 가능
    - 한계
      - 크기: 일반적으로 100만행 까지만
      - 보안: 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 제한 기능만 제공
      - 정확성
        - 강원 -> 강윈도 라면? 일일히 전체 다 수정
        - 여러 파일에 분산되어 있다면 더 큰 문제
- 데이터베이스의 역할
  - CRUD
    - Create 
    - Read
    - Update
    - Delete
# 2. Relational Database
- Relational Database란?
  - 관계형 데이터베이스: 데이터 간에 관계가 있는 데이터 항목들의 모음
  - 테이블, 행, 열의 정보를 구조화하는 방식
  - 서로 관련된 데이터 포인터를 저장하고 이에 대한 엑세스를 제공
- 관계
  - 여러 테이블 간의 논리적 연결
  - 관계로 할 수 있는 것
    - 이 관계로 인해 두 테이블을 사용하여 데이터를 다양한 형식으로 조회할 수 있음
      - 특정 날짜에 구매한 모든 고객
      - 지난 달에 배송일이 지연된 고객 등
![img](img/SQL1.png)
- 관계형 데이터베이스의 예시
  - 다음과 같이 고객데이터가 테이블에 저장되어 있다고 가정
  - 고객 데이터 간 비교를 위해서는 어떤 값을 활용해야 할까?
    - 각 데이터에 고유한 식별값을 부여하기(PK)
    - 주문 정보에 고객의 고유한 식별 값을 저장하기(외래 키 Foreign Key)
![img](img/SQL2.png)

- 관계형 데이터베이스 관련 키워드
  - 테이블(Relation): 데이터를 기록하는 곳
  - 필드(Field, Column, Attribute): 지정된 고유한 데이터 형식
  - 레코드(Record, Row, Tuple): 구체적인 데이터 값
  - 데이터베이스(Database, Schema): 테이블의 집합
  - Primary Key(기본키, PK): 각 레코드의 고유값, 관계형 DB에서 레코드의 식별자로 활용
  - Foreign Key(외래 키, FK): 테이블의 다른 필드 중 다른 테이블의 레코드를 식별할 수 있는 키. 다른 테입르의 기본 키를 참조. 관계를 만드는데 사용
## 2.1 RDBMS
- DBMS
  - 데이터베이스를 관리하는 소프트웨어 프로그램
  - 데이터 저장 및 관리를 용의하게 하는 시스템
  - 데이터베이스와 사용자 간의 인터페이스 역할
  - 사용자가 데이터 구성, 업데이트 모니터링, 백업, 복구 등을 할 수 있도록 도움
- RDBMS
  - 관계형 데이터베이스 관리 소프트웨어 프로그램
- RDBNS 서비스 종류
  - SQLite
  - MySQL
  - PostgreSQL
  - Oracle Database 등
- SQLite
  - 경량의 오픈소스 데이터베이스 관리 시스템
  - 설치 없이 가볍게 실행 가능해 모바일이나 소규모 프로그램에 적합
  - 컴퓨터나 모바일 기기에 내장되어 간단하고 효율적인 데이터 저장 관리 가능

- 데이터베이스 정리
  - Table은 데이터가 기록되는 곳
  - Table에는 행에서 고유하게 식별 가능한 기본키 라는 속성이 있으며 외래키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음
  - 데이터는 기본 키 또는 외래 키를 통해 결합될 수 있는 여러 테이블에 걸쳐 구조화됨

# 3. SQL(Structure Query Language)
- 테이블 형태로 구조화 된 관계형 데이터베이스에 요청을 질의
```sql
SELECT column_name FROM table_name;
```
- 1. SQL 키워드는 대소문자를 구분하지 않음.
  - 그렇지만 명령어는 대문자로 작성하는걸 권장
- 2. SQL Statements의 끝에는 세미콜론 ';'가 필요
  - 세미콜론은 각 SQL Statements를 구분하는 방법(명령어의 마침표)
## 3.1 SQL Statements
- SQL을 구성하는 가장 기본적인 코드 블록
- SQL Statements의 예시
```sql
SELECT column_name FROM table_name;
```
- 수행 목적에 따른 SQL Statements 4가지 유형
  - DDL: 데이터 정의
  - DQL: 데이터 검색
  - DML: 데이터 조작
  - DCL: 데이터 제어

| 유형 | 역할 | SQL 키워드 |
| ---- |  ---- |  ---- |
| DDL(Data Definition Language) | 데이터의 기본 구조 및 형식 변경 | CREATE, DROP, ALTER |
| DQL(Data Query Language) | 데이터 검색 | SELECT |
| DML(Data Mainpulation Language) | 데이터 조작(추가, 삭제, 수정) | INSERT, UPDATE, DELETE |
| DCL(Data Control Language) | 데이터 및 작업에 대한 사용자 권한 제어 | COMMIT, ROLLBACK, GRANT, REVOKE |
# 4. Querying Data
## 4.1 DQL(Data Query Language)
- SELECT syntax
```sql
SELECT
  select_list
FROM
  table_name;
```
- SELECT 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
- FROM 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정

# 5. Sorting data
## 5.1 ORDER BY
```sql
SELECT
  select_list
FROM
  table_name;
ORDER BY
  column1 [ASC|DESC], 
  column2 [ASC|DESC], 
```
- FROM clause 뒤에 위치
- 하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC, 기본값), 내림차순(DESC)로 정렬
# 6. Filtering data
- Clause
  - DISTINTIC
  - WHERE
  - LIMIT
- Operator
  - BETWEEN
  - IN
  - LIKE
  - Comprison
  - Logical
## 6.1 DISTINCT
```sql
SELECT DISTINCT
  select_list
FROM
  table_name;
```
- SELECT 바로 뒤에 작성
- SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드 지정
## 6.2 WHERE
```sql
SELECT
  select_list
FROM
  table_name
WHERE
  search__condition;
```
- FROM clause 뒤에 위치
- search_condition은 비교연산자 및 논리연산자(AND, OR, NOT)를 사용하는 구문이 됨
## 6.3 Operators
- Comparison Operators
  - 비교 연산자
  - =, >=, <=, !=
  - IS, LIKE, IN
  - BETWEEN...AND
- Logical Operators
  - 논리 연산자
  - AND(&&)
  - OR(||)
  - NOT(!)
- Wildcard Characters
  - %: 0개 이상의 문자열과 일치하는지 확인
  - _: 단일 문자와 일치하는지 확인
## 6.4 LIMIT
```sql
SELECT
  select_list
FROM
  table_name
LIMIT [offset, ] row_count;
```
- 하나 또는 두 개의 인자를 사용(0 또는 양의 정수 사용)
- row_count는 조회하는 최대 레코드 수를 지정
# 7. Grouping data
## 7.1 GROUP BY
```sql
SELECT
  c1, c2, ... , arrgeate_function(ci)
FROM
  table_name
GROUP BY
  c1, c2, ... , cn;
```
- FROM및 WHERE 절 뒤에 배치
- GROUP BY 절 뒤에 그룹화 할 필드 목록을 작성
- Aggregation Functions. 집계 함수
  - 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
    - SUM, AVG, MAX, MIN, COUNT
## 7.2 HAVING
- WHERE 과 HAVING 비교
- WHERE
  - 목적
    - 개별 행에 대한 조건을 지정하여 데이터를 필터링
  - 적용 시점
    - FROM과 JOIN등의 단계 이후, GROUP BY이전에 적용
 - 사용 예시
   - 특정 조건을 만족하는 행만을 대상으로 집계나 정렬 등의 작업을 수행할때 사용
- HAVING
   - 목적
      - GROUP BY에 의해 그룹화된 결과에 대해 조건을 지정하여 그룹을 필터링
   - 적용시점
      - 그룹핑 및 집계 함수 적용 후에 조건을 평가
   - 사용예
     - 그룹별 집계 결과에 조건을 걸어 특정 그룹만을 선택할 때 사용
![img](img/SQL3.png)
# 8. 참고
## 8.1 Query
- 데이터베이스로부터 정보를 요청하는 것
- 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함
## 8.2 NULL 비교
- SQL에서 NULL은 실제 값이 아니라 "값이 없음" 또는 "알 수 없음"을 의미
  - 때문에 일반적인 등호("=")로 NULL을 비교하면 의도한 대로 동작하지 않음
- SQL의 3값 논리
  - 1. TRUE
  - 2. FALSE
  - 3. UNKNOWN(알수없음)
  - 예를 들어 NULL = NULL 의 결과는 TRUE 가 아닌 UNKNOWN이 됨
  - 이는 두 NULL이 실제 어떤 값을 가지지 않기 때문
- 값의 부재와 불확실성
  - NULL은 값이 존재하지 않음을 나타냄으로 특정 값과 동일하다고 볼 수 있음
  - = 연산자를 쓰면 NULL은 어떤 값과도 비교할 수 없음으로 결과가 UNKNOWN이 되어 기대한 결과를 얻지 못함
- 명시적 비교: IS와 IS NOT
  - SQL 표준은 NULL 값을 비교할때 명시적으로 IS NULL 이나 IS NOT NULL 구문을 사용하도록 규정
  - WHERE column IS NULL은 해당 컬럼에 값이 없음을 정확하게 확인할 수 있도록 해줌
  - 반대로 WHERE column IS NOT NULL은 은 값이 존재하는 행을 찾음
- IS와 =비교
- =
  - 일반적인 값의 동등성(같음)을 비교할 때 사용
  - 제한 사항
    - 만약 비교하는 값 중 하나라도 NULL이면 결과는 UNKNOWN이 됨
    - 예를 들어 NULL = NULL 의 결과는 TRUE 가 아니라 UNKNOWN
    - SQL의 3값 논리(참, 거짓, 알 수 없음)체계 떄문에 이런 결과가 발생
```sql
SELECT * FROM employees
WHERE department = 'Salse';
```
- IS
  - NULL과 같은 특별한 값을 비교할 때 사용
  - 사용처
    - NULL 비교
    - Boolean 값 비교
```sql
SELECT * FROM employees
WHERE department IS NULL
AND is_active IS TRUE;
```

# 1. Managing Tables
## 1.1 Create a table
```sql
CREATE TABLE table_name (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);
```
- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건(constraints) 작성

- SQL의 데이터 타입
  - NULL: 아무런 값도 포함하지 않음
  - INTEGER: 정수
  - REAL: 부동소수점
  - TEXT: 문자열
  - BLOB: 이미지, 동영상, 문서 등의 바이너리 데이터
- Constraints(제약 조건)
  - 테이블의 필드에 적용되는 규칙 또는 제한 사항
  - 데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장
- 대표 제약 조건 3가지
  - PK(Primary Key)
    - 해당 필드를 기본 키로 지정
    - INTEGER 타입에만 지정 가능. INT, BIGINT 등과 같은 다른 정수 유형은 안됨.
  - NOT NULL
    - 기본값에 NULL 값을 허용하지 않음
  - FOREIGN KEY
    - 다른 테이블과의 외래 키 관계를 정의
  - AUTOINCREMENT 
    - 필드의 자동 증가를 나타내는 특수한 키워드
    - 주로 PK에 적용
    - INTEGER PRIMARY KEY AUTOINCREMENT 가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대값보다 큰 값을 할당하게 됨
    - 삭제된 값은 무시. 재사용 할 수 없게 됨
      - 라 생각하지만 가능. 마지막 번호에 대해 별도 필드에 갱신해서 관리하는거라 이거 조작하면 예전 값 다시 사용할 수 있게 처리 가능
## 1.2 Modifying table fields
- ALTER TABLE
| 명령어 | 역할 |
| ---- | ---- |
| ALTER TABLE ADD COLUMN | 필드 추가 |
| ALTER TABLE RENAME COLUMN | 필드 이름 변경 |
| ALTER TABLE DROP COLUMN | 필드 삭제 |
| ALTER TABLE RENAME TO | 테이블 이름 변경 |

```SQL
-- ADD COLUMN
ALTER TABLE
  users 
ADD COLUMN
  Country VARCHAR(100) NOT NULL DEFAULT 'default value';

-- RENAME COLUMN
ALTER TABLE
  users
RENAME COLUMN
  Country TO Countrys;

-- DROP TABLE
ALTER TABLE
  users
DROP COLUMN
  Country;

-- RENAME TO
ALTER TABLE
  users
RENAME TO
  MyUsers;
```
## 1.3 Delete a table
```sql
DROP TABLE MyUsers;
```
# 2. Modifying Data
## 2.1 Insert Data
- 사전 준비
  - 생성하려는 테이블과 동일한 이름을 가진 테이블이 존재하는지 확인
  - 불필요한 테이블이라면 DROP TABLE 명령어로 테이블 삭제
  - 정상적으로 삭제되었는지 PRAGMA 활용하여 체크
```SQL
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

-- INSERT INTO 실습
INSERT INTO articles
  (title, content, createAt)
VALUES
  ('hello', 'world', '2200-01-01');
```
## 2.2 Update Data
```sql
UPDATE articles
SET title = 'update_title'
WHERE id = 1;
```
## 2.3 Delete Data
```SQL
DELETE FROM articles
WHERE id = 1;
```
# 3. Multi table queries
- 관계의 필요성
  - 커뮤니티 페이지를 생각해보자. 유저 정보는 뭐가 필요할까?
  - 아이디, 제목, 글, 작성자, 권한 등 5개만 관리해본다고 해 보자
  - 이 때 이걸 하나의 테이블에서 관리하면 골치가 아프다. 뭐 하나 생길때마다 행이 추가되는거니까
  - 따라서 사용처에 따라 테이블을 구분하고 이를 묶어서 관리할 필요가 있다. 이걸 join 연산을 통해서 해 보자

![img](img/SQL4.png)
## 3.1 Join
- 작성자가 있는(존재하는 모든 회원)모든 게시글을 작성자 정보와 함께 조회해보자

```sql
SELECT * FROM articles
INNER JOIN users ON users.id = articles.userID;
```
- LEFT JOIN
  - 테이블 A와 B를 JOIN 한다 했을 때, FROM 절에 지정된 테이블의 전체, B테이블은 겹치는 부분만
```SQL
SELECT * FROM articles
LEFT JOIN users
ON articles.id = users.id;
```
# 4. 참고
## 4.1 타입 선호도
- 컬럼에 데이터 타입이 명시적으로 지정되지 않았거나 지원하지 않을 때 SQLite가 자동으로 데이터 타입을 추론하는 것
- 목적
  - 1. 유연한 데이터 타입 지원
    - 타입을 명시하지 않아도 데이터를 저장하고 조회 가능
    - 컬럼에 저장되는 값을 기반으로 데이터타입을 유추
  - 2. 간편한 데이터 처리
    - INTEGER type Affinity를 가진 열에 문자열 데이터를 저장해도 SQLite는 자동으로 숫자로 변환하여 처리
  - 3. SQL 호환성
    - 다른 데이터베이스 시스템과 호환성을 유지
## 4.2 NOT NULL
- 반드시 NOT NULL을 해야 할까?
  - 아님.
  - 대부분은 NOT NULL을 정의
  - 값이 없다는 표현을 테이블에 기록하는게 좋음. 0이나 빈 문자열 넣는게 속 편함
## 4.3 날짜와 시간
- SQLite에서는 날짜 및 시간 저장하기 위한 별도 데이터타입이 없음
- 대신 날짜 및 시간에 대한 함수를 사용해 표기 형식에 따라 TEXT, REAL, INTEGER값으로 저장.


# 1. Many to one relationships
## 1.1 모델 관계
- 관계(relationship)
  - 데이터베이스 내 여러 테이블 간의 논리적인 연결 관계를 나타냄
- 관계의 종류
  - 1:1 관계(One to One)관계
    - 한 테이블의 레코드는 다른 테이블의 한 레코드와 연결됨
    - 예시) 한 사람당 하나의 주민등록번호
  - N:1 관계(Many to one)관계
    - 여러 개의 레코드가 하나의 레코드와 연결됨
    - 예시) 여러 교육생(N)을 한 강사가 가르침
  - N:M 관계(Many to Many)관계
    - 여러 레코드가 여러 레코드와 상호 연결됨
    - 보통 중간 테이블(예: 수강신청)을 사용해 구현됨
    - 여러 학생(N)이 여러 과목(M)을 수강함
![img](img/SQL5.png)
- 댓글과 게시글의 관계
  - Comment(N) : Article(1)
    - 하나의 게시글, 여러 댓글
  - 테이블 관계 설정
    - 관계 설정을 위한 Foreign Key(외래 키)를 N:1에서 1을 담당하는 테이블에 위치하면 안됨
    - Article Table에 Foreign Key 컬럼을 위치시키면 중복 데이터로 인해 낭비가 심함
![img](img/SQL6.png)
## 1.2 댓글 모델 정의
- 외래 키(Foreign Key(to, on_delete))
  - 한 모델(테이블)이 다른 모델(테이블)을 참조하는 관계를 설정하는 필드
    - N:1관계 표현할 때 사용
    - 데이터베이스에서 외래키로 구현됨
- ForeignKey(to, on_delete)
  - to 속성
    - 참조하는 모델 class 이름(N:1에서 N이 아닌 1의 class 정보)
  - on_delete 속성
    - 외래키가 참조하는 객체(1)이 사라졌을 때 외래 키를 가진 객체(N)을 어떻게 처리할지를 정의하는 설정(데이터 무결성)
- on_delete 속성 종류
  - CASCADE
    - 참조 된 객체(부모 객체)가 삭제될 때 이를 참조하는 모든 객체도 삭제되도록 지정
    - 예) 게시글이 삭제되면 해당 게시글의 모든 댓글을 삭제
  - PROTECT
    - 삭제하려는 부모 객체에 자식 객체가 존재한다면 해당 부모 객체를 삭제하지 못하도록 지정
    - 예) 게시글을 삭제할 때 해당 게시글에 댓글이 존재하면 게시글 삭제 못함
  - SET_NULL
    - 부모 객체가 삭제되면 해당 필드에 값이 NULL이 저장되도록 지정
    - 단, 해당 ForeignKey 필드 설정이 NOT NULL 이면 안됨
- 댓글 모델 정의하기
  - ForeignKey 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장

```python
# articles/models.py

class Comment(model.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.CharField(max_length=200)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
# 단일 객체를 참조함으로 단수형으로 해야 의미가 명확
```
- Migration 이후 댓글 테이블 확인
  - 만들어 지는 필드 이름 규칙
    - "작성한 외래 키 필드명" + "_" + "id"
  - 댓글 테이블의 article_id 외래 키 필드 확인
    - bigint(64비트 정수형)으로 설정됨 확인
![img](img/SQL7.png)
# 2. 관계 모델 참조
- 참조
  - 직접 대상의 정보를 저장하고 필요할 때 활용하는 것
- 특정 게시글(Article)의 댓글(Comment) 정보 조회하기
  - QuerySet API의 .all() 사용하기 x
    - 특정 Article의 Comment가 아닌 모든 댓글 정보를 가져오게 됨
  - .filter()사용해서 불러오기
```python
article = Article.objects.get(pk=1)
comments = Comment.objects.filter(article=article)
```
## 2.1 역참조
- 역참조
  - 누가 나를 참조하는지 거꾸로 조회 하는것
- 역참조 기본 구조
  - **article.comment_set.all()**
  - 모델인스턴스.역참조이름.QuerySetAPI
- 1. 모델 인스턴스(article)
  - models.py에 정의된 모델 클래스로 생성된 실제 데이터를 의미
    - article.title 과 같이 속성에 접근 가능하며 속성을 수정할 수 있음.
  - 역참조에서는 참조 가능한 필드가 없는 모델 클래스의 인스턴스를 사용하면 됨
    - Article(1) : Comment(N) => Article에 참조 필드가 없어서 Article의 인스턴스를 사용
- 2. related manager(역참조 이름)
  - related manager 라고 불리며 N:1 혹은 N:M 관계에서 역참조 시에 사용하는 매니저를 의미
  - object 매니저를 통해 QuerySet API를 사용했던 것 처럼 related manager를 통해 QuerySet API를 사용할 수 있게 됨
- 3. QuerySet API
  - 데이터를 가져오기 위한 쿼리 결과 집합을 만드는 인터페이스
  - SQL 쿼리를 직접 쓰지 않고도 DB를 사용할 수 있음.
- related manger(역참조 이름) 이름 규칙
  - 모델 클래스명 + _set 이 기본 값이며 Django에서 자동으로 생성해줌
  - 관계를 직접 정의하지 않은 모델에서 연결된 객체들을 조회할 수 있게 함
  - 특정 댓글의 게시글 참조(Comment -> article)
    - comment.article
  - 특정 게시글의 댓글 목록 역참조(Article -> Comment)
    - article.comment_set.all()
# 3. 댓글 구현
## 3.1 댓글 CREATE
- 사용자로부터 댓글 데이터를 입력받기 위한 CommentForm 정의
```python
# articles/forms.py

from .models import ARticle, Comment

class CommentForm(form.ModelForm):
  class Meta:
    model = Comment
    fields = "__all__"
```
- 댓글이 작성되는 곳은 게시글 상세 페이지 하단.
- detail view 함수에서 CommentForm을 detail 페이지에서 사용할 수 있도록 context로 전달
```python
# article/views.py
def detail(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm()
  context = {
    'article':article,
    'comment_form':comment_form,
  }
  return render(request, 'articles/detail.html', context)
```
- 댓글이 작성되는 detail페이지 하단에 commentForm 을 사용하여 렌더링
```html
<!--articles/detail.html-->

<form action="#" method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit">
</form>
```
- Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요한 필드이기 때문에 출력되는 것
- 하지만 외래 키 필드는 사용자로부터 입력 받는 값이 아닌 view 함수 내에서 다른 방법으로 전달받아 저장되어야 함.
![img](img/SQL8.png)

- CommentForm의 출력 필드 조정하여 외래키가 출력되지 않도록 해야함
```python
articles/forms.py
from .models import Article, Comment

class CommentForm(form.ModelForm):
  class Meta:
    model = Comment
    fields = ('context', ) # 실제 출력되는걸 context 외엔 없게 처리. 마지막 콤마는 필수
```
- 그럼 외래 키는 어디서 받아와야 하나?
  - detail 페이지의 URL에 게시글 정보가 존재
  - path('<int/>pk>/', views.detail, name='detail')
- 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk값
- 댓글 저장 로직은 detail함수가 아닌 개별 함수로 작성
  - 댓글 저장은 게시글 상세보기와 전혀 다른 기능(단일 책임 원칙)
  - 댓글 저장 시 게시글 pk정보를  URL로 전달하여 사용
```html
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
  {%csrf_token%}
  {{comment_form}}
  <input type="submit">
</form>
```
```python
# articles/urls.py
app_name = 'article'
urlpatterns = [
  path('<int:pk>/comments/>', views.comments_create, name="comments_create")
]
```
- 댓글 만드는 comments_create 함수는 POST 작성만 진행
  - 댓글 작성 form을 출력하는 GET 동작은 이미 detail에 들어가있음
```python
def comments_create(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid():
    comment_form.save()
    return redirect('articles:detail', article.pk)
  context = {
    'article':article,
    'comment_form':comment_form
  }
  return render(request, 'articles/detail.html', context)
```
- save 메서드의 commit 인자
  - save(commit=False)
- 기본적으로 commit 속성은 True 가 기본 값
  - 설정 값이 True인 경우 인스턴스를 생성하고 반환한 다음 DB에도 저장 요청을 보냄
- commit이 False인 경우 DB에 저장 요청을 보내지 않고 인스턴스만 반환
- 댓글을 저장할 때 바로 DB에 저장 요청을 보내는 것이 아닌 게시글 정보를 추가한 후 저장 요청을 보내도록 로직을 구성하면 게시글 정보와 함께 댓글을 저장할 수 있게 됨

```python
# articles/views.py
def comments_create(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid():
    comment = comment_form.save(commit=False)
    comment.article = article
    comment.save()
    return redirect('articles:detail', article.pk)
  context = {
    'article':article,
    'comment_form':comment_form
  }
  return render(request, 'articles/detail.html', context)

```
## 3.2 댓글 READ
- 댓글이 보이는 위치는 게시글 상세 페이지 하단
  - detail view 함수에서 전체 댓글 데이터를 조회해서 detail.html로 전달하여 댓글 데이터 조회
```python
def detail(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm()
  comment = article.comment_set.all() # 역참조로 댓글 목록 가져오기
  context = {
    'article':article,
    'comment_form': comment_form,
    'comments':comments,
  }
  return render(request, 'arcitles/detail.html', context)
```
## 3.3 댓글 DELETE
- 개별 댓글마다 삭제할 수 있도록 기능을 추가
- 어떤 댓글을 삭제해야 하는지 삭제 대상 정보를 전달하기 위해 variable routing을 이용
```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
  path('<int:article_pk>/comments/<int:comment_pk>/delete.', views.comment_delete, name='comment_delete')
]
```
- 댓글 삭제 view 함수 정의
```python
# articles/views.py

def comment_delete(request, article_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()
  return redirect('articles:detail', article_pk)
```

# 4. 참고
## 4.1 데이터 무결성
- 데이터 무결성이란?
  - 데이터베이스에 저장된 데이터의 정확성, 일관성, 유효성을 유지하는 것
  - 데이터베이스에 저장된 데이터 값의 정확성을 보장하는 것
  - 중요성
    - 데이터의 신뢰성 확보
    - 시스템 안정성
    - 보안 강화
## 4.2 admin site 댓글 등록
- 작성된 comment 모델에 대해 Admin site에서 관리할 수 있도록 아래와 같이 등록
```python
# articles/admin.py
from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)

```
## 4.3 댓글 추가 구현
