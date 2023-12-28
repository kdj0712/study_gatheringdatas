# # Selenium 버전에 따라 인자의 이름이 변경되었을 수 있으므로, 정상적인 설치 및 기능이 안 될 경우 아래의 방식으로 진행을 하도록 한다.
# from selenium import webdriver                                          # 통상과 동일 
# from selenium.webdriver.chrome.service import Service as ChromeService  #
# from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
# browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# capabilities = browser.capabilities
# browser.get("https://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1002213#sortCd%%I$$pageNum%%10 > normal_prd")
# from selenium.webdriver.common.by import By
# # items = "normal_prd"
# # results = browser.find_elements(by=By.CSS_SELECTOR,value=items)

# result = browser.find_elements(by=By.CSS_SELECTOR,value="div > div.photo_wrap > a")

# time.sleep(4)

# for i in range(4):
#     result = browser.find_elements(by=By.CSS_SELECTOR,value="div > div.photo_wrap > a")
#     result[i].click()
#     time.sleep(2)

#     browser.back()      # 이전 화면으로 다시 복귀
#     time.sleep(2)       # 이전 화면으로 다시 복귀
#     pass
# pass
# # 브라우저 종료
# browser.quit()






# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.w3schools.com/)
url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb'
browser.get(url)

# - 정보 획득
from selenium.webdriver.common.by import By

element_companies = browser.find_elements(by=By.CSS_SELECTOR, value="div > a > span.best")
# for index in range(len(element_companies)) :
for index in range(4) :
    element_companies = browser.find_elements(by=By.CSS_SELECTOR, value="div > a > span.best")
    element_companies[index].click()
    time.sleep(1)       # 화면 완성 term
    # 앱 상세 제목 : div > h1
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="div > h1.title")
    print("App company Name : {}".format(element_title.text))
    
    browser.back()      # 제품 리스트로 이동
    time.sleep(1)       # 화면 완성 term
    pass
pass

# 브라우저 종료
# browser.quit()