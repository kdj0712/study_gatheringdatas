# 정상 구동 시 이대로 충분, 정상적으로 작동하지 않을 경우 format_re.py를 참조

# * 웹 크롤링 동작
from selenium import webdriver

# - chrome browser 열기   - launch chrome browser
browser = webdriver.Chrome()
# chrome class 생성자
# module인지 생성자인지는 ()안에 변수 등이 들어가있는 유무 여부 등

# - 주소 https://www.w3schools.com/ 입력 - enter 'https://www.w3schools.com/index.html' 
browser.get("https://www.w3schools.com/")

# - 가능 여부에 대한 OK 받음 - response for possibility signal
pass 

# html 파일 받음 (and 확인)  - recieve html file(and check)
html = browser.page_source
print(html)

# - 정보 획득
pass
browser.quit()

# 이상 V1

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
# - 주소 https://www.w3schools.com/ 입력
browser.get("https://www.w3schools.com/")
# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
print(html)
# - 정보 획득
pass
# 브라우저 종료
browser.quit()


# 이상 V2 (결과물은 동일)