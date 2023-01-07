import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성

a = ['id', 'title', 'vote_average', 'overview', 'genre_ids']

for b in a:
    if b in movie:
        # print(b)
        print(f"'{b}': {movie.get(b)} \n")