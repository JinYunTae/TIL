# ๐PJT 02

## ๐์ด๋ฒ pjt ๋ฅผ ํตํด ๋ฐฐ์ด ๋ด์ฉ

* HTML์ ํตํด ์น ํ์ด์ง๋ฅผ ๋งํฌ์ ํ  ์ ์๋ค.
* CSS ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ดํดํ๊ณ  ํ์ฉํ  ์ ์๋ค.
* ์ปดํ๋ํธ ๋ฐ ๊ทธ๋ฆฌ๋ ์์คํ์ ํ์ฉํ  ์ ์๋ค.
* ์ปค๋ฎค๋ํฐ ์๋น์ค ๋ฐ์ํ ๋ ์ด์์์ ๊ตฌ์ฑํ  ์ ์๋ค.



## ๐ A. 01_nav_footer

* ์๊ตฌ ์ฌํญ : ์ปค๋ฎค๋ํฐ ์๋น์ค ๊ฐ๋ฐ์ ์ํ ํ๋ฉด ๊ตฌ์ฑ ๋จ๊ณ๋ก, ์ ์ ๊ฐ ๋ณด๋ ํ๋ก ํธ ์๋๋ฅผ ๊ฐ๋ฐํฉ๋๋ค.

> * ๋ค๋น๊ฒ์ด์ ๋ฐ(Navigation Bar)
>   1. ๋ค๋น๊ฒ์ด์ ๋ฐ๋ ์คํฌ๋กค์ ํ๋๋ผ๋ ํญ์ ์๋จ์ ๊ณ ์ ๋์ด ์์ต๋๋ค.
>   2. ๋ก๊ณ  ์ด๋ฏธ์ง๋ images ํด๋ ์์ logo.png ํ์ผ์ ์ฌ์ฉํฉ๋๋ค.
>   2. ๋ก๊ณ  ์ด๋ฏธ์ง๋ ํด๋ฆญ์ด ๊ฐ๋ฅํ ๋งํฌ์ด๋ฉฐ, ํด๋น ํ์ด์ง(02_home.html)๋ก ์ด๋ํด์ผ ํฉ๋๋ค.
>   2. ๋ค๋น๊ฒ์ด์ ๋ฐ ๋ด๋ถ์ ๋ฆฌ์คํธ(Home, Community, Login)๋ ul๊ณผ li์์๋ฅผ ์ฌ์ฉํฉ๋๋ค.
>   2. ๋ค๋น๊ฒ์ด์ ๋ฐ ๋ด๋ถ์ ๋ค๋น๊ฒ์ด์ ๋ฆฌ์คํธ(Home, Community, Login)๋ ์ค๋ฅธ์ชฝ์ ๋ฐฐ์นํฉ๋๋ค.
>   2. ๋ค๋น๊ฒ์ด์ ๋ฆฌ์คํธ์ ๊ฐ ํญ๋ชฉ๋ค์ ํด๋ฆญ์ด ๊ฐ๋ฅํ ๋งํฌ์ด๋ฉฐ, ํด๋น ํ์ด์ง(02_home.html, 03_community.html, #)๋ก ์ด๋ํด์ผ ํฉ๋๋ค.
>   2. Viewport์ ๊ฐ๋ก ํฌ๊ธฐ๊ฐ 768px ๋ฏธ๋ง์ผ ๊ฒฝ์ฐ์๋ ๋ค๋น๊ฒ์ด์ ๋ฆฌ์คํธ(Home, Community, Login)๊ฐ ํ๋ฒ๊ฑฐ ๋ฒํผ์ผ๋ก ๊ต์ฒด๋๋ฉฐ, ํด๋ฆญํ์ ์ ์ธ๋ถ ํญ๋ชฉ์ ๋ณผ ์ ์์ต๋๋ค.
>   2. ๋ค๋น๊ฒ์ด์ ๋ฆฌ์คํธ(Home, Community, Login)์ ํญ๋ชฉ๋ค ์ค์์ Home์ ๊ฐ์กฐํฉ๋๋ค.
>   9. ๋ค๋น๊ฒ์ด์ ๋ฆฌ์คํธ์ Login ํญ๋ชฉ์ ํด๋ฆญ ์ ์์๊ฐ Modal ์ปดํฌ๋ํธ๋ฅผ ํตํ์ฌ ๋ํ๋ฉ๋๋ค.
>      (ํ์ด์ง ์ด๋์ด ์ผ์ด๋์ง ์์ต๋๋ค.)
>   10. Modal ์ปดํฌ๋ํธ ๋ด๋ถ์๋ form์์๋ฅผ ๋ฐฐ์นํฉ๋๋ค.
>   11. Modal ์ปดํฌ๋ํธ์์ form์์ ๋ด๋ถ์ ๋น๋ฐ๋ฒํธ๋ ํ์๋์ง ์์ต๋๋ค.
>   
> * ํธํฐ(Footer)
>   1. ํธํฐ๋ ์คํฌ๋กค์ ํ๋๋ผ๋ ํญ์ ํ๋จ์ ๊ณ ์ ๋์ด ์์ต๋๋ค.
>   2. ํธํฐ์ ์์ฑ๋ ๋ด์ฉ์ ์ํ์ผ๋ก ์ ๋ ฌ๋์ด ์์ต๋๋ค. (์ผ์ชฝ, ์ค๋ฅธ์ชฝ ์ฌ๋ฐฑ์ด ๊ฐ์ต๋๋ค.)
>   2. ํธํฐ์ ์์ฑ๋ ๋ด์ฉ์ ๋น ๋ถ๋ถ(`_____`)์ ๋ณธ์ธ์ ์ด๋ฆ์ ์์ฑํฉ๋๋ค.
>   2. ์์ ๋ช์๋ ๋ด์ฉ ์ด์ธ์๋ ์์ ๋กญ๊ฒ ์์ฑํฉ๋๋ค.

* ๋ฌธ์  ์ ๊ทผ ๋ฐฉ๋ฒ ๋ฐ ์ฝ๋ ์ค๋ช

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
    <p class="my-1">Web-bootstrap PJT, by์ง์คํ</p>
  </footer>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
</body>
</html>
```

* ๋ฌธ์ ํ๊ธฐ

>* ์ด ๋ฌธ์ ์์ ์ด๋ ค์ ๋์ 
>  * ๋ค๋น๊ฒ์ด์ ๋ฐ๋ฅผ ๋ณต์ฌํด์ ์ฌ์ฉํ์ง ์๊ณ  ์ค์ตํ ๊ฒฝํ์ ์ด์ฉํด ์ง์  ์์ฑํด์ ์๊ฐ์ด ๋ง์ด ๊ฑธ๋ ธ์ต๋๋ค.
>  * ์ด๋ฏธ์ง์ ํฌ๊ธฐ๊ฐ ๋๋ฌด ์ปค์ ์กฐ์ ํ๊ธฐ ํ๋ค์์ต๋๋ค. ๋น์จ์ ์ด์ฉํด ์ค์ ํ๋ ํ๋ฉด์ด ์์์ง๋ฉด ๋๋ฌด ์์์ง๋ ๋ฌธ์ ๊ฐ ์์ด ๋น์จ ์กฐ์ ์ด ํ๋ค์์ต๋๋ค.
>  * ๋ค๋น๊ฒ์ด์ ๋ฐ์์ ํ๋ฉด ํฌ๊ธฐ๊ฐ ์์์ง๋ฉด ํ๋ฒ๊ฑฐ ๋ฒํผ์ผ๋ก ์ ํํ๋ฉด์ ๋ง์ ์ด๋ ค์์ด ์์์ต๋๋ค.
>* ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ
>  * ํ๋ฉด ํฌ๊ธฐ๊ฐ ์์์ง๋ฉด ๋ค๋น๊ฒ์ด์ ๋ฐ์ ํญ๋ชฉ์ด ํ๋ฒ๊ฑฐ ๋ฒํผ์ผ๋ก ์ ํ๋๋ ๊ฒ์ด ๊ฐ์ฅ ํต์ฌ์ด ๋๋ ํฌ์ธํธ ๊ฐ์ต๋๋ค.

-----

## ๐ B. 02_home

* ์๊ตฌ ์ฌํญ : 01_nav_footer๋ฅผ ์์ฑํ๋ค๋ฉด, ๋ค๋น๊ฒ์ด์ ๋ฐ์ ํธํฐ๋ฅผ ๋ณต์ฌํด ์ฌ์ฉํฉ๋๋ค.

> * ๋ค๋น๊ฒ์ด์ ๋ฐ(Navigation Bar) ๋ฐ ํ์ด์ง ๊ตฌ์ฑ
>   1. ๋ค๋น๊ฒ์ด์ ๋ฆฌ์คํธ(Home, Community, Login)์ ํญ๋ชฉ๋ค ์ค์์ Home์ ๊ฐ์กฐํฉ๋๋ค.
>      (active)
>   2. Home ํ์ด์ง๋ ํฌ๊ฒ ์๋จ Header์ ํ๋จ Section์์๋ก ์ด๋ฃจ์ด์ ธ ์์ต๋๋ค.
> * ํค๋(Header) 
>   1. Header๋ Carousel ์ปดํฌ๋ํธ๋ก ๊ตฌ์ฑํฉ๋๋ค. ์ด๋ฏธ์ง๋ ์ต์ 3์ฅ์ด๋ฉฐ, ์๋์ผ๋ก ์ ํ๋ฉ๋๋ค.
>      (images/ ํด๋ ์์ header ์ด๋ฏธ์ง๋ค์ ์ฌ์ฉํฉ๋๋ค.)
> * ์น์(Section)
>   1. Box Office ๋ฌธ๊ตฌ๋ ์์ ๋กญ๊ฒ ์คํ์ผ๋ง ํฉ๋๋ค.
>   2. Section์ ์ปจํ์ด๋ ๋ด๋ถ์ ์์นํฉ๋๋ค.
>   3. Section ๋ด๋ถ์ ๊ฐ๋ณ ์์(article)๋ค์ ์ด๋ฏธ์ง, ์ ๋ชฉ, ์ค๋ช์ ํฌํจํ๋ Card ์ปดํฌ๋ํธ๋ก
>      ๊ตฌ์ฑํฉ๋๋ค. (์ด๋ฏธ์ง๋ images ํด๋์ ํฌ์คํฐ ์ด๋ฏธ์ง๋ฅผ ์ฌ์ฉํฉ๋๋ค. (์ด6๊ฐ))
>   4. ๊ฐ ์์๋ค์ ์ข์ฐ ์ผ์ ํ ๊ฐ๊ฒฉ์ผ๋ก ๋จ์ด์ ธ ์์ต๋๋ค. (๊ฐ๊ฒฉ์ ์์ ๋กญ๊ฒ ์ค์  ๊ฐ๋ฅํฉ๋๋ค.)
>   5. Section ๋ด๋ถ์ ์์(article)๋ค์ Viewport์ ๊ฐ๋ก ํฌ๊ธฐ๊ฐ 576px๋ฏธ๋ง์ผ ๊ฒฝ์ฐ์๋ ํ ํ
>      (row)์ 1๊ฐ์ฉ ํ์๋ฉ๋๋ค.
>   6. Section ๋ด๋ถ์ ์์(article)๋ค์ Viewport์ ๊ฐ๋ก ํฌ๊ธฐ๊ฐ 576px์ด์์ผ ๊ฒฝ์ฐ์๋ ํ ํ
>      (row)์ 2๊ฐ ์ด์ ์์ ๋กญ๊ฒ ํ์ํฉ๋๋ค.
>   7. ์์ ๋ช์๋ ๋ด์ฉ ์ด์ธ์๋ ์์ ๋กญ๊ฒ ์์ฑํฉ๋๋ค.

* ๋ฌธ์  ์ ๊ทผ ๋ฐฉ๋ฒ ๋ฐ ์ฝ๋ ์ค๋ช

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
  <!-- 01_nav_footer ์์ ์์ฑํ Navigation bar ์ฝ๋๋ฅผ ๋ถ์ฌ๋ฃ์ด ์ฃผ์ธ์. -->
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
  <!-- 01_nav_footer ์์ ์์ฑํ Footer ์ฝ๋๋ฅผ ๋ถ์ฌ๋ฃ์ด ์ฃผ์ธ์. -->
  <footer class="fixed-bottom bg-light text-center">
    <p class="my-1">Web-bootstrap PJT, by์ง์คํ</p>
  </footer>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>  
</body>
</html>
```

* ๋ฌธ์ ํ๊ธฐ

> * ์ด ๋ฌธ์ ์์ ์ด๋ ค์ ๋์ 
>   * ๊ธฐ์กด์ ๋ง์ด ์ค์ตํ๋ฉด์ ์ฐ์ตํ๋ ๋ด์ฉ์ด๋ผ ๋คํ์ด ๋ฌด๋ฆฌ ์์ด ์งํํ  ์ ์์์ต๋๋ค.
> * ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ
>   * ๊ธฐ์กด์ ๋ง์ด ์ค์ตํ๋ ์ฌ์ง์ ๋ฐฐ์น๊ฐ ์ฃผ๋ ์์์ฌ์ ๋น๊ต์  ์ฝ๊ฒ ํด๊ฒฐํ  ์ ์์์ต๋๋ค. ํนํ ์ด์  ์ค์ต ์๊ฐ์ card์ carousel์ ์๋ ค์ฃผ์์ ์ํํ๊ฒ ํ  ์ ์์์ต๋๋ค.

## ๐ C. 03_community

* ์๊ตฌ ์ฌํญ : 01_nav_footer๋ฅผ ์์ฑํ๋ค๋ฉด, ๋ค๋น๊ฒ์ด์ ๋ฐ์ ํธํฐ๋ฅผ ๋ณต์ฌํ์ฌ ์ฌ์ฉํฉ๋๋ค.

> * ๋ค๋น๊ฒ์ด์ ๋ฐ(Navigation Bar) ๋ฐ ํ์ด์ง ๊ตฌ์ฑ
>
>   1. ๋ค๋น๊ฒ์ด์ ๋ฆฌ์คํธ(Home, Community, Login)์ ํญ๋ชฉ๋ค ์ค์์ Community๋ฅผ
>      ๊ฐ์กฐํฉ๋๋ค. (active)
>   2. Community ํ์ด์ง๋ ํฌ๊ฒ ๊ฒ์ํ ๋ชฉ๋ก, ๊ฒ์ํ์ผ๋ก ์ด๋ฃจ์ด์ ธ ์์ต๋๋ค.
>   2. ๊ฒ์ํ ๋ชฉ๋ก๊ณผ ๊ฒ์ํ์ div.main ์์๋ก ๋๋ฌ ์์ฌ ์์ต๋๋ค.
>   2. ๊ฒ์ํ ๋ชฉ๋ก๊ณผ ๊ฒ์ํ, ๊ฒ์๊ธ ํ์ด์ง์ ๋ชจ๋ ์ปจํ์ด๋ ๋ด๋ถ์ ์์นํฉ๋๋ค.
>
> * ๊ฒ์ํ ๋ชฉ๋ก
>   1. ๊ฒ์ํ ๋ชฉ๋ก์ aside ์์๋ก ์ด๋ฃจ์ด์ ธ ์์ต๋๋ค.
>   2. ๊ฒ์ํ ๋ชฉ๋ก ๋ด๋ถ์ ๊ฐ ํญ๋ชฉ(Boxoffice, Movies, Genres, Actors)์ List group
>      ์ปดํฌ๋ํธ๋ฅผ ํ์ฉํฉ๋๋ค.
>   3. ๊ฒ์ํ ๋ชฉ๋ก ๋ด๋ถ์ ๊ฐ ํญ๋ชฉ์ ํด๋ฆญ์ด ๊ฐ๋ฅํ ๋งํฌ์ด์ง๋ง, URL์ ๋ณ๋๋ก ์์ด #์ผ
>      ๋ก ์ง์ ํฉ๋๋ค.
>   4. Viewport์ ๊ฐ๋ก ํฌ๊ธฐ๊ฐ 992px ์ด์์ผ ๊ฒฝ์ฐ์๋ ๊ฒ์ํ ๋ชฉ๋ก ๋ด๋ถ์ ํญ๋ชฉ
>      (Boxoffice, Movies, Genres, Actors)์ div.main์์ญ์ ๋ด๋ถ์์ ์ข์ธก 1/6 ๋งํผ
>      ์ ๋๋น๋ฅผ ๊ฐ์ง๋๋ค.
>   5. Viewport์ ๊ฐ๋ก ํฌ๊ธฐ๊ฐ 992px ๋ฏธ๋ง์ผ ๊ฒฝ์ฐ์๋ ๊ฒ์ํ ๋ชฉ๋ก ๋ด๋ถ์ ํญ๋ชฉ
>      (Boxoffice, Movies, Genres, Actors)์ div.main์์ญ์ ๋ด๋ถ์์ ์ ์ฒด๋งํผ์ ๋
>      ๋น๋ฅผ ๊ฐ์ง๋๋ค.
>   
> * ๊ฒ์ํ
>
>   1. ๊ฒ์ํ์ Viewport์ ๊ฐ๋กํฌ๊ธฐ์ ๋ฐ๋ผ ์ ํ ๋ค๋ฅธ ์์๋ฅผ ํ์ํฉ๋๋ค.
>
>      1. Viewport์ ๊ฐ๋ก ํฌ๊ธฐ๊ฐ 992px ์ด์์ผ ๊ฒฝ์ฐ์๋ ๊ฒ์๊ธ์ด ํ(table) ์์๋ก
>         ํ์๋๋ฉฐ, div.main์์ญ์ ๋ด๋ถ์์ ์ฐ์ธก 5/6 ๋งํผ์ ๋๋น๋ฅผ ๊ฐ์ง๋๋ค.
>
>      2. Viewport์ ๊ฐ๋ก ํฌ๊ธฐ๊ฐ 992px ๋ฏธ๋ง์ผ ๊ฒฝ์ฐ์๋ ๊ฒ์๊ธ์ด ๊ธ(article) ์์๋ค
>         ์ ์งํฉ์ผ๋ก ํ์๋๊ณ  ๊ฐ๋ก์ ์ผ๋ก ๊ตฌ๋ถํฉ๋๋ค(์คํ์ผ๋ง์ ์์ ๋กญ๊ฒ ์งํํฉ๋
>         ๋ค). div.main์์ญ์ ๋ด๋ถ์์ ์ ์ฒด๋งํผ์ ๋๋น๋ฅผ ๊ฐ์ง๋๋ค.
>
>   2. ๊ฒ์๊ธ์ ๊ธ ์ ๋ชฉ, ์ํ ์ ๋ชฉ, ์ฌ์ฉ์ id, ์์ฑ์๊ฐ์ผ๋ก ๊ตฌ์ฑ๋์ด ์์ต๋๋ค.
>
>   3. ํ์คํธ ๊ฒ์๊ธ์ ๊ฐ์์ ๋ด์ฉ์ 2๊ฐ ์ด์์ผ๋ก ์์ ๋กญ๊ฒ ๊ตฌ์ฑํ  ์ ์์ต๋๋ค.
>
>   4. ๊ฒ์๊ธ ํ์ด์ง(paginator)์ ๊ฒ์ํ ์๋์ ์์นํ๋ฉฐ, ๋๋น๋ ์์ ๋กญ๊ฒ ํฉ๋๋ค.
>
>   5. ๊ฒ์๊ธ ํ์ด์ง(paginator)์ ์์ ์ ์์ญ ์์์ ์ข์ฐ ์ค์ ์ ๋ ฌ๋์ด ์์ต๋๋ค.
>
>   6. ๊ฒ์๊ธ ํ์ด์ง(paginator) ๋ด๋ถ์ ์์๋ค์ ํด๋ฆญ์ด ๊ฐ๋ฅํ ๋งํฌ์ด๋ฉฐ, URL์ ๋ณ๋
>      ๋ก ์์ด #์ผ๋ก ์ง์ ํฉ๋๋ค.
>
>   7. ์์ ๋ช์๋ ๋ด์ฉ ์ด์ธ์๋ ์์ ๋กญ๊ฒ ์์ฑํฉ๋๋ค.

* ๋ฌธ์  ์ ๊ทผ ๋ฐฉ๋ฒ ๋ฐ ์ฝ๋ ์ค๋ช

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
  <!-- 01_nav_footer ์์ ์์ฑํ Navigation bar ์ฝ๋๋ฅผ ๋ถ์ฌ๋ฃ์ด ์ฃผ์ธ์. -->
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
                <th class="col">๊ธ ์ ๋ชฉ</th>
                <th class="col">์ํ ์ ๋ชฉ</th>
                <th class="col">์ฌ์ฉ์ id</th>
                <th class="col">์์ฑ์๊ฐ</th>
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
  <!-- 01_nav_footer ์์ ์์ฑํ Footer ์ฝ๋๋ฅผ ๋ถ์ฌ๋ฃ์ด ์ฃผ์ธ์. -->
  <footer class="fixed-bottom bg-light text-center">
    <p class="my-1">Web-bootstrap PJT, by์ง์คํ</p>
  </footer>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>  
</body>
</html>
```

* ๋ฌธ์ ํ๊ธฐ

> * ์ด ๋ฌธ์ ์์ ์ด๋ ค์ ๋์ 
>   * ๋ฐ๋์ ์์๊ฐ ํ๋ฉด์ ํฌ๊ธฐ์ ๋ฐ๋ผ ๋ค๋ฅด๊ฒ ์ถ๋ ฅ๋๋ ๊ฒ์๋๋ค. ๋ฐฉ๋ฒ์ ์๊ธฐ ์ ์๋ ์๋นํ ํค๋งธ์ง๋ง ๋ฐฉ๋ฒ์ ์๊ณ  ๋ ๋ค์๋ ๊ธ๋ฐฉ ํด๊ฒฐํ  ์ ์์์ต๋๋ค.
> * ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ
>   * ํ๋ฉด์ ํฌ๊ธฐ์ ๋ฐ๋ผ ์์๊ฐ ์ฌ๋ผ์ง๊ณ  ๋ํ๋๊ฒ ํ  ์ ์๋ ๊ฒ์๋๋ค.

# ๐กํ๊ธฐ

* web์ ๊ฒฝ์ฐ ์ง์  ์์ฑํ๋ฉด์ ๋ง์ ์ฐ์ต์ด ํ์ํ ๊ฒ์ ๋๊ผ์ต๋๋ค. ๊ตฌ์กฐ๋ฅผ ๋ง๋ค์ด ๊ฐ๋ฉด์ ๊ตฌ์ญ์ ์ด๋ป๊ฒ ๋๋๋๊ฐ์ ๋ฐ๋ผ ๋ฐฐ์นํ  ๋์ ๊ฒฐ๊ณผ๊ฐ ์กฐ๊ธ์ฉ ๋ฌ๋ผ์ง๋ฉด์ ์๊ฐ๋ณด๋ค ์ํ๋๋๋ก ๊น๋ํ๊ฒ ์ด์ฉํ๋ ๊ฒ์ด ์์ง์ ์ด๋ ต๋ค๊ณ  ๋๊ผ์ต๋๋ค.
* bootstrap๊ฐ CSS ๋ณด๋ค ํธํด์ CSS ์์ด ์์ฑํ๋ ๊ฒ์ด ์์นซ ์๋ชปํ๋ฉด ์ต๊ด์ด ๋  ๊ฒ ๊ฐ์ต๋๋ค. ์ง๊ธ๊น์ง ์ค์ต๊ณผ homeworkshop์ ํ๋ฉด์ ์ผ๋ถ๋ CSS์ ๊ธฐ๋ฅ์ ์ด์ฉํด์ผ ํ๋ ๊ฒฝ์ฐ๊ฐ ์์๋๋ฐ CSS๋ฅผ ๋๋ฌด ์ด์ฉํ์ง ์๋๋ค๋ฉด ํ์ํ ๊ฒฝ์ฐ์ ๊ธฐ๋ฅ์ ๊ตฌํํ๋๋ฐ ์ฐจ์ง์ ๊ฒช๊ฑฐ๋ CSS์ ๋ฌธ๋ฒ์ ์ด์ฉํด ์์์ ์คํ์ผ์ ์ง์ ํ๋ ๋ฐฉ๋ฒ์ ์๋ฌํ  ์ ์๊ฒ ๋๋ ๊ฐ๋์ฉ์ด๋ผ๋ CSS๋ฅผ ์ด์ฉํด ์ฐ์ตํด ๋ด์ผ๊ฒ ์ต๋๋ค.
