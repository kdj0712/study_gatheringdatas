import requests

url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

# from : https://www.data.go.kr/iim/api/selectAPIAcountView.do  자세한 세부 규칙도 여기서 확인할 것
# https://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list?
# serviceKey=yJgnzrDPngw7nw8rHXdq2exc9xxcXlYp9knUeoaMTvMiiQipAFQsyhr9xYT2a0sr%2BR%2Bw1LLReXys9t18Q27yIA%3D%3D
# &pageNo=1
# &numOfRows=10
# &dataType=JSON

params = {'serviceKey':'yJgnzrDPngw7nw8rHXdq2exc9xxcXlYp9knUeoaMTvMiiQipAFQsyhr9xYT2a0sr+R+w1LLReXys9t18Q27yIA=='
          ,'pageNo' : 1
          , 'numOfRows' : 10
          , 'dataType' : 'JSON'}

response = requests.get(url, params=params)

print(response.content)

import json

contents = json.loads(response.content)

type(contents)
# <class 'dict'>
contents['header']
# {'resultCode': '00', 'resultMsg': '정상'}
contents['header']['resultCode']
# '00'
contents['body']['totalCount']
# 18
type(contents['body']['items'])   # DB에 저장할 리스트 
# <class 'list'>

# mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["data_go_kr"]
# collection 작업
collection = database['rent-loan-rate-info_rate-list']
# insert 작업 진행
result = collection.insert_many(contents['body']['items'])

pass