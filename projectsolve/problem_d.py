import json


def max_revenue(movies):
    # 여기에 코드를 작성합니다.  
    # case1. 최대값을 찾고 이를 이용해 인덱스를 찾아 제목 출력
    # title = []
    # revenue = []
    # for movie in movies :
    #     movie_id = str(movie.get('id'))
    #     more_info_file = open(f'data/movies/{movie_id}.json', encoding='UTF8')
    #     movie_more_info = json.load(more_info_file)
    #     title += [movie_more_info.get('title')]
    #     revenue += [movie_more_info.get('revenue')]
    # print(revenue)
    # print(title)
    # maximum = revenue[0]
    # for rev in revenue :
    #     if maximum < rev :
    #         maximum = rev

    # cnt = 0
    # for rev in revenue :
    #     if rev != maximum :
    #         cnt += 1
    #     else :
    #         break
       
    # return title[cnt]

    # case2. 이전 최대값을 저장해 비교를 통해 필요시 갱신
    max_revenue = 0
    for movie in movies :
        movie_id = str(movie.get('id'))
        more_info_file = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_more_info = json.load(more_info_file)
        revenue = movie_more_info.get('revenue')
        
        if max_revenue < revenue :
            title = movie.get('title')
            max_revenue = revenue

    return title

 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))