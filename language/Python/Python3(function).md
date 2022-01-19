# Python의 함수

## 함수 기초

함수란? - 특정한 기능을 하는 코드의 조각(묶음)

특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

MEME : E = mc^2, error는 (more code)^2에 비례한다.

* 사용자 함수(Custom Function)

  구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능

  ```python
  def function_name (parameter) :
      # code block
      return returning_value
  ```

* 함수를 사용해야 하는 이유

  > 표준편차를 구하는 코드

  ```python
  values = [100, 75, 85, 90, 65, 95, 90, 60, 85, 50, 90, 80]
  
  total = 0
  cnt = 0
  
  for value in values :
      total += value
      cnt += 1
      
  mean = total / cnt
  
  total_var = 0
  
  for value in values :
      total_var += (value - mean) ** 2
      
  sum_var = total_var / cnt
  
  target = sum_var
  
  count = 0
  
  while True :
      count += 1
      root = 0.5 * (target + (sum_var / target))
      if (abs(root - target) < 1e-10) :
          break
      target = root
      
  std_dev = target
  print(std_dev)    # 재사용이 가능한가? - 불가!
  ```

  내장함수(Built-in Function) 활용

  ```python
  import math
  values = [100, 75, 85, 90, 65, 95, 90, 60, 85, 50, 90, 80]
  cnt = len(values)
  mean = sum(values) / cnt
  sum_var = sum(pow(value - mean, 2) for value in values) / cnt
  std_dev = math.sqrt(sum_var)
  print(std_dev)    # 훨씬 간편!
  ```

  전용 기능의 함수를 쓰면?

  ```python
  import statistics
  values = [100, 75, 85, 90, 65, 95, 90, 60, 85, 50, 90, 80]
  statistics.pstdev(values)    # 매우 간편!
  ```

  코드 중복 방지 and 재사용 용이!

* 함수 기본 구조

  > pstdev 함수

  ![image-20220119092416087](Python3(function).assets/image-20220119092416087.png)

  ![image-20220119092737810](Python3(function).assets/image-20220119092737810.png)

  * 선언과 호출(define & call)
  * 입력(Input)
  * 문서화(Doc-string)
  * 범위(Scope)
  * 결과값(Output)

  ## 함수의 선언과 호출(define & call)

* **함수의 선언**은 **def**  키워드를 활용함

  들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함

  * Docstring은 함수 body 앞에 선택적으로 작성 가능
  * 작성시에는 반드시 첫 번째 문장에 문자열 `''' '''`

  함수는 parameter를 넘겨줄 수 있음

  함수는 동작 후에 return을 통해 결과값을 전달함

* 함수는 **함수명()으로 호출** - 이름()의 형태는 모두 함수였다

> 예시

```python
num1 = 0
num2 = 1

def func1(a, b) :
    return a + b

def func2(a, b) :
    return a - b

def func3(a, b) :
    return func1(a, 5) + func2(5, b)

result = func3(num1, num2)
print(result)    # 9가 출력됨
```

함수는 호출되면 코드를 실행하고 return 값을 반환하며 종료된다.

> 실습문제

* 입력 받은 수를 세제곱하여 반환하는 함수 cube를 작성하시오.

  ```python
  def cube(n) :
      return n ** 3
  
  num = int(input())
  print(cube(num))
  ```

* 함수 cube를 활용하여 2의 세제곱, 100의 세제곱을 구하시오.

  ```python
  print(cube(2), cube(100))
  ```

## 함수의 결과(Output)

* Void function

  명시적인 return 값이 없는 경우, None을 반환하고 종료

  ```python
  #Void function
  a = print('hello')    # hello 출력 됨
  print(a)    # print()의 반환값 None출력 됨
  ```

  

* Value returning function

  함수 실행 후, return문을 통해 값 반환

  return을 하게 되면, 값 반환 후 함수가 바로 종료

  ```python
  # Value returning function
  b = float('3.14')    # 3.14를 반환해서 할당
  ```

주의! return vs. print

​	return은 함수 안에서만 사용되는 **키워드**

​	print는 출력을 위해 사용된느 **함수**

​	REPL(Read-Eval-Print Loop) 환경에서는 마지막으로 작성된 코드의 리턴값을 보여준다. print 된 것이 아님!

* 두 개 이상의 값 반환

  ```python
  def minus_and_plus(x, y) :
      return x - y
  	return x + y
  ```

  함수는 return 후 종료되므로 3행의 return은 실행불가

  => 함수는 항상 단일한 값만을 반환한다

  => return문을 한번만 사용해서 두 개 이상의 값을 반환하는 방법은?

  ```python
  def minus_and_plus(x, y) :
      return x - y, x + y
  ```

  위 코드는 x-y와 x+y를 튜플 형식으로 반환하게 된다!

> 실습문제

* 너비와 높이를 입력 받아 사각형의 넓이와 둘레를 튜플로 반환하는 함수 rectangle을 작성하시오.

  ```python
  def rectangle (width, height) :
      area = width * height
      round = 2 * (width + height)
      return area, round
  ```

  

* 함수 rectangle을 활용하여 아래의 사각형의 넓이와 둘레를 구하시오.

  ```python
  sq_area, sq_length = rectangle(30, 20)
  ```

  

## 함수의 입력(Input)

* Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자

* Argument : 함수를 호출할 때, parameter를 통해 전달되는 값

  ​	Argument는 소괄호 안에 할당 func_name(argument)

  * 필수 Argument : 반드시 전달되어야 하는 argument
  * 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

  ```python
  def say_anything(anything) :	# parameter = say_ anything
      print(f'hello {anything}')
      
  say_anything('python')			# argument = 'python'
  ```

  1. Positional Arguments (위치 인자)

     기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

     ```python
     def add (x, y) :
         return x + y
     
     add(2, 3)    # x = 2, y = 3으로 대입 됨
     ```

  2. Keyword Arguments (키워드 인자)

     직접 변수의 이름으로 특정 Argument를 전달할 수 있음

     ```python
     def add (x, y) :
         return x + y
     
     add(x=2, y=5)    # 이름을 지정해 전달
     add(2, y=5)    # positional 다음에 keyword 사용
     ```

     **주의!**

     Keyword Argument 다음에 Positional Argument를 활용할 수 없음

     ```python
     add(x=2, 5)    # 에러 발생!!
     ```

     SyntaxError : positional argument follows keyword argument

  3. Default Atguments Values (기본 인자 값)

     기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함

     ​	정의된 것 보다 더 적은 개수의 argument들로 호출 될 수 있음

     ```python
     def add (x, y=0) :
         return x + y
     
     add(2)    # y=0이 기본이라 따로 전달 안해도 됨
     ```

     **주의!** 

     기본 argument 값을 가지는 argument 다음에 기본 값이 없는 argument로 정의 할 수 없음!

     ```python
     def add (x=0, y) :    # 에러 발생!!
         return x + y
     ```

     SyntaxError : non-default argument follows default argument

**keyword(키워드) 인자는 호출 / default(기본값) 인자는 선언!**

### 정해지지 않은 여러 개의 Arguments 처리

* **Positional** Arguments **Packing/Unpacking**

  연산자 (*)를 이용, 여러개의 Positional Atgument를 하나의 필수 parameter로 받아서 사용 (튜플로 받게 됨)

  몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

  ```python
  def add (*args) : # 튜플로 받는다.
      for arg in args :
          print(arg)
  
  add(2)
  add(2, 3, 4, 5)
  ```

* **Keyword** Arguments **Packing/Unpacking**

  함수가 임의의 개수 Argument를 Keyword Argument로 호출될 수 있도록 지정

  Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현

  ```python
  def family(**kwargs) :
      for key, value in kwargs :
          print(key, ':', value)
          
  family(father = 'John', mother = 'Jane', me='John Jr.')
  ```

> 실습 문제

* *args와 *kwargs를 각각 활용하여 함수를 정의해보고 type을 출력해보시오.

```python
def args_type (*args) :
    print(type(args))

def kwargs_type (**kwargs) :
    print(type(kwargs))

args_type(1, 2, 3)
kwargs_type('1' = 2, '2' = 3)
```

<class 'tuple'> <class'dict'>

* python 표준 라이브러리, 외부 라이브러리 소스코드나 문서 등을 살펴보고 함수가 어떻게 정의 되어 있는지 살펴 보시오.

## 함수의 범위(Scope)

함수는 코드 내부에 **local scope**를 생성하며, 그 외의 공간인 **global scope**로 구분

* scope
  * global scope : 코드 어디에서든 참조할 수 있는 공간
  * local scope : 함수가 만든 scope, 함수 내부에서만 참조 가능
* variable
  * global variable : global scope에 정의된 변수
  * local variable : local scope에 정의된 변수

### 변수 수명주기(lifecycle)

변수는 각자의 수명주기(lifecycle)가 존재

* built-in-scope

  파이썬이 실행된 이후부터 영원히 유지

* global scope

  모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지

* local scope

  함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

```python
def func() :
    a = 20    # 함수 종료(return) 후 수명주기 종료
    print('local', a)
    
func()
print('global', a)    # a는 Local scope에서만 존재
```

local 20만 출력됨

### 이름 검색 규칙(Name Resolution)

파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음

아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름

* Local scope : 함수
* Enclosed scope : 특정 함수의 상위 함수
* Global scope : 함수 밖의 변수, import 모듈
* Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

**즉, 함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음**

> LEGB 예시

```python
a = 0
b = 1
def enclosed() :
    a = 10
    c = 3
    def local(a, b, c) :
        print(a, b, c)
    local(300)
    print(a, b, c)
enclosed()
print(a, b)
```

10(E) 1(G) 300(L)

10(E) 1(G) 3(E)    # ()는 참조된 변수의 scope

0(G) 1(G)

### global 문

현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global variable임을 나타냄

* global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
* global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함

> 예시

```python
a = 10
def func() :
    global a
    a = 3

print(a)    # 10
func()
print(a)    # 3
```

Local scope에서 global 변수 값의 변경

global 키워드를 사용하지 않으면, Local scope에 a 변수가 생성됨

> global 관련 에러

```python
a = 10
def func () :
    print(a)    # global 하기 전에 a라는 이름이 사용됨
    global a
    a = 3
    
print(a)    # 10
func()    # 에러 발생!!
print(a)
```

```python
a = 10
def func(a) :    # a가 parameter랑 global로 중복됨
    global a
    a = 3
    
print(a)
func(3)    # 에러 발생!!
print(a)
```

### nonlocal

global을 제외하고 가장 가까운 (둘러 싸고 있는) scope의 변수를 연결하도록 함

* nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
* nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함

**global과 달리 이미 존재하는 이름과의 연결만 가능**

> 예시

```python
x = 0
def func1() :
    x = 1
    def func2() :
        nonlocal x
        x = 2    # enclosed scope(func1)의 변수x의 변경
    func2()
    print(x)
    
func1()
print(x)
```

2(E)

0(G)



> nonlocal, global 비교

```python
def func1 () :
    global out    # 선언된 적 없는 변수
    out = 3

func1()
print(out)    # 3출력 됨
#------------------------------------------
def func2 () :
    def func3() :
        nonlocal y    # 선언된 적 없는 변수, 에러 발생!!
        y = 2    # SyntaxError : no binding for nonlocal 'y' found
    func3()
    print(y)
    
func2()
```

nonlocal은 이름공간상에 존재하는 변수만 가능

### 정리

* 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라짐
* 해당 scope에 변수가 없는 경우 LEGB rule에 의해 이름을 검색함
  * 변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없음
  * 값을 할당하는 경우 해당 scope의 이름 공간에 새롭게 생성되기 때문
  * **단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것 (클로저* 제외)**
    * (참고) 클로저 : 어떤 함수 내부에 중첩된 형태로써 외부 scope 변수에 접근 가능한 함수
* 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능
  * 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류가 발생
  * 가급적 사용하지 않는 것을 권장하며, **함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값을 사용하는 것을 추천**

### 범위 확인하기

globals와 locals()

* namespace (global, local, builtin)을 딕셔너리(dict)로 정리
  * locals() : locals()가 실행되는 함수 내의 local namespace 들을 정리
  * globals() : global, local, builtin 정보 모두 dict 형태로 정리

> 예시코드

```python
a_var = range(2)
def locals_test () :
    b_var = 3
    c_var = locals()
    print(c_var)    # locals_test의 local 이름공간 출력
locals_test()
d_var = globals()
print(d_vars)    # global의 이름공간 출력
```

## 함수의 문서화(Doc-string)

함수나 클래스의 설명

### Naming Convention

좋은 함수와 parameter 이름을 짓는 방법

* 상수 이름은 영문 전체를 대문자
* 클래스 및 예외의 이름은 각 단어의 첫 글자만 영문 대문자
* 이외 나머지는 소문자 또는 밑줄로 구분한 소문자 => 함수

* 스스로를 설명
  * 함수의 이름만으로 어떠한 역할을 하는 함수인지 파악 가능해야 함
  * 어떤 기능을 수행하는지, 결과 값으로 무엇을 반환하는지 등
* 약어 사용을 지양
  * 보편적으로 사용하는 약어를 제외하고 가급적 약어 사용을 지양

## 함수의 응용

### 내장 함수(Built-in Functions)

파이썬 인터피리터에는 항상 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음

### map

``` python
map(function, iterable)
```

순회 가능한 데이터 구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과를 map object로 반환

```python
numbers = [1, 2, 3]
result = map(str, numbers)
print(result, type(result))
```

`<map object at 0x9자리16진수값>` <class 'map'>

```python
list(result)    # 리스트 형변환을 통해 결과 직접 확인
```

['1', '2', '3']

> 활용 사례

알고리즘 문제 풀이 시 input 값들을 숫자로 바로 활용하고 싶을 때

```python
n, m = map(int, input().split())
```

3 5

```python
print(n, m)
print(type(n), type(m))
```

3 5

<class 'int'> <class 'int'>

### filter

```python
filter(function, iterable)
```

순회 가능한 데이터 구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과가 True인 것들을 filter object로 반환

``` python
def add (n) :
    return n % 2
numbers = [1, 2, 3]
result = filter[add, numbers]
print(result, type(result))
```

`<filter object at 0x9자리16진수값>` <class 'filtre'>

``` python
list(result)    # 리스트 형변환을 통해 결과 직접 확인
```

[1, 3]

### zip

``` python
zip(*iterables)
```

복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls = ['jane', 'ashley']
boys = ['eric','justin']
pair = zip(girls, boys)
print(pair, type(pair))
```

`<zip object at 0x9자리16진수값>` <class 'zip'>

```python
list(pair)    # 리스트 형변환을 통해 결과 직접 확인
```

[('jane', 'eric'), ('ashley', 'justin')]

### lambda 함수

```python
lambda [parameter] : 표현식
```

표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림

* 특징
  * return문을 가질 수 없음
  * 간편 조건문 외 조건문이나 반복문을 가질 수 없음
* 장점
  * 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  * def를 사용할 수 없는 곳에서도 사용 가능

> 예시

```python
# 삼각형의 넓이를 구하는 공식 - def
def triangle_area (b, h) :
    return 0.5 * b * h
trianlge_area(5, 6)
```

15.0

```python
# 삼각형의 넓이를 구하는 공식 - 람다
triangle_area = lambda b, h : 0.5 * b * h
triangle_area(5, 6)
```

15.0

### 재귀함수(recursive function)

자기 자신을 호출하는 함수

* 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
  * 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음(ex. 점화식)
  * 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
* 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

> 예시

```python
# Factorial
# n! = n * (n-1)! = n * (n-1) * (n-2)
def factorial (n) :
    if n == 0 or n == 1 :
        return 1
    else :
        return n * factorial(n-1)

factorial(4)
```

24

### 재귀 함수 주의사항

* 재귀 함수는 base case에 도달할 때까지 함수를 호출함
* 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨
* 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Error발생

### 반복문과의 비교

``` python
# 반복문으로도 작성 가능
def fact (n) :
    result = 1
    while n > 1 :
        result *= n
        n -= 1
    return result
```

* 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용함
* 재귀 호출은 변수 사용을 줄여줄 수 있음
* 재귀 호출은 입력값이 커질 수록 연산 속도가 오래 걸림