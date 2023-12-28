# Selenium 버전에 따라 인자의 이름이 변경되었을 수 있으므로, 정상적인 설치 및 기능이 안 될 경우 아래의 방식으로 진행을 하도록 한다.
from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능



webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

capabilities = browser.capabilities


browser.get("https://getbootstrap.com/docs/5.3/examples/checkout/")
html = browser.page_source
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# Select(driver.find_element(By.TAG_NAME, “select”)).select_by_index(2)

# 국가 selectbox 선택
selector_element = "#country"
element_countries = browser.find_element(by=By.CSS_SELECTOR,value=selector_element)
Select(element_countries).select_by_index(1)
# 주 selectbox 선택
selector_element = "#state"
element_state = browser.find_element(by=By.CSS_SELECTOR,value=selector_element)
Select(element_state).select_by_index(1)

pass

browser.quit()