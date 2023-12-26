
# # Selenium 버전에 따라 인자의 이름이 변경되었을 수 있으므로, 정상적인 설치 및 기능이 안 될 경우 아래의 방식으로 진행을 하도록 한다.
from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
import time
# 패키지를 사용하여 Chrome WebDriver를 관리하는 방식입니다. 이 패키지는 WebDriver를 자동으로 다운로드하고 최신 버전을 유지해줍니다

# browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
# 이 과정들을 다 포함하여 webdriver 크롬 브라우저가 실행되도록 선언 

# 또는 이렇게도 할 수 있다.
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))


# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
# - 주소 https://www.w3schools.com/ 입력
browser.get("https://pedia.watcha.com/ko-KR/contents/m5ZlbBL/comments")

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
    time.sleep(1)
    pass

element_body.find_elements(by=By.CSS_SELECTOR,value="ul > div.css-13j4ly.egj9y8a4")


browser.quit()