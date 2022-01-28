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

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
