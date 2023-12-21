# * 웹 크롤링 동작
from selenium import webdriver
# - chrome browser 열기
browser = webdriver.Chrome()
# chrome class 생성자
# module인지 생성자인지는 ()안에 변수 등이 들어가있는 유무 여부 등

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://www.w3schools.com/")

# - 가능 여부에 대한 OK 받음
pass

# html 파일 받음 (and 확인)
html = browser.page_source
print(html)

# - 정보 획득
pass
browser.quit()

# - launch chrome browser
# - enter 'https://www.w3schools.com/index.html' 
# - response for possibility signal
# - recieve html file(and check)
