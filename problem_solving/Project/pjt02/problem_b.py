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

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
