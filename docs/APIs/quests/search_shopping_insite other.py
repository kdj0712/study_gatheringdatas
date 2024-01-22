# from https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md#%EC%87%BC%ED%95%91%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%B6%84%EC%95%BC%EB%B3%84-%ED%8A%B8%EB%A0%8C%EB%93%9C-%EC%A1%B0%ED%9A%8C

import requests   # postman 역할

# request API 요청
url = "https://openapi.naver.com/v1/datalab/shopping/categories"
headers = { "X-Naver-Client-Id": "BOmq7WuvGENwf353WeCQ",
            "X-Naver-Client-Secret" : "2fqIUaIyE3"}
bodies = {
          "startDate": "2024-01-01",
          "endDate": "2024-01-21",
          "timeUnit": "date",
          "category": [{"name": "디지털/가전", "param": [ "50000003"]}]
          }
import json
response = requests.post(url, headers=headers, json = bodies)


# 뤼튼의 설명으로 갈음

# params는 URL의 쿼리 문자열에 데이터를 추가하는 데 사용되며, 주로 GET 요청에서 사용됩니다.

# POST 요청에서 데이터를 보낼 때는 보통 data 또는 json 인자를 사용합니다. 특히, JSON 형식의 데이터를 보낼 때는 json 인자를 사용하면 편리합니다.

# 따라서, 코드를 다음과 같이 수정할 수 있습니다:

# 이렇게 수정하면, params의 내용이 요청 본문에 JSON 형식으로 포함되어 전송됩니다. 그리고 'Content-Type' 헤더는 'application/json'으로 자동 설정되므로, 직접 설정할 필요가 없습니다.



# response API 응답
response.content

print(response.content)

contents = json.loads(response.content)


# mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["data_go_kr"]
# collection 작업
collection_info = database["shoping_insite2"]

# insert 작업 진행
collection_info.insert_many(contents['results'][0]['data'])


pass