from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager           # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
import time
webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = browser.capabilities
browser.get("https://play.google.com/store/apps/details?id=com.nhlife.customer.healthcare&hl=ko-KR&pli=1")
time.sleep(3)
html = browser.page_source
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


button = "#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > header > div > div:nth-child(2) > button"
comment_button = browser.find_element(by=By.CSS_SELECTOR, value=button)
comment_button.click()

modal_body = "div > div.fysCi"
elements_scrollableDiv = browser.find_element(by=By.CSS_SELECTOR, value=modal_body)

comments = "div.RHo1pe"
elements_comment = browser.find_elements(by=By.CSS_SELECTOR, value=comments)
print("Count Comment before done scroll : {}".format(len(elements_comment)))

previous_scrollHeight = 0
# browser.execute_script("var scrollableDiv = document.querySelector('div.fysCi');")
# browser.execute_script("scrollableDiv.scrollTo(0, scrollableDiv.scrollHeight);")
while True:
    # python 방식 변수 매칭
    # print("{0}.scrollTo{1},{0}.scrollHeight);".format(elements_scrollableDiv,previous_scrollHeight))
    # javascript와 python 결합 방식 변수 매칭
    browser.execute_script("arguments[0].scrollTo(arguments[1], arguments[0].scrollHeight);"
                                                  ,elements_scrollableDiv, previous_scrollHeight)
    current_scrollheight = browser.execute_script("return arguments[0].scrollHeight;"
                                                  ,elements_scrollableDiv)
    if previous_scrollHeight >= current_scrollheight:
    # 만약 전체 높이와 비교하여 남아있는 공간이 없다면 행동을 멈추도록 선언한다.
        break
    else:
        previous_scrollHeight = current_scrollheight
        # 그렇지 않다면 해당 내용이 같아질 떄까지 반복한다.
    time.sleep(2)
    # 행동을 반복할 텀을 1초정도 준다. 반복이 진행되면서 페이지가 로딩이 될 여유를 준다.
  
    comments = "div.RHo1pe"
    elements_comment = browser.find_elements(by=By.CSS_SELECTOR, value=comments)
    print("Count Comment after done scroll : {}".format(len(elements_comment)))

    pass