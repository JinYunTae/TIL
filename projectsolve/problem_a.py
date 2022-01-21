import json
from pprint import pprint


def movie_info(movie):
    # 여기에 코드를 작성합니다.    
    movie_id = movie.get('id')
    title = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')
    
    return {'genre_ids': genre_ids,
            'id': movie_id,
            'overview': overview,
            'poster_path': poster_path,
            'title': title,
            'vote_average': vote_average
            }

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))