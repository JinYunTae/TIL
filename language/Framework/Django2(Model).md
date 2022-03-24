# Django Model

---

## 1. Model

"웹 애플리케이션의 데이터를 **구조화**하고 **조작**하기 위한 도구"

* 단일한 데이터에 대한 정보를 가짐
  * 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
* 저장된 데이터베이스의 구조(layout)
* Django는 model을 통해 데이터에 접속하고 관리
* 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨

---

## 2. Database

* 데이터베이스(DB)
  * 체계화된 데이터의 모임
* 쿼리(Query)
  * 데이터를 조회하기 위한 명령어
  * 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  * "Query를 날린다" = DB를 조작한다

### 2.1. Database의 기본 구조

* 스키마(Schema)
  * 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조(structure)
* 테이블(Table)
  * 열(column) : 필드(field) or 속성
  * 행(row) : 레코드(record) or 튜플

![image-20220309231840546](Django2(Model).assets/image-20220309231840546-16468391627251.png)

![image-20220309231911547](Django2(Model).assets/image-20220309231911547-16468392009182.png)

![image-20220310002106285](Django2(Model).assets/image-20220310002106285.png)

![image-20220309231932764](Django2(Model).assets/image-20220309231932764-16468392059693.png)

![image-20220309231953418](Django2(Model).assets/image-20220309231953418-16468392210244.png)

---

## 3. ORM

* Object-Relational-Mapping

* 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django-SQL) 데이터를 변환하는 프로그래밍 기술

* OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

* Django는 내장 Django ORM을 사용함

  결과적으로 우리는 **DB를 객체(object)로 조작하기 위해** ORM을 사용한다

![image-20220309232354835](Django2(Model).assets/image-20220309232354835-16468392820175.png)

### 3.1. ORM의 장점과 단점

* 장점
  * SQL을 잘 알지 못해도 DB 조작이 가능
  * SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
* 단점
  * ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음
* 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것! (**생산성**)

### 3.2. models.py 작성

![image-20220309232939647](Django2(Model).assets/image-20220309232939647-16468393139306.png)

* 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨
  * django.db.models 모듈의 Model 클래스를 상속받음
* models 모듈을 통해 어떠한 타입의 DB 칼럼을 정의할 것인지 정의
  * title과 content은 모델의 필드를 나타냄
  * 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 매핑

### 사용 모델 필드

* CharField(max_length=None, **options)
  * 길이의 제한이 있는 문자열을 넣을 때 사용
  * CharField의 max_length는 필수 인자
  * 필드의 최대 길이(문자), 데이터베이스 레벨과 Django의 유효성 검사(값을 검증하는 것)에서 활용
* TextField(**options)
  * 글자의 수가 많을 때 사용
  * max_length 옵션 작성시 자동 양식 필드인 textarea 위젯에 반영은 되지만 모델과 데이터베이스 수준에는 적용되지 않음
    * max_length는 CharField에서 사용해야 함

* 그 외 다양한 필드는 Django의 공식문서 참조

---

## 4. Migrations

### 4.1. 명령어 및 실제 DB table 확인

* "Django가 model에 생긴 변화를 반영하는 방법"

* Migration(이하 마이그레이션) 실행 및 DB 스키마를 다루기 위한 몇가지 명령어

  * makemigrations

    ```bash
    $ python manage.py makemigrations
    ```

    * model을 변경한 것을 기반한 새로운 마이그레이션(like 설계도)을 만들 때 사용
    * 첫 마이그레이션은 **migrations/0001_initial.py**으로 생성 됨

  * migrate

    ```bash
    $ python manage.py migrate
    ```

    * 마이그레이션을 DB에 반영하기 위해 사용
    * 설계도를 실제 DB에 반영하는 과정
    * 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸

  * sqlmigrate

    ```bash
    $ python manage.py sqlmigrate app_이름 마이그레이션_번호
    ```

    * 마이그레이션에 대한 SQL 구문을 보기 위해 사용
    * 마이그레이션이 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인할 수 있음

    <실행 예시>

    ![image-20220309234840420](Django2(Model).assets/image-20220309234840420-16468393210477.png)

    실제 데이터베이스에 전달되는 SQL문

  * showmigrations

    ```bash
    $ python manage.py showmigrations
    ```

    * 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
    * 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인할 수 있음

    <실행 예시>

    ![image-20220309234953404](Django2(Model).assets/image-20220309234953404-16468393246458.png)

    [X]된 파일들은 적용된 상태

### 4.2. model 수정

![image-20220309235320316](Django2(Model).assets/image-20220309235320316-16468393277519.png)

추가 필드 작성 후 makemigrations -> migrate 과정을 진행해주어야 데이터베이스에 반영됨

#### DateField's options

* **auto_now_add** (default값이 필수로 필요함)
  * 최초로 생성된 날짜와 시간을 저장(테이블에 어떤 값을 최초로 넣을 때)
  * Django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신
* **auto_now**
  * 최종 수정된 날짜와 시간을 저장
  * Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

#### DateTimeField가 아닌 DateField의 options를 확인한 이유

* DateTimeField는 Datefield와 동일한 추가 인자(extra argument)를 사용함

* DateTimeField는 Datefield의 서브클래스임

  ![image-20220313234329009](Django2(Model).assets/image-20220313234329009.png)

#### default 값이 필요한 경우

실행하면서 어떤 기본값을 설정할 것인지 질문하는 단계가 나타남

![image-20220313232931858](Django2(Model).assets/image-20220313232931858.png)

* 1번 : django에서 기본으로 설정해주는 기본값 사용하기
* 2번 : 실행을 종료하고 직접 입력하기

---

## 5. Datebase API

* **DB를 조작하기 위한 도구**
* Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
* Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만듦
* database-abstract API 혹은 data-access API 라고도 함

### 5.1. DB API 구문 - Making Queries

![image-20220313234814558](Django2(Model).assets/image-20220313234814558.png)

### 5.2. DB API

* Manager
  * Django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
  * 기본적으로 모든 Django 모델 클래스에 objects라는 Manager를 추가
* QuerySet
  * 데이터 베이스로부터 전달받은 객체 목록
  * queryset안의 객체는 0개, 1개 혹은 여러 개일 수 있음
  * 데이터베이스로부터 조회, 필터, 정렬 등을 수행 할 수 있음

### 5.3. Django shell

* 일반 Python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음
* 그래서 장고 프로젝트 설정이 load도니 Python shell을 활용해 DB API 구문 테스트 진행
* 기본 Django shell 보다 더 많은 기능을 제공하는 shell_plus를 사용해서 진행
  * Django-extensions 라이브러리의 기능 중 하나

#### [실습]

* 라이브러리 설치

![image-20220314232512367](Django2(Model).assets/image-20220314232512367.png)

More powerful interactive shell을 위한 2가지 라이브러리 설치

* 라이브러리 등록 및 실행

![image-20220314232618782](Django2(Model).assets/image-20220314232618782.png)

앱 등록 후 shell_plus 실행

![image-20220314232647997](Django2(Model).assets/image-20220314232647997.png)

shell_plus 실행 화면

---

## 6. CRUD

* 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인

  Create(생성), Read(읽기), Update(갱신), Delete(삭제)를 묶어서 일컫는 말

### 6.1. 실습

#### CREATE

CREATE 관련 메서드

* save() method
  * Saving objects
  * 객체를 데이터베이스에 저장함
  * 데이터 생성 시 save()를 호출하기 전에는 ID 값이 무엇인지 알 수 없음
    * ID 값은 Django가 아니라 DB에서 계산되기 때문
  * 단순히 모델을 인스턴스화 하는 것이 DB에 영향을 미치지 않기 때문에 반드시 save()가 필요

1. 인스턴스 생성 후 인스턴스 변수 설정

![image-20220321230913299](Django2(Model).assets/image-20220321230913299.png)

2. 초기값과 함께 인스턴스 생성

![image-20220321231010961](Django2(Model).assets/image-20220321231010961.png)

3. QuerySet API - create() 사용

![image-20220321231106546](Django2(Model).assets/image-20220321231106546.png)

#### 테이블 확인

실제로 저장 되었는지 확인

![image-20220321231305156](Django2(Model).assets/image-20220321231305156.png)

#### READ

READ 관련 method

* QuerySet API method를 사용해 다양한 조회를 하는 것이 중요
* QuerySet API method는 크게 2가지로 분류
  1. Methods that return new querysets
  2. Methods that do not return querysets

1. 현재 QuerySet의 복사본을 반환

![image-20220321232447355](Django2(Model).assets/image-20220321232447355.png)

​	전체 article 객체 조회

![image-20220321231212716](Django2(Model).assets/image-20220321231212716.png)

2. get()
   * 주어진 lookup 매개변수와 일치하는 객체를 반환
   * 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
   * 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유(unique)성을 보장하는 조회에서 사용해야 함

![image-20220321232927676](Django2(Model).assets/image-20220321232927676.png)

3. filter()
   * 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

![image-20220321233931494](Django2(Model).assets/image-20220321233931494.png)

#### str method

![image-20220321231857806](Django2(Model).assets/image-20220321231857806.png)

표준 파이썬 클래스의 메소드인 str()을 정의하여 각각의 object가 사람이 읽을 수 있는 문자열을 반환(return)하도록 할 수 있음 (주의! 작성 후 반드시 shell_plus를 재시작해야 반영됨)

#### UPDATE

article 인스턴스 객체의 인스턴스 변수의 값을 변경 후 저장

![image-20220324233208207](Django2(Model).assets/image-20220324233208207.png)

#### DELETE

* delete()
  * QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행하고, 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환

![image-20220324233350050](Django2(Model).assets/image-20220324233350050.png)

### 6.2. Field lookups

* 조회 시 특정 검색 조건을 지정
* QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인수로 지정됨
* 사용 예시)
  * Article.objects.filter(pk__gt=2)
  * Article.objects.filter(content__contains='ja')

### 6.3. QuerySet API

* 데이터베이스 조작을 위한 다양한 QuerySet API methods는 해당 공식문서를 반드시 참고하여 학습할 것
* https://docs.Djangoproject.com/en/3.2/ref/models/querysets/#queryset-api-reference

---

## 7. Admin Site

