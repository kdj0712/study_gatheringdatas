import requests

url = '	http://apis.data.go.kr/1360000/TourStnInfoService1/getCityTourClmIdx1'

# http://apis.data.go.kr/1360000/TourStnInfoService1/getCityTourClmIdx1
# serviceKey=yJgnzrDPngw7nw8rHXdq2exc9xxcXlYp9knUeoaMTvMiiQipAFQsyhr9xYT2a0sr%2BR%2Bw1LLReXys9t18Q27yIA%3D%3D
# pageNo=1
# numOfRows=10
# dataType=JSON
# CURRENT_DATE=2018123110
# DAY=3
# CITY_AREA_ID=5013000000

params = {'serviceKey':'yJgnzrDPngw7nw8rHXdq2exc9xxcXlYp9knUeoaMTvMiiQipAFQsyhr9xYT2a0sr+R+w1LLReXys9t18Q27yIA=='
          ,'pageNo' : 1
          , 'numOfRows' : 10
          , 'dataType' : 'JSON'
          , 'CURRENT_DATE' : '2018123110'
          , 'DAY' : 3
          , 'CITY_AREA_ID' : 5013000000 }

response = requests.get(url, params=params)

print(response.content)

import json

contents = json.loads(response.content)
pass
# type(contents)
# # <class 'dict'>
# contents['response']['header']
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
database = mongoClient["data_go_kr"]
# collection 작업
collection = database['TourStnInfoService1']
# insert 작업 진행
result = collection.insert_many(contents['response']['body']['items']['item'])

pass