# # Selenium 버전에 따라 인자의 이름이 변경되었을 수 있으므로, 정상적인 설치 및 기능이 안 될 경우 아래의 방식으로 진행을 하도록 한다.
from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager     
from selenium.webdriver.chrome.options import Options           # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
import time
# 패키지를 사용하여 Chrome WebDriver를 관리하는 방식입니다. 이 패키지는 WebDriver를 자동으로 다운로드하고 최신 버전을 유지해줍니다
chrome_options = Options()
# browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
# 이 과정들을 다 포함하여 webdriver 크롬 브라우저가 실행되도록 선언 
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
# 또는 이렇게도 할 수 있다.
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory),options=chrome_options)
# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
# - 주소 https://www.w3schools.com/ 입력
browser.get("https://pedia.watcha.com/ko-KR/contents/md76ovO/comments")

html = browser.page_source

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 한 페이지 씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")
previous_scrollHeight = 0

while True:
    element_body.send_keys(Keys.END)
    current_scrollheight = browser.execute_script("return document.body.scrollHeight")
    if previous_scrollHeight >= current_scrollheight:
        break
    else:
        previous_scrollHeight = current_scrollheight
    time.sleep(3)
    
selector_value = "css-13j4ly.egj9y8a4"
bodies = element_body.find_elements(by=By.CSS_SELECTOR, value=selector_value)

for items in bodies:
    element_name = items.find_element(by=By.CSS_SELECTOR, value="a > div.css-eldyae.e10cf2lr1")
    name = element_name.text

    element_point = items.find_element(by=By.CSS_SELECTOR, value="div.css-31ods0.egj9y8a0 > span")
    point = element_point.text

    element_comment = items.find_element(by=By.CSS_SELECTOR, value=" div.css-2occzs.egj9y8a1 > a > div > span")
    comment = element_comment.text
    print("name : " + name)
    if point:
        print("point : " + point)
    else:
        print("point : " + "")
    print("comment : " + comment)

browser.quit()



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # ChromeDriverManager 버전 확인
# webdriver_manager_directory = ChromeDriverManager().install()

# # WebDriver 옵션 설정
# chrome_options = Options()
# chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# # WebDriver 실행
# browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory), options=chrome_options)

# # 주소로 이동
# browser.get("https://pedia.watcha.com/ko-KR/contents/md76ovO/comments")

# # 페이지 스크롤
# element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")
# previous_scrollHeight = 0

# while True:
#     element_body.send_keys(Keys.END)
#     time.sleep(3)

#     current_scrollheight = browser.execute_script("return document.body.scrollHeight")
#     if previous_scrollHeight >= current_scrollheight:
#         break
#     else:
#         previous_scrollHeight = current_scrollheight

# selector_value = "css-13j4ly egj9y8a4"
# bodies = element_body.find_elements(by=By.CSS_SELECTOR, value=selector_value)

# for items in bodies:
#     element_name = items.find_elements(by=By.CSS_SELECTOR, value="div.css-drz8qh.egj9y8a2 > a > div.css-eldyae.e10cf2lr1")
#     for names in element_name:
#         name = names.find_element(by=By.CSS_SELECTOR, value="div.css-drz8qh.egj9y8a2 > a > div.css-eldyae.e10cf2lr1")
#         naming = name.text.split()

#     element_point = items.find_elements(by=By.CSS_SELECTOR, value="div.css-31ods0.egj9y8a0 > span")
#     for points in element_point:
#         point = points.find_element(by=By.CSS_SELECTOR, value="div.css-31ods0.egj9y8a0 > span")
#         pointing = point.text

#     element_comment = items.find_elements(by=By.CSS_SELECTOR, value="div.css-2occzs.egj9y8a1 > a > div > span")
#     for comments in element_comment:
#         comment = comments.find_element(by=By.CSS_SELECTOR, value="div.css-2occzs.egj9y8a1 > a > div > span")
#         commenting = comment.text.split()

#     print("name : " + ' '.join(naming))
#     if point:
#         print("point : " + ' '.join(pointing))
#     else:
#         print("point : " + "")
#     print("comment : " + ' '.join(comment))

# # WebDriver 종료
# browser.quit()