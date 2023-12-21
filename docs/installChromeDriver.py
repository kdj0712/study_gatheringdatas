# - chrome browser 열기
from webdriver_manager.chrome import ChromeDriverManager
# ChromeDriver 업데이트
webdriver_manager = ChromeDriverManager().install()
# ChromeDriver 실행

pass

# Chrome browser의 import가 되지 않는 경우 적용해 볼 것
# # selenium 4
# from selenium import webdriver 
# from selenium.webdriver.chrome.service import Service as ChromeService 
# from webdriver_manager.chrome import ChromeDriverManager  webdriver_manager 패키지를 사용하여 Chrome WebDriver를 관리하는 방식입니다. 이 패키지는 WebDriver를 자동으로 다운로드하고 최신 버전을 유지해줍니다

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))




# 개발자의 설명 
# from : https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/
# For now support:

# ChromeDriver
# EdgeChromiumDriver
# GeckoDriver
# IEDriver
# OperaDriver
# Compatible with Selenium 4.x and below.

# Before: You need to download the chromedriver binary, unzip it somewhere on your PC and set the path to this driver like this:
# Chromedriver 바이너리를 다운로드하여 PC 어딘가에 압축을 풀고 이 드라이버의 경로를 다음과 같이 설정해야 합니다.
# from selenium import webdriver
# driver = webdriver.Chrome('/home/user/drivers/chromedriver')
# It’s boring!!! Moreover, every time a new version of the driver is released, you need to repeat all these steps again and again.
# 그것은 지루!!! 게다가 새 버전의 드라이버가 출시될 때마다 이 모든 단계를 반복해서 반복해야 합니다
# With webdriver manager, you just need to do two simple steps:
# Webdriver Manager를 사용하면 다음 두 가지 간단한 단계만 수행하면 됩니다.
