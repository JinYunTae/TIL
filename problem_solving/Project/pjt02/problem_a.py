import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    '''
    1. URL 준비 //
    2. 요청 -> 응답 // 200
    3. 응답자료 처리 // data화 -> 리스트 발견 -> 개수 세기 끝
    4. 반환
    '''
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

if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
