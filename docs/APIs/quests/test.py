import requests

url = "https://openapi.naver.com/v1/datalab/shopping/categories"

params = {"startDate": "2024-01-01",
          "endDate":"2024-01-14",
           "timeUnit": "date",
             "category": [{"name": "디지털/가전", "param": [ "50000003"]}]}
headers = { "X-Naver-Client-Id": "BOmq7WuvGENwf353WeCQ",
            "X-Naver-Client-Secret" : "2fqIUaIyE3"}

response = requests.post(url, json=params, headers=headers)
print(response.text)
