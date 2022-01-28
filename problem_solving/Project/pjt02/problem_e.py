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
        if act.get('cast_id') < 10 : # id가 10보다 작은 배우들을
            cast.append(act.get('name')) # 목록에 추가합니다.
    
    all_crew = cred_data.get('crew')
    crew = [] # 감독 정보를 저장하기 위한 리스트입니다.
    for staff in all_crew: # 모든 스태프들에 대해
        if staff.get('department') == 'Directing': # 감독이라면
            crew.append(staff.get('name')) # 목록에 추가합니다.

    cast_n_crew = {'cast' : cast, 'crew' : crew} # 배우와 감독의 정보를 담은 딕셔너리입니다.
    
    return cast_n_crew

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
