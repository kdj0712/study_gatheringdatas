# * 웹 크롤링 동작
from selenium import webdriver
import time
# - chrome browser 열기
browser = webdriver.Chrome()
# - 주소 입력
browser.get("https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000184922&dispCatNo=1000001001200040001&trackingCd=Cat1000001001200040001_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EB%B2%A0%EC%9D%B4%EC%8A%A4/%ED%83%91%EC%BD%94%ED%8A%B8_%EC%86%8C_%EB%B2%A0%EC%9D%B4%EC%8A%A4/%ED%83%91%EC%BD%94%ED%8A%B8__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=1")

from selenium.webdriver.common.by import By

item = browser.find_elements(by=By.CSS_SELECTOR, value = "#Contents > div.prd_detail_box.renew")
items = []
for i in item:
    element_brand = browser.find_element(by=By.CSS_SELECTOR, value="#moveBrandShop")
    brand = element_brand.text
    
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="p.prd_name")
    title = element_title.text
    
    img = browser.find_element(by=By.CSS_SELECTOR, value="#mainImg")
    element_img = img.get_attribute('src')
    
    element_price = browser.find_element(by=By.CSS_SELECTOR, value="span.price-2 > strong")
    price = element_price.text
    items.append({"brand" : brand,
                    "title" : title,
                    "element_img" : element_img,
                    "price" : price})

    review_click = browser.find_element(by=By.CSS_SELECTOR, value = "#reviewInfo").click()
    time.sleep(3)
    reviews = [ ]
    review = browser.find_elements(by=By.CSS_SELECTOR, value="#gdasList > li")

    for x in review:
        try : 
            element_writer = x.find_element(by=By.CSS_SELECTOR, value="div.user.clrfix")
            writer = element_writer.text
        except : 
            writer = ""
        try : 
            element_grade = x.find_element(by=By.CSS_SELECTOR, value="span.review_point > span.point")
            grade = element_grade.text
        except : 
            grade = ""
        try : 
            element_option = x.find_element(by=By.CSS_SELECTOR, value="p.item_option")
            option = element_option.text
        except : 
            option = ""
        try : 
            element_comments = x.find_element(by=By.CSS_SELECTOR, value="div.txt_inner")
            comments = element_comments.text
        except : 
            comments = ""
        pass

        print(writer)
        print(grade)
        print(option)
        print(comments)



    reviews.append({"writer" : writer,
                    "grade" : grade,
                    "option" : option,  
                    "comments" : comments})
def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://192.168.10.236:27017") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["gatheringdatas"] # 해당 포트에 접속해서 database에 연결
    return database # collection이 반환되도록 지정
collections = Connect()




items,
# 위에 지정한 functions을 실행할 때 for 구문에서 나온 sta_dep이라는 변수를 가져가서 사용하고 그 실행 결과를 results라는 변수로 지정한다.
for result in results:
    # function이 동작하면서 반환된 내용을 result라는 변수에 담아서 그 갯수만큼 반복적으로 실행하도록 구문을 작성한다.
    number = result.get('사건 번호', '기본값').replace('\n', '')
    # 추출된 데이터를 가져올 때 깔끔한 정리를 위해, 작동하지 않는 \n 을 빈칸으로 치환하도록 선언하여 number라는 변수로 지정
    locate = result.get('소재지 및 내역', '기본값').replace('\n', '')
    # 추출된 데이터를 가져올 때 깔끔한 정리를 위해, 작동하지 않는 \n 을 빈칸으로 치환하도록 선언하여 locate라는 변수로 지정
    collection.insert_one({
        '법원 / 소재지 정보': sta_dep,
        '사건 번호': number,
        '소재지 및 내역': locate,
    })
# return items,reviews
time.sleep(3)


