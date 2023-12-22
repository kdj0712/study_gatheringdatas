from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

capabilities = browser.capabilities

browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033")

pass
html = browser.page_source
print(html)
# 하나의 Elelemts만 가져오기
from selenium.webdriver.common.by import By
# 정보 획득 시 거의 대부분 사용할 기능
# elements_path = browser.find_element( by = By.CSS_SELECTOR , value = "#ty_thmb_view > ul > li:nth-child(1) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit")
# or
# selector = "#ty_thmb_view > ul > li:nth-child(1) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit"
# elements_path = browser.find_element( by = By.CSS_SELECTOR , value = selector)
# or 
# 규칙이 명확할 경우(또는 오류가 없다고 자신할 수 있을 경우에만....)
# browser.find_element(By.CSS_SELECTOR, "#ty_thmb_view > ul > li:nth-child(1) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit")
# type(elements_path)
# <class 'selenium.webdriver.remote.webelement.WebElement'>

# get text in tag
# elements_path.text
# # '반려견패드(중)40*50cm*100매'

# elements_path.get_attribute('class')
# 'mnemitem_goods_tit'
pass
# 여러개 elements의 정보 가저오기


selector = "span.mnemitem_goods_tit"
elements_paths = browser.find_elements( by = By.CSS_SELECTOR , value = selector)
# type(elements_paths)
# <class 'list'>
# type(elements_paths[0])
# <class 'selenium.webdriver.remote.webelement.WebElement'>
# elements_paths[0]
# <selenium.webdriver.remote.webelement.WebElement (session="91aa5730bfa2991fe564aa016d1d5ce0", element="6FBB31F95D75237BF883CD30817DBD0B_element_115")>
# elements_paths[0].text
# '시리우스 펫퓸 반려견 러블리플라워 샴푸 500ML'
# elements_paths[1].text
# '시리우스 펫퓸 반려견 드라이풋샴푸 270ML'

for webelements in elements_paths:
    title = webelements.text
    print("{}".format(title))
    pass

pass
# 브라우저 종료
browser.quit()