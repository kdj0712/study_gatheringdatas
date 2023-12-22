
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
browser.get("https://github.com/login")


from selenium.webdriver.common.by import By
element_login_field = browser.find_element(by=By.CSS_SELECTOR, value ="#login_field")
element_login_field.send_keys("kdj0712@gmail.com")

element_password_field = browser.find_element(by=By.CSS_SELECTOR, value= "#password")
element_password_field.send_keys("*******")


element_login_button = browser.find_element(by=By.CSS_SELECTOR, value= "div > input.btn.btn-primary.btn-block.js-sign-in-button")
element_login_button.click
pass
# 브라우저 종료
browser.quit()


# 이상 V2 (결과물은 동일)