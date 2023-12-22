from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

capabilities = browser.capabilities

browser.get("https://corners.auction.co.kr/corner/categorybest.aspx")
html = browser.page_source
from selenium.webdriver.common.by import By
# 정보 획득 시 거의 대부분 사용할 기능from selenium.webdriver.common.by import By

selector_value = "div.info"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)
for element_item in element_bundle:
    # 상품 제목
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value ="div.info > em > a")
    title = element_title.text
    # 상품 판매 원가
    try :
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value =" ul > li.c_price > span")
        old_price = element_old_price.text
    except:
        old_price = ""
        pass
    finally:
        pass

    element_sale_price = element_item.find_element(by=By.CSS_SELECTOR, value="span.sale")
    sale_price = element_sale_price.text

    delivery_types = []
    element_delivery_types = element_item.find_element(by=By.CSS_SELECTOR, value="div.icon > div")
    elements = element_delivery_types.text.split()

    print("title : "+ title)
    print("old price : " + old_price)
    print("sale price : " + sale_price)
    if elements:
        for deliveries in elements:
            print("delivery type : " + deliveries)
    else:
        print("delivery type :" + "")
        
browser.quit()
            