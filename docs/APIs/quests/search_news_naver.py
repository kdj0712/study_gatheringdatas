# from https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

import requests   # postman 역할

# request API 요청
url = 'https://openapi.naver.com/v1/search/shop.json'

params = {'query':'인공지능'}
headers = { 'X-Naver-Client-Id': 'BOmq7WuvGENwf353WeCQ',
            'X-Naver-Client-Secret' : '2fqIUaIyE3' }
response = requests.get(url, params=params, headers=headers)

# response API 응답
response.content

print(response.content)

import json

contents = json.loads(response.content)
interger_value = {}
string_value = {}

for key,value in contents.items():
    if isinstance(value, int):
        interger_value[key] = value
    elif isinstance(value, str):
        string_value[key] = value

# mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["data_go_kr"]
# collection 작업
collection_info = database['search_shop_info']
collection_list = database['search_shop_list']
# insert 작업 진행
collection_info.insert_many([interger_value])
collection_list.insert_many([string_value])
collection_list.insert_many(contents['items'])

pass