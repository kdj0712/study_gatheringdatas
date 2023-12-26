# Selenium 버전에 따라 인자의 이름이 변경되었을 수 있으므로, 정상적인 설치 및 기능이 안 될 경우 아래의 방식으로 진행을 하도록 한다.
from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
# 패키지를 사용하여 Chrome WebDriver를 관리하는 방식입니다. 이 패키지는 WebDriver를 자동으로 다운로드하고 최신 버전을 유지해줍니다

# 23.12.16 추가 구간
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
# 이 과정들을 다 포함하여 webdriver 크롬 브라우저가 실행되도록 선언 

# 또는 이렇게도 할 수 있다.
webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory),chrome_options = Options())


# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# browser.capabilities를 사용하여 현재 브라우저가 JavaScript를 지원하는지, 쿠키를 사용할 수 있는지, 웹 드라이버 버전 정보 등을 확인할 수 있습니다.
# 이를 통해 특정 기능을 사용하기 전에 브라우저의 지원 여부를 확인하고, 필요한 조치를 취할 수 있습니다.
# Ex) :  capabilities['javascriptEnabled']
# 이상 뤼튼의 capabilities에 대한 설명


# - 주소 https://www.w3schools.com/ 입력
browser.get("https://www.w3schools.com/")
# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
print(html)
# - 정보 획득
pass

browser.save_screenshot('./format_re.png')

# 브라우저 종료
browser.quit()