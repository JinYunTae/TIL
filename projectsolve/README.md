# 📂PJT 01

## 📚이번 pjt 를 통해 배운 내용

* .get() 메서드에 대해 처음 알게되어 실제 활용까지 바로 경험해 볼 수 있었습니다.
* for 반복문은 iterable한 객체를 이용할 때 객체 내부의 요소를 변수에 할당하는 방식을 이용합니다. 이를 이용해 각 딕셔너리에 순차적으로 접근하는 것을 활용할 수 있었습니다.
* 딕셔너리를 포함하는 리스트에서 각각의 key를 이용해 value를 찾아보는 과정을 심도있게 다뤄볼 수 있었습니다.
* 아래에 미리 작성 된 코드를 참고해 json 파일을 읽어와 변수에 값을 할당해 활용해 볼 수 있었습니다.



## 📕 A. 제공되는 영화 데이터의 주요내용 수집

* 요구 사항 : 주어진 샘플 영화데이터 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성합니다.

  * 데이터
    1. 제공되는 movie.json 파일을 활용합니다.
    2. movie.json은 '쇼생크 탈출' 영화 정보를 가지고 있습니다.

* 결과 : 

  1. 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids키에 해당하는 정보만 가져옵니다.
  2. 가져온 정보를 새로운 dictionary로 반환하는 함수 movie_info를 완성합니다.

  * 문제 접근 방법 및 코드 설명

  ```python
  # 하나의 movie 정보만 넘어온 경우
  def movie_info(movie):    # movie는 딕셔너리이므로 바로 .get()을 이용해 원하는 값을 참조
      movie_id = movie.get('id')
      title = movie.get('title')
      poster_path = movie.get('poster_path')
      vote_average = movie.get('vote_average')
      overview = movie.get('overview')
      genre_ids = movie.get('genre_ids')
  
      # 각 항목들을 딕셔너리로 생성해 반환 (미리 값 받으면서 묶었으면 더 깔끔했을 듯)
      return {'genre_ids': genre_ids,
              'id': movie_id,
              'overview': overview,
              'poster_path': poster_path,
              'title': title,
              'vote_average': vote_average
              }
  ```

  * 이 문제에서 어려웠던점
    * .get()을 처음 써보면서 약간의 적응이 필요했습니다.
  * 내가 생각하는 이 문제의 포인트
    * 문제 내에서 특정 키 항목이 없는 딕셔너리는 없었지만, 단순 인덱스 참조가 아닌 .get()을 이용한 참조를 통해 특정 키가 없는 딕셔너리라도 같이 이용할 수 있다는 것 입니다.

-----

## 📗 B. 제공되는 영화 데이터의 주요내용 수집

* 요구 사항 : A에서 만들었던 데이터 중 genre_ids를 genre_names로 바꿔 반환하는 함수를 완성합니다.

  * 데이터
    1. 제공되는 movie.json, genres.json 파일을 활용합니다.
    2. movie.json은 '쇼생크 탈출' 영화 정보를 가지고 있습니다.
    3. genres.json은 장르의 id, name 정보를 가지고 있습니다.

* 결과 : 

  1. 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids키에 해당하는 정보만 가져옵니다.
  2. genres.json파일을 이용하여 genre_ids를 genre_names로 변환하여 dictionary에 추가합니다.
  3. 완성된 dictionary를 반환하는 함수 movie_info를 완성합니다.

  * 문제 접근 방법 및 코드 설명

  ```python
  def movie_info(movie, genres):
      # 여기에 코드를 작성합니다.  
      movie_id = movie.get('id')
      title = movie.get('title')
      poster_path = movie.get('poster_path')
      vote_average = movie.get('vote_average')
      overview = movie.get('overview')
      genre_ids = movie.get('genre_ids')
      genre_names = []    # 장르 이름을 저장하기 위한 리스트
  
      for i in genres :    # genres의 딕셔너리들을 하나씩 전달 (i보다 genre가 더 좋았을 듯)
          if i.get('id') in genre_ids :    # 전달받은 딕셔너리의 id가 리스트에 있다면
              genre_names += [i.get('name')]    # 장르 이름을 리스트에 저장
      
      return {
              'genre_names': genre_names,
              'id': movie_id,
              'overview': overview,
              'poster_path': poster_path,
              'title': title,
              'vote_average': vote_average
              }
  ```

  * 이 문제에서 어려웠던점
    * genre_ids의 경우 value가 리스트로 구성되어 있는데 이것을 모르고 코드를 작성하다 초반에 에러가 몇 번 발생했습니다. 앞서 print를 이용해 movie를 몇 번 출력하고도 확인을 못했습니다.
    * genres를 이용하면서 딕셔너리가 포함된 리스트를 활용하는 것이 생각보다 자연스럽게 와닿지 않아서 이러한 구조에 적응할 필요가 있음을 느꼈습니다.
  * 내가 생각하는 이 문제의 포인트
    * 딕셔너리가 포함된 리스트를 이용해 값을 참조하고 변경하는 것 입니다.

## 📘 C. 다중 데이터 분석 및 수정

* 요구 사항 : TMDB기준 평점이 높은 20개의 영화데이터 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성합니다. 

  * 데이터
    1. 제공되는 movies.json, genres.json 파일을 활용합니다.
    2. movies.json은 영화 전체 정보를 가지고 있습니다.
    3. genres.json은 장르의 id, name 정보를 가지고 있습니다.

* 결과 : 

  1. 이전 단계의 함수 구조를 재사용합니다.
  2. 영화 전체 정보를 수정하여 반환하는 함수 movie_info를 완성합니다.

  * 문제 접근 방법 및 코드 설명

  ```python
  def movie_info(movies, genres):
      # 여기에 코드를 작성합니다.
      dict_list = []  
      for movie in movies :    # moveis의 여러 딕셔너리를 movie로 각각 받아 기존 코드로 구동가능
          movie_id = movie.get('id')
          title = movie.get('title')
          poster_path = movie.get('poster_path')
          vote_average = movie.get('vote_average')
          overview = movie.get('overview')
          genre_ids = movie.get('genre_ids')
          genre_names = []
          
          for i in genres :
              if i.get('id') in genre_ids :
                  genre_names += [i.get('name')]
          
          dict_list += [
              {
              'genre_names': genre_names,
              'id': movie_id,
              'overview': overview,
              'poster_path': poster_path,
              'title': title,
              'vote_average': vote_average
              }
          ]
      return dict_list
  ```

  * 이 문제에서 어려웠던점
    * movies의 구조를 확인하기 위해 출력해보면서 마찬가지로 리스트 안에 딕셔너리를 넣는 방식을 떠올렸습니다. 만약 이것을 확인하지 못했다면 genres를 보는 것으로라도 떠올릴 수 있었을지 의문입니다.
  * 내가 생각하는 이 문제의 포인트
    * 앞선 문제들의 구조를 가져와 반복시키면서 각각의 결과들을 저장하는 것 입니다. 직접 리스트 내부에 딕셔너리를 저장해 실습에서 주어진 자료와 동일한 구조를 만들어 볼 수 있었습니다.

## 📙 D. 알고리즘을 통한 데이터 출력

* 요구 사항 : 세부적인 영화 정보 중 수익 정보(revenue)를 이용하여 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성합니다. 

  * 데이터

    1. movies.json과 movies폴더 내부의 파일들을 사용합니다.

    2. movies.json은 영화 전체 데이터를 가지고 있습니다.

    3. movies 폴더 내부의 파일들은 각 영화의 상세정보를 가지고 있습니다.

    4. movies 폴더의 파일의 이름은 영화의 id로 구성되어 있습니다.

    5. 수익정보는 상세정보 파일을 통해 확인할 수 있습니다.

       힌트 : 반복문을 통해 상세 정보 파일을 오픈해야 합니다.

* 결과 : 

  1. 수익이 가장 높은 영화의 제목을 출력하는 함수 max_revenue를 완성합니다.

  * 문제 접근 방법 및 코드 설명

  ```python
  def max_revenue(movies):
      # 여기에 코드를 작성합니다.  
      # case1. 최대값을 찾고 이를 이용해 인덱스를 찾아 제목 출력
  	title = []
      revenue = []
      for movie in movies :
          movie_id = str(movie.get('id'))
          # id를 이용해 상세정보 파일 열기
          more_info_file = open(f'data/movies/{movie_id}.json', encoding='UTF8')
          # 상세정보 파일을 로드
          movie_more_info = json.load(more_info_file)
          title += [movie_more_info.get('title')]    # 제목들을 리스트에 저장
          revenue += [movie_more_info.get('revenue')]    # 수익을 리스트에 저장
      print(revenue)    # 확인용 출력문 안지웠음!!
      print(title)      # 확인용 출력문 안지웠음!! 주의할 것!!
      maximum = revenue[0]
      for rev in revenue :    # 최대 수익을 저장
          if maximum < rev :
              maximum = rev
  
      cnt = 0
      for rev in revenue :    # 최대 수익을 이용해 인덱스 계산
          if rev != maximum :
              cnt += 1
          else :
              break
         
      return title[cnt]    # 계산된 인덱스의 제목을 반환
  ```
  
  ```python
  def max_revenue(movies):
      # case2. 이전 최대값을 저장해 비교를 통해 필요시 갱신
      max_revenue = 0    # 최대 수익 저장을 위한 변수
      for movie in movies :
          movie_id = str(movie.get('id'))
          more_info_file = open(f'data/movies/{movie_id}.json', encoding='UTF8')
          movie_more_info = json.load(more_info_file)
          revenue = movie_more_info.get('revenue')
          
          if max_revenue < revenue :    # 현재 불러온 수익이 저장된 최대 수익보다 크다면
              title = movie.get('title')    # 해당 영화의 제목을 저장
              max_revenue = revenue    # 현재 불러온 수익을 최대 수익에 저장
  
      return title    # 저장된 영화 제목을 반환
  ```
  
  * 이 문제에서 어려웠던점
    * 세부사항이 적힌 파일을 어떻게 열어야할지 고민이 가장 길었습니다. 아래에 이미 완성된 코드가 있었음에도 불구하고 다른 파일을 어떻게 열 수 있는지, 반복을 이용해 열어야 한다의 의미가 무엇인지 고민했습니다.
    * 초기 구상에서 인덱스로 접근하는 max함수 만들기에 너무 익숙해진 나머지 무리하게 인덱스를 이용해 처리를 진행했습니다. revenue 항목들을 반복하면서 동일 반복문 내에서 인덱싱까지 모두 끝내는 방식을 고민했으나 구현은 하지 못했습니다.
    * 이후 README작성 중 값을 반복적으로 참조하면 그것 자체를 활용할 수 있다고 깨닫고 두번째 케이스를 작성했습니다.
  * 내가 생각하는 이 문제의 포인트
    * 외부의 파일을 열어 정보를 직접 가져오는 것과 값 갱신 자체를 이용한 최대값 찾기입니다.

## 📒 E. 알고리즘을 통한 데이터 출력

* 요구 사항 : 세부적인 영화 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성합니다. 

  * 데이터

    1. movies.json과 movies폴더 내부의 파일들을 사용합니다.

    2. movies.json은 영화 전체 데이터를 가지고 있습니다.

    3. movies 폴더 내부의 파일들은 각 영화의 상세정보를 가지고 있습니다.

    4. movies 폴더의 파일의 이름은 영화의 id로 구성되어 있습니다.

    5. 개봉일 정보는 상세정보 파일을 통해 확인할 수 있습니다.

       힌트 : 반복문을 통해 상세 정보 파일을 오픈해야 합니다.


* 결과 : 

1. 개봉일이 12월인 영화들의 제목을 리스트로 출력하는 함수 dec_movies를 완성합니다.

* 문제 접근 방법 및 코드 설명

```python
def dec_movies(movies):
    # 여기에 코드를 작성합니다.  
    title = []    # 제목들을 저장하기 위한 리스트
    for movie in movies :
        movie_id = str(movie.get('id'))
        movie_info_file = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_more_info = json.load(movie_info_file)
        release_date = movie_more_info.get('release_date')    # 개봉일 정보 저장
        
        if release_date[5:7] == '12':    # 개봉일 정보의 월 정보가 12라면
            title += [movie_more_info.get("title")]    # 제목을 리스트에 저장
                                             # = movie.get('title') 불필요하게 길게 쓰지 말자
    return title
```

* 이 문제에서 어려웠던점
  * movies의 구조를 확인하기 위해 출력해보면서 마찬가지로 리스트 안에 딕셔너리를 넣는 방식을 떠올렸습니다. 만약 이것을 확인하지 못했다면 genres를 보는 것으로라도 떠올릴 수 있었을지 의문입니다.
* 내가 생각하는 이 문제의 포인트
  * 앞선 문제들의 구조를 가져와 반복시키면서 각각의 결과들을 저장하는 것 입니다. 직접 리스트 내부에 딕셔너리를 저장해 실습에서 주어진 자료와 동일한 구조를 만들어 볼 수 있었습니다.



# 💡후기

* 문제를 하나씩 풀면서 효과적인 프로그램 작성 순서를 직접 경험해 볼 수 있어 좋았습니다. 학교 강의나 구미 1반 교수님께서 항상 보여주시는 방법임에도 습관에 따라 실질적 구동부가 아닌 코드 상 위쪽에 오는 행부터 작성(절차지향?)해서 직접 이런 순서를 따라 보기는 처음이었습니다. 코드의 실행을 바로바로 확인하면서 작성할 수 있다는 장점도 있고 앞서 만든 구조가 뒤에 그대로 이용되는 것을 보면서 훨씬 실수나 에러를 줄일 수 있다고 느껴서 앞으로 손에 익을 수 있게 해야겠다고 생각했습니다.
* 웹엑스 화면으로 잠깐 보였던 교수님의 화면에 값을 받아오면서 바로 딕셔너리로 묶으시는 것을 보고 또 하나 배웠습니다. 코드를 길게 쓸 필요 없이 깔끔하게 작성할 수 있게 됨과 동시에 가독성이 엄청 개선되는 방법이었습니다. (E = mc^2!) 리턴문에 그렇게 길게 쓰면서도 못 느낀 것이 신기합니다.
* 효율적이고 가독성 좋은 코드 작성을 위해 파이팅!
