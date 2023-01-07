import json

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성

a = {}
list = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
for k in list:        
    for one_dict in movies_list:
        print('{')
        for i_keys in one_dict:
            # print(ii) 
            if i_keys in list:
                b = one_dict.get(i_keys)
                a[i_keys] = b
                print(f"'{i_keys}' :  {a.get(i_keys)}")
        print('} \n')