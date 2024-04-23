from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re

def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://trainings.iptime.org:48001/") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["project"] # 해당 포트에 접속해서 database에 연결
    collection = database['helpline_Symptoms'] # 데이터베이스에서 11st_comments 이라는 collection에 연결
    return collection # collection이 반환되도록 지정

webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
driver = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = driver.capabilities
# for page_num in range(124):
#     driver.get(f"https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfList.do?menu=A0100&pageIndex={page_num+1}&fixRdizInfTab=&rdizCd=&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=&schSort=kcdCd&schOrder=desc")
#     origin_tab = driver.current_window_handle
#     html = driver.page_source
#     from selenium.webdriver.common.by import By
#     main_board = "#frm > div > table"
#     main_body = driver.find_elements(by=By.CSS_SELECTOR, value=main_board) 
#     table_rows = driver.find_elements(by=By.CSS_SELECTOR, value="#frm > div > table > tbody > tr")
#     time.sleep(2)
#     for x in range(len(table_rows)):
#         table = driver.find_elements(by=By.CSS_SELECTOR, value=f"#frm > div > table > tbody > tr:nth-child({x+1})")
#         try:
#             dise_name_kr = driver.find_element(by=By.CSS_SELECTOR, value=f"#frm > div > table > tbody > tr:nth-child({x+1}) > td:nth-child(2) > dl > dt").text
#         except:
#             dise_name_kr = ""
#             pass
#         finally:
#             pass
#         try:
#             dise_name_en = driver.find_element(by=By.CSS_SELECTOR, value=f"#frm > div > table > tbody > tr:nth-child({x+1}) > td:nth-child(2) > dl > dt > p").text
#         except:
#             dise_name_en = ""
#             pass
#         finally:
#             pass
#         try:
#             KCD_code = driver.find_element(by=By.XPATH, value=f'//*[@id="frm"]/div/table/tbody/tr[{x+1}]/td[1]/dl/dd/ul/li[4]').text
#             # 전체 <li> 요소의 텍스트를 가져옵니다.
#             # 'KCD코드 :' 텍스트를 제거합니다.
#             dise_KCD_code = KCD_code.replace('KCD코드 : ', '').strip()
#         except:
#             dise_KCD_code = ""
#             pass
#         finally:
#             pass
#         try:
#             spc = driver.find_element(by=By.XPATH, value=f'//*[@id="frm"]/div/table/tbody/tr[{x+1}]/td[1]/dl/dd/ul/li[5]').text
        
#             dise_spc_code = spc.replace('산정특례 특정기호 : ', '').strip()
#         except:
#             dise_spc_code = ""
#             pass
#         finally:
#             pass
#         try:
#             group = driver.find_element(by=By.XPATH, value=f'//*[@id="frm"]/div/table/tbody/tr[{x+1}]/td[1]/dl/dd/ul/li[1]').text
#             dise_group = group.replace('항목분류 : ', '').strip()
#         except:
#             dise_group = ""
#             pass
#         finally:
#             pass
#         try:
#             support = driver.find_element(by=By.XPATH, value=f'//*[@id="frm"]/div/table/tbody/tr[{x+1}]/td[1]/dl/dd/ul/li[3]').text
#             dise_support = support.replace('의료비지원 : ', '').strip()
#         except:
#             dise_support = ""
#             pass
#         finally:
#             pass
#         try:
#             link_element = driver.find_element(by=By.CSS_SELECTOR, value="a[title='질환정보 바로가기']")
#             # 'onclick' 속성에서 필요한 정보를 추출합니다.
#             onclick_attr = link_element.get_attribute('onclick')
#             # 정규 표현식을 사용하여 'fn_moveDetail' 함수의 인자 값을 추출합니다.
#             match = re.search(r"fn_moveDetail\('(.+?)'\);", onclick_attr)
#             if match:
#                 detail_code = match.group(1)  # 첫 번째 그룹에 해당하는 인자 값
#                 print(detail_code)  # 필요하다면 이 코드를 사용하여 추가 작업을 수행
#             else:
#                 detail_code = None  # 일치하는 것을 찾지 못한 경우
#             url_template = 'https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&rdizCd={}'
#             dise_url = url_template.format(detail_code)
#         except:
#             dise_url = ""
#             pass
#         finally:
#             pass

#         collection = Connect()
#         collection.insert_one({"dise_name_kr":dise_name_kr,"dise_name_en":dise_name_en,"dise_KCD_code":dise_KCD_code, "dise_spc_code":dise_spc_code,"dise_group":dise_group,"dise_support":dise_support,"dise_url":dise_url})
#         time.sleep(2)
    # 페이지 로딩 대기
collection = Connect()

for page_num in range(124):
    driver.get(f"https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfList.do?menu=A0100&pageIndex={page_num+1}")
    time.sleep(2)  # 페이지 로딩 대기
    table_rows = driver.find_elements(by=By.CSS_SELECTOR, value="#frm > div > table > tbody > tr")

    for row in table_rows:
        data = {}
        try:
            full_text = row.find_element(by=By.CSS_SELECTOR, value="td:nth-child(2) > dl > dt").text
            # '\n'을 기준으로 문자열을 분리하고, 첫 번째 부분만 사용합니다.
            dise_name_kr = full_text.split('\n')[0]
            # 이제 dise_name_kr에는 '\n'과 그 이후의 부분이 제거된 상태로 저장됩니다.
            data['dise_name_kr'] = dise_name_kr
        except:
            data['dise_name_kr'] = ""

        try:
            data['dise_name_en'] = row.find_element(by=By.CSS_SELECTOR, value="td:nth-child(2) > dl > dt > p").text
        except:
            data['dise_name_en'] = ""

        try:
            KCD_code = row.find_element(by=By.XPATH, value='.//td[1]/dl/dd/ul/li[4]').text
            data['dise_KCD_code'] = KCD_code.replace('KCD코드 : ', '').strip()
        except:
            data['dise_KCD_code'] = ""

        try:
            spc = row.find_element(by=By.XPATH, value='.//td[1]/dl/dd/ul/li[5]').text
            data['dise_spc_code'] = spc.replace('산정특례 특정기호 : ', '').strip()
        except:
            data['dise_spc_code'] = ""

        try:
            group = row.find_element(by=By.XPATH, value='.//td[1]/dl/dd/ul/li[1]').text
            data['dise_group'] = group.replace('항목분류 : ', '').strip()
        except:
            data['dise_group'] = ""

        try:
            support = row.find_element(by=By.XPATH, value='.//td[1]/dl/dd/ul/li[3]').text
            data['dise_support'] = support.replace('의료비지원 : ', '').strip()
        except:
            data['dise_support'] = ""

        try:
            link_element = row.find_element(by=By.CSS_SELECTOR, value="a[title='질환정보 바로가기']")
            onclick_attr = link_element.get_attribute('onclick')
            match = re.search(r"fn_moveDetail\('(.+?)'\);", onclick_attr)
            if match:
                detail_code = match.group(1)
                url_template = 'https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfDetail.do?menu=A0100&rdizCd={}'
                data['dise_url'] = url_template.format(detail_code)
            else:
                data['dise_url'] = ""
        except:
            data['dise_url'] = ""
        
        collection.insert_one(data)
        time.sleep(2)