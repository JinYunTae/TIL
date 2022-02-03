# Python 데이터 구조 및 활용

## 1. 순서가 있는 데이터 구조

### 문자열(String Type)

* 문자들의 나열(sequence of characters)
  * 모든 문서는 str타입
* 문자열은 작은 따옴표('')나 큰 따옴표("")를 활용하여 표기
  * 문자열을 묶을 때 동일한 문장부호를 활용
  * PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

#### 문자열 조회/탐색 및 검증 메소드

| 문법         | 설명                                                         |
| ------------ | ------------------------------------------------------------ |
| s.find(x)    | x의 **첫 번째 위치**를 반환, 없으면 **-1**을 반환            |
| s.index(x)   | x의 **첫 번째 위치**를 반환, 없으면 **오류 발생**            |
| s. isalpha() | 알파벳 문자 여부<br />*단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함) |
| s.isupper()  | 대문자 여부                                                  |
| s.islower()  | 소문자 여부                                                  |
| s.istitle()  | 타이틀 형식 여부                                             |
| s.isdigit()  | 문자열 의미가 숫자인지 여부                                  |

<예시코드>

1. **문자열 조회/탐색**

* .find(x)

> ```python
> 'apple'.find('p')
> ```
>
> 1
>
> ```python
> 'apple'.find('k')
> ```
>
> -1

* .index(x)

> ```python
> 'apple'.index('p')
> ```
>
> 1
>
> ```python
> 'apple'.index('k')
> ```
>
> **ValueError: substring not found**

2. **문자열 검증**

* .isalpha()

> ```python
> 'abc'.isalpha()
> ```
>
> True
>
> ```python
> 'ㄱㄴㄷ'isalpha()    # 유니코드 문자면 True
> ```
>
> True

* .isupper()

> ```python
> 'Ab'.isupper()
> ```
>
> False

* .islower()

> ```python
> 'ab'.islower()
> ```
>
> True

* .istitle()

> ```python
> 'Title Title!'.istitle()
> ```
>
> True

* .isnumeric()

> .isdecimal() ⊆ .isdigit() ⊆ .isnumeric()
>
> ```python
> '⅜'.isnumeric()
> 'Ⅲ Ⅳ'.isnumeric()
> '④⑧'.isnumeric()
> '萬'.isnumeric()
> ```
>
> True
>
> ```python
> 'abc'.isnumeric()
> '38.0'.isnumeric()
> '-38'.isnumeric()
> ```
>
> False

#### 문자열 변경 메소드

| 문법                         | 설명                                       |
| ---------------------------- | ------------------------------------------ |
| s.replace(old, new[,count])  | 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 |
| s.strip([char])              | 공백이나 특정 문자를 제거                  |
| s.split([char])              | 공백이나 특정 문자를 기준으로 분리         |
| 'separator'.join([iterable]) | 구분자로 iterable을 합침                   |
| s.capitalize()               | 가장 첫 번째 글자를 대문자로''             |
| s.title()                    | '나 공백 이후를 대문자로                   |
| s.upper()                    | 모두 대문자                                |
| s.lower()                    | 모두 소문자                                |
| s.swapcase()                 | 대소문자 변경                              |

<예시코드>

* .replace(old, new[,count])

> * 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
> * count를 지정하면, 해당 개수만큼만 시행
>
> ```python
> 'coone'.replace('o', 'a')
> ```
>
> 'caane'
>
> ```python
> 'wooooowoo'.replace('o', '!', 2)
> ```
>
> 'w!!ooowoo'

* .strip([char])

> * 특정 문자들을 지정하면,
>   * 양쪽을 제거하거나(strip)
>   * 왼쪽을 제거하거나(lstrip)
>   * 오른쪽을 제거(rstrip)
> * 문자열을 지정하지 않으면 공백을 제거함
>
> ```python
> '	와우!\n'.strip()
> ```
>
> '와우!'
>
> ```python
> '	와우!\n'.lstrip()
> ```
>
> '와우\n'
>
> ```python
> '	와우!\n'.rstrip()
> ```
>
> '	와우!'
>
> ```python
> '안녕하세요?????'.rstrip(?)
> ```
>
> '안녕하세요'

* .split([chars])

> * 문자열을 특정한 단위로 나눠 리스트로 반환
>
> ```python
> 'a,b,c'.split('_')
> ```
>
> ['a,b,c']
>
> ```python
> 'a b c'.split()
> ```
>
> ['a', 'b', 'c']

* 'separator'.join([iterable])

> * 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환 
>
> ```python
> '!'.join('ssafy')
> ```
>
> 's!s!a!f!y'
>
> ```python
> ' '.join(['3', '5'])
> ```
>
> '3 5'
>
> * 문자열 변경 추가 예시
>
>   ```python
>   msg = 'hI! Everyone, I\'m ssafy'
>   print(msg)
>   print(msg.capitalize())    # 첫 대문자 나머지 소문자
>   print(msg.title())    # 각 단어의 첫 글자 대문자
>   print(msg.upper())    # 전체 대문자
>   print(msg.lower())    # 전체 소문자
>   print(msg.swapcase())    # 대소문자 변환
>   ```
>
>   hI! Everyone, I'm ssafy
>
>   Hi! everyone, i'm ssafy
>
>   Hi! Everyone, I'M Ssafy
>
>   HI! EVERYONE, I'M SSAFY
>
>   hi! everyone, i'm ssafy
>
>   Hi! eVERYONE, i'M SSAFY

### 리스트(List)

* 순서를 가지는 0개 이상의 객체를 참조하는 자료형
  * 생성된 이후 내용 변경이 가능 => 가변자료형
  * 유연성 때문에 파이썬에서 가장 흔히 사용
* 항상 대괄호 형태로 출력

#### 리스트 메소드

| 문법                   | 설명                                                         |
| ---------------------- | ------------------------------------------------------------ |
| L.append(x)            | 리스트 마지막에 항목 x를 추가                                |
| L.insert(i, x)         | 리스트 인덱스 i에 항목 x를 삽입                              |
| L.remove(x)            | 리스트가장 왼쪽에 있는 항목(첫 번째) x를 제거<br />항목이 존재하지 않을 경우, ValueError |
| L.pop()                | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거        |
| L.pop(i)               | 리스트의 인덱스 i에 있는 항목을 반환 후 제거                 |
| L.extend(m)            | 순회형 m의 모든 항목들을 리스트 끝에 추가(+=과 같은 기능)    |
| L.index(x, start, end) | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
| L.reverse()            | 리스트를 거꾸로 정렬                                         |
| L.sort(...)            | 리스트를 정렬 (매개변수 이용가능)                            |
| L.count(x)             | 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환             |

<예시코드>

* .append(x)

> 리스트에 값을 추가함
>
> ```python
> cafe = ['starbucks', 'tomntoms', 'hollys']
> print(cafe)
> cafe.append('banapresso')
> print(cafe)
> ```
>
> ['starbucks', 'tomntoms', 'hollys']
>
> ['starbucks', 'tomntoms', 'hollys', 'banspresso']

* .extend(iterable)

>리스트에 iterable의 항목을 추가함
>
>```python
>cafe = ['starbucks', 'tomntoms', 'hollys']
>print(cafe)
>cafe.extend(['coffee'])    # += 와 같은 기능
>print(cafe)
>cafe.extend('coffee')    # 차이점 / 같은 리스트가 아니라도 추가됨
>print(cafe)
>```
>
>['starbucks', 'tomntoms', 'hollys']
>
>[['starbucks', 'tomntoms', 'hollys', 'coffee']
>
>[['starbucks', 'tomntoms', 'hollys', 'c', 'o', 'f', 'f', 'e', 'e']

* .insert(i, x)

> ```python
> cafe = ['starbucks', 'tomntoms', 'hollys']
> print(cafe)
> cafe.insert(0, 'start')
> print(cafe)
> ```
>
> ['starbucks', 'tomntoms', 'hollys']
>
> [['start', 'starbucks', 'tomntoms', 'hollys']
>
> ```python
> cafe = ['starbucks', 'tomntoms', 'hollys']
> print(cafe)
> cafe.insert(10000, 'end')    # 삽입 인덱스가 리스트 길이보다 큰 경우 맨 뒤에 삽입
> print(cafe)
> ```
>
> ['starbucks', 'tomntoms', 'hollys', 'end']

* .remove(x)

> ```python
> numbers = [1, 2, 3, 4, 'hi']
> print(numbers)
> numbers.remove('hi')
> print(numbers)
> ```
>
> [1, 2, 3, 'hi']
>
> [[1, 2, 3]
>
> ```python
> numbers.remove('hi')
> ```
>
> **ValueError: list.remove(x) : x not in list**

* .pop(i)

> * 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함
> * i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함
>
> ```python
> numbers = ['hi', 1, 2, 3]
> print(numbers)
> numbers.pop()
> print(numbers)
> ```
>
> ['hi', 1, 2, 3]
>
> ['hi', 1, 2]
>
> ```python
> numbers = ['hi', 1, 2, 3]
> print(numbers)
> numbers.pop(0)
> print(numbers)
> ```
>
> ['hi', 1, 2, 3]
>
> [1, 2, 3]
>
> * 

* .clear()

> * 모든 항목을 삭제함
>
> ```python
> numbers = [1, 2, 3]
> print(numbers)
> numbers.clear()
> print(numbers)
> ```
>
> [1, 2, 3]
>
> []

* .index(x)

> * x값을 찾아 해당 index 값을 반환
>
> ```python
> numbers = [1, 2, 3, 4]
> print(numbers.index(3))
> print(numbers.index(100))    # 없는 경우 ValueError
> ```
>
> 2
>
> **ValueError: 100 is not in list**

* .count(x)

> * 원하는 값의 개수를 반환함
>
> ```python
> numbers = [1, 2, 3, 1, 1]
> numbers.count(1)
> numbers.count(100)    # 없으면 0 반환
> ```
>
> 3
>
> 0

* .sort()

>* 원본 리스트를 정렬함. **None 반환**
>* sorted 함수와 비교
>
>```python
>numbers = [3, 2, 5, 1]
>result = sorted(numbers)    #sorted
>print(numbers, result)
>result = numbers.sort()    # .sort()
>print(numbers, result)
>```
>
>[3, 2, 5, 1] [1, 2, 3, 5]    # 원본변경 x, 정렬된 리스트를 반환
>
>[1, 2, 3, 5] None    # 원본 리스트를 정렬, 반환 없음

* .reverse()

> * 순서를 반대로 뒤집음(정렬하는 것이 아님)
>
> ```python
> numbers = [3, 2, 5, 1]
> result = numbers.reverse()
> print(numbers, result)
> ```
>
> [1, 5, 2, 3] None

### 튜플(Tuple)

* 순서를 가지는 0개 이상의 객체를 참조하는 자료형
  * 생성 후, 담고있는 객체 변경이 불가 => 불변 자료형(immutable)
* 항상 소괄호 형태로 출력

#### 튜플 관련 메소드

* 튜플은 변경할 수 없기 때문에 값에 영향을 미치지 않는 메소드만을 지원
* 리스트 메소드 중 항목을 변경하는 메소드들을 제외하고 대부분 동일



## 2. 순서가 없는 데이터 구조

### 셋(Set)

* 순서없이 0개 이상의 해시가능한 객체를 참조하는 자료형
  * 해시 가능한 객체(불변자료형)만 담을 수 있음
* 담고있는 객체를 삽입 변경, 삭제 가능 => 가변자료형(mutable)
* 수학에서의 집합과 동일한 구조를 가짐
  * 집합 연산이 가능
  * 중복된 값이 존재하지 않음

#### 셋 메소드

| 문법           | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| s.copy()       | 셋의 얕은 복사본을 반환                                      |
| s.add(x)       | 항목 x가 셋 s에 없다면 추가                                  |
| s.pop()        | 셋 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거<br />set이 비어 있을 경우, **KeyError** |
| s.remove(s)    | 항목 x가 셋 s에 있는 경우, 항목 x를 셋 s에서 삭제<br />항목이 존재하지 않을 경우, KeyError |
| s.discard(x)   | 항목 x가 셋 s에 있는 경우, 항목 x를 셋 s에서 삭제            |
| s.update(t)    | 셋 t에 있는 모든 항목 중 셋 s에 없는 항목을 추가             |
| s.clear()      | 모든 항목을 제거                                             |
| s.isdisjoint() | 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환 |
| s.issubset()   | 셋 s가 셋 t의 하위 셋인 경우, True 반환                      |
| s.issuperset() | 셋 s가 셋 t의 상위 셋인 경우, True 반환                      |

<예시코드>

* .add(elem)

> * 셋에 값을 추가
>
> ```python
> a = {'사과', '바나나', '수박'}
> print(a)
> a.add('딸기')
> print(a)
> ```
>
> {'바나나', '사과', '수박'}
>
> {'바나나', '사과', '딸기', '수박'}

* .update(*others)

> * 여러 값을 추가
>
> ```python
> a = {'사과', '바나나', '수박'}
> print(a)
> a.update(['딸기', '바나나', '참외'])
> print(a)
> ```
>
> {'바나나', '사과', '수박'}
>
> {'바나나', '사과', '참외', '수박', '딸기'}

* .remove(elem)

> * 셋에서 삭제하고, 없으면 **KeyError**(고유한 값들은 key라고 생각하자)
>
> ```python
> a = {'사과', '바나나', '수박'}
> print(a)
> a.remove('사과')
> print(a)
> a.remove('애플')    # 없는 값 => KeyError
> print(a)
> ```
>
> {'바나나', '사과', '수박'}
>
> {'바나나', '수박'}

* .discard(elem)

> * 셋에서 삭제하고 없어도 에러가 발생하지 않음
>
> ```python
> a = {'사과', '바나나', '수박'}
> print(a)
> a.remove('사과')
> print(a)
> a.remove('애플')    # 없는 값도 상관없음
> print(a)
> ```
>
> {'바나나', '사과', '수박'}
>
> {'바나나', '수박'}
>
> {'바나나', '수박'}

* .pop()

> * 임의의 원소를 제거해 반환
>
> ```python
> a = {'사과', '바나나', '수박'}
> print(a)
> a.pop()
> print(a)
> ```
>
> {'바나나', '사과', '수박'}
>
> {'사과', '수박'}
>
> ```python
> a = {'3', '1', '2'}
> print(a)
> a.pop()
> print(a)
> ```
>
> {'3', '1', '2'}
>
> {'1', '2'}

### 딕셔너리(Dictionary)

* 순서 없이 키-값(key-value) 쌍으로 이뤄진 객체를 참조하는 자료형
  * 딕셔너리의 키(Key) : 해시가능한 불변 자료형만 가능
  * 각 키의 값(values) : 어떠한 형태든 관계 없음

| 문법            | 설명                                                         |
| --------------- | ------------------------------------------------------------ |
| d.clear()       | 모든 항목을 제거                                             |
| d.copy()        | 딕셔너리 d의 얕은 복사본을 반환                              |
| d.keys()        | 딕셔너리 d의 모든 키를 담은 뷰를 반환                        |
| d.values()      | 딕셔너리 d의 모든 값을 담은 뷰를 반환                        |
| d.items()       | 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환                |
| d.get(k)        | 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 None을 반환 |
| d.get(k, v)     | 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환 |
| d.pop(k)        | 키의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데,<br />키 k가 딕셔너리 d에 없을 경우 KeyError를 발생 |
| d.pop(k, v)     | 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데,<br />키 k가 딕셔너리 d에 없을 경우 v를 반환 |
| d.update(... .) | 딕셔너리 d의 값을 매핑하여 업데이트                          |

<예시코드>

* .get(key[,default])

> * key를 통해 value를 가져옴
> * **KeyError가 발생하지 않으며**, default 값을 설정할 수 있음(기본 : None)
>
> ```python
> my_dict = {'apple' : '사과', 'banana' : '바나나'}
> my_dict['pineapple']
> ```
>
> KeyError: 'pineapple'
>
> ```python
> my_dict = {'apple' : '사과', 'banana' : '바나나'}
> print(my_dict.get('pineapple'))
> print(my_dict.get('apple'))
> print(my_dict.get('pineapple', 0))
> ```
>
> None
>
> 사과
>
> 0

* .pop(key[,default])

> * key가 딕셔너리에 있으면 제거하고 해당 값을 반환
> * 그렇지 않으면 default를 반환
> * **default값이 없으면 KeyError**
>
> ```python
> my_dict = {'apple' : '사과', 'banana' : '바나나'}
> data = my_dict.pop('apple')
> print(data, my_dict)
> ```
>
> 사과 {'banana' : '바나나'}
>
> ```python
> my_dict = {'apple' : '사과', 'banana' : '바나나'}
> data = my_dict.pop('pineapple')
> print(data, my_dict)
> ```
>
> KeyError: 'pineapple'
>
> ```python
> my_dict = {'apple' : '사과', 'banana' : '바나나'}
> data = my_dict.pop('pineapple', 0)
> print(data, my_dict)
> ```
>
> 0 {'apple' : '사과', 'banana' : '바나나'}

* .update()

> * 값을 제공하는 key, value로 덮어씁니다.
>
> ```python
> my_dict = {'apple' : '사', 'banana' : '바나나'}
> my_dict.update(apple = '사과')
> print(my_dict)
> ```
>
> {'apple' : '사과', 'banana' : '바나나'}

## 얕은 복사와 깊은 복사(Shallow Copy & Deep Copy)

### 복사 방법

* 할당 (Assignment)
* 얕은 복사 (Shallow copy)
* 깊은 복사 (Deep copy)

#### 할당

* 대입 연산자 (=)

>  리스트 복사 확인하기
>
> 대입 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
>
> ```python
> original_list = [1, 2, 3]
> copy_list = original_list
> print(original_list, copy_list)
> ```
>
> [1, 2, 3] [1, 2, 3]
>
> 해당 주소의 일부 값을 변경하는 경우 이를 참조하는 모든 변수에 영향
>
> ![image-20220124221511247](Python5(data_structure).assets/image-20220124221511247.png)
>
> ```python
> copy_list[0] = 'hello'
> print(original_list, copy_list)
> ```
>
> ['hello', 2, 3] ['hello', 2, 3]

#### 얕은 복사(shallow copy)

* Slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사 (다른 주소)

> ```python
> a = [1, 2, 3]
> b = a[:]
> print(a, b)
> b[0] = 5
> print(a, b)
> ```
>
> [1, 2, 3] [1, 2, 3]
>
> [1, 2, 3] [5, 2, 3]

* 주의사항

> 복사하는 리스트의 원소가 주소를 참조하는 경우
>
> ![image-20220124222021292](Python5(data_structure).assets/image-20220124222021292.png)
>
> ```python
> a = [1, 2, ['a', 'b']]
> b = a[:]
> print(a, b)
> b[2][0] = 0
> print(a, b)
> ```
>
> [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
>
> [1, 2, [0, 'b']] [1, 2, [0, 'b']]

#### 깊은 복사(deep copy)

* 리스트 복사 확인하기

> ```python
> import copy
> a = [1, 2, ['a', 'b']]
> b = copy.deepcopy(a)
> print(a, b)
> b[2][0] = 0
> print(a, b)
> ```
>
> [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
>
> [1, 2, ['a', 'b']] [1, 2, [0, 'b']]