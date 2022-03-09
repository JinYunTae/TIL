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

* DateTimeField(auto_now_add=True)
* DateTimeField(auto_now=True)