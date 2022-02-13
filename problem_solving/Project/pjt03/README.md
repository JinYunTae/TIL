# 📂PJT 02

## 📚이번 pjt 를 통해 배운 내용

* HTML을 통해 웹 페이지를 마크업 할 수 있다.
* CSS 라이브러리를 이해하고 활용할 수 있다.
* 컴표넌트 및 그리드 시스템을 활용할 수 있다.
* 커뮤니티 서비스 반응형 레이아웃을 구성할 수 있다.



## 📕 A. 01_nav_footer

* 요구 사항 : 커뮤니티 서비스 개발을 위한 화면 구성 단계로, 유저가 보는 프론트 엔드를 개발합니다.

> * 네비게이션 바(Navigation Bar)
>   1. 네비게이션 바는 스크롤을 하더라도 항상 상단에 고정되어 있습니다.
>   2. 로고 이미지는 images 폴더 안의 logo.png 파일을 사용합니다.
>   2. 로고 이미지는 클릭이 가능한 링크이며, 해당 페이지(02_home.html)로 이동해야 합니다.
>   2. 네비게이션 바 내부의 리스트(Home, Community, Login)는 ul과 li요소를 사용합니다.
>   2. 네비게이션 바 내부의 네비게이션 리스트(Home, Community, Login)는 오른쪽에 배치합니다.
>   2. 네비게이션 리스트의 각 항목들은 클릭이 가능한 링크이며, 해당 페이지(02_home.html, 03_community.html, #)로 이동해야 합니다.
>   2. Viewport의 가로 크기가 768px 미만일 경우에는 네비게이션 리스트(Home, Community, Login)가 햄버거 버튼으로 교체되며, 클릭했을 시 세부 항목을 볼 수 있습니다.
>   2. 네비게이션 리스트(Home, Community, Login)의 항목들 중에서 Home을 강조합니다.
>   9. 네비게이션 리스트의 Login 항목은 클릭 시 요소가 Modal 컴포넌트를 통하여 나타납니다.
>      (페이지 이동이 일어나지 않습니다.)
>   10. Modal 컴포넌트 내부에는 form요소를 배치합니다.
>   11. Modal 컴포넌트에서 form요소 내부의 비밀번호는 표시되지 않습니다.
>   
> * 푸터(Footer)
>   1. 푸터는 스크롤을 하더라도 항상 하단에 고정되어 있습니다.
>   2. 푸터에 작성된 내용은 수평으로 정렬되어 있습니다. (왼쪽, 오른쪽 여백이 같습니다.)
>   2. 푸터에 작성된 내용의 빈 부분(`_____`)은 본인의 이름을 작성합니다.
>   2. 위에 명시된 내용 이외에는 자유롭게 작성합니다.

* 문제 접근 방법 및 코드 설명

```HTML
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  
  <title>Navbar Footer Test</title>
</head>
<body>
  <!-- 01_nav_footer.html -->
  <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="loginModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="loginInputEmail1" class="form-label">Email address</label>
              <input type="email" class="form-control" id="loginInputEmail1" aria-describedby="emailHelp">
              <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div class="mb-3">
              <label for="loginInputPassword1" class="form-label">Password</label>
              <input type="password" class="form-control" id="loginInputPassword1">
            </div>
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="loginCheck1">
              <label class="form-check-label" for="loginCheck1">Check me out</label>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top text-light">
    <div class="container-fluid">
      <a href="02_home.html" class="mx-0 w-25">
        <img src="./images/logo.png" alt="logo" class="w-50">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse flex-grow-0" id="navbarNav">
        <ul class="list-unstyled my-0 d-flex justify-content-start d-flex align-items-center">
          <li class="mx-3 nav-item"><a class="text-decoration-none text-light active" href="02_home.html">Home</a></li>
          <li class="mx-3 nav-item"><a class="text-decoration-none text-light" href="03_community.html">Community</a></li>
          <li class="mx-3"><button type="button" class="btn btn-link text-decoration-none text-light" data-bs-toggle="modal" data-bs-target="#loginModal">
            Login
          </button>
        </li>
        </ul>
      </div>
    </div>
  </nav>
  
  <footer class="fixed-bottom bg-light text-center">
    <p class="my-1">Web-bootstrap PJT, by진윤태</p>
  </footer>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
</body>
</html>
```

* 문제후기

>* 이 문제에서 어려웠던점
>  * 네비게이션 바를 복사해서 사용하지 않고 실습한 경험을 이용해 직접 작성해서 시간이 많이 걸렸습니다.
>  * 이미지의 크기가 너무 커서 조절하기 힘들었습니다. 비율을 이용해 설정하니 화면이 작아지면 너무 작아지는 문제가 있어 비율 조정이 힘들었습니다.
>  * 네비게이션 바에서 화면 크기가 작아지면 햄버거 버튼으로 전환하면서 많은 어려움이 있었습니다.
>* 내가 생각하는 이 문제의 포인트
>  * 화면 크기가 작아지면 네비게이션 바의 항목이 햄버거 버튼으로 전환되는 것이 가장 핵심이 되는 포인트 같습니다.

-----

## 📗 B. 02_home

* 요구 사항 : 01_nav_footer를 완성했다면, 네비게이션 바와 푸터를 복사해 사용합니다.

> * 네비게이션 바(Navigation Bar) 및 페이지 구성
>   1. 네비게이션 리스트(Home, Community, Login)의 항목들 중에서 Home을 강조합니다.
>      (active)
>   2. Home 페이지는 크게 상단 Header와 하단 Section요소로 이루어져 있습니다.
> * 헤더(Header) 
>   1. Header는 Carousel 컴포넌트로 구성합니다. 이미지는 최소 3장이며, 자동으로 전환됩니다.
>      (images/ 폴더 안의 header 이미지들을 사용합니다.)
> * 섹션(Section)
>   1. Box Office 문구는 자유롭게 스타일링 합니다.
>   2. Section은 컨테이너 내부에 위치합니다.
>   3. Section 내부의 개별 요소(article)들은 이미지, 제목, 설명을 포함하는 Card 컴포넌트로
>      구성합니다. (이미지는 images 폴더의 포스터 이미지를 사용합니다. (총6개))
>   4. 각 요소들은 좌우 일정한 간격으로 떨어져 있습니다. (간격은 자유롭게 설정 가능합니다.)
>   5. Section 내부의 요소(article)들은 Viewport의 가로 크기가 576px미만일 경우에는 한 행
>      (row)에 1개씩 표시됩니다.
>   6. Section 내부의 요소(article)들은 Viewport의 가로 크기가 576px이상일 경우에는 한 행
>      (row)에 2개 이상 자유롭게 표시합니다.
>   7. 위에 명시된 내용 이외에는 자유롭게 작성합니다.

* 문제 접근 방법 및 코드 설명

```python
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  <link rel="stylesheet" href="02_home.css">
  
  <title>Home</title>
</head>
<body>

  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Navigation bar 코드를 붙여넣어 주세요. -->
  <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="loginModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="loginInputEmail1" class="form-label">Email address</label>
              <input type="email" class="form-control" id="loginInputEmail1" aria-describedby="emailHelp">
              <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div class="mb-3">
              <label for="loginInputPassword1" class="form-label">Password</label>
              <input type="password" class="form-control" id="loginInputPassword1">
            </div>
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="loginCheck1">
              <label class="form-check-label" for="loginCheck1">Check me out</label>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top text-light">
    <div class="container-fluid">
      <a href="02_home.html" class="mx-0 w-25">
        <img src="./images/logo.png" alt="logo" class="w-50">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse flex-grow-0" id="navbarNav">
        <ul class="list-unstyled my-0 d-flex justify-content-start d-flex align-items-center">
          <li class="mx-3"><a class="text-decoration-none text-light active" href="02_home.html">Home</a></li>
          <li class="mx-3"><a class="text-decoration-none text-light" href="03_community.html">Community</a></li>
          <li class="mx-3"><button type="button" class="btn btn-link text-decoration-none text-light" data-bs-toggle="modal" data-bs-target="#loginModal">
            Login
          </button>
        </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- 02_home.html -->
  <header>
    <div id="carouselSlidesOnly" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="./images/header1.jpg" class="d-block w-100" alt="header1">
        </div>
        <div class="carousel-item">
          <img src="./images/header2.jpg" class="d-block w-100" alt="header2">
        </div>
        <div class="carousel-item">
          <img src="./images/header3.jpg" class="d-block w-100" alt="header3">
        </div>
      </div>
    </div>
  </header>

  <h1 class="my-4 text-center">Boxoffice</h1>

  <div class="container">
    <section class="row row-cols-1 row-cols-sm-3 g-4">
      <div div class="col">
        <article calss="card">
          <img src="./images/movie1.jpg" class="card-img-top" alt="movie1">
          <div class="card-body">
            <h5 class="card-title">Movie title</h5>
            <p class="card-text">Movie text</p>
          </div>
        </article>
      </div>
      <div div class="col">
        <article calss="card">
          <img src="./images/movie2.jpg" class="card-img-top" alt="movie2">
          <div class="card-body">
            <h5 class="card-title">Movie title</h5>
            <p class="card-text">Movie text</p>
          </div>
        </article>
      </div>
      <div div class="col">
        <article calss="card">
          <img src="./images/movie3.jpg" class="card-img-top" alt="movie3">
          <div class="card-body">
            <h5 class="card-title">Movie title</h5>
            <p class="card-text">Movie text</p>
          </div>
        </article>
      </div>
      <div div class="col">
        <article calss="card">
          <img src="./images/movie4.jpg" class="card-img-top" alt="movie4">
          <div class="card-body">
            <h5 class="card-title">Movie title</h5>
            <p class="card-text">Movie text</p>
          </div>
        </article>
      </div>
      <div div class="col">
        <article calss="card">
          <img src="./images/movie5.jpg" class="card-img-top" alt="movie5">
          <div class="card-body">
            <h5 class="card-title">Movie title</h5>
            <p class="card-text">Movie text</p>
          </div>
        </article>
      </div>
      <div div class="col">
        <article calss="card">
          <img src="./images/movie6.jpg" class="card-img-top" alt="movie6">
          <div class="card-body">
            <h5 class="card-title">Movie title</h5>
            <p class="card-text">Movie text</p>
          </div>
        </article>
      </div>
    </section>
  </div>


  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Footer 코드를 붙여넣어 주세요. -->
  <footer class="fixed-bottom bg-light text-center">
    <p class="my-1">Web-bootstrap PJT, by진윤태</p>
  </footer>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>  
</body>
</html>
```

* 문제후기

> * 이 문제에서 어려웠던점
>   * 기존에 많이 실습하면서 연습했던 내용이라 다행이 무리 없이 진행할 수 있었습니다.
> * 내가 생각하는 이 문제의 포인트
>   * 기존에 많이 실습했던 사진의 배치가 주된 요소여서 비교적 쉽게 해결할 수 있었습니다. 특히 이전 실습 시간에 card와 carousel을 알려주셔서 원활하게 할 수 있었습니다.

## 📘 C. 03_community

* 요구 사항 : 01_nav_footer를 완성했다면, 네비게이션 바와 푸터를 복사하여 사용합니다.

> * 네비게이션 바(Navigation Bar) 및 페이지 구성
>
>   1. 네비게이션 리스트(Home, Community, Login)의 항목들 중에서 Community를
>      강조합니다. (active)
>   2. Community 페이지는 크게 게시판 목록, 게시판으로 이루어져 있습니다.
>   2. 게시판 목록과 게시판은 div.main 요소로 둘러 쌓여 있습니다.
>   2. 게시판 목록과 게시판, 게시글 페이징은 모두 컨테이너 내부에 위치합니다.
>
> * 게시판 목록
>   1. 게시판 목록은 aside 요소로 이루어져 있습니다.
>   2. 게시판 목록 내부의 각 항목(Boxoffice, Movies, Genres, Actors)은 List group
>      컴포넌트를 활용합니다.
>   3. 게시판 목록 내부의 각 항목은 클릭이 가능한 링크이지만, URL은 별도로 없이 #으
>      로 지정합니다.
>   4. Viewport의 가로 크기가 992px 이상일 경우에는 게시판 목록 내부의 항목
>      (Boxoffice, Movies, Genres, Actors)은 div.main영역의 내부에서 좌측 1/6 만큼
>      의 너비를 가집니다.
>   5. Viewport의 가로 크기가 992px 미만일 경우에는 게시판 목록 내부의 항목
>      (Boxoffice, Movies, Genres, Actors)은 div.main영역의 내부에서 전체만큼의 너
>      비를 가집니다.
>   
> * 게시판
>
>   1. 게시판은 Viewport의 가로크기에 따라 전혀 다른 요소를 표시합니다.
>
>      1. Viewport의 가로 크기가 992px 이상일 경우에는 게시글이 표(table) 요소로
>         표시되며, div.main영역의 내부에서 우측 5/6 만큼의 너비를 가집니다.
>
>      2. Viewport의 가로 크기가 992px 미만일 경우에는 게시글이 글(article) 요소들
>         의 집합으로 표시되고 가로선으로 구분합니다(스타일링은 자유롭게 진행합니
>         다). div.main영역의 내부에서 전체만큼의 너비를 가집니다.
>
>   2. 게시글은 글 제목, 영화 제목, 사용자 id, 작성시간으로 구성되어 있습니다.
>
>   3. 테스트 게시글의 개수와 내용은 2개 이상으로 자유롭게 구성할 수 있습니다.
>
>   4. 게시글 페이징(paginator)은 게시판 아래에 위치하며, 너비는 자유롭게 합니다.
>
>   5. 게시글 페이징(paginator)은 자신의 영역 안에서 좌우 중앙 정렬되어 있습니다.
>
>   6. 게시글 페이징(paginator) 내부의 요소들은 클릭이 가능한 링크이며, URL은 별도
>      로 없이 #으로 지정합니다.
>
>   7. 위에 명시된 내용 이외에는 자유롭게 작성합니다.

* 문제 접근 방법 및 코드 설명

```python
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  <link rel="stylesheet" href="03_community.css">

  <title>Community</title>
</head>
<body>

  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Navigation bar 코드를 붙여넣어 주세요. -->
  <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="loginModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="loginInputEmail1" class="form-label">Email address</label>
              <input type="email" class="form-control" id="loginInputEmail1" aria-describedby="emailHelp">
              <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div class="mb-3">
              <label for="loginInputPassword1" class="form-label">Password</label>
              <input type="password" class="form-control" id="loginInputPassword1">
            </div>
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="loginCheck1">
              <label class="form-check-label" for="loginCheck1">Check me out</label>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top text-light">
    <div class="container-fluid">
      <a href="02_home.html" class="mx-0 w-25">
        <img src="./images/logo.png" alt="logo" class="w-50">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse flex-grow-0" id="navbarNav">
        <ul class="list-unstyled my-0 d-flex justify-content-start d-flex align-items-center">
          <li class="mx-3 nav-item"><a class="text-decoration-none text-light" href="02_home.html">Home</a></li>
          <li class="mx-3 nav-item"><a class="text-decoration-none text-light active" href="03_community.html">Community</a></li>
          <li class="mx-3"><button type="button" class="btn btn-link text-decoration-none text-light" data-bs-toggle="modal" data-bs-target="#loginModal">
            Login
          </button>
        </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- 03_community.html -->
  <div class="container">
    <div class="main row text-center">
      <h1 class="my-4">Community</h1>
      <!-- Sidebar -->
      <aside class="col-12 col-lg-2 mb-4">
        <ul class="list-group text-start">
          <li class="list-group-item"><a href="#">Boxoffice</a></li>
          <li class="list-group-item"><a href="#">Movies</a></li>
          <li class="list-group-item"><a href="#">Genres</a></li>
          <li class="list-group-item"><a href="#">Actors</a></li>
        </ul>
      </aside>

      <!-- Board -->
      <section class="col-12 col-lg-10">
        <div class="d-none d-lg-block col-lg-12">
          <table class="table table-striped text-start">
            <thead>
              <tr class="row table-dark">
                <th class="col">글 제목</th>
                <th class="col">영화 제목</th>
                <th class="col">사용자 id</th>
                <th class="col">작성시간</th>
              </tr>
            </thead>
            <tbody>
              <tr class="row">
                <td class="col">Title_of_article</td>
                <td class="col">Title_of_movie</td>
                <td class="col">user_id</td>
                <td class="col">update_time</td>
              </tr>
              <tr class="row">
                <td class="col">Title_of_article</td>
                <td class="col">Title_of_movie</td>
                <td class="col">user_id</td>
                <td class="col">update_time</td>
              </tr>
              <tr class="row">
                <td class="col">Title_of_article</td>
                <td class="col">Title_of_movie</td>
                <td class="col">user_id</td>
                <td class="col">update_time</td>
              </tr>
              <tr class="row">
                <td class="col">Title_of_article</td>
                <td class="col">Title_of_movie</td>
                <td class="col">user_id</td>
                <td class="col">update_time</td>
              </tr>
              <tr class="row">
                <td class="col">Title_of_article</td>
                <td class="col">Title_of_movie</td>
                <td class="col">user_id</td>
                <td class="col">update_time</td>
              </tr>
            </tbody>
          </table>
        </div>


        <div class="text-start d-block d-lg-none">
          <hr class="row">
          <article class="col">
            <h5 class="my-2">Title_of_article</h5>
            <p>Title_of_movie</p>
            <p>user_id / update_time</p>
          </article>
          <hr class="row">
          <article class="col">
            <h5 class="my-2">Title_of_article</h5>
            <p>Title_of_movie</p>
            <p>user_id / update_time</p>
          </article>
          <hr class="row">
          <article class="col">
            <h5 class="my-2">Title_of_article</h5>
            <p>Title_of_movie</p>
            <p>user_id / update_time</p>
          </article>
          <hr class="row">
          <article class="col">
            <h5 class="my-2">Title_of_article</h5>
            <p>Title_of_movie</p>
            <p>user_id / update_time</p>
          </article>
          <hr>
        </div>
      </section>
    </div>
    <div class="d-flex justify-content-center mb-4">
      <nav aria-label="Page navigation">
        <ul class="pagination">
          <li class="page-item"><a class="page-link" href="#">Previous</a></li>
          <li class="page-item"><a class="page-link" href="#">1</a></li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
          <li class="page-item"><a class="page-link" href="#">Next</a></li>
        </ul>
      </nav>
    </div>
  </div>

  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Footer 코드를 붙여넣어 주세요. -->
  <footer class="fixed-bottom bg-light text-center">
    <p class="my-1">Web-bootstrap PJT, by진윤태</p>
  </footer>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>  
</body>
</html>
```

* 문제후기

> * 이 문제에서 어려웠던점
>   * 바디의 요소가 화면의 크기에 따라 다르게 출력되는 것입니다. 방법을 알기 전에는 상당히 헤맸지만 방법을 알고 난 뒤에는 금방 해결할 수 있었습니다.
> * 내가 생각하는 이 문제의 포인트
>   * 화면의 크기에 따라 요소가 사라지고 나타나게 할 수 있는 것입니다.

# 💡후기

* web의 경우 직접 작성하면서 많은 연습이 필요한 것을 느꼈습니다. 구조를 만들어 가면서 구역을 어떻게 나누는가에 따라 배치할 때의 결과가 조금씩 달라지면서 생각보다 원하는대로 깔끔하게 이용하는 것이 아직은 어렵다고 느꼈습니다.
* bootstrap가 CSS 보다 편해서 CSS 없이 작성하는 것이 자칫 잘못하면 습관이 될 것 같습니다. 지금까지 실습과 homeworkshop을 하면서 일부는 CSS의 기능을 이용해야 하는 경우가 있었는데 CSS를 너무 이용하지 않는다면 필요한 경우에 기능을 구현하는데 차질을 겪거나 CSS의 문법을 이용해 요소의 스타일을 지정하는 방법을 숙달할 수 없게 되니 가끔씩이라도 CSS를 이용해 연습해 봐야겠습니다.
