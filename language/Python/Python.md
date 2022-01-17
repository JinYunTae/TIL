# Python 기초

## 파이썬의 특징

* 파이썬(python)은 다른 프로그래밍 언어보다 문법이 간단하면서도 엄격하지 않음

  > ex) 변수에 별도의 타입 지정이 필요 없음

* 문법 표현이 매우 간결해서 프로그래밍 경험이 없어도 짧은 시간 내에 마스터 할 수 있음

  >ex) 문장을 구분할 때 중괄호 ({}) 대신 들여쓰기를 사용

* Expressive Language

  > ex) 같은 작업에 대해서도 C나 Java보다 더 간결하게 작성 가능
  >
  > ```C
  > # include<stdio.h>
  > 
  > int main (void) {
  >     printf("Hello World!");
  >     return 0;
  > }
  > ```
  >
  > ```java
  > public class HelloWorld {
  >     public static void main(String[] args) {
  >         System.out.println("Hello World!")
  >     }
  > }
  > ```
  >
  > ```python
  > print('Hello World!')
  > ```

* 크로스 플랫폼 언어

  윈도우즈(Windows), macOS, 리눅스(Linux), 유닉스(Unix) 등 다양한 운영체제에서 실행 가능

* 인터프리터 언어(Interpreter)

  * 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
  * 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음

* 객체 지향 프로그램(Object Oriented Programming)

  파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음

  객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것

  

## 파이썬 개발 환경

### 대화형 환경

* 파이썬 **기본 Interpreter** : IDLE (Intergrated Development and Learning Environment)
  * 내장 프로그램으로 파이썬 설치 시 기본적으로 설치 - 인터프리터가 대화형 모드로 동작함
  * 여러 줄의 코드가 작성되는 경우 보조 프롬프트(...)가 사용됨
  * 프롬프트(>>>)에 코드를 작성하면 해당 코드가 실행됨
  * Python이 설치된 환경에서는 기본적으로 활용 가능하나 디버깅 및 코드 편집, 반복 실행이 곤란
* **Jupyter Notebook** : 웹 브라우저 환경에서 코드를 작성할 수 있는 오픈소스
  * Syntax Highlighting, Indentation, Tab completion 등 편의 기능 제공
  * 브라우저에서 코드를 실행하고 결과를 확인할 수 있음
  * HTML, LaTeX, PNG, SVG을 바탕으로 다양한 표현이 가능
  * Markdown을 기반으로 문서 작성이 가능
  * 데이터분석/머신러닝/딥러닝 시 많이 활용 가능하며, Google colab 등 유사한 환경의 서비스도 있음
* **pycharm**
* **VS code**

### 스크립트 실행

파이썬 프로그램(.py) 파일을 작성하고, IDE 혹은 Text Editor 활용

## 기초문법

### 코드 스타일 가이드

코드를 **'어떻게 작성할지'**에 대한 가이드라인 - 일관적인 코드 작성스타일을 유지

* 파이썬에서 제안하는 스타일 가이드 : [PEP8](https://www.python.org/dev/peps/pep-0008/)
* 기업, 오픈소스 등에서 사용되는 스타일 가이드 : [Google Style guide](https://google.github.io/styleguide/pyguide.html) 등

### 들여쓰기(Identation)

Space Sensitive

* 문장을 구분할 때, 중괄호({}) 대신 <들여쓰기(indentation)>를 사용
* 들여쓰기 할 때는 4칸(space 4번) 혹은 1탭(Tab 1번)을 입력
  * 주의! 한 코드 안에서는 반드시 한 종류의 들여쓰기만 사용 - 혼용하면 안됨
  * 원칙적으로는 공백(빈칸, space) 사용을 권장 (PEP8)

### 변수

컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

* 파이썬은 객체지향 언어로 모든것이 객체로 구현되어 있음

* 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에, 즉, 참조하는 객체가 바뀔 수 있기 때문에 '변수'라고 불림

* 변수는 할당 연산자(=)를 통해 값을 할당(assignment)

  * type() : 변수에 할당된 값의 타입
  * id() : 변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리주소

* 변수 할당

  * 같은 값을 동시에 할당할 수 있음

  ```python
  x = y = 1004
  print(x, y)	>>>	1004 1004
  ```

  * 다른 값을 동시에 할당할 수 있음(multiple assignment)

  ```python
  x, y = 1, 2	#	x, y = (1, 2)와 동일, 언패킹 이용
  print(x, y)	>>> 1 2
  x, y = y, x	# 서로 값 바꾸기도 가능
  print(x, y)	>>> 2 1
  ```

  ​	다른 값의 동시 할당은 튜플을 이용하는 방식 - 인자의 수가 다르면 에러 발생

* 변수 연산

  ```python
  i = 5 ; j = 3; s = '파이썬'
  
  i + j	>>> 8
  
  i * j / 3	>>> 5.0
  
  i = i - j
  print(i)	>>>	2
  
  j = -2
  i * j	>>>	-4
  
  '안녕' + s	>>>	'안녕파이썬'		#문자열에 대한 연산도 가능
  
  s = s * 3
  print(s)	>>>	'파이썬파이썬파이썬'
  
  s = 'Python'
  s + ' is fun'	>>>	'Python is fun'
  ```

### 식별자(Identifiers)

파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name)

규칙

* 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성

* 첫 글자에 숫자가 올 수 없음

* 길이제한이 없고, 대소문자를 구별

* 다음의 키워드(keywords)는 예약어(reserved words)로 사용할 수 없음

  ```python
  False, None, True, __peg_parser__, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
  ```

  이들 키워드들은 내장함수나 모듈 등의 이름으로도 만들면 안됨 - 기존 이름에 다른 값을 할당하게 되므로 더 이상 동작하지 않게 됨

### 사용자 입력

사용자로부터 값을 즉시 입력 받을 수 있는 내장함수

```python
input([prompt])
```

* 대괄호 부분에 문자열을 넣으면 입력 시, 해당 문자열을 출력할 수 있음
* 반환값은 항상 **문자열**의 형태로 변환

### 주석(Comment)

코드에 대한 설명

* 중요한 점이나 다시 확인해야 하는 부분을 표시
* 컴퓨터는 주석을 인식하지 않음, 사용자만을 위한 것
* 개발자에게 주석을 다는 습관은 매우 중요
* 쉬운 이해와 코드의 분석 및 수정이 용이
  * 주석은 코드 실행에 영향을 미치지 않을 뿐만 아니라 프로그램의 속도, 용량에도 영향 없음

한 줄 주석

* 주석으로 처리될 내용 앞에 **#**을 입력
* 한 줄을 온전히 사용할 수도 있고, 그 줄 코드 뒷부분에 작성할 수 있음

``` python
# 이름을 출력합니다.
print('홍길동') # 이름은 홍길동
```

여러 줄의 주석

* 한 줄씩 **#**을 사용하거나 '''또는 """으로 표현
  * '''또는 """으로 표현하는 방법은 docstirng을 위해 사용
  * docstring은 함수/클래스의 설명을 작성하는데 사용

## 자료형(Datatype)

