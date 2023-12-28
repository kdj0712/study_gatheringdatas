from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
from selenium.common.exceptions import NoSuchElementException
import time

def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://192.168.10.236:27017") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["gatheringdatas"] # 해당 포트에 접속해서 database에 연결
    collection = database['11st_items_comments'] # 데이터베이스에서 11st_comments 이라는 collection에 연결
    return collection # collection이 반환되도록 지정

webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = browser.capabilities
browser.get("https://www.11st.co.kr/products/1881101601?&trTypeCd=21&trCtgrNo=1002213")
html = browser.page_source

from selenium.webdriver.common.by import By
# iframe으로 전환
browser.switch_to.frame('ifrmReview')
# iframe 내의 대상 영역 세팅
main_board = "#review-list-area"
element_body = browser.find_elements(by=By.CSS_SELECTOR, value=main_board) 
# 해당 페의지의 CSS_SELECTOR 선택자가 미리 지정한 main_board에 해당되는 내용을 찾아온다.
button = "#review-list-page-area > div > button"
# 인용할 버튼의 위치를 button이라는 변수로 선언
time.sleep(5)
# 행동을 반복할 텀을 5초정도 준다.
while True:
    try:
        element_button = browser.find_element(by=By.CSS_SELECTOR, value=button)
        element_button.click()
        time.sleep(5)
        # 내용을 더 확인하기 위하여 버튼을 클릭하는 것을 버튼이 더 이상 생성되지 않을 때 까지 계속 반복하여 생성
    except:
        break  # 버튼이 더 이상 생성되지 않으면 반복문 종료

selector_value = "li.review_list_element"
# 해당 페이지의 ""li.review_list_element" 부분을 selector_value 라는 변수로 지정
bodies = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value) 
# ""li.review_list_element" 에 해당되는 내용의 요소들을 가져온 것을 bodies라는 변수로 선언한다. 이는 요소가 여러가지 이므로 리스트의 형태로 불려온다.

for items in bodies: # bodies의 내용물을 items라는 변수에 담는다. 조건이 맞는 경우 아래의 행동들을 반복한다.
    try:
        element_id = items.find_element(by=By.CSS_SELECTOR, value="dt.name")
        # 가져온 items의 내용물을 비교하여 value에 지정한 값과 같은 것을 찾는다면, 그것을 element_id 라는 변수로 선언한다.
        id = element_id.text
    except:
        id = ""
        pass
    finally:
        pass

    try:
        element_options_first = items.find_element(by=By.CSS_SELECTOR, value="div.option")
        option1 = element_options_first.text
        options = option1
        # 영역은 다르지만 비슷한 컨셉의 아이템을 선별하여 텍스트화 한 뒤 options라는 변수로 선언
        element_options_second = items.find_element(by=By.CSS_SELECTOR, value="p.option")
        option2 = element_options_second.text
        options = option2
    except NoSuchElementException: # 조건에 맞지 않는 것이 나와도 다른 액션을 취하지 않고 그냥 흘러가도록 지정함
        pass
    finally:
        pass

    try:
        element_point = items.find_element(by=By.CSS_SELECTOR, value="div > p.grade > span > em")
        # 가져온 items의 내용물을 비교하여 value에 지정한 값과 같은 것을 찾는다면, 그것을 element_point라는 변수로 선언한다.
        point = element_point.text
        # element_point을 텍스트화 한 것을 comment라는 변수로 선언
    except:
        point = ""
        pass
    finally:
        pass

    try:
        element_comment = items.find_element(by=By.CSS_SELECTOR, value="div.cont_text_wrap > p")
        # 가져온 items의 내용물을 비교하여 value에 지정한 값과 같은 것을 찾는다면, 그것을 element_comment라는 변수로 선언한다.
        comment = element_comment.text
        # element_comment을 텍스트화 한 것을 comment라는 변수로 선언
    except:
        comment = ""
        pass
    finally:
        pass

    print("id  :" + id)
    print("options  :" + options)
    print("point  :" + point)
    print("comment  :" + comment)

    # collection = Connect()
    # # database를 연동하는 function을 선언하여 기능을 호출한 것을 collection이라는 변수로 선언한다.
    # collection.insert_one({"ID":id,"Option":options,"Point":point,"Comment":comment})
    # # 콜렉션에 해당 항목 들을 반복하여 집어 넣는다.

browser.quit()