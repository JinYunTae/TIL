import json
from pprint import pprint


def movie_info(movies, genres):
    # 여기에 코드를 작성합니다.
    dict_list = []  
    for movie in movies :
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

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))