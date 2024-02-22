from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
from selenium.common.exceptions import NoSuchElementException
import time

def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://192.168.10.236:27017") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["project"] # 해당 포트에 접속해서 database에 연결
    collection = database['naver_kin_Symptom'] # 데이터베이스에서 11st_comments 이라는 collection에 연결
    return collection # collection이 반환되도록 지정

webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = browser.capabilities
browser.get("https://kin.naver.com/search/list.naver?query=%EC%A6%9D%EC%83%81")
html = browser.page_source

from selenium.webdriver.common.by import By
# iframe으로 전환
# browser.switch_to.frame('ifrmReview')
# iframe 내의 대상 영역 세팅
main_board = "#s_content > div.section"
element_body = browser.find_elements(by=By.CSS_SELECTOR, value=main_board) 
# 해당 페의지의 CSS_SELECTOR 선택자가 미리 지정한 main_board에 해당되는 내용을 찾아온다.

recently = browser.find_element(by=By.CSS_SELECTOR,value="ul.option_sort > li.sp_sort2 > strong > a")
recently.click()

origin_browser = browser.current_window_handle
"s_content > div.section > ul > li:nth-child(1) > dl > dt > a"




def get_source():
    # 아래 동작을 수행할 function을 get_source라는 이름으로 지정한다.
    element_numbers = browser.find_elements(by=By.CSS_SELECTOR,value="table.Ltbl_list > tbody > tr > td:nth-child(2)")
    # 반복할 횟수를 지정하기 위해 방문하는 페이지의 컨텐츠의 개수를 사전 파악해서 element_numbers 라는 변수로 지정한다.
    results = []
    # 빈 리스트인 results를 생성한다.
    for j in range(len(element_numbers)): # 컨텐츠의 개수를 영역 설정하여 J라는 변수로 지정한다
        auction_number = browser.find_elements(by=By.CSS_SELECTOR,value="table.Ltbl_list > tbody > tr > td:nth-child(2)")
        # 경매 문건 번호의 정보를 가져와서 auction_number라는 변수로 담아낸다.
        number = auction_number[j].text
        # 현재 반복문의 회차와 동일한 위치값의 경매 문건 번호를 나중에 반환하기 위해 number라는 변수로 지정한다.
        element_locate = browser.find_elements(by=By.CSS_SELECTOR,value="td:nth-child(4)")
        # 경매 물건 소재지의 정보를 가져와서 element_locate라는 변수로 담아낸다.
        locate = element_locate[j].text
        # 현재 반복문의 회차와 동일한 위치값의 경매 물건 소재지를 나중에 반환하기 위해 locate라는 변수로 지정한다.
        results.append((number,locate))
        # 나중에 사용할 값인 number와 locate를 딕셔너리 형태로 반복적으로 보낸다.
        pass
    return results 
    # 나중에 사용할 값으로 number와 locate를 results라는 변수로 반환한다.






















# for items in bodies: # bodies의 내용물을 items라는 변수에 담는다. 조건이 맞는 경우 아래의 행동들을 반복한다.
#     try:
#         element_id = items.find_element(by=By.CSS_SELECTOR, value="dt.name")
#         # 가져온 items의 내용물을 비교하여 value에 지정한 값과 같은 것을 찾는다면, 그것을 element_id 라는 변수로 선언한다.
#         id = element_id.text
#     except:
#         id = ""
#         pass
#     finally:
#         pass

#     try:
#         element_options_first = items.find_element(by=By.CSS_SELECTOR, value="div.option")
#         option1 = element_options_first.text
#         options = option1
#         # 영역은 다르지만 비슷한 컨셉의 아이템을 선별하여 텍스트화 한 뒤 options라는 변수로 선언
#         element_options_second = items.find_element(by=By.CSS_SELECTOR, value="p.option")
#         option2 = element_options_second.text
#         options = option2
#     except NoSuchElementException: # 조건에 맞지 않는 것이 나와도 다른 액션을 취하지 않고 그냥 흘러가도록 지정함
#         pass
#     finally:
#         pass

#     try:
#         element_point = items.find_element(by=By.CSS_SELECTOR, value="div > p.grade > span > em")
#         # 가져온 items의 내용물을 비교하여 value에 지정한 값과 같은 것을 찾는다면, 그것을 element_point라는 변수로 선언한다.
#         point = element_point.text
#         # element_point을 텍스트화 한 것을 comment라는 변수로 선언
#     except:
#         point = ""
#         pass
#     finally:
#         pass

#     try:
#         element_comment = items.find_element(by=By.CSS_SELECTOR, value="div.cont_text_wrap > p")
#         # 가져온 items의 내용물을 비교하여 value에 지정한 값과 같은 것을 찾는다면, 그것을 element_comment라는 변수로 선언한다.
#         comment = element_comment.text
#         # element_comment을 텍스트화 한 것을 comment라는 변수로 선언
#     except:
#         comment = ""
#         pass
#     finally:
#         pass

#     collection = Connect()
#     # database를 연동하는 function을 선언하여 기능을 호출한 것을 collection이라는 변수로 선언한다.
#     collection.insert_one({"Question":id,"Answer":options})
#     # 콜렉션에 해당 항목 들을 반복하여 집어 넣는다.

browser.quit()

