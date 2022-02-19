# 반응형Web (Bootstrap)

<hr>

## 1. CSS Layout

### 1.1. CSS layout techniques

* Display
* Position
* Flat (CSS1, 1996)
* Flexbox (2012)
* Grid(2017)
* 기타
  * Responsive Web Design (2010), Media Queries (2012)

<hr>

## 2. Float

CSS 기본원칙 1, 2인 모든 요소는 **네모(박스모델)**이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로**(좌상단에 배치)** 쌓인다.

그렇다면 어떤 요소를 감싸는 형태로 배치는? 좌/우측 배치는?

### 2.1. Float

* 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wraping 하도록 함
* 요소가 Normal flow를 벗어나도록 함

![image-20220219224514258](Bootstrap.assets/image-20220219224514258.png)

### 2.2. Float 속성

* none : 기본값
* left : 요소를 왼쪽으로 띄움
* right : 요소를 오른쪽으로 띄움

<예시 코드>

> Float 예시 1
>
> ```html
> <body>
>   <div class="box left">float left</div>
>   <p>lorem300 자동 완성으로 길~게</p>
> </body>
> ```
>
> ```CSS
> .box {
>   width: 150px;
>   higth: 150px;
>   border: 1px solid black;
>   background-color: crimson;
>   color: white;
>   margin-right: 30px;
> }
> 
> .left {
>   float: left;
> }
> ```
>
> ![image-20220219225056768](Bootstrap.assets/image-20220219225056768.png)
>
> Float 예시 2
>
> ```HTML
> <body>
>   <header>
>     <div class="box1">div</div>
>   </header>
>   <div class="box2">div</div>
> </body>
> ```
>
> ![image-20220219225635605](Bootstrap.assets/image-20220219225635605.png)
>
> ```HTML
> <body>
>   <header>
>     <div class="box1 left">div</div>
>   </header>
>   <div class="box2">div</div>
> </body>
> ```
>
> ```CSS
> <style>
>   /* style에 float left 추가*/
>   .left {
>     float: left;
>   }
> </style>
> ```
>
> ![image-20220219225745315](Bootstrap.assets/image-20220219225745315.png)
>
> Clearing Float
>
> ```HTML
> <body>
>   <header class="clearfix">
>     <div class="box1 left">div</div>
>   </header>
>   <div class="box2">div</div>
> </body>
> ```
>
> ```CSS
> .clearfix::after {
>   content: "";
>   display: block;
>   clear: both;
> }
> ```
>
> ![image-20220219225928838](Bootstrap.assets/image-20220219225928838.png)

### 2.3. Clearing Float

* Float는 Normal Flow에서 벗어나 부동 상태 (떠 있음)
* 따라서, 이후 요소에 대하여 Float 속성이 적용되지 않도록 Clearing이 필수적임
  * ::after : 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성
    * 보통 content 속성과 함께 짝지어, 요소에 장식용 콘텐츠를 추가할 때 사용
  * clear 속성 부여

### 2.4. Float 정리

* Float는 레이아웃을 구성하기 위해 필수적으로 활용 되었으며, 최근엔 Flexbox, Grid 등장과 함께 사용도가 낮아짐
* Float 활용 전략 - Normal Flow에서 벗어난 레이아웃 구성
  * 원하는 요소들을 Float로 지정하여 배치
  * 부모 요소에 반드시 Clearing Float를 하여 이후 요소부터 Normal Flow를 가지도록 지정

### 2.5. Float 활용 사례

![image-20220219230602467](Bootstrap.assets/image-20220219230602467.png)

<hr>

## 3. Flexbox



