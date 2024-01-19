from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
from selenium.webdriver.chrome.options import Options

webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = browser.capabilities
browser.get("https://cafe.naver.com/peopledisc")
html = browser.page_source

from selenium.webdriver.common.by import By
element_click = browser.find_element(by=By.CSS_SELECTOR, value= "#menuLink84")
element_click.click()
# browser.find_element(by=By.CSS_SELECTOR, value= "#menuLink84").click()
# 이것과 동일하나, 위에 적은 것이 좀 더 정확하다.

# iframe으로 전환
browser.switch_to.frame('cafe_main')


# 게시판 게시물 selector : #main-area > div:nth-child(4) > table > tbody > tr
cafe_list = browser.find_elements(by=By.CSS_SELECTOR, value= "#main-area > div:nth-child(4) > table > tbody > tr")
pass

#mongoDB 저장
browser.quit()