from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://trainings.iptime.org:48001/") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["project"] # 해당 포트에 접속해서 database에 연결
    collection = database['helpline_Symptom2'] # 데이터베이스에서 11st_comments 이라는 collection에 연결
    return collection # collection이 반환되도록 지정

webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
driver = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = driver.capabilities
driver.get("https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfList.do?menu=A0100")
origin_tab = driver.current_window_handle
while True:
    html = driver.page_source
    main_board = "#frm > div > table"
    main_body = driver.find_elements(by=By.CSS_SELECTOR, value=main_board) 
    for i in range(5, 14):
        into = "#frm > div > table > tbody > tr > td > a"
        element_buttons = driver.find_elements(by=By.CSS_SELECTOR, value=into)
        time.sleep(1)
        for x in element_buttons:
            x.click()
            try:
                disease_korean_title = driver.find_element(by=By.CSS_SELECTOR, value="#frm > div > table.listT2.help_list > tbody > tr > td.subject > em").text
            except:
                disease_korean_title = ""
                pass
            finally:
                pass

            try:
                related_diseases  = driver.find_element(by=By.CSS_SELECTOR, value="#frm > div > table.dic_viewT > tbody > tr:nth-child(1) > td:nth-child(2)").text
            except:
                related_diseases = ""
            finally:
                pass

            try:
                diseases_symptoms = driver.find_element(by=By.CSS_SELECTOR, value="#frm > div > table.dic_viewT > tbody > tr:nth-child(2) > td:nth-child(2) > pre").text
            except:
                diseases_symptoms = ""
                pass
            finally:
                pass

            try:
                cause_diseases = driver.find_element(by=By.CSS_SELECTOR, value="#frm > div > table.dic_viewT > tbody > tr:nth-child(2) > td:nth-child(4)").text
            except:
                cause_diseases = ""
                pass
            finally:
                pass

            collection = Connect()
            collection.insert_one({"disease_korean_title":disease_korean_title,"related_diseases":related_diseases,"diseases_symptoms":diseases_symptoms, "cause_diseases":cause_diseases})
            time.sleep(1)
            driver.back()
        page_button = driver.find_element(by=By.CSS_SELECTOR, value=f'#frm > div > ul.paging > li:nth-child({i})') 
    page_button.click()
    time.sleep(1)
    next_button = driver.find_element(by=By.XPATH, value='//*[@id="frm"]/div/ul[2]/li[15]/a/img')
    next_button.click()

driver.quit()
