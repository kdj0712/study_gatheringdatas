import requests

url = 'http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'

# http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo
# serviceKey=yJgnzrDPngw7nw8rHXdq2exc9xxcXlYp9knUeoaMTvMiiQipAFQsyhr9xYT2a0sr+R+w1LLReXys9t18Q27yIA==
# pageNo=1&numOfRows=10
# type=json
# bidNtceBgnDt=201712010000
# bidNtceEndDt=201712312359

params = {'serviceKey':'yJgnzrDPngw7nw8rHXdq2exc9xxcXlYp9knUeoaMTvMiiQipAFQsyhr9xYT2a0sr+R+w1LLReXys9t18Q27yIA=='
          ,'pageNo' : 1
          , 'numOfRows' : 10
          , 'type' : 'json'
          ,'bidNtceBgnDt' : 201712010000
          ,'bidNtceEndDt' : 201712312359}

response = requests.get(url, params=params)

print(response.content)

import json

contents = json.loads(response.content)

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
collection = database['PubDataOpnStdService']
# insert 작업 진행
result = collection.insert_many(contents['response']['body']['items'])

pass