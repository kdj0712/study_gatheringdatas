
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
browser.get("https://www.jobplanet.co.kr/users/sign_in")


from selenium.webdriver.common.by import By
element_login_field = browser.find_element(by=By.CSS_SELECTOR, value ="#user_email")
element_login_field.send_keys("kdj0712@hanmail.net")
# 지정한 field에 내가 입력한 특정 key값이 입력되도록 한다.

element_password_field = browser.find_element(by=By.CSS_SELECTOR, value= "#user_password")
element_password_field.send_keys("********")
# 지정한 field에 내가 입력한 특정 key값이 입력되도록 한다.

element_login_button = browser.find_element(by=By.CSS_SELECTOR, value= "section.section_email.er_r > fieldset > button")
element_login_button.click
# 지정한 위치의 버튼을 클릭하도록 한다.
pass
# 브라우저 종료
browser.quit()
