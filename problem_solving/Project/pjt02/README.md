# ๐PJT 02

## ๐์ด๋ฒ pjt ๋ฅผ ํตํด ๋ฐฐ์ด ๋ด์ฉ

* ์ค์  ์ด์ฉ๋๋ ์ฌ์ดํธ๋ค์ URL์ด ์ด๋ค ๋ฐฉ์์ผ๋ก ๊ตฌ์ฑ๋์ด ์๋์ง ์์ ๋ณผ ์ ์์์ต๋๋ค.
* API์ ์ด์ฉํด ์ฌ์ดํธ์ ์ ๋ณด๋ฅผ ์์ฒญํ๊ณ  ์๋ต์ ๋ฐ์ ์ฌ์ดํธ ๋ด ์๋ฃ๋ฅผ ์ง์  ํ์ฉํด ๋ณผ ์ ์์์ต๋๋ค.



## ๐์๊ตฌ์ฌํญ

์ปค๋ฎค๋ํฐ ์๋น์ค ๊ฐ๋ฐ์ ์ํ ๋ฐ์ดํฐ ์์ง ๋จ๊ณ๋ก, ์ ์ฒด ๋ฐ์ดํฐ ์ค ํ์ํ ์ํ ๋ฐ์ดํฐ๋ฅผ ์์งํ๋ ๊ณผ์ ์๋๋ค. ์๋ ๊ธฐ์ ๋ ์ฌํญ์ ํ์์ ์ผ๋ก ๊ตฌํํด์ผ ํ๋ ๋ด์ฉ์๋๋ค. ์์ฑ๋ ๊ธฐ๋ฅ๋ค์, ํฅํ ์ปค๋ฎค๋ํฐ ์๋น์ค์์ ํ์ฉํ  ์ ์์ต๋๋ค.

### ๐ A. ์ธ๊ธฐ ์ํ ์กฐํ

* ์๊ตฌ ์ฌํญ : ์ธ๊ธฐ ์ํ์ ๊ฐ์๋ฅผ ์ถ๋ ฅํฉ๋๋ค.

> * ์์ฒญ
>   1. requests๋ฅผ ์ด์ฉํ์ฌ ์ธ๊ธฐ ์ํ ์ ๋ณด(Get Popular)์ ์์ฒญ์ ๋ณด๋๋๋ค.
> * ๊ฒฐ๊ณผ : 
>   1. popular๋ฅผ ๊ธฐ์ค์ผ๋ก ๋ฐ์์จ ๋ฐ์ดํฐ์์ ์ํ ๋ฆฌ์คํธ์ ๊ฐ์๋ฅผ ๊ณ์ฐํฉ๋๋ค.
>   2. ๊ณ์ฐํ ์ ๋ณด๋ฅผ ๋ฐํํ๋ ํจ์ popular_count๋ฅผ ์์ฑํฉ๋๋ค.

* ๋ฌธ์  ์ ๊ทผ ๋ฐฉ๋ฒ ๋ฐ ์ฝ๋ ์ค๋ช

```python
import requests


def popular_count():
	pass
 	# ์ฌ๊ธฐ์ ์ฝ๋๋ฅผ ์์ฑํฉ๋๋ค.
    
    # ๊ธฐ๋ณธ์ด ๋๋ URL์๋๋ค.
    BASE_URL = 'https://api.themoviedb.org/3'
    # ๊ธฐ๋ฅ์ ์ํ path์๋๋ค.
    path = '/movie/popular'
    # ํ์ํ ํ๋ผ๋ฏธํฐ๋ค์๋๋ค.
    params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko',
        'region' : 'KR'
    }

    # ์์ฒญ์ ๋ฐ๋ฅธ ์๋ต์ ๋ฐ์ต๋๋ค.
    response = requests.get(BASE_URL + path, params = params)
    # print(response) # 200!
    data = response.json() # dict
    # dict_keys(['page', 'results', 'total_pages', 'total_results'])
    pm_list = data.get('results')
    # print(data.get('results')) # results ํญ๋ชฉ์ ์ํ ์ ๋ณด๊ฐ ๋ค ์์ต๋๋ค.
    # print(type(data.get('results'))) # results์ ํญ๋ชฉ์ ๋์๋๋ฆฌ๋ฅผ ์์๋ก ๊ฐ๋ ๋ฆฌ์คํธ์๋๋ค.
    num_of_popular = len(pm_list) # ์ธ๊ธฐ์๋ ์ํ์ ์
    # print(num_of_popular) # => 20
    
    return num_of_popular
```

* ๋ฌธ์ ํ๊ธฐ

>* ์ด ๋ฌธ์ ์์ ์ด๋ ค์ ๋์ 
>   * ์์ฒญ์ ๋ํ ์๋ต์ ๋ฐ์์จ ๋ค ๋ฐ์ดํฐ๋ฅผ ์ฒ๋ฆฌํ  ๋ ์ด๋ค ์๋ฃํ์ด ๋์ด์๋์ง ๋งค ์ ์ฐจ๋ง๋ค ํ์ธ์ด ํ์ํ์ต๋๋ค. ๋ํ ๊ฐ ์๋ฃํ์์ ์ด๋ค ํญ๋ชฉ์ ์์๋ค์ ์ด์ฉํด์ผํ๋์ง ์์๋ณด๊ธฐ ์ํด ๊ฐ ๊ณผ์ ๋ง๋ค ์ถ๋ ฅํด ํ์ธํด์ผ ํ์ต๋๋ค. 
>* ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ
>   * ์๋ต๋ฐ์ ์ ๋ณด๊ฐ ์ด๋ค ํํ์ธ์ง, ์ด๋ ํ ์ ๋ณด๋ฅผ ๋ด๊ณ  ์๋์ง ๊ฐ ๋จ๊ณ๋ณ๋ก ํ์ธํด ํ์ํ ๊ฐ๋ค์ ์ฐพ์ ์ธ ์ ์๋๋ก ํ๋ ๊ฒ์๋๋ค. ๋ค๋ฅธ ์์์ ํ๋๋ผ๋ ์ด๋ฌํ ๊ณผ์ ์ ๊ฑฐ์น๊ฒ ๋๋ฉด ๋ฐ์ดํฐ๋ฅผ ์ ๋ชป ์ฌ์ฉํด ๋ฌธ์ ๊ฐ ๋ฐ์ํ๋ ๊ฒ์ ๋ฐฉ์งํ  ์ ์์ต๋๋ค.

-----

### ๐ B. ํน์  ์กฐ๊ฑด์ ๋ง๋ ์ธ๊ธฐ ์ํ ์กฐํ I

* ์๊ตฌ ์ฌํญ : popular๋ฅผ ๊ธฐ์ค์ผ๋ก ๊ฐ์ ธ์จ ์ํ ๋ชฉ๋ก ์ค ํ์ ์ด 8 ์ด์์ธ ์ํ๋ค์ ๋ชฉ๋ก์ ์ถ๋ ฅํฉ๋๋ค.

> * ์์ฒญ
>   1. requests๋ฅผ ์ด์ฉํ์ฌ ์ธ๊ธฐ ์ํ ์ ๋ณด(Get Popular)์ ์์ฒญ์ ๋ณด๋๋๋ค.
> * ๊ฒฐ๊ณผ : 
>   1. ๋ฐ์์จ ๋ฐ์ดํฐ์์ vote_average๋ฅผ ๊ธฐ์ค์ผ๋ก ์ ์๊ฐ 8 ์ด์์ธ ์ํ๋ค์ ๋ชฉ๋ก์ ๋ฆฌ์คํธ๋ก ๋ฐํํ๋ ํจ์ vote_average_movies๋ฅผ ์์ฑํฉ๋๋ค.

* ๋ฌธ์  ์ ๊ทผ ๋ฐฉ๋ฒ ๋ฐ ์ฝ๋ ์ค๋ช

```python
import requests
from pprint import pprint


def vote_average_movies():
	pass
 	# ์ฌ๊ธฐ์ ์ฝ๋๋ฅผ ์์ฑํฉ๋๋ค.
    
    # ๊ธฐ๋ณธ์ด ๋๋ URL์๋๋ค.
    BASE_URL = 'https://api.themoviedb.org/3'
    # ๊ธฐ๋ฅ์ ์ํ path์๋๋ค.
    path = '/movie/popular'
    # ํ์ํ ํ๋ผ๋ฏธํฐ์๋๋ค.
    params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko',
        'region' : 'KR'
    }

    #์์ฒญ์ ๋ฐ๋ฅธ ์๋ต์ ๋ฐ์ต๋๋ค.
    response = requests.get(BASE_URL + path, params = params)
    # print(response) # 200!
    data = response.json()
    p_m_list = data.get('results') # dict
    # print(data.get('results')[0].keys())
    # dict_keys([
    #       'adult', 'backdrop_path', 'genre_ids',
    #       'id', 'original_language', 'original_title',
    #       'overview', 'popularity', 'poster_path',
    #       'release_date', 'title', 'video',
    #       'vote_average', 'vote_count'
    # ])
    # vote_average์ value๋ฅผ ์ด์ฉ
    
    high_score_movie = []
    for movie in p_m_list:
        if movie.get('vote_average') >= 8: # ์ํ์ ํ์ ์ด 8์  ์ด์์ด๋ฉด
            high_score_movie.append(movie) # ๋ชฉ๋ก์ ์ถ๊ฐํฉ๋๋ค.
    
    return high_score_movie
```

* ๋ฌธ์ ํ๊ธฐ

> * ์ด ๋ฌธ์ ์์ ์ด๋ ค์ ๋์ 
>   * ์์ ๊ตฌํํ ์กฐํ์์ ๋ ๋์๊ฐ ๋ฆฌ์คํธ์ ์์๋ก ํฌํจ๋ ๋์๋๋ฆฌ๋ฅผ ์ด์ฉํด ์ ๋ณด๋ฅผ ์ฐพ์์ค๋ ๊ณผ์ ์ด์์ต๋๋ค. ์ง๋ ํ๋ก์ ํธ์ ์ด์ด ๋์ผํ ๋ฐฉ์์ ์ด์ฉํ๋ฉด ๋์๊ธฐ์ ํฌ๊ฒ ์ด๋ ค์์ ์์์ต๋๋ค.
>   * ์ฒ์ ์ฝ๋๋ฅผ ์ง๋ ๋์ค์๋ ์ฒซ ๋์๋๋ฆฌ์ ํค๋ค๋ง ์ฐธ๊ณ ๋ก ํ์ธํ ๊ฒ์ ๋ํด ๋ค๋ฅธ ๋์๋๋ฆฌ์ ํค ๊ตฌ์ฑ์ด ๋ค๋ฅผ ๊ฒฝ์ฐ ์ด๋ป๊ฒ ํ๋ ๊ณ ๋ฏผํ์ผ๋ .get()์ ์ฐ๋ฉด์ ๋ง์ฝ ์ํ๋ ํค๊ฐ ์๋๋ผ๋ ๋ฌธ์ ๊ฐ ์๋ค๋ ๊ฒ์ ๋ค์ ๋ ์ฌ๋ ธ์ต๋๋ค.
> * ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ
>   * ๋ฆฌ์คํธ ๋ด๋ถ์ ์์๋ก ํฌํจ๋ ๋ง์ ๋์๋๋ฆฌ์ ์ ๊ทผํด key๋ก value๋ฅผ ์ฐธ์กฐํ  ์ ์๋๊ฐ๋ฅผ ๋ค์ ๋ณต์ตํ๋ ๋ฌธ์ ์์ต๋๋ค.
>   * ์ฝ๋๋ฅผ ๋ค ์์ฑํ๊ณ  ๋์๋ณด๋ฉด์ 8 ์ด์์ธ ์๊ตฌ์กฐ๊ฑด์ 8 ์ด๊ณผ๋ก ์๋ชป ์ ์ฉํ๋ ๊ฒ์ ํ์ธํ๊ณ  ์์ ํ์ต๋๋ค.  ๊ฒฝ๊ณ์กฐ๊ฑด์ ๋ํ ๋ด์ฉ์ ์ค์๋ฅผ ํ์ง ์๋๋ก ์ฃผ์ํด์ผ๊ฒ ์ต๋๋ค.

### ๐ C.  ํน์  ์กฐ๊ฑด์ ๋ง๋ ์ธ๊ธฐ ์ํ ์กฐํ II

* ์๊ตฌ ์ฌํญ : ์ํ๋ชฉ๋ก์ ํ์ ์์ผ๋ก ์ถ๋ ฅํ๋ ํจ์๋ฅผ ์์ฑํฉ๋๋ค. ํด๋น ๊ธฐ๋ฅ์ ํฅํ ์ปค๋ฎค๋ํฐ ์๋น์ค์์ ๊ธฐ๋ณธ์ผ๋ก ์ ๊ณต๋๋ ์ํ ์ ๋ณด๋ก ์ฌ์ฉ๋ฉ๋๋ค.

> * ์์ฒญ
>   1. requests๋ฅผ ์ด์ฉํ์ฌ ์ธ๊ธฐ ์ํ ์ ๋ณด(Get Popular)์ ์์ฒญ์ ๋ณด๋๋๋ค.
> * ๊ฒฐ๊ณผ : 
>   1. ๋ฐ์์จ ๋ฐ์ดํฐ ์ค ํ์ ์ด ๋์ ์ํ ๋ค์ฏ๊ฐ์ ์ ๋ณด๋ฅผ ๋ฆฌ์คํธ๋ก ๋ฐํํ๋ ํจ์ ranking์ ์์ฑํฉ๋๋ค.

* ๋ฌธ์  ์ ๊ทผ ๋ฐฉ๋ฒ ๋ฐ ์ฝ๋ ์ค๋ช

```python
import requests
from pprint import pprint


def ranking():
    pass
 	# ์ฌ๊ธฐ์ ์ฝ๋๋ฅผ ์์ฑํฉ๋๋ค.
    
    # ๊ธฐ๋ณธ์ด ๋๋ URL์๋๋ค.
    BASE_URL = 'https://api.themoviedb.org/3'
    # ๊ธฐ๋ฅ์ ์ํ path์๋๋ค.
    path = '/movie/popular'
    # ํ์ํ ํ๋ผ๋ฏธํฐ๋ค์๋๋ค.
    params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko',
        'region' : 'KR'
    }

    #์์ฒญ์ ๋ฐ๋ฅธ ์๋ต์ ๋ฐ์ต๋๋ค.
    response = requests.get(BASE_URL + path, params = params)
    # print(response) # 200!
    p_m_list = response.json().get('results') # results ํญ๋ชฉ๋ง ๋ฐ์ต๋๋ค.

    for i in range(1, len(p_m_list)): # ๋ด๋ถ ๋์๋๋ฆฌ๋ค์ ํ์ ์ ๋ฐ๋ผ ์ ๋ ฌํฉ๋๋ค.
        for j in range(len(p_m_list)-i):
            # ํ์ ์ด ๋์ ์์ผ๋ก ์ ๋ ฌํฉ๋๋ค.
            if p_m_list[j]['vote_average'] < p_m_list[j+1]['vote_average']: 
                p_m_list[j], p_m_list[j+1] = p_m_list[j+1], p_m_list[j]

    return p_m_list[:5] # ํ์ ์ด ๋์ 5๊ฐ์ ์ํ ์ ๋ณด๋ฅผ ๋ฐํํฉ๋๋ค.
```

```python
# sorted()๋ฅผ ์ด์ฉํ ๊ฒฝ์ฐ

```

* ๋ฌธ์ ํ๊ธฐ

> * ์ด ๋ฌธ์ ์์ ์ด๋ ค์ ๋์ 
>   * ๋์๋๋ฆฌ์ value๋ฅผ ๊ธฐ์ค์ผ๋ก sorted()๋ฅผ ์ ์ฉํด ๋ณธ ์ ์ด ์์ด์ ์ ๋ ฌ ์๊ณ ๋ฆฌ์ฆ์ ์ง์  ๊ตฌ์ฑํ์ต๋๋ค.  ๋ํ ๋ฆฌ์คํธ ๋ด๋ถ์ ํฌํจ๋ ๋์๋๋ฆฌ์ ๋ํด ํน์  value๋ฅผ ์ด์ฉํด ์ ๋ ฌํ๋ ๋ฐฉ๋ฒ์ ์์ง ์ฐพ์ง ๋ชปํ์ต๋๋ค. ๋ง์ฝ ์ฐพ๊ฒ๋๋ค๋ฉด ์๋์ ์ถ๊ฐํ๊ฒ ์ต๋๋ค.
> * ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ
>   * ๋ฆฌ์คํธ์ ํฌํจ๋ ๋์๋๋ฆฌ ์์๋ค์ ๋์๋๋ฆฌ ๋ด๋ถ์ ํน์  value๋ฅผ ์ด์ฉํด ์ ๋ ฌํ๋ ๊ฒ์๋๋ค. ์ผ๋จ ์ธ๋ฑ์ค๋ฅผ ์ด์ฉํด ์ฐธ์กฐํด ์ ๋ ฌ์ ํ  ์๋ ์์์ผ๋ ํ์ด์ฌ์ ๊ธฐ๋ฅ์ ์ธ ๋ฉด๋ค์ ์ด์ฉํด ์ ๋ ฌํ๋ ๋ฐฉ๋ฒ์ ์ถ๊ฐ๋ก ์ฐพ์๋ด์ผ๊ฒ ์ต๋๋ค.

### ๐ D. ํน์  ์ํ ์ถ์ฒ ์ํ ์กฐํ

* ์๊ตฌ ์ฌํญ : ์ ๊ณต๋ ์ํ ์ ๋ชฉ์ ๊ธฐ์ค์ผ๋ก ์ถ์ฒ์ํ ๋ชฉ๋ก์ ์ถ๋ ฅํฉ๋๋ค.

> * ์์ฒญ
>
>   1. requests๋ฅผ ์ด์ฉํ์ฌ ์ํ ๊ฒ์(Search Movies) ์์ฒญ์ ๋ณด๋๋๋ค.
>   2. ์๋ต ๋ฐ์ ๊ฒฐ๊ณผ๋ฅผ ๋ฐํ์ผ๋ก id๋ฅผ ์ฐพ์ ์ถ์ฒ์ํ ๋ชฉ๋ก ์กฐํ(Get Recommendations) URL์ ์์ฑํฉ๋๋ค.
>   2. requests๋ฅผ ์ด์ฉํ์ฌ URL์ ์์ฒญ์ ๋ณด๋๋๋ค.
>
> * ๊ฒฐ๊ณผ : 
>   1. TMDB์์ ์ถ์ฒ๋ฐ์ ์ํ ๋ฆฌ์คํธ์์ ์ ๋ชฉ์ ๋ฆฌ์คํธ์ ์ ์ฅํฉ๋๋ค.
>   1. ์ ์ฅ๋ ๋ฆฌ์คํธ๋ฅผ ๋ฐํํ๋ ํจ์ recommendation์ ์์ฑํฉ๋๋ค.
>   1. ์ฌ๋ฐ๋ฅด์ง ์์ ์ํ ์ ๋ชฉ์ผ๋ก id๊ฐ ์๋ ๊ฒฝ์ฐ None์ ๋ฐํํฉ๋๋ค.
>   1. id๊ฐ์ ์์ง๋ง ์ถ์ฒ ์ํ๊ฐ ์๋ ๊ฒฝ์ฐ ๋น ๋ฆฌ์คํธ๋ฅผ ๋ฐํํฉ๋๋ค.

* ๋ฌธ์  ์ ๊ทผ ๋ฐฉ๋ฒ ๋ฐ ์ฝ๋ ์ค๋ช

```python
import requests
from pprint import pprint


def recommendation(title):
    pass 
    # ์ฌ๊ธฐ์ ์ฝ๋๋ฅผ ์์ฑํฉ๋๋ค.
    
    # ๊ธฐ๋ณธ์ด ๋๋ URL์๋๋ค.
    BASE_URL = 'https://api.themoviedb.org/3'
    # ๊ธฐ๋ฅ์ ์ํ path์๋๋ค.
    path = '/search/movie'
    # ํ์ํ ํ๋ผ๋ฏธํฐ๋ค์๋๋ค.
    params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko',
        'region' : 'KR',
        'query' : title
    }

    #์์ฒญ์ ๋ฐ๋ฅธ ์๋ต์ ๋ฐ์ต๋๋ค.
    response = requests.get(BASE_URL + path, params = params)
    # print(response) # 200!
    # pprint(response.json()) # ์ด์ ๊ณผ ๋์ผํ ํํ
    data = response.json().get('results')
    
    movie_id = None # id์ ๊ธฐ๋ณธ๊ฐ์ None์ผ๋ก ํฉ๋๋ค.
    for movie in data: # ๊ฐ ์ํ์ ๋ํด
        if movie.get('title') == title: # ํ์ํ๊ณ ์ ํ๋ ์ํ์ ์ ๋ชฉ์ด ๊ฐ๋ค๋ฉด
            movie_id = movie.get('id') # ์ํ์ id๋ฅผ ์ ์ฅํฉ๋๋ค.
    	# ๊ฒ์ํ๋ ์ํ์ ์ ๋ชฉ๊ณผ ์ผ์นํ๋ ์ํ๊ฐ ์๋ค๋ฉด
        # ์ฌ๋ฐ๋ฅด์ง ์์ ์ ๋ชฉ์ด๋ผ ๊ฐ์ฃผํ๊ณ  return None ํ์ ์ ์์ ๊ฒ ๊ฐ์ต๋๋ค.
        
    if movie_id == None: # ์ํ๋ช์ด ๊ฒ์๋์ง ์๋๋ค๋ฉด id๊ฐ ๋ณํํ์ง ์์ต๋๋ค.
        return None # None์ ๋ฐํํ๊ณ  ์ข๋ฃํฉ๋๋ค.
    
    # ์ ์ฅ๋ id๋ฅผ ์ด์ฉํด ์ถ์ฒ ์ํ๋ฅผ ๊ฒ์ํฉ๋๋ค.
    # ์ถ์ฒ ๊ธฐ๋ฅ์ ์ํ ๊ฒฝ๋ก์๋๋ค.
    re_path = f'/movie/{movie_id}/recommendations'
    # ์ถ์ฒ ๊ธฐ๋ฅ์ ํ์ํ ํ๋ผ๋ฏธํฐ๋ค์๋๋ค.
    re_params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko'
    }
    # ์ถ์ฒ URL์ ์ด์ฉํ ์์ฒญ์ ์๋ต์ ๋ฐ์ต๋๋ค.
    re_response = requests.get(BASE_URL + re_path, params = re_params)
    # print(re_response) # 200!
    re_data = re_response.json().get('results')
    
    re_titles = [] # ์ถ์ฒ ๋ชฉ๋ก์ ์ ๋ชฉ์ ์ ์ฅํ  ๋ฆฌ์คํธ์๋๋ค.
    for movie in re_data: # ์ถ์ฒ ์ํ๋ค์ ๋ํด
        re_titles.append(movie.get('title')) # ๊ฐ ์ํ์ ์ ๋ชฉ์ ๋ชฉ๋ก์ ์ถ๊ฐํฉ๋๋ค.

    return re_titles
```

* ๋ฌธ์ ํ๊ธฐ

>* ์ด ๋ฌธ์ ์์ ์ด๋ ค์ ๋์ 
>   * ์ฌ๋ฐ๋ฅด์ง ์์ ์ํ ์ ๋ชฉ์ ๋ํด id๊ฐ ์์ผ๋ฉด None์ ๋ฐํํ๋ ๋ฐฉ์์ ์ ํ๋๋ฐ ์ฝ๊ฐ ์ด๋ ค์์ด ์์์ต๋๋ค. ์ด๊ธฐ์๋ ๊ฒ์๋์ง ์๋ ์ด๋ฆ์ ๋ํด ๋ฌธ์ ๊ฐ ๋ฐ์ํ๋ฉด ํด๋น ๋ถ๋ถ์ None๋ฐํ์ ๋ผ์๋ฃ์์ง ๊ณ ๋ คํ๊ณ  ์์์ต๋๋ค. ๊ทธ๋ฌ๋ ๋ณ๋์ ๋ฌธ์  ์์ด ์ฝ๋๊ฐ ๋์ด๊ฐ ๋ค์ชฝ์์ ๋ฌธ์ ๊ฐ ๋ฐ์ํ๋ ๊ฒ์ ๋ณด๊ณ  ๋ณ๊ฒฝ๋์ง ์๋๋ค๋ฉด None์ ๋ฐํํ๋ ํํ๋ก ์ฝ๋๋ฅผ ๊ตฌ์ฑํ์ต๋๋ค.
>   * README๋ฅผ ์์ฑํ๋ฉด์ ๋ค์ ๋์๋ณด๋ ์ฌ๋ฌ ๊ฒ์ ๊ฒฐ๊ณผ์ ๋ํด ์ํ์ ์ด๋ฆ์ ๊ฒ์ฆํ๋ if๋ฌธ์ else์ ๊ฒฝ์ฐ๋ก return None์ ์คํํ๋ ๊ฒ์ด ๋ถํ์ํ ๊ณผ์ ์ ์ค์ด๊ณ  ๋ ๋น ๋ฅด๊ฒ ์คํํ ์ ์๋ ๋ฐฉ๋ฒ์ด๋ผ๊ณ  ์๊ฐ๋ฉ๋๋ค.
> * ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ
>   * ์๋ต์ผ๋ก ๋ฐ์ ์๋ฃ๋ฅผ ์ด์ฉํด ํน์  ์์๋ฅผ ๋ฝ์๋ด๊ณ , ์ด๋ฅผ ์ด์ฉํ์ฌ ๋ค์ ์ฌ์ดํธ์ ์ถ๊ฐ ์์ฒญ์ ํ  ์ ์๋ค๋ ๊ฒ์๋๋ค. ์ํ๋ ์ ๋ณด๋ฅผ ์ถ์ถํด๋ด๊ณ  ๋์ผํ ๊ณผ์ ์ ๋ค์ ํ ๋ฒ ๊ฑฐ์น๋ฉด ๋๋ ๋ด์ฉ์ด์ง๋ง ์ฒ์ ๋ฌธ์ ๋ฅผ ์ฝ๊ณ  ๋ฐ๋ก ๋ ์ฌ๋ฆฌ์ง ๋ชปํ๋ฉด ์๊ตฌ์ฌํญ ์ดํดํด ์๊ฐ์ด ๊ฝค ๊ฑธ๋ฆฌ๋ ๋ฌธ์ ์์ต๋๋ค.

### ๐ E. ๋ฐฐ์ฐ, ๊ฐ๋ ๋ฆฌ์คํธ ์ถ๋ ฅ

* ์๊ตฌ ์ฌํญ :  ์ํ์ ์ถ์ฐํ ๋ฐฐ์ฐ๋ค๊ณผ ๊ฐ๋์ ์ ๋ณด๊ฐ ์ ์ฅ๋ ๋์๋๋ฆฌ๋ฅผ ์ถ๋ ฅํฉ๋๋ค.

> * ๋ฐ์ดํฐ
>
>   1. requests๋ฅผ ์ด์ฉํ์ฌ ์ํ ๊ฒ์(Search Movies) ์์ฒญ์ ๋ณด๋๋๋ค.
>   5. ์๋ต ๋ฐ์ ๊ฒฐ๊ณผ๋ฅผ ๋ฐํ์ผ๋ก id๋ฅผ ์ฐพ์ ํฌ๋ ๋ง ์กฐํ(Get Credits) URL์ ์์ฑํฉ๋๋ค.
>   5. requests๋ฅผ ์ด์ฉํ์ฌ URL์ ์์ฒญ์ ๋ณด๋๋๋ค.
>
> * ๊ฒฐ๊ณผ : 
>   1. cast_id ๊ฐ์ด 10๋ณด๋ค ์์ ๋ฐฐ์ฐ์ ์ด๋ฆ์ ๋ฆฌ์คํธ์ ์ ์ฅํฉ๋๋ค.
>   1. department ๊ฐ์ด Directing์ธ ๊ฐ๋์ ์ด๋ฆ์ ๋ฆฌ์คํธ์ ์ ์ฅํฉ๋๋ค.
>   1. ๋ฐํ๋๋ ๋์๋๋ฆฌ๋ cast, crew ๋๊ฐ์ key๋ฅผ ๊ฐ์ง๊ณ  ๊ฐ๊ฐ ๋ฐฐ์ฐ๋ฆฌ์คํธ์ ๊ฐ๋๋ฆฌ์คํธ๋ฅผ value๋ก ๊ฐ์ต๋๋ค.
>   1. ์์ฑ๋ ๋์๋๋ฆฌ๋ฅผ ๋ฐํํ๋ ํจ์ credits์ ์์ฑํฉ๋๋ค.

* ๋ฌธ์  ์ ๊ทผ ๋ฐฉ๋ฒ ๋ฐ ์ฝ๋ ์ค๋ช

```python
import requests
from pprint import pprint


def credits(title):
    pass 
    # ์ฌ๊ธฐ์ ์ฝ๋๋ฅผ ์์ฑํฉ๋๋ค.  
    # ๊ธฐ๋ณธ์ด ๋๋ URL์๋๋ค.
    BASE_URL = 'https://api.themoviedb.org/3'
    # ๊ธฐ๋ฅ์ ์ํ path์๋๋ค.
    path = '/search/movie'
    # ํ์ํ ํ๋ผ๋ฏธํฐ๋ค์๋๋ค.
    params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko',
        'region' : 'KR',
        'query' : title
    }

    #์์ฒญ์ ๋ฐ๋ฅธ ์๋ต์ ๋ฐ์ต๋๋ค.
    response = requests.get(BASE_URL + path, params = params)
    # print(response) # 200!
    # pprint(response.json()) # ์ด์ ๊ณผ ๋์ผํ ํํ
    data = response.json().get('results')
    
    movie_id = None # id์ ๊ธฐ๋ณธ๊ฐ์ None์ผ๋ก ํฉ๋๋ค.
    for movie in data: # ๊ฐ ์ํ์ ๋ํด
        if movie.get('title') == title: # ํ์ํ๊ณ ์ ํ๋ ์ํ์ ์ ๋ชฉ์ด ๊ฐ๋ค๋ฉด
            movie_id = movie.get('id') # ์ํ์ id๋ฅผ ์ ์ฅํฉ๋๋ค.
    
    if movie_id == None: # ์ํ๋ช์ด ๊ฒ์๋์ง ์๋๋ค๋ฉด id๊ฐ ๋ณํํ์ง ์์ต๋๋ค.
        return None # None์ ๋ฐํํ๊ณ  ์ข๋ฃํฉ๋๋ค.

    # ์ ์ฅ๋ id๋ฅผ ์ด์ฉํด ๊ฐ๋ ๋ฐ ๋ฐฐ์ฐ ์ ๋ณด๋ฅผ ๊ฒ์ํฉ๋๋ค.
    # credit ๊ธฐ๋ฅ์ ์ํ ๊ฒฝ๋ก์๋๋ค.
    cred_path = f'/movie/{movie_id}/credits'
    # credit ๊ธฐ๋ฅ์ ์ํ ํ๋ผ๋ฏธํฐ๋ค์๋๋ค.
    cred_params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko'
    }
    # credit URL์ ์ด์ฉํ ์์ฒญ์ ์๋ต์ ๋ฐ์ต๋๋ค.
    cred_response = requests.get(BASE_URL + cred_path, params = cred_params)
    # print(cred_response) # 200!
    cred_data = cred_response.json() # dict
    # print(cred_data.keys()) # dict_keys(['id', 'cast', 'crew'])
    
    all_cast = cred_data.get('cast') # ํ์ list, ์์๋ dict
    cast = [] # ๋ฐฐ์ฐ ์ ๋ณด๋ฅผ ์ ์ฅํ๊ธฐ ์ํ ๋ฆฌ์คํธ์๋๋ค.
    for act in all_cast: # ๋ชจ๋  ๋ฐฐ์ฐ๋ค์ ๋ํด
        if act.get('cast_id') < 10 : # cast_id๊ฐ 10๋ณด๋ค ์์ ๋ฐฐ์ฐ๋ค์
            cast.append(act.get('name')) # ๋ชฉ๋ก์ ์ถ๊ฐํฉ๋๋ค.
    
    all_crew = cred_data.get('crew')
    crew = [] # ๊ฐ๋ ์ ๋ณด๋ฅผ ์ ์ฅํ๊ธฐ ์ํ ๋ฆฌ์คํธ์๋๋ค.
    for staff in all_crew: # ๋ชจ๋  ์คํํ๋ค์ ๋ํด
        if staff.get('department') == 'Directing': # department = Directing์ด๋ผ๋ฉด
            crew.append(staff.get('name')) # ๋ชฉ๋ก์ ์ถ๊ฐํฉ๋๋ค.

    cast_n_crew = {'cast' : cast, 'crew' : crew} # ๋ฐฐ์ฐ์ ๊ฐ๋์ ์ ๋ณด๋ฅผ ๋ด์ ๋์๋๋ฆฌ์๋๋ค.
    
    return cast_n_crew
```

* ๋ฌธ์ ํ๊ธฐ

> * ์ด ๋ฌธ์ ์์ ์ด๋ ค์ ๋์ 
>   * ์์  ๋ด์ฉ๋ค์ ๋ํด ์ ์ดํดํ๊ณ  ๋์ด์๋ค๋ฉด ํฌ๊ฒ ์ด๋ ค์์ ์์์ต๋๋ค. ๋ค๋ง, ์์  ์ํ๋ค์ ์ ๋ณด๊ฐ ๋ฆฌ์คํธ์ ํฌํจ๋ ๋์๋๋ฆฌ ํํ์ ๊ตฌ์กฐ์๋ค๋ฉด credit๊ณผ ๊ด๋ จํ ์ ๋ณด๋ ์์ฒด๋ก ๋์๋๋ฆฌ ํํ์ด๊ธฐ ๋๋ฌธ์ ์ด๋ฅผ ํ์ธํ์ง ์๊ณ  ์ด์ ์ ๋ฐฉ๋ฒ์ ๊ทธ๋๋ก ์๋ํ๋ค๋ฉด ์ค๋ฅ๋ฅผ ํ๋ฒ ๋ณด๊ณ  ๋ค์ ํ์์ ํ์ธํ๋ ๊ณผ์ ์ผ๋ก ๋์๊ฐ์ผ ํ์ต๋๋ค.
> * ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ
>   * problem_d์ ๋ง์ฐฌ๊ฐ์ง๋ก ์๋ต๋ฐ์ ์ ๋ณด์์ ์ํ๋ ์์๋ฅผ ์ถ์ถํด ์ด๋ฅผ ์ด์ฉํด ๋ค์ ํ์ด์ง์ ์์ฒญ์ ํ๋ ๊ฒ์๋๋ค. ์ดํ์ ์ ๋ณด๋ ์์ ๋ง์ด ์ค์ตํ ๋ฐฉ๋ฒ์ ์ด์ฉํด ์ฝ๊ฒ ์๋ฃ๋ฅผ ์ถ์ถํ๊ณ  ์ ์ฅํ  ์ ์์์ต๋๋ค.



# ๐กํ๊ธฐ

* URL์ ๊ตฌ์ฑํ๋ ๋ฐฉ์์ด ์๊ฐ๋ณด๋ค ๋งค์ฐ ๊ฐ๋จํ๋ค๋ ๊ฒ์ ์๊ฒ ๋์์ต๋๋ค. ๊ฐ ์ฌ์ดํธ๋ณ ๋ฐ์๋ค์ด๋ ๋งค๊ฐ๋ณ์์ ์ฐจ์ด๊ฐ ์์ด ํญ๋ชฉ ์ฐจ์ด๋ ์์ผ๋ ์ ์ฒด์ ์ธ ์์ฑ ๋ฐฉ๋ฒ์ ๋์ผํ๊ธฐ ๋๋ฌธ์ ๊ฐ๊ฐ์ ํญ๋ชฉ์ด ๋ฌด์์ ์๋ฏธํ๋ ๊ฒ์ธ์ง ์์๋ธ๋ค๋ฉด URL์ ์ค์ ์ ์์๋ผ ์ ์์ ๊ฒ์๋๋ค. ๋ํ ์ผ๋ฐ ๊ฒ์์ฐฝ์ ์ฃผ์๋ฅผ ๋ดค์ ๋ ๋ณด์์ ์ด์ ๋ก ๊ฐ ์ฌ์ดํธ๋ง๋ค ๋ค๋ฅธ ๋ฐฉ์์ ์ด์ฉํด ๋งค๊ฐ๋ณ์์ ๋ด์ฉ์ ์ค๋ ์ฌ์ฉํ api key์ ์ ์ฌํ ํํ๋ก ์ํธํ ํ ๊ฒ์ ๋ณผ ์ ์์์ต๋๋ค.
* ํด๋ผ์ด์ธํธ๊ฐ ์๋ฒ์ ์ ๋ณด๋ฅผ ์์ฒญํ  ๋์๋ URL์ ์ด์ฉํ๊ณ  ์๋ฒ๊ฐ ์ ๋ณด๋ฅผ ์ ๊ณตํ  ๋์๋ HTML, XML, JSON์ ์ด์ฉํ๋ค๋ ๊ฒ์ ์๊ฒ ๋์๊ณ  ์ด๋ค ์ฌ์ด์ ํต์  ๊ท์ฝ์ด HTTP์ธ ๊ฒ์ ์๊ฒ ๋์์ต๋๋ค.
* ์ค์  ์น์ฌ์ดํธ์ ์ ๋ณด๋ฅผ ๊ฐ์ ธ์ค๊ณ  ํ์ฉํด ๋ณด๋ฉด์ ์๊ณ ๋ฆฌ์ฆ ๋ฌธ์  ํ์ด์์๋ ์์ง ๋ง์ด ์ฌ์ฉํด ๋ณด์ง ์์๋ ๋์๋๋ฆฌ๊ฐ ์ค์  ์๋ฌด์์๋ ๋ง์ ๊ณณ์ ์ฌ์ฉ๋๊ณ  ์๋ค๋ ๊ฒ์ ์๊ฒ ๋์์ต๋๋ค. ์ด๋ฅผ ์ํด ๋์๋๋ฆฌ๋ฅผ ํ์ฉํ๊ธฐ ์ํ ํจ์๋ ๋ฉ์๋ ๋ฑ์ ๋ฅ์ํ๊ฒ ๋ค๋ฃฐ ์ ์๋๋ก ์ฐ์ตํ  ํ์๊ฐ ์์ ๊ฒ ๊ฐ์ต๋๋ค.
