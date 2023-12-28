# Selenium 버전에 따라 인자의 이름이 변경되었을 수 있으므로, 정상적인 설치 및 기능이 안 될 경우 아래의 방식으로 진행을 하도록 한다.
from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager     
from selenium.webdriver.chrome.options import Options           # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
# 패키지를 사용하여 Chrome WebDriver를 관리하는 방식입니다. 이 패키지는 WebDriver를 자동으로 다운로드하고 최신 버전을 유지해줍니다
import time                 # time 기능을 선언한다.

def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://192.168.10.236:27017") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["gatheringdatas"] # 해당 포트에 접속해서 database에 연결
    return database # collection이 반환되도록 지정

collections = Connect()
collection = collections['watcha_comments']
# 데이터베이스에서 watcha_comments 이라는 collection에 연결
chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
# 잦은 접속으로 로봇 호출이 나오기 전에 user-agent를 알려주어, 접속의 패널티의 가능성을 줄이는 기능

webdriver_manager_directory = ChromeDriverManager().install() 
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory),options=chrome_options) # 위에 명기된 기능들이 작동되도록 호출하여 선언
# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

browser.get("https://pedia.watcha.com/ko-KR/contents/md76ovO/comments")
# - 주소 https://pedia.watcha.com/ko-KR/contents/md76ovO/comments 입력하여 페이지 내부의 내용을 가져오도록 선언

html = browser.page_source
# 가져오는 것이 가능하다면 열려있는 소스 코드를 html 변수에 저장

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

element_body = browser.find_element(by=By.CSS_SELECTOR, value="body") 
# 해당 페의지의 CSS_SELECTOR 선택자가 'body'에 해당되는 내용을 찾아온다.
previous_scrollHeight = 0
# 해당 페이지의 높이의 초기값을 0이라고 선언한다.

while True:
    element_body.send_keys(Keys.END) # page end의 기능을 적용하여 이동할 공간이 있다면 계속 이동하도록 한다.
    current_scrollheight = browser.execute_script("return document.body.scrollHeight")
     # (Java Script의 기능을 사용하여)페이지의 전체 높이를 반환하여 계산한 값을 current_scrollheight 라는 변수로 선언한다.
    if previous_scrollHeight >= current_scrollheight: # 만약 전체 높이와 비교하여 남아있는 공간이 없다면 행동을 멈추도록 선언한다.
        break
    else:
        previous_scrollHeight = current_scrollheight # 그렇지 않다면 해당 내용이 같아질 떄까지 반복한다.
    time.sleep(2) # 행동을 반복할 텀을 2초정도 준다. 반복이 진행되면서 페이지가 로딩이 될 여유를 준다.
        

selector_value = "div.css-13j4ly.egj9y8a4"
# 해당 페이지의 "div.css-13j4ly.egj9y8a4" 부분을 selectoc_value 라는 변수로 지정
bodies = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value) 
# "div.css-13j4ly.egj9y8a4" 에 해당되는 내용의 요소들을 가져온 것을 bodies라는 변수로 선언한다. 이는 요소가 여러가지 이므로 리스트의 형태로 불려온다.

for items in bodies: # bodies의 내용물을 items라는 변수에 담는다. 조건이 맞는 경우 아래의 행동들을 반복한다.
    element_name = items.find_element(by=By.CSS_SELECTOR, value="a > div.css-eldyae.e10cf2lr1")
    # 가져온 items의 내용물을 비교하여 value에 지정한 값과 같은 것을 찾는다면, 그것을 element_name이라는 변수로 선언한다.
    name = element_name.text
    # element_name을 텍스트화 한 것을 name이라는 변수로 선언
    try :   # 조건에 맞다면 아래의 내용을 실행
        element_point = items.find_element(by=By.CSS_SELECTOR, value="div.css-jqudug.egj9y8a3 > div.css-31ods0.egj9y8a0")
        # 가져온 정보에서 value의 위치값과 동일한 내용들을 element_point 라는 변수로 지정한다.
        point = element_point.text
        # 가져온 element_point의 문자화 한 내용을 point라는 변수로 지정한다.
    except: # try의 조건에 맞지 않는 항목이 발생할 경우 오류가 발생할 수 있으니, 아래의 내용을 실행하여 대체한다.
        point = "" # 위의 조건에 맞는 값이 없으면 빈 값으로 치환한 것을 point라는 변수로 지정한다.
        pass
    finally:
        pass
    element_comment = items.find_element(by=By.CSS_SELECTOR, value="div.css-2occzs.egj9y8a1 > a > div")
    # 가져온 items의 내용물을 비교하여 value에 지정한 값과 같은 것을 찾는다면, 그것을 element_comment라는 변수로 선언한다.
    comment = element_comment.text
    # element_comment을 텍스트화 한 것을 comment라는 변수로 선언
    print("name : " + name) # name의 내용물을 출력한다.
    print("point : " + point) # point의 내용물을 출력한다.
    print("comment : " + comment) # comment의 내용물을 출력한다.

    collection = Connect()
    # database를 연동하는 function을 선언하여 기능을 호출한 것을 collection이라는 변수로 선언한다.
    collection.insert_one({"name":name,"point":point,"comment":comment})
    # 구문 초반에 미리 조건을 제시한 collection에, 각 요소의 Key 값과 Value 값을 제시하여 저장이 되도록 한다.

# 위 구문은 찾아낸 요소들이 전부 사용될 때 까지 반복이 된다.
browser.quit()

# 모든 기능을 마친 다면 브라우저를 종료한다.