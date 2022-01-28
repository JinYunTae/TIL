# 📂PJT 02

## 📚이번 pjt 를 통해 배운 내용

* 실제 이용되는 사이트들의 URL이 어떤 방식으로 구성되어 있는지 알아 볼 수 있었습니다.
* API을 이용해 사이트의 정보를 요청하고 응답을 받아 사이트 내 자료를 직접 활용해 볼 수 있었습니다.



## 📖요구사항

커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 영화 데이터를 수집하는 과정입니다. 아래 기술된 사항은 필수적으로 구현해야 하는 내용입니다. 완성된 기능들은, 향후 커뮤니티 서비스에서 활용할 수 있습니다.

### 📕 A. 인기 영화 조회

* 요구 사항 : 인기 영화의 개수를 출력합니다.

> * 요청
>   1. requests를 이용하여 인기 영화 정보(Get Popular)에 요청을 보냅니다.
> * 결과 : 
>   1. popular를 기준으로 받아온 데이터에서 영화 리스트의 개수를 계산합니다.
>   2. 계산한 정보를 반환하는 함수 popular_count를 완성합니다.

* 문제 접근 방법 및 코드 설명

```python
import requests


def popular_count():
	pass
 	# 여기에 코드를 작성합니다.
    
    # 기본이 되는 URL입니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    # 기능을 위한 path입니다.
    path = '/movie/popular'
    # 필요한 파라미터들입니다.
    params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko',
        'region' : 'KR'
    }

    # 요청에 따른 응답을 받습니다.
    response = requests.get(BASE_URL + path, params = params)
    # print(response) # 200!
    data = response.json() # dict
    # dict_keys(['page', 'results', 'total_pages', 'total_results'])
    pm_list = data.get('results')
    # print(data.get('results')) # results 항목에 영화 정보가 다 있습니다.
    # print(type(data.get('results'))) # results의 항목은 딕셔너리를 요소로 갖는 리스트입니다.
    num_of_popular = len(pm_list) # 인기있는 영화의 수
    # print(num_of_popular) # => 20
    
    return num_of_popular
```

* 문제후기

>* 이 문제에서 어려웠던점
>   * 요청에 대한 응답을 받아온 뒤 데이터를 처리할 때 어떤 자료형이 넘어왔는지 매 절차마다 확인이 필요했습니다. 또한 각 자료형에서 어떤 항목의 요소들을 이용해야하는지 알아보기 위해 각 과정마다 출력해 확인해야 했습니다. 
>* 내가 생각하는 이 문제의 포인트
>   * 응답받은 정보가 어떤 형태인지, 어떠한 정보를 담고 있는지 각 단계별로 확인해 필요한 값들을 찾아 쓸 수 있도록 하는 것입니다. 다른 작업을 하더라도 이러한 과정을 거치게 되면 데이터를 잘 못 사용해 문제가 발생하는 것을 방지할 수 있습니다.

-----

### 📗 B. 특정 조건에 맞는 인기 영화 조회 I

* 요구 사항 : popular를 기준으로 가져온 영화 목록 중 평점이 8 이상인 영화들의 목록을 출력합니다.

> * 요청
>   1. requests를 이용하여 인기 영화 정보(Get Popular)에 요청을 보냅니다.
> * 결과 : 
>   1. 받아온 데이터에서 vote_average를 기준으로 점수가 8 이상인 영화들의 목록을 리스트로 반환하는 함수 vote_average_movies를 완성합니다.

* 문제 접근 방법 및 코드 설명

```python
import requests
from pprint import pprint


def vote_average_movies():
	pass
 	# 여기에 코드를 작성합니다.
    
    # 기본이 되는 URL입니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    # 기능을 위한 path입니다.
    path = '/movie/popular'
    # 필요한 파라미터입니다.
    params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko',
        'region' : 'KR'
    }

    #요청에 따른 응답을 받습니다.
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
    # vote_average의 value를 이용
    
    high_score_movie = []
    for movie in p_m_list:
        if movie.get('vote_average') >= 8: # 영화의 평점이 8점 이상이면
            high_score_movie.append(movie) # 목록에 추가합니다.
    
    return high_score_movie
```

* 문제후기

> * 이 문제에서 어려웠던점
>   * 앞서 구현한 조회에서 더 나아가 리스트의 요소로 포함된 딕셔너리를 이용해 정보를 찾아오는 과정이었습니다. 지난 프로젝트에 이어 동일한 방식을 이용하면 되었기에 크게 어려움은 없었습니다.
>   * 처음 코드를 짜던 도중에는 첫 딕셔너리의 키들만 참고로 확인한 것에 대해 다른 딕셔너리의 키 구성이 다를 경우 어떻게 하나 고민했으나 .get()을 쓰면서 만약 원하는 키가 없더라도 문제가 없다는 것을 다시 떠올렸습니다.
> * 내가 생각하는 이 문제의 포인트
>   * 리스트 내부에 요소로 포함된 많은 딕셔너리에 접근해 key로 value를 참조할 수 있는가를 다시 복습하는 문제였습니다.
>   * 코드를 다 작성하고 돌아보면서 8 이상인 요구조건을 8 초과로 잘못 적용했던 것을 확인하고 수정했습니다.  경계조건에 대한 내용에 실수를 하지 않도록 주의해야겠습니다.

### 📘 C.  특정 조건에 맞는 인기 영화 조회 II

* 요구 사항 : 영화목록을 평점순으로 출력하는 함수를 완성합니다. 해당 기능은 향후 커뮤니티 서비스에서 기본으로 제공되는 영화 정보로 사용됩니다.

> * 요청
>   1. requests를 이용하여 인기 영화 정보(Get Popular)에 요청을 보냅니다.
> * 결과 : 
>   1. 받아온 데이터 중 평점이 높은 영화 다섯개의 정보를 리스트로 반환하는 함수 ranking을 완성합니다.

* 문제 접근 방법 및 코드 설명

```python
import requests
from pprint import pprint


def ranking():
    pass
 	# 여기에 코드를 작성합니다.
    
    # 기본이 되는 URL입니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    # 기능을 위한 path입니다.
    path = '/movie/popular'
    # 필요한 파라미터들입니다.
    params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko',
        'region' : 'KR'
    }

    #요청에 따른 응답을 받습니다.
    response = requests.get(BASE_URL + path, params = params)
    # print(response) # 200!
    p_m_list = response.json().get('results') # results 항목만 받습니다.

    for i in range(1, len(p_m_list)): # 내부 딕셔너리들을 평점에 따라 정렬합니다.
        for j in range(len(p_m_list)-i):
            # 평점이 높은 순으로 정렬합니다.
            if p_m_list[j]['vote_average'] < p_m_list[j+1]['vote_average']: 
                p_m_list[j], p_m_list[j+1] = p_m_list[j+1], p_m_list[j]

    return p_m_list[:5] # 평점이 높은 5개의 영화 정보를 반환합니다.
```

```python
# sorted()를 이용한 경우

```

* 문제후기

> * 이 문제에서 어려웠던점
>   * 딕셔너리에 value를 기준으로 sorted()를 적용해 본 적이 없어서 정렬 알고리즘을 직접 구성했습니다.  또한 리스트 내부에 포함된 딕셔너리에 대해 특정 value를 이용해 정렬하는 방법을 아직 찾지 못했습니다. 만약 찾게된다면 아래에 추가하겠습니다.
> * 내가 생각하는 이 문제의 포인트
>   * 리스트에 포함된 딕셔너리 요소들을 딕셔너리 내부의 특정 value를 이용해 정렬하는 것입니다. 일단 인덱스를 이용해 참조해 정렬을 할 수는 있었으나 파이썬의 기능적인 면들을 이용해 정렬하는 방법을 추가로 찾아봐야겠습니다.

### 📙 D. 특정 영화 추천 영화 조회

* 요구 사항 : 제공된 영화 제목을 기준으로 추천영화 목록을 출력합니다.

> * 요청
>
>   1. requests를 이용하여 영화 검색(Search Movies) 요청을 보냅니다.
>   2. 응답 받은 결과를 바탕으로 id를 찾아 추천영화 목록 조회(Get Recommendations) URL을 생성합니다.
>   2. requests를 이용하여 URL에 요청을 보냅니다.
>
> * 결과 : 
>   1. TMDB에서 추천받은 영화 리스트에서 제목을 리스트에 저장합니다.
>   1. 저장된 리스트를 반환하는 함수 recommendation을 완성합니다.
>   1. 올바르지 않은 영화 제목으로 id가 없는 경우 None을 반환합니다.
>   1. id값은 있지만 추천 영화가 없는 경우 빈 리스트를 반환합니다.

* 문제 접근 방법 및 코드 설명

```python
import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.
    
    # 기본이 되는 URL입니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    # 기능을 위한 path입니다.
    path = '/search/movie'
    # 필요한 파라미터들입니다.
    params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko',
        'region' : 'KR',
        'query' : title
    }

    #요청에 따른 응답을 받습니다.
    response = requests.get(BASE_URL + path, params = params)
    # print(response) # 200!
    # pprint(response.json()) # 이전과 동일한 형태
    data = response.json().get('results')
    
    movie_id = None # id의 기본값을 None으로 합니다.
    for movie in data: # 각 영화에 대해
        if movie.get('title') == title: # 탐색하고자 하는 영화와 제목이 같다면
            movie_id = movie.get('id') # 영화의 id를 저장합니다.
    	# 검색하는 영화의 제목과 일치하는 영화가 없다면
        # 올바르지 않은 제목이라 간주하고 return None 했을 수 있을 것 같습니다.
        
    if movie_id == None: # 영화명이 검색되지 않는다면 id가 변화하지 않습니다.
        return None # None을 반환하고 종료합니다.
    
    # 저장된 id를 이용해 추천 영화를 검색합니다.
    # 추천 기능을 위한 경로입니다.
    re_path = f'/movie/{movie_id}/recommendations'
    # 추천 기능에 필요한 파라미터들입니다.
    re_params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko'
    }
    # 추천 URL을 이용한 요청의 응답을 받습니다.
    re_response = requests.get(BASE_URL + re_path, params = re_params)
    # print(re_response) # 200!
    re_data = re_response.json().get('results')
    
    re_titles = [] # 추천 목록의 제목을 저장할 리스트입니다.
    for movie in re_data: # 추천 영화들에 대해
        re_titles.append(movie.get('title')) # 각 영화의 제목을 목록에 추가합니다.

    return re_titles
```

* 문제후기

>* 이 문제에서 어려웠던점
>   * 올바르지 않은 영화 제목에 대해 id가 없으면 None을 반환하는 방식을 정하는데 약간 어려움이 있었습니다. 초기에는 검색되지 않는 이름에 대해 문제가 발생하면 해당 부분에 None반환을 끼워넣을지 고려하고 있었습니다. 그러나 별도의 문제 없이 코드가 넘어가 뒤쪽에서 문제가 발생하는 것을 보고 변경되지 않는다면 None을 반환하는 형태로 코드를 구성했습니다.
>   * README를 작성하면서 다시 돌아보니 여러 검색 결과에 대해 영화의 이름을 검증하는 if문에 else의 경우로 return None을 실행하는 것이 불필요한 과정을 줄이고 더 빠르게 실행할수 있는 방법이라고 생각됩니다.
> * 내가 생각하는 이 문제의 포인트
>   * 응답으로 받은 자료를 이용해 특정 요소를 뽑아내고, 이를 이용하여 다시 사이트에 추가 요청을 할 수 있다는 것입니다. 원하는 정보를 추출해내고 동일한 과정을 다시 한 번 거치면 되는 내용이지만 처음 문제를 읽고 바로 떠올리지 못하면 요구사항 이해해 시간이 꽤 걸리는 문제였습니다.

### 📒 E. 배우, 감독 리스트 출력

* 요구 사항 :  영화에 출연한 배우들과 감독의 정보가 저장된 딕셔너리를 출력합니다.

> * 데이터
>
>   1. requests를 이용하여 영화 검색(Search Movies) 요청을 보냅니다.
>   5. 응답 받은 결과를 바탕으로 id를 찾아 크레딧 조회(Get Credits) URL을 생성합니다.
>   5. requests를 이용하여 URL에 요청을 보냅니다.
>
> * 결과 : 
>   1. cast_id 값이 10보다 작은 배우의 이름을 리스트에 저장합니다.
>   1. department 값이 Directing인 감독의 이름을 리스트에 저장합니다.
>   1. 반환되는 딕셔너리는 cast, crew 두개의 key를 가지고 각각 배우리스트와 감독리스트를 value로 갖습니다.
>   1. 완성된 딕셔너리를 반환하는 함수 credits을 완성합니다.

* 문제 접근 방법 및 코드 설명

```python
import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    # 기본이 되는 URL입니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    # 기능을 위한 path입니다.
    path = '/search/movie'
    # 필요한 파라미터들입니다.
    params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko',
        'region' : 'KR',
        'query' : title
    }

    #요청에 따른 응답을 받습니다.
    response = requests.get(BASE_URL + path, params = params)
    # print(response) # 200!
    # pprint(response.json()) # 이전과 동일한 형태
    data = response.json().get('results')
    
    movie_id = None # id의 기본값을 None으로 합니다.
    for movie in data: # 각 영화에 대해
        if movie.get('title') == title: # 탐색하고자 하는 영화와 제목이 같다면
            movie_id = movie.get('id') # 영화의 id를 저장합니다.
    
    if movie_id == None: # 영화명이 검색되지 않는다면 id가 변화하지 않습니다.
        return None # None을 반환하고 종료합니다.

    # 저장된 id를 이용해 감독 및 배우 정보를 검색합니다.
    # credit 기능을 위한 경로입니다.
    cred_path = f'/movie/{movie_id}/credits'
    # credit 기능을 위한 파라미터들입니다.
    cred_params = {
        'api_key' : '9ea41a22c7a6135e48233cc8b7f5a834',
        'language' : 'ko'
    }
    # credit URL을 이용한 요청의 응답을 받습니다.
    cred_response = requests.get(BASE_URL + cred_path, params = cred_params)
    # print(cred_response) # 200!
    cred_data = cred_response.json() # dict
    # print(cred_data.keys()) # dict_keys(['id', 'cast', 'crew'])
    
    all_cast = cred_data.get('cast') # 타입 list, 요소는 dict
    cast = [] # 배우 정보를 저장하기 위한 리스트입니다.
    for act in all_cast: # 모든 배우들에 대해
        if act.get('cast_id') < 10 : # cast_id가 10보다 작은 배우들을
            cast.append(act.get('name')) # 목록에 추가합니다.
    
    all_crew = cred_data.get('crew')
    crew = [] # 감독 정보를 저장하기 위한 리스트입니다.
    for staff in all_crew: # 모든 스태프들에 대해
        if staff.get('department') == 'Directing': # department = Directing이라면
            crew.append(staff.get('name')) # 목록에 추가합니다.

    cast_n_crew = {'cast' : cast, 'crew' : crew} # 배우와 감독의 정보를 담은 딕셔너리입니다.
    
    return cast_n_crew
```

* 문제후기

> * 이 문제에서 어려웠던점
>   * 앞선 내용들에 대해 잘 이해하고 넘어왔다면 크게 어려움은 없었습니다. 다만, 앞선 영화들의 정보가 리스트에 포함된 딕셔너리 형태의 구조였다면 credit과 관련한 정보는 자체로 딕셔너리 형태이기 때문에 이를 확인하지 않고 이전의 방법을 그대로 시도했다면 오류를 한번 보고 다시 타입을 확인하는 과정으로 돌아가야 했습니다.
> * 내가 생각하는 이 문제의 포인트
>   * problem_d와 마찬가지로 응답받은 정보에서 원하는 요소를 추출해 이를 이용해 다시 페이지에 요청을 하는 것입니다. 이후의 정보는 앞서 많이 실습한 방법을 이용해 쉽게 자료를 추출하고 저장할 수 있었습니다.



# 💡후기

* URL을 구성하는 방식이 생각보다 매우 간단하다는 것을 알게 되었습니다. 각 사이트별 받아들이는 매개변수에 차이가 있어 항목 차이는 있으나 전체적인 작성 방법은 동일하기 때문에 각각의 항목이 무엇을 의미하는 것인지 알아낸다면 URL의 설정을 알아낼 수 있을 것입니다. 또한 일반 검색창의 주소를 봤을 때 보안을 이유로 각 사이트마다 다른 방식을 이용해 매개변수의 내용을 오늘 사용한 api key와 유사한 형태로 암호화 한 것을 볼 수 있었습니다.
* 클라이언트가 서버에 정보를 요청할 때에는 URL을 이용하고 서버가 정보를 제공할 때에는 HTML, XML, JSON을 이용한다는 것을 알게 되었고 이들 사이의 통신 규약이 HTTP인 것을 알게 되었습니다.
* 실제 웹사이트의 정보를 가져오고 활용해 보면서 알고리즘 문제 풀이에서는 아직 많이 사용해 보지 않았던 딕셔너리가 실제 업무에서는 많은 곳에 사용되고 있다는 것을 알게 되었습니다. 이를 위해 딕셔너리를 활용하기 위한 함수나 메소드 등을 능숙하게 다룰 수 있도록 연습할 필요가 있을 것 같습니다.
