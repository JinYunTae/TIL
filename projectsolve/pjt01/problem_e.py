import json


def dec_movies(movies):
    # 여기에 코드를 작성합니다.  
    title = []
    for movie in movies :
        movie_id = str(movie.get('id'))
        movie_info_file = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_more_info = json.load(movie_info_file)
        release_date = movie_more_info.get('release_date')
        
        if release_date[5:7] == '12':
            title += [movie_more_info.get("title")]
    
    return title
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))