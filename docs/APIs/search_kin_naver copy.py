# from https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

import requests   # postman 역할

# request API 요청
url = 'https://openapi.naver.com/v1/search/kin.json'

params = {'query':'증상'}
headers = { 'X-Naver-Client-Id': 'BOmq7WuvGENwf353WeCQ',
            'X-Naver-Client-Secret' : '2fqIUaIyE3' }
response = requests.get(url, params=params, headers=headers)

# response API 응답
response.content



pass

print(response.content)

import json

contents = json.loads(response.content)

type(contents)
# <class 'dict'>
# contents['items']
# # {'resultCode': '00', 'resultMsg': '정상'}
# contents['header']['resultCode']
# # '00'
# contents['body']['totalCount']
# # 18
# type(contents['body']['items'])   # DB에 저장할 리스트 
# # <class 'list'>

# mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["project"]
# collection 작업
collection = database['naver_kin_Symptom']
# insert 작업 진행
result = collection.insert_many(contents['body']['items'])

pass