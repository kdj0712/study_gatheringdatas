from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()

chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory),options=chrome_options)

capabilities = browser.capabilities

# for page_number in [1,2,3,4,5,6] : # page number
for page_number in range(1,7) :  # page number
    url = "https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214355&page={}".format(page_number)
    browser.get(url)
    time.sleep(3)
  # 해당 브라우저의 내용을 가져오는 명령어
    html = browser.page_source        
    pass                                     # 가져온 browser의 내용을 html이라는 변수로 선언
pass
from selenium.webdriver.common.by import By
# 정보 획득 시 거의 대부분 사용할 기능from selenium.webdriver.common.by import By
# 가져온 정보에서 특별한 식별자를 추출하기 위한 선택자 부호

# selector_value = "div.info"   # 해당 페이지에서 div.info를 기준점으로 selector_value라는 변수를 선언한다.
# element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)
# # 페이지 내에 존재하는 CSS_SELECTOR 중 div.info의 영역 내에 있는 모든 요소를 찾아서,element_bundle이라는 변수로 지정한다.
# for element_item in element_bundle:   # 찾아낸 element_bundle을 element_item이라는 요소로 지칭하며 조건에 맞을 경우 아래의 내용을 실행한다.
#     element_title = element_item.find_element(by=By.CSS_SELECTOR, value ="div.info > em > a")
#     # 가져온 정보에서 value의 위치값과 동일한 내용들을 element_title이라는 변수로 지정한다.
#     title = element_title.text
#     # 가져온 element_title의 문자화한 내용을 title이라는 변수로 지정한다.

#     try :   # 조건에 맞다면 아래의 내용을 실행
#         element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value =" ul > li.c_price > span") 
#         # 가져온 정보에서 value의 위치값과 동일한 내용들을 element_old_price 라는 변수로 지정한다.
#         old_price = element_old_price.text
#         # 가져온 element_old_price의 문자화 한 내용을 old_price라는 변수로 지정한다.
#     except: # try의 조건에 맞지 않는 항목이 발생할 경우 오류가 발생할 수 있으니, 아래의 내용을 실행하여 대체한다.
#         old_price = "" # 위의 조건에 맞는 값이 없으면 빈 값으로 치환
#         pass
#     finally:
#         pass

#     element_sale_price = element_item.find_element(by=By.CSS_SELECTOR, value="span.sale")
#     # 가져온 정보에서 value의 위치값과 동일한 내용들을 element_sale_price 라는 변수로 지정한다.
#     sale_price = element_sale_price.text
#     # 가져온 element_sale_price의 문자화 한 내용을 old_price라는 변수로 지정한다.

#     element_delivery_types = element_item.find_element(by=By.CSS_SELECTOR, value="div.icon > div")
#     # 가져온 정보에서 value의 위치값과 동일한 내용들을 element_delivery_types 라는 변수로 지정한다.
#     elements = element_delivery_types.text.split()
#     # 가져온 element_delivery_types 의 문자화 한 내용을 elements라는 변수로 지정한다.
#     # 공백을 기준으로 분할하여 elements 변수에 리스트 형태로 저장한다. 
    
#     print("title : "+ title)
#     # title 변수의 내용을 출력
#     print("old price : " + old_price)
#     # old_price 변수의 내용을 출력
#     print("sale price : " + sale_price)
#     # sale_price 변수의 내용을 출력
#     if elements:
#         # elements 변수에 내용이 있다면
#         for deliveries in elements:
#             # elements_의 항목을 deliveries라는 변수로 지정 후 복수의 값이 있을 수 있으므로 반복을 지시
#             print("delivery type : " + deliveries)
#             # deliveries 변수의 내용을 출력
#     else: # elements 에 내용이 없을 경우
#         print("delivery type :" + "")
#         # deliveries 변수의 내용이 없으므로 빈 문자열을 출력
        
browser.quit()
# browser에 대한 모든 지시 사항을 이행한 경우 quit할 것을 지시

            