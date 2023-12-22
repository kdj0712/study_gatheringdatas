# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

from selenium.webdriver.common.by import By

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://www.coupang.com/np/categories/194898")

# - 가능 여부에 대한 OK 받음
pass
# selector = "a"
# elements_bundle = browser.find_elements(by = By.CSS_SELECTOR , value = selector)

# for element_item in elements_bundle:
#     print(element_item.text)
#     element_title = element_item.find_element(by = By.CSS_SELECTOR, value= "div.name")
#     title = element_title.text

#     # element_old_price = element_item.find_element(by = By.CSS_SELECTOR, value= "div.mnemitem_price_row.ty_oldpr")
#     # old_price = element_old_price.text

#     print("title : {}".format(title))
#     pass

# pass
# # 브라우저 종료
# browser.quit()




from selenium.webdriver.common.by import By
selector_value = "a"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)
for element_item in element_bundle :
    # 상품 제목
    print("{}".format(element_item.text))
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value ="#\\35 308384395 > a > dl > dd > div.name")
    title = element_title.text
    # 상품 판매 원가
    element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value ="div.price > span.price-info > del")
    old_price = element_old_price.text
    try :
        pass
    except:
        old_price = " "
        pass
    finally:
        pass
    print("title : {}, old price : {}".format(title,old_price))
# 브라우저 종료
browser.quit()