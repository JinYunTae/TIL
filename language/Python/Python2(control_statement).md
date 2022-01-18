# Python의 제어문

파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령 수행

특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함

제어문은 순서도(flow chart)로 표현이 가능

## 조건문(Conditional Statement)

조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

### 기본 형식

expression에는 참/거짓에 대한 조건식

* 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭을 실행
* 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭을 실행 (선택적으로 활용 가능)

```python
if <expression == True> :
    #True Run Block
else :
    #False Run Block
```

> 예시
>
> ```python
> # 홀/짝 출력 프로그램
> num = int(input())
> if num % 2 : # if num % 2 == 1 :
>     print('홀수')
> else :
>     print('짝수')
> ```

### 복수 조건문

복수의 조건식을 활용할 경우 elif를 활용하여 포현함

```python
if <expression1> :
    #True1 Run Block
elif <expression2> :
    #True2 Run Block
else :
    #False Run Block
```

> 예시
>
> ```python
> dust = int(input())
> 
> if dust > 150 :
>     print('매우 나쁨')
> elif dust > 80 :			#	python 조건문엔 150 >= dust > 80과 같은 표현도 가능함!
>     print('나쁨')
> elif dust > 30 :
>     print('보통')
> else :
>     print('좋음')
> print('미세먼지 확인 완료!')
> ```

### 중첩 조건문

조건문은 다른 조건문에 중첩되어 사용될 수 있음

* 들여쓰기를 유의하여 작성할 것

```python
if <expression1> :
    #True1 Run Block
    if <expression2> :
        #True2 Run Block, 1참 -> 2참 이어야 동작
else :
    #False1 Run Block
```

> 예시
>
> ```python
> dust = int(input())
> 
> if dust > 150 :
>     print('매우 나쁨')
>     if dust > 300 :			#	150 초과일 때 300이 넘는다면 실행
>         print('실외 활동을 자제하세요.')
> elif dust > 80 :
>     print('나쁨')
> ...
> ```

### 조건 표현식

조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용

삼항 연산자(Ternary Operator)로 부르기도 함

```python
<true인 경우 값> if <expression> else <false인 경우 값>
<true1인 경우 값> if <expression1> else <true2인 경우 값> if <expression2> else <false인 경우 값> # 중첩표현식 but 가독성 안좋음... 비추
```

> 예시
>
> ```python
> value = num if num >= 0 else -num	#절대값을 value에 저장하는 조건문
> result = '홀수' if num % 2 else result = '짝수'	#	홀/짝 판별문
> print(result)
> ```

## 반복문

특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장

* while 문

  * 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 반복적으로 실행됨
  * 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
  * while문은 무한 루프를 하지 않도록 **종료조건이 반드시 필요**

  ```python
  while <expression> :
      #Run Block
  ```

* for 문

  * For문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable) 요소를 모두 순회하면 종료 (별도의 종료조건이 필요 없음)

  ``` python
  for <변수명> in <iterable> :
      #True Run Block
  else :                # 선택사항
      #False Run Block
  ```

  * Iterable

    * 순회할 수 있는 자료형(str, list, dict 등)

      * string 순회

      ```python
      string = input()
      for i in string :
          print(i)
          
      for i in range(len(string)) :
          print(string(i))
      ```

      * dictionary 순회

        ```python
        grades = {'john' : 80, 'eric' : 90}
        for student in grades :
            print(student, grades[student])
        ```

        * 추가 메서드를 활용해 순회
          * keys() : Key로 구성된 결과
          * values() : value로 구성된 결과
          * items() : (Key, value)의 튜플로 구성된 결과

        ```python
        grades = {'john' : 80, 'eric' : 90}
        for name, score in grades.items() :
            print(name, score)
        ```

      * enumerate 순회

        인덱스 개체를 쌍으로 담은 열거형(enumerate)객체를 반환

        (index, value) 형태의 tuple로 구성된 열거 객체를 반환

        > enumerate(iterable, start = 0)
        >
        > 열거 객체를 돌려줍니다. iterable은 시퀀스, 이터레이터 또는 이터레이션을 지원하는 다른 객체여야 합니다. enumerate() 에 의해 반환된 이터레이터의 `__next__()` 메서드는 카운트 (기본값 0을 갖는 start부터)와 Iterable을 이터레이션 해서 얻어지는 값을 포함하는 튜플을 돌려줍니다.
        >
        > ```python
        > seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        > >>>list(enumerate(seasons))
        > [(0,'Spring'), (1,'Summer'), (2,'Fall'), (3,'Winter')]
        > ```

    * List Comperehension

      표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

      ```python
      [<expression> for <변수> in <iterable>]
      [<expression> for <변수> in <iterable> if <조건식>]
      ```

      ```python
      [number ** 3 for number in range(1, 10) if number % 2] # 짝수만 3제곱하는 코드
      ```

    * 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법

      ```python
      {key:value for <변수> in <iterable> if <조건식>}
      ```

      ```python
      {number:number**3 for number in range(1,10)} # 1~10의 세제곱 결과가 담긴 dict
      ```

      

* 반복 제어

  * break

    * 반복문 종료

  * continue

    * continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

  * pass

    * 아무것도 하지 않음

      특별이 할 일이 없을 때 자리를 채우는 용도로 사용

      반복문 아니여도 사용 가능

  * for~else

    * 끝까지 반복문을 실행한 이후에 else문 실행

      break를 통해 중간에 종료되는 경우 else문 실행되지 않음