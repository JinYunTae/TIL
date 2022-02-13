# CSS

CSS : Cascading Style Sheets

* CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
* 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
* 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  * 속성 (Property) : 어떤 스타일 기능을 변경할지 결정
  * 값 (Value) : 어떻게 스타일 기능을 변경할지 결정

**CSS 구문** - 용어 정리

![image-20220210221524532](CSS.assets/image-20220210221524532.png)

<hr>

## 1. CSS 정의 방법

* 인라인(inline)

  ![image-20220210221957894](CSS.assets/image-20220210221957894.png)

* 내부 참조(embedding) - `<style>`

  ![image-20220210222055833](CSS.assets/image-20220210222055833.png)

  ![image-20220210222247622](CSS.assets/image-20220210222247622.png)

* 외부 참조(link file) - 분리된 CSS 파일

  ![image-20220210222127914](CSS.assets/image-20220210222127914.png)

  ![image-20220210222339317](CSS.assets/image-20220210222339317.png)

**TIP : 주로 활용하는 속성 위주로 기억하자!**

#### CSS with 개발자 도구

* style : 해당 요소에 선언된 모든 CSS
* computed : 해당 요소에 최종 계산된 CSS

<hr>

## 2. CSS Selectors

### 2.1. 선택자(Selector) 유형

* 기본 선택자
  * 전체 선택자, 요소 선택자
  * 클래스 선택자, 아이디 선택자, 속성 선택자
* 결합자(Combinatiors)
  * 자손 결합자, 자식 결합자
  * 일반 형제 결합자, 인접 형제 결합자
* 의사 클래스/요소(Pseudo Class)
  * 링크, 동적 의사 클래스
  * 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

#### 선택자 with 개발자 도구

* #sect1 > ul > li:nth-child(1)

  ![image-20220210223335812](CSS.assets/image-20220210223335812.png)

![image-20220210223432000](CSS.assets/image-20220210223432000.png)

#### VScode에서 직접 해보기

![image-20220210223527656](CSS.assets/image-20220210223527656.png)

### 2.2. CSS 선택자 정리

* 요소 선택자
  * HTML 태그를 직접 선택
* 클래스(class) 선택자
  * 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
* 아이디(id) 선택자
  * `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  * 일반적으로 하나의 문서에 1번만 사용. 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장

### 2.3. CSS 적용 우선순위 (cascading order) !!

* CSS 우선순위를 아래와 같이 그룹을 지어볼 수 있다
  1. 중요도 (Importance) - 사용시 주의
     * !important
  2. 우선 순위 (Specificity)
     * 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
  3. CSS파일 로딩 순서

#### Quiz

![image-20220210224346475](CSS.assets/image-20220210224346475.png)

ANS.

![image-20220210224637630](CSS.assets/image-20220210224637630.png)

### 2.4. CSS 상속 (MDN에도 추가로 확인!)

* CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다

  * 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다

  * 상속 되는 것 예시

    예) Text 관련 요소(font, color, text-align), opacity, visibility 등

  * 상속 되지 않는 것 예시

    예) Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)

    ​	  position 관련 요소(position, top/right/bottom/left, z-index) 등

#### VScode에서 직접해보기

![image-20220210225455619](CSS.assets/image-20220210225455619.png)

<hr>

## 3. CSS 기본 스타일

### 3.1. 크기 단위

* px(픽셀)
  * 모니터 해상도의 한 화소인 '픽셀' 기준
  * 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
* %
  * 백분율 단위
  * 가변적인 레이아웃에서 자주 사용
* em
  * (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  * 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
* rem
  * (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  * 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
* viewport
  * 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역 (디바이스 화면)
  * 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  * vw, vh, vmin, vmax

#### VScode에서 직접해보기

![image-20220210230034900](CSS.assets/image-20220210230034900.png)

#### 크기 단위 em vs rem

![image-20220210230221448](CSS.assets/image-20220210230221448.png)

![image-20220210230140696](CSS.assets/image-20220210230140696.png)

### 3.2. 색상 단위

* 색상 키워드
  * 대소문자를 구분하지 않음
  * red, blue, black과 같은 특정 색을 직접 글자로 나타냄
* RGB 색상
  * 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
* HSL 색상
  * 색상, 채도, 명도를 통해 특정 색을 표현하는 방식

![image-20220210230511134](CSS.assets/image-20220210230511134.png)

### 3.3. CSS 문서 표현 - 추후에 하나씩

* 텍스트
  * 서체, 서체 스타일
  * 자간, 단어 간격, 행간, 들여쓰기 등
* 컬러(color), 배경(background-image, background-color)
* 기타 HTML 태그별 스타일링
  * 목록(li), 표(table)

<hr>

## 4. Selectors 심화

