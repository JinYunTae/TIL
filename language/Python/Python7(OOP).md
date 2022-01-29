# Python 객체지향 프로그래밍

## 객체지향 프로그래밍(OOP, Object Oriented Programming)

### 객체

파이썬은 모두 객체(object)로 이뤄져 있다

객체는 특정 타입의 인스턴스(instance) 이다.

* 123, 900, 5는 모두 int의 인스턴스
* 'hello', 'bye'는 모두 string의 인스턴스
* [232, 89, 1], []은 모두 list의 인스턴스

#### 객체의 특징

* 타입(type) : 어떤 연산자(operator)와 조작(method)가 가능한가?
* 속성(attribute) : 어떤 상태(데이터)를 가지는가?
* 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

> Python의 객체와 클래스
>
> 객체(Object) = 속성(Attribute) + 기능(Method)

### 객체지향 프로그래밍

프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

> 예시(시각화)
>
> 콘서트 - 가수 객체, 감독 객체, 관객 객체

#### cf) 절차지향 프로그래밍

* 절차지향 프로그래밍

  데이터와 함수로 인한 변화

![image-20220127104109065](Python7(OOP).assets/image-20220127104109065.png)

* 객체지향 프로그래밍

  데이터와 기능(메소드) 분리, 추상화 된 구조(인터페이스)

  ![image-20220127104600779](Python7(OOP).assets/image-20220127104600779.png)

### 객체지향 프로그래밍이 필요한 이유

* 현실 세계를 프로그램 설계에 반영(추상화)

  > ```python
  > class Person:
  >     
  >     def __init__(self, name, gender) :
  >         self.name = name
  >         self.gender = gender
  >         
  >     def greeting(self) :
  >         print(f'안녕하세요, {self.name}입니다.')
  > ```
  >
  > ```python
  > jimin = Person('지민', '남')
  > jimin.greeting()
  > ```
  >
  > 안녕하세요, 지민입니다.
  >
  > ```python
  > jieun = Person('아이유', '여')
  > jieun.greeting()
  > ```
  >
  > 안녕하세요, 아이유입니다.

<예시코드>

* 절차지향 프로그래밍

>```python
>a = 10
>b = 30
>square1_area = a * b
>square_circumferene = 2 * (a + b)
>
>c = 300
>d = 20
>square2_area = c * d
>square_circumference = 2 * (c + d)
>```
>
>각 경우에 대해 따로 작성해야 함
>
>```python
>def area(x, y) :
>    return x * y
>
>def circumference(x, y) :
>    return 2 * (x + y)
>
>a = 10
>b = 30
>c = 300
>d = 20
>square1_area = area(a, b)
>square1_circumference = circumference(a, b)
>square2_area = area(c, d)
>square2_circumference = circumference(c, d)
>```
>
>함수를 쓰더라도 따로 모두 작성해야 함

* 객체지향 프로그래밍

>```python
>class Rectangle:
>    def __ init__(self, x, y) :
>        self.x = x
>        self.y = y
>    
>    def area(self) :
>        return self.x * self.y
>    
>    def circumference(self) :
>        return 2 * (self.x + self.y)
>
>r1 = Rectangle(10, 30)
>r1.area()
>r1.circumference()
>
>r2 = Rectangle(300, 20)
>r2.area()
>r2.circumference()
>```
>
>객체화와 메소드를 이용해 간단하게 복제하고 구할 수 있다.
>
>위의 예제에서
>
>* 사각형 - 클래스(class)
>* 각 사각형(R1, R2) - 인스턴스(instance)
>* 사각형의 정보 - 속성(attribute)
>  * 가로 길이, 세로 길이
>* 사각형의 행동 - 메소드(method)
>  * 넓이를 구한다. 높이를 구한다.

### 객체지향의 장점(위키피디아)

* 객체 지향 프로그래밍은 **프로그램을 유연하고 변경이 용이**하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용된다.
* 또한, 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며, 보다 **직관적인 코드 분석**을 가능하게 하는 장점을 가지고 있다.

## OOP 기초

### 기본 문법

```python
class MyClass :    # 클래스 정의
'''
클래스명은 각 단어의 첫 글자를 대문자로 = Pascal case(Upper Camel case)
/ 첫 글자가 소문자면 lower camel case 주로 얘기하는 camel case
'''
my_instance = MyClass()    # 인스턴스 생성
my_instance.my_method()    # 메소드 호출
my_instance.my_attribute    # 속성
```

### 클래스와 인스턴스

객체의 틀(클래스)을 가지고, 객체(인스턴스)를 생성한다.

> 예시
>
> Person(클래스) -> 가수 이지은(인스턴스), 감독 강해피(인스턴스), 팬 김빅팬 ...
>
> 여러 객체들을 생성하는 기본 틀로 사용 가능

* 클래스 : 객체들의 분류(class)
* 인스턴스 : 하나하나의 실체 / 예(instance)

> ```python
> class Person:
>     pass
> ```
>
> ```python
> type(Person)
> ```
>
> type
>
> ```python
> person1 = Person()
> isinstance(person1, Person)
> ```
>
> True
>
> ```python
> type(person1)
> ```
>
> `__main__`.Person
>
> 파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스

* 속성 : 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미

> ```python
> class Person:
>     
>     def __init__(self, name):
>         self.name = name
> ```
>
> ```python
> person1 = Person('지민')
> ```
>
> ```python
> person1.name
> ```
>
> '지민'

* 메소드 : 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)

> ```python
> class Person:
>     
>     def talk(self):
>         print('안녕')
>         
>    	def eat(self, food):
>         print(f'{food}를 냠냠')
> ```
>
> ```python
> persona1 = Person()
> ```
>
> ```python
> person1.talk()
> ```
>
> 안녕
>
> ```python
> person1.eat('피자')
> ```
>
> 피자를 냠냠
>
> ```python
> person1.eat('치킨')
> ```
>
> 치킨을 냠냠

### 객체 비교하기

* ==
  * 동등한(equal)
  * 변수가 참조하는 객체가 동등한(내용이 같은)  경우 True
  * 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
* is
  * 동일한(identical)
  * 두 변수가 동일한 객체를 가리키는 경우 True

## 인스턴스

### 인스턴스 변수

* 인스턴스 변수
  * 인스턴스가 개인적으로 가지고 있는 속성(attribute)
  * 각 인스턴스들의 고유한 변수
* 생성자 메소드에서 `self.변수명`으로 정의

* 인스턴스가 생성된 이후 `인스턴스명.변수명`으로 접근 및 할당

>```python
>class Person:
>    
>    def __init__(self, name):
>        self.name = name
>```
>
>```python
>john = Person('john')
>```
>
>```python
>print(john.name)
>```
>
>john
>
>```python
>john.name = 'John Kim'
>```
>
>```python
>print(john.name)
>```
>
>John Kim

### 인스턴스 메소드

* 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
* 클래스 내부에 정의되는 메소드의 기본
* 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

> ```python
> class MyClass:
>     
>     def instance_method(self, arg1, ...):
> ```
>
> ```python
> my_instance = MyClass()
> my_instance.instance_method(...)
> ```

### self

* 인스턴스 자기자신
* 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
  * 매개변수 이름으로 self를 첫번째 인자로 정의
  * 다른 단어로 써도 작됭하지만, 파이썬의 암묵적인 규칙

### 생성자(constructor) 메소드

* 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
* 인스턴스 변수들의 초깃값을 설정
  * 인스턴스 생성
  * `__init__`메소드 자동 호출

> ```python
> class Person:
>     
>     def __init__(self):
>         print('인스턴스가 생성되었습니다.')
> ```
>
> ```python
> person1 = Person()
> ```
>
> 인스턴스가 생성되었습니다.
>
> ```python
> class Person:
>     
>     def __init__(self, name):
>         print(f'인스턴스가 생성되었습니다. {name}')
> ```
>
> ```python
> person1 = Person('지연')
> ```
>
> 인스턴스가 생성되었습니다. 지연

### 소멸자(destructor) 메소드

* 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드

> ```python
> class Person:
>     
>     def __del__(self):
>         print('인스턴스가 사라졌습니다.')
> ```
>
> ```python
> person1= Person()
> del persona1
> ```
>
> 인스턴스가 사라졌습니다.

### 매직 메소드

* Double underscore(__)가 있는 메소드는 특수한 동작을 위해 만들어진 메소드로, 스페셜 메소드 혹은 매직 메소드라고 불림
* 특정 상황에 자동으로 불리는 메소드

>* `__str__(self)`, `__len__`(self), `__repr__`(self)
>
>* `__lt__`(self, other), `__le__`(self, other), `__eq__`(self, other)
>
>* `__gt__`(self, other), `__ge__`(self, other), `__ne__`(self, other)

* `__str__` : 해당 객체의 출력 형태를 지정
  * 프린트 함수를 호출할 때, 자동으로 호출
  * 어떤 인스턴스를 출력하면 `__str__`의 return값이 출력
* `__gt__` : 부등호 연산자(>, greater than)

<예시코드>

>```python
>class Circle:
>    
>    def __init__(self, r):
>        self.r = r
>    
>    def area(self):
>        return 3.14 * self.r * self.r
>    
>    def __str__(self):
>        return f'[원] radius: {self.r}'
>    
>    def __gt__(self, other):
>        return self.r > other.r
>```
>
>```python
>c1 = Circle(10)
>C2 = Circle(1)
>```
>
>```python
>print(c1)
>```
>
>[원] radius: 10
>
>```python
>print(c2)
>```
>
>[원] radius: 1
>
>```python
>c1 > c2
>```
>
>True
>
>```python
>c1 < c2
>```
>
>False

## 클래스

### 클래스 변수

* 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성(클래스 내의 local변수?)

​	클래스 이름 대신 인스턴스 이름을 쓰게되면 인스턴스 변수가 된다.

* 클래스 속성(attribute)
  * 한 클래스 내의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성
* 클래스 선언 내부에서 정의
* `클래스명.변수명`으로 접근 및 할당

> ```python
> class Circle:
>     pi = 3.14
> ```
>
> ```python
> c1 = Circle()
> c2 = Circle()
> ```
>
> ```python
> print(Circle.pi)
> print(c1.pi)
> print(c2.pi)
> ```
>
> 3.14
>
> 3.14
>
> 3.14

### 클래스 메소드

* 클래스가 사용할 메소드
* @classmethod 데코레이터를 사용하여 정의
  * 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
* 호출 시, 첫번째 인자로 클래스(cls)가 전달됨

> ```python
> class MyClass:
>     
>     @classmethod
>     def class_method(cls, arg1, ...):
>         pass
> ```
>
> ```python
> Myclass.class_method(...)    # 클래스명.메소드명()
> ```

### 스태틱 메소드

* 스태틱 메소드
  * 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드
* 언제 사용하는가?
  * 속성을 다루지 않고 단지 기능(행동)만을 하는 메소드를 정의할 때, 사용

* 클래스가 사용할 메소드
* @staticmethod 데코레이터를 사용하여 정의
* 호출 시, 어떠한 인자도 전달되지 않음(클래스 정보에 접근/수정 불가)

> ```python
> class MyClass:
>     
>     @staticmethod
>     def static_method(arg1, ...):
>         pass
> ```
>
> ```python
> MyClass.static_method(...)    # 클래스명.메서드명(), 외부 인자를 받는 것은 된다.
> ```

### 인스턴스와 클래스 간의 이름 공간(namespace)

* 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
* 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
* 인스턴스에서 특정 속성에 접근하면, 인스턴스- 클래스 순으로 탐색

![image-20220127210802537](Python7(OOP).assets/image-20220127210802537.png)

> ```python
> # Person 정의
> class Person:
>     name = 'unknown'
>     
>     def talk(self):
>         print(self.name)
> ```
>
> ```python
> p1 = Person()    # p1은 인스턴스 변수가 정의되어 있지 않아 클래스 변수(Unknown)가 출력됨
> p1.talk()
> ```
>
> unknown
>
> ```python
> # p2 인스턴스 변수 설정 전/후
> p2 = Person()
> p2.talk()    # p2는 인스턴스 변수가 정의되어 인스턴스 변수(Kim)가 출력됨
> p2.name = 'Kim'
> p2.talk()
> ```
>
> ```python
> print(Person.name)
> pritn(p1.name)    # Person 클래스의 값이 Kim으로 변경된 것이 아닌 p2 인스턴스 이름 공간에 name이 Kim으로 지정
> print(p2.name)
> ```
>
> unknown
>
> nuknown
>
> Kim
>
> ![image-20220127211529564](Python7(OOP).assets/image-20220127211529564.png)

### 정리

* 클래스 구현
  * 클래스 정의
  * 데이터 속성 정의(객체의 정보는 무엇인지)
  * 메서드 정의(객체를 어떻게 사용할 것인지)
* 클래스 활용
  * 해당 객체 타입의 인스턴스 생성 및 조작

## 메소드 정리

Python Methods

### 인스턴스 메소드 (Instance Method)

self 매개변수를 통해 동일한 객체에 정의된 속성 및 다른 메소드에 자유롭게 접근 가능

클래스 자체에도 접근 가능 => **인스턴스 메소드가 클래스 상태를 수정**할 수도 있음

<주요 특징>

* 가장 흔히 사용됨
* self 매개변수를 필수로 사용해야 함
* 데코레이터가 필요없음
* 객체(클래스의 인스턴스)를 통해 참조 가능

### 클래스 메소드(Class Method)

클래스를 가리키는 cls 매개변수를 받음

cls 인자에만 접근 할 수 있기 때문에 객체 인스턴스 상태를 수정할 수 없음

<주요 특징>

* self 매개변수가 필요없음
* cls 매개변수를 이용해야함
* @classmethod 데코레이터가 필요함
* 클래스를 통해 바로 참조, 인스턴스가 필요없음

### 스태틱 메소드(Static Method)

임의개수의 매개변수를 받을 수 있지만, self나 매개변수는 사용하지 않음

객체 상태나 클래스 상태를 수정할 수 없음

일반 함수처럼 동작하지만 클래스의 이름공간에 귀속 됨

* self나 cls 매개변수가 필요없음
* @staticmethod 데코레이터가 필요함
* 인수로 전달된 매개변수에만 접근할 수 있음

<예시코드>

* 각 메소드들의 형태

> ```python
> class MyClass:
>     
>     def method(self):
>         return 'instance method', self
>     
>     @classmethod
>     def classmethod(cls):
>         return 'class method', cls
>     
>     @staticmethod
>     def staticmethod():
>         return 'static method'
> ```

* 인스턴스 메소드의 호출 결과

> ```python
> obj = MyClass()
> ```
>
> ```python
> obj.method()
> ```
>
> ('instance method', <`__main__`.MyClass at 0x11자리의16진수값>)
>
> ```python
> MyClass.method(obj)
> ```
>
> ('instance method', <`__main__`.MyClass at 0x11자리의16진수값>)

* 클래스 자체에서 각 메소드를 호출하는 경우

  인스턴스 메소드는 호출할 수 없음

> ```python
> MyClass.classmethod()
> ```
>
> ('class method', `__main__`.MyClass)
>
> ```python
> MyClass.staticmethod()
> ```
>
> 'static method'
>
> ```python
> MyClass.method()
> ```
>
> TypeError: method() missing 1 required positional argument: 'self'

* **인스턴스**는 **클래스 메소드와 스태틱 메소드 모두 접근**할 수 있음

>```python
>obj.classmethod()
>```
>
>('class method', `__main__`.MyClass)
>
>```python
>MyClass.classmethod()
>```
>
>('class method', `__main__`.MyClass)
>
>```python
>obj.staticmethod()
>```
>
>'static method'

## 객체 지향의 핵심개념

### 추상화

현실 세계를 프로그램 설계에 반영

ex) Preson class / Person class를 상속받는 Professor, Student class

> ```python
> # 학생 클래스
> class Student:
>     
>     def __init__(self, name, age, gpa):
>         self.name = name
>         self.age = age
>         self.gpa = gpa
>         
>     def talk(self):
>         print(f'반갑습니다. {self.name}입니다.')
>         
>     def study(self):
>         self.gpa += 0.1
> ```
>
> ```python
> # 교수 클래스
> class Professor:
>     
>     def __init__(self, name, age, department):
>         self.name = name
>         self.age = age
>         self.department = department
>         
>     def talk(self):
>         print(f'반갑습니다. {self.name}입니다.')
>         
>     def teach(self):
>         self.age += 0.1
> ```
>
> ```python
> # 사람 클래스
> class Person:
>     
>     def __init__(self, name, age):
>         self.name = name
>         self.age = age
>         
>     def talk(self):
>         print(f'반갑습니다. {self.name}입니다.')
> ```

### 상속

두 클래스 사이 부모 - 자식 관계를 정립하는 것

클래스는 상속이 가능함

* 모든 파이썬 클래스는 object를 상속 받음

  ```python
  Class ChildClass(ParentClass):
      pass
  ```

* 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속받음

* 부모 클래스의 속성, 메소드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐

> 앞서 살펴본 학생, 교수, 사람 클래스를 상속으로 다시 살펴보면
>
> ```python
> class Person:    # 사람 클래스
>     
>     def __init__(self, name, age):
>         self.name = name
>         self.age = age
>         
>     def talk(self):
>         print(f'반갑습니다. {self.name}입니다.')
> 
> class Professor(Person):    # 교수 클래스, 사람 클래스 상속
>     
>     def __init__(self, name, age, department):
>         self.name = name
>         self.age = age
>         self.department = department
>         
> class Person:    # 학생 클래스, 사람 클래스 상속
>     
>     def __init__(self, name, age):
>         self.name = name
>         self.age = age
>         self.gpa = gpa
> ```
>
> ```python
> p1 = Professor('박교수', 49, '컴퓨터공학과')
> ```
>
> ```python
> s1 = Student('김학생', 20, 3.5)
> ```
>
> ```python
> # 부모 Person 클래스의 talk 메소드를 활용
> p1.talk()
> ```
>
> 반갑습니다. 박교수입니다.
>
> ```python
> # 부모 Person 클래스의 talk 메소드를 활용
> s1.talk()
> ```
>
> 반갑습니다. 김학생입니다.

### 상속 관련 함수와 메소드

* isinstance(object, calssinfo)

  classinfo의 instance거나 subclass인 경우

> ```python
> class Person:
>     pass
> 
> class Professor:
>     pass
> 
> class Student(Person):
>     pass
> 
> p1 = Professor()
> s1 = Student()
> 
> print(isinstance(p1, Person)) # => True
> print(isinstance(p1, Professor)) # => True
> print(isinstance(p1, Student)) # => False
> print(isinstance(s1, Person)) # => True
> print(isinstance(s1, Professor)) # => False
> print(isinstance(s1, Student)) # => True
> ```

* issubclass(class, classinfo)

  class가 classinfo의 subclass면 True

  classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사

> ```python
> issubclass(bool, int)
> ```
>
> True
>
> ```python
> issubclass(float, int)
> ```
>
> False
>
> ```python
> issubclass(Professor, Person)
> ```
>
> True
>
> ```python
> issubclass(Professor, (Person, Student))
> ```
>
> True

* super()

  자식클래스에서 부모클래스를 사용하고 싶은 경우

> ```python
> class Person:    # 사람 클래스
> 
>  def __init__(self, name, age):
>      self.name = name
>      self.age = age
> 
>  def talk(self):
>      print(f'반갑습니다. {self.name}입니다.')
> 
> class Professor(Person):    # 교수 클래스, 사람 클래스 상속
> 
>  def __init__(self, name, age, department):
>      super().__init__(name, age)    # 부모 클래스(Person)의 __init__임을 명시
>      self.department = department
> ```

* mro 메소드(Method Resolution Order)

  해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메소드

  기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

  (예시는 아래 다중 상속에서...)

### 상속 정리

* 파이썬의 모든 클래스는  object로부터 상속됨
* 부모 클래스의 모든 요소(속성, 메소드)가 상속됨
* super()를 통해 부모 클래스의 요소를 호출할 수 있음
* 메소드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
* 상속관계에서의 이름 공간은 **인스턴스, 자식 클래스, 부모 클래스** 순으로 탐색

### 다중 상속

여러 부모 클래스를 상속 가능, 만약 중복되는 요소가 있다면 첫 상속 클래스의 요소를 우선으로 실행

>```python
>class Person:
>    def __init__(self, name):
>        self.name = name
>        
>    def greeting(self):
>        return f'안녕, {self.name}'
>```
>
>```python
>class Mom(Person):
>    gene = 'XX'
>    
>    def swim(self):
>        return '엄마가 수영'
>```
>
>```python
>class Dad(Person):
>    gene = 'XX'
>    
>    def walk(self):
>        return '아빠가 걷기'
>```
>
>```python
>class Child(Mom, Dad):
>    def walk(self):    # 오버라이드
>        return '아기가 걷기'
>    
>    def cry(self):
>        return '아기가 응애'
>```
>
>```python
>baby = Chile('애기')
>```
>
>```python
>baby.cry()
>```
>
>'아기가 응애'
>
>```python
>baby.walk()
>```
>
>'아기가 걷기'
>
>```python
>baby.swim()
>```
>
>'엄마가 수영'
>
>```python
>baby.gene    # 중복된 요소는 앞선 상속 클래스가 우선
>```
>
>'XX'

* mro 메소드 예시

> ```python
> Child.mro()
> ```
>
> [`__main__`.Childㄶ, `__main__`.Mom, `__main__`.Dad, `__main__`.Person, `__main__`.object]

## 다형성

* 여러 모양을 뜻하는 그리스어
* 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미
* 즉, 서로 다른 클래스에 속해있는 객체들이 **동일한 메시지에 대해 다른 방식으로 응답될 수 있음**

### 메소드 오버라이딩

* 상속 받은 메소드를 재정의
  * 클래스 상속 시, 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경
  * 부모 클래스의 메소드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
  * 부모 클래스의 메소드를 실행시키고 싶은 경우 super를 활용

<예시코드>

> ```python
> class Person:
>     def __init__(self, name):
>         self.name = name
>         
>     def talk(self):
>         print(f'반갑습니다. {self.name}입니다.')
> 
> # 자식 클래스
> class Professor(Person):
>     def talk(self):
>         print(f'{self.name}일세.')
>         
> # 자식 클래스
> def Student(Person):
>     def talk(self):
>         super().talk()
>         print(f'저는 학생입니다.')
> ```
>
> ```python
> p1 = Professor('김교수')
> p1.talk()
> ```
>
> 김교수일세.
>
> ```python
> s1 = Student('이학생')
> s1.talk()
> ```
>
> 반갑습니다. 이학생입니다.
>
> 저는 학생입니다.
