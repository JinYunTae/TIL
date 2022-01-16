# Java 프로그램 구조 및 데이터 타입

## Java 프로그램 구조

* 자바 프로그램은 하나의 `.java`파일에 하나의 클래스를 정의
* 클래스 내부에 실행에 필요한 변수나 메서드(또는 함수)등을 정의

> 예시

```java
public class FirstClass {
    // 실행할 내용
}
```

public : 자바의 예약어로써, FirstClass.java 파일의 클래스(FirstClass)를 외부에 공개함

{} : 클래스에서 제공할 명령 작성

// : 주석



클래스란? 자바 프그램의 최소 구성 단위로, 선언된 클래스 내부에 실행에 필요한 변수나 메서드 등이 정의됨. 이때 자바 코드는 클래스 블록({}) 안에 작성되게 됨



### Java의 주석문

주석은 프로그램 작성 일자나 버전, 작성자, 작성 목적, 그 밖의 프로그램 내의 부분적인 요소들에 대한 설명이 필요할 때 사용. 컴파일 시 프로그램 코드로 인식되지 않음. 따라서 컴파일 결과로 얻어낸 `.class` 파일의 크기에는 영향이 없음

1. // : 단일 행 주석 처리

2. /* */ : 다중 행 주석처리

3. /** */ : Javadoc(자바독) 형태의 주석 처리

   예시

   ```java
   /**
    * 파일명 : commentsTest.java
    * 작성일 : yyyy/mm/dd
    * 작성자 : 홍길동
   */
   
   /* 다음 클래스는 다음과 같은 두 줄의 내용을 출력하는 자바 프로그램이다.
   	"출력될 내용은 다음과 같습니다."
   	"처음 작성한 자바 프로그램입니다."
   */
   
   // 단일 행 주석처리
   ```

   `+`자바 Document 생성하기

   자바 소스 파일을 작성한 후 JDK에 포함된 javadoc이라는 명령을 사용하면 해당 자바 파일 내에서 javadoc(/** */) 주석문 내에 포함된 내용과 이 클래스 내의 여러 코드들 (변수, 메서드, 생성자 정보 등)에 대한 설명이 html 문서로 제공된다.

   ``` java
   javadoc CommentsTest.java
   ```

   해당 명령의 결과로 여러 html 파일들이 생성되는데 이 중 index.html 파일을 열어보면 해당 설명문이 열린다.

   

## Java 어필리케이션 작성 및 실행

자바 애플리케이션은 바이트 코드로 번역된 후에 바로 실행할 수 있는 일반 프로그램으로 클래스 내에 'java'라는 명령어로 프로그램을 실행할 때 자동으로 호출되어 프로그램을 시작하는 main() 메서드를 가지고 있어야 함

1. **메모장**을 이용해 Java 프로그램을 작성하는 법

   ```java
   public class JavaApp { // 클래스 영역 시작
       //변수 선언
       //메서드 선언
       public static void main(String args[]) { // 메서드 영역 시작
           System.out.println("Hello World!");//실행될 프로그램 코드
       } // 메서드 영역 종료
   } // 클래스 영역 종료
   ```

   코드 작성 후 도스창을 열어 해당 .java파일이 작성된 폴더로 이동한 후 

   ```java
   c:\javatest>javac 파일명.java
   ```

   명령을 실행하면 컴파일 결과로 `파일명.class` 파일이 생성됨

   

2. **이클립스**를 이용해 Java 프로그램을 작성하는 법

   1. 이클립스 pakage Explorer 화면에 새로운 Project 생성 : [File]-[New]-[Java Project] 메뉴 선택
   2. 프로젝트 이름 설정 후 [Finish] 버튼 클릭
   3. 프로젝트 파일을 펼쳐서 src를 선택하고 우클릭 - New - class 선택
   4. 자바 클래스 이름과 main()메서드 지정(`public static void main(String[] args)` 체크)
   5. main() 메서드 내부에 실행할 문장 작성 후 저장 (이클립스는 파일 수정 후 저장 시 자동으로 컴파일 완료됨)
   6. `ctrl + F11`로 실행

   * 블록({}) - 짝이 안맞으면 컴파일 오류. for, if, try~catch 등에서도 사용.

     즉, 블록은 관련된 자바 문장들의 집합이고, 이를 하나의 단위로 묶기 위해 사용

   * 세미콜론(;) - 자바 문장이 여러 라인으로 이루어지거나, 한 라인으로 이루어질 때 각 문장을 구분하기 위해 사용

   

### Java에서 프로그램 입출력 작업이란?

Java에서 입출력은 실제 입/출력 장치들과 밀접하게 관련있어 처리하기 쉽지 않음

java.io 패키지를 이용해 처리하기 어려운 입출력 작업을 효율적으로 지원, 입출력 프로그램을 구현함

예시코드)

```java
System.out.println("Hello World")
```

System. : 클래스	out. : 변수	println : 매서드	("Hello World") : 출력할 데이터 혹은 문장



### Java의 식별자

클래스, 변수, 메서드에 주어지는 이름으로 각 요소의 식별을 가능하게 함



식별자 생성 규칙

1. 첫 문자는 A-Z, a-z, 유니코드(Unicode)로 시작해야 함
2. 특수문자 사용 불가
3. 대소문자를 구별하고, 길이에 제한이 없음
4. 예약어를 포함할 수 있으나, 예약어만을 사용할 수는 없음
5. 숫자를 사용할 수 있으나, 첫 문자에는 사용 불가

관례상 클래스 이름은 대문자, 메서드 이름은 소문자, 변수는 소문자, 상수는 대문자로 시작



### Java의 예약어

시스템에서 일정 특성을 가진 언어로 등록된 것으로 데이터 타입이나 프로그램 정의를 위해 사용됨

Java의 모든 예약어는 소문자로 이루어짐 (약 50여개)

| abstract | assert  |  boolean   |   break   |    byte    |  cast   |    catch     |
| :------: | :-----: | :--------: | :-------: | :--------: | :-----: | :----------: |
|   char   |  class  |   const    | continue  |  default   |   do    |    double    |
|   else   | extends |   false    |   final   |  finally   |  float  |     for      |
|   goto   |   if    | implements |  import   | instanceof |   int   |  interface   |
|   long   | native  |    new     |   null    |  package   | private |  protected   |
|  public  | return  |   short    |  static   |   super    | switch  | synchronized |
|   this   |  throw  |   throws   | transient |    true    |   try   |     void     |
| volatile |  while  |            |           |            |         |              |

const, goto는 현재 사용되고 있지 않으며, 식별자로도 사용할 수 없음

sizeof 예약어는 Java에서 더 이상 사용되지 않음



## Java 데이터 타입과 변수

프로그램 언어에서는 사용할 데이터를 변수에 저장하고 관리

정의된 변수를 통해 데이터의 의미를 정확하게 해석하여 사용

데이터 타입은 변수의 성격을 규정

> 예시
>
> int age;	//	기본형인 int 형의 age 변수
>
> age = 25;	//	age 변수에 값 할당



### 데이터의 표현

bit : 데이터 표현의 가장 기본단위 0, 1로 구성됨 => 8개 모이면 1byte가 되어 하나의 문자를 표현한다

기본 데이터 타입의 종류

| 표현형태  | 데이터 타입 | 정의                                                         |
| --------- | ----------- | ------------------------------------------------------------ |
| 논리값    | boolean     | True/False의 리터럴(literal) 값을 나타내는 값<br />1bit만 사용 |
| 단일 문자 | char        | 16bit의 유니코드 문자 데이터                                 |
| 정수      | byte        | 부호가 있는 8bit의 정수                                      |
|           | short       | 부호가 있는 16bit의 정수                                     |
|           | int         | 부호가 있는 32bit의 정수                                     |
|           | long        | 부호가 있는 64bit의 정수                                     |
| 실수      | float       | 부호가 있는 32bit의 부동소수점 실수                          |
|           | double      | 부호가 있는 64bit의 부동소수점 실수                          |

* 논리값

  int형과 boolean형은 서로 형변환 불가능 - boolean에는 true/false만 할당가능

  

* 단일 문자

  하나의 문자는 char형으로 표현되고, char형 리터럴은 홑따옴표('')안에 넣어야 함

  char는 정수형으로 형변환이 가능하지만 0부터 값을 갖는 비부호형(Unsigned)값임

  자바의 문자형은 16비트 유니코드 문자로 표현됨 (다른 언어는 8bit)

  > 문자형 예시
  >
  > ``` java
  > char letter, tab, uniChar 	// 변수 선언
  > letter = 'a'				//	ASCII 문자
  > tab = '\t'					//	탭과 같은 특수문자를 나타낸다.
  > uniChar = '\u 4개의16진수값'	/*	특정 유니코드 문자. 유니코드 사용 시 							문자 앞에 \u를 명시하고 4개의 16진수 값으							로 문자를 표현한다.	*/
  > ```



* 정수형

  정수형은 byte, short, int, long으로 네 가지 형이 있으며, 부호형(Singed)임

  부호형은 값의 첫번째 비트가 부호비트로 동작하는 것으로 0이면 양수 1이면 음수

  네 가지 기본형은 가질 수 있는 범위에 제한이 있으며, byte가 가장 작고 long이 가장 넓음

  형을 명시하지 않은 경우 int형으로 기본 정의함

  | 데이터 타입 | 크기  | 표현범위                                                     |
  | ----------- | ----- | ------------------------------------------------------------ |
  | byte        | 1byte | -2^7 ~ 2^7 - 1 (-128 ~ 127)                                  |
  | short       | 2byte | -2^15 ~ 2^15 - 1 (-32768 ~ 32767)                            |
  | int         | 4byte | -2^31 ~ 2^31 - 1 (-2147483648 ~ 2147483647)                  |
  | long        | 8byte | -2^63 ~ 2^63 -1 <br />(-9223372036854775808 ~ 9223372036854775807) |

  10진수(Decimal), 8진수(Octal), 16진수(Hexadecimal)로 표현가능

  > 정수형 예시
  >
  > ```java
  > 23		:	10진수 표기법
  > 023		:	8진수 표기법으로 0으로 시작
  > 0xBAAC	:	16진수 표기법으로 0x로 시작
  >     
  > long 형을 사용할 경우 문자 L이나 l을 사용
  > 23L, 023L, 0xBAACL
  > ```

  

* 실수형

  실수형은 float, double 두 가지 형이 있음

  형을 명시하지 않으면 double이 기본형으로 정의됨

  실수형 포멧은 표준인 IEEE 754를 채택하여 자바를 플랫폼 독립적인 언어로 만듦

  | 데이터 타입 | 크기  | 표현범위                          |
  | ----------- | ----- | --------------------------------- |
  | float       | 4byte | 1.4E-45 ~ 3.4028235E38            |
  | double      | 8byte | 4.9E-324 ~ 1.7976931348623157E308 |

  실수형 리터럴은 소수점과 지수로 표현됨

  ```java
  E 또는 e (지수표현)
  F 또는 f (float를 표현)
  D 또는 d (double을 표현)
      
  3.14	:	간단한 실수 값(double 형)
  6.02E23	:	큰 실수 값
  1.718F	:	float 형의 실수 값
  ```



	#### 데이터 다입의 범위 초과 시 발생하는 오류

* 변수 초기화 시 데이터 타입의 범위를 초과하는 값을 저장하면 컴파일 시에 오류 발생
* +, - 등의 연산 결과로 값의 범위를 초과하는 경우에도 오류 발생

``` java
public class PrimitiveTypeTest {
    public static void main(String args[]) {
        int num = 2147483648;	//	int형의 표현범위를 초과한 값을 가질 경우 컴파일 오류 발생
        
        int num1 = 2147483647;	//	num1, num2 모두 int형의 표현범위 내임
        int num2 = 1;
        
        int num3 = num1 + num2;	//	num3은 두 변수를 더한 결과를 저장하던 중 int 표현범위를 넘음 - 아래 출력에서 전혀 다른 연산 결과가 출력됨
        System.out.println(num1);
        System.out.println(num2);
        System.out.println(num3);	// num1 = 2147483646으로 수정해야 함
    }
}
```



### 변수 및 변수선언

* 변수

  프로그래머가 메모리상의 데이터에 접근하기 위한 방법으로 컴퓨터 내부의 데이터와 1:1 대응됨 => 실제 데이터를 의미하는 변수를 통해 메모리상의 데이터에 접근 가능함

  한 가지 유형의 데이터만을 저장할 수 있고, 각 변수가 저장할 수 있는 데이터 유형이 정해져 있음

  기본형(Primitive Type)과 참조형(Reference Type) 두 가지 변수가 존재함

  

* 변수선언

  자바 가상 머신(JVM)에게 데이터를 저장하기 위한 메모리 할당을 요청하는 것

  데이터가 필요로 하는 크기의 메모리 할당을 위해 데이터 타입을 명시해야 함

  ``` java
  데이터타입 변수명;	(데이터 타입과 변수명 사이에 하나 이상의 공백!)
  ex) int num;
  ```

  ``` java
  int age;	//	변수 선언
  age = 25;	//	변수 초기화
  int age = 25;	//	앞의 과정을 한 문장으로 처리
  ```

  기본형의 경우 할당된 메모리에 직접 값이 들어감

  

* 자동 초기화

  자바에서는 변수에 **값을 할당하지 않은 경우 자동으로 초기화**됨. 변수의 값이 자동으로 초기화되는 것을 **Default 초기화**라고 하며, **각 데이터 유형별로 할당되는 기본값**이 존재함. 단, 메서드 안에서 선언된 변수인 **지역변수는 자동으로 초기화 되지 않음**.

  <자동 초기화 값>

  | 데이터 타입 | 초기 값         |
  | :---------: | :-------------- |
  |    byte     | 0               |
  |    short    | 0               |
  |     int     | 0               |
  |    long     | 0L              |
  |    float    | 0.0F            |
  |   double    | 0.0D            |
  |    char     | '\u0000' (NULL) |
  |   boolean   | false           |
  |   참조형    | null            |



> 예제	변수 선언 및 값 할당
>
> ``` java
> public class AssignTest {
>     public static void main(String args[]) {
>         int x, y;				//	int형 변수 선언
>         x = 6;					//	int형 변수에 값 대입
>         y = 1000;				//	int형 변수에 값 대입
>         float z = 3.1414f;		//	float형 변수 선언 후 값 대입
>         double w = 3.1415;		//	double형 변수 선언 후 값 대입
>         boolean truth = true;	//	boolean형 변수 선언 후 값 대입
>         char c;					//	char형 변수 선언
>         c = 'A'					//	char형 변수 선언 후 값 대입
>         String str;				//	String(Class 형)형 변수 선언
>         String str1 = "bye";	//	String(Class 형)형 변수 선언 후 값 대입
>         str = "Hi out there!"	//	String(Class 형)형 변수 선언 후 값 대입
>     }
> }
> ```



#### 전역변수와 지역변수

* 전역(Global)변수

  클래스 선언부 밑에 선언된 변수 - 여러 메서드에서 공통으로 사용 가능

  

* 지역(Local)변수

  메서드 선언부 밑에 선언된 변수 / 메서드 매개변수로 선언된 변수

  => 해당 변수가 선언된 메서드 내에서만 사용가능

  

> 예시
>
> ``` java
> public class VariableDemo {
>     int sum;									// 전역(global) 변수
>     
>     public void addScore(int javaScore) {		// 지역(local) 변수
>         int score = javaScore;					// 지역(local) 변수
>         sum = sum + score;
>     }
>     public getSum() {
>         return sum;
>     }
> }
> ```



변수는 자신이 속한 블록({})을 벗어나면 사용 불가

> 예시
>
> ```java
> public class BlockTest {
>     boolean win;
>     public void setWin(int s) {
>         int score = s;
>         if (score > 10) {
>             win = true;
>         }
>     }
>     public void printWinner() {
>         if (win == true) {
>             System.out.println("이기다.");
>         }
>     }
> }
> ```
>
> 위 프로그램의 setWin에서 true가 되더라도 블록 나가면서 지역변수(local) 할당이 끝나게 된다. 그러므로 printWinner는 값이 false로 자동 할당된 전역변수(global) win의 값을 받아 아무 문장도 출력하지 않게 된다.



#### 데이터 타입의 변환 = 형변환

데이터 타입의 변환은 변수의 타입을 다른 타입으로 변경하고자 할 때 형변환 연산자를 사용하여 변환 함

* 작은 데이터 타입 -> 큰 데이터 타입 : Pronotion(묵시적 형변환)

  데이터 손실의 우려가 없어 자동 캐스팅

  > 규칙
  >
  > byte - short -int - long - float - double
  >
  > char - int - long - float - double 순으로 변경

  

* 큰 데이터 타입 -> 작은 데이터 타입 : Demotion(명시적 형변환)

  데이터 손실의 우려로 명시적 캐스팅 - 데이터 타입이 변환된 후에도 해당 값을 표현할 수 있어야 함

  > 명시적 형변환 후 다른 값을 가지게 되는 경우는?
  >
  > ```java
  > int sum = 128;
  > byte data = (byte)sum;	=>	data 변수에 -128 할당됨
  > ```
  >
  > byte 변수가 가질 수 있는 범위 : -127 ~ 128
  >
  > 4byte로 표현된 128을 1byte로 축소해 형변환 => data 변수가 byte 범위 밖의 128을 올바르게 표현할 수 없음, 맨 앞의 1이 부호비트가 되버림.



`+` add on

* 변수는 데이터가 어떤 의미인지 식별해주는 역할을 한다. 그냥 숫자 34가 적혀있으면 어떤 데이터인지 정확하게 해석할 수가 없다. 그러나 이를 age라는 변수에 저장하면 이 34를 나이에 해당하는 숫자로 해석할 수 있다. 이러한 변수를 식별자라고 하며, 대표적인 식별자가 변수이다.
* 변수 사용을 위해서는 선언이 필요하고 이 선언에는 반드시 데이터 타입이 필요하다. 데이터 타입에 따라 변수가 저장할 수 있는 값의 종류와 범위가 달라지므로 매우 중요한 요소이다.
* 자바는 크게 기본형 타입과 참조형 타입 두 가지 데이터 타입을 제공한다. 기본 데이터 타입은 논리형(boolean), 문자형(char), 정수형(byte, short, int, long), 실수형(float, double)이 있으며, 참조형은 배열이나 String 같은 클래스를 참조형 타입이라고 한다.



