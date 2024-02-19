# Selenium 버전에 따라 인자의 이름이 변경되었을 수 있으므로, 정상적인 설치 및 기능이 안 될 경우 아래의 방식으로 진행을 하도록 한다.
from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.expected_conditions import alert_is_present
chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory),options = Options())
capabilities = browser.capabilities
browser.get("https://m.kinolights.com/title/601/reviews")
html = browser.page_source

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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

    try:
        wait = WebDriverWait(browser, 5)
        element_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.has-spoiler > button')))
        element_button.click()
        wait = WebDriverWait(browser, 5)
        wait.until(alert_is_present())

        # 팝업창에 대한 참조를 얻음
        alert = Alert(browser)
        
        # 팝업창에 'Enter' 키를 입력
        alert.send_keys(Keys.ENTER)
    except NoSuchElementException:
        pass
    except TimeoutException:
        pass
    pass

selector_value = "div.review-area"
bodies = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value) 

for items in bodies: # bodies의 내용물을 items라는 변수에 담는다. 조건이 맞는 경우 아래의 행동들을 반복한다.
    try:
        element_id = items.find_element(by=By.CSS_SELECTOR, value="div.user-info-wrap > a > div.writer-name")
        id = element_id.text
    except NoSuchElementException:
        id = ""
        pass
    finally:
        pass
    try:
        element_point = items.find_element(by=By.CSS_SELECTOR, value="div.movie-meta-info > span > span.user-star-score")
        point = element_point.text
    except NoSuchElementException: 
        point = ""
        pass
    finally:
        pass
    try:
        element_comment = items.find_element(by=By.CSS_SELECTOR, value="div.review-wrap.reviewContentsSection > a > div")
        comment = element_comment.text
    except NoSuchElementException: 
        comment = ""
        pass
    finally:
        pass
    print("id  :" + id)
    print("point  :" + point)
    print("comment  :" + comment)
pass


browser.quit()