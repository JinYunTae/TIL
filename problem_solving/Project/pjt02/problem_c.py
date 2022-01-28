import requests
from pprint import pprint


def ranking():
    pass 
    # 여기에 코드를 작성합니다.  
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

    #요청에 따른 응답을 받습니다.
    response = requests.get(BASE_URL + path, params = params)
    # print(response) # 200!
    p_m_list = response.json().get('results') # results 항목만 받습니다.

    for i in range(1, len(p_m_list)): # 내부 딕셔너리들을 평점에 따라 정렬합니다.
        for j in range(len(p_m_list)-i):
            if p_m_list[j]['vote_average'] < p_m_list[j+1]['vote_average']: # 평점이 높은 순으로 정렬합니다.
                p_m_list[j], p_m_list[j+1] = p_m_list[j+1], p_m_list[j]

    return p_m_list[:5] # 평점이 높은 5개의 영화 정보를 반환합니다.
    '''
    dic_li = [{'id' : 1, 'a' : 'a'},{'id' : 3, 'a' : 'e'},{'id' : 4, 'a' : 's'},{'id' : 5, 'a' : 'f'},{'id' : 2, 'a' : 'e'}]
    test2 = sorted(dic_li, key= lambda x : dic_li[x]['id'])
    print(test2)

if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
