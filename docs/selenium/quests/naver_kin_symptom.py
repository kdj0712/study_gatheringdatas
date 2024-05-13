from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
from selenium.common.exceptions import NoSuchElementException, TimeoutException,UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import os
import math
def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://trainings.iptime.org:45003") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["data_analysis"] # 해당 포트에 접속해서 database에 연결
    collection = database['naver_cafe_Symptom'] # 데이터베이스에서 11st_comments 이라는 collection에 연결
    return collection # collection이 반환되도록 지정

webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
driver = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = driver.capabilities
collection = Connect()
dise_list = [
    # {"유전성근병증NOS" : "G71.9"}, {"멜라스증후군" : "G71.3"}, {"네말린근병증" : "G71.2"},
    # {"근세관성(중심핵성)근병증" :"G71.2"}, {"근섬유형 불균형":"G71.2"}, {"워커-워버그 증후군":"G71.2"}, {"선천성근병증" : "G71.2"},
    # {"근디스트로피 NOS": "G71.2"}, {"근긴장증 NOS":"G71.1"}, {"근긴장장애":"G71.1"}, {"근긴장디스트로피[스타이너트]" :"G71.1"},
    # {"우성 선천성 근긴장증" : "G71.1"}, {"열성 선천성 근긴장증" : "G71.1"}, {"선천성 이상근긴장증" : "G71.1"},
    # {"근디스트로피": "G71.0"}, {"만성 염증성 탈수초성 다발신경병증" : "G61.8"},
    # {"다초점 운동신경병증" : "G61.8"}, {"길랭바레증후군" : "G61.0"} , {"비골근위축" : "G60.0"}, {"샤르코 마리 투스" : "G60.0"},
    # {"멜커슨증후군" : "G51.2"}, {"멜커슨-로젠탈증후군" : "G51.2"}, {"하다드증후군" : "G47.31"},
    # {"레녹스-가스토증후군" : "G40.4"}, 
    # {"데빅병" : "G36.0"}, {"아이카디-구티에레스 증후군" : "G31.88"}, {"아급성 괴사성 뇌병증" : "G31.81"},
    # {"강직인간증후군" : "G25.8"},  {"핵상안근마비" : "G23.1"}, {"스틸-리차드슨-올스제위스키" : "G23.1"},
    # {"산발형 근위축측삭경화증" : "G12.21"},
    # {"유전성 강직성 하반신마비" : "G11.4"},
    # {"모세혈관확장성운동실조" : "G11.3"}, {"X-연관 열성 척수소뇌성 운동실조" : "G11.1" }, {"헌팅톤무도병" : "G10"},
    # {"헌팅톤병" : "G10"}, {"자가면역 뇌염" : "G04.8"}, {"라스무센 뇌염" : "G04.8"}
]


driver.get("https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsection.cafe.naver.com%2Fca-fe%2Fhome")
def find_next_button(xpath):
    try:
        return driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return None
def move_to_next_page(driver, current_page, counts):

    # 현재 페이지가 10 이하인 경우, 직접 페이지 번호를 클릭
    if counts <= 10:
        # 현재 페이지가 마지막 페이지가 아닌 경우에만 다음 페이지로 이동
        if current_page <= counts:
            next_page_xpath = [f'/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[{current_page + 1}]',
                               f'/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/button[{current_page + 1}]']
            for xpath in next_page_xpath:
                next_button = find_next_button(xpath)
                if next_button:
                    next_button.click()

    else:
        # 현재 페이지가 10 이하인 경우, 직접 페이지 번호를 클릭
        if current_page <= 10:
            next_page_xpath = [f'/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[{current_page + 1}]',
                               f'/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/button[{current_page + 1}]']
            for xpath in next_page_xpath:
                next_button = find_next_button(xpath)
                if next_button:
                    next_button.click()

        else:
            # 현재 페이지가 10 초과이고, 마지막 페이지 범위에 있지 않은 경우, '다음' 버튼 클릭
            page_position_in_group = (current_page - 1) % 10 + 1
            if page_position_in_group < 10:
                next_page_xpath = [f'/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[{page_position_in_group + 2}]',
                                   f'/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/button[{page_position_in_group + 2}]']
                for xpath in next_page_xpath:
                    next_button = find_next_button(xpath)
                    if next_button:
                        next_button.click()

            else:
                # 페이지 그룹의 마지막 페이지에서는 '다음' 버튼(11번째 버튼)을 클릭
                next_page_xpath = [f'/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[{page_position_in_group + 2}]',
                                   f'/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/button[{page_position_in_group + 2}]']
                for xpath in next_page_xpath:
                    next_button = find_next_button(xpath)
                    if next_button:
                        next_button.click()

def move_to_next_page_for_last(driver, current_page, counts):

    # 현재 페이지가 10 이하인 경우, 직접 페이지 번호를 클릭
    if counts <= 10:
        # 현재 페이지가 마지막 페이지가 아닌 경우에만 다음 페이지로 이동
        if current_page <= counts:
            next_page_xpath = [f'/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[{current_page}]',
                               f'/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/button[{current_page}]']
            for xpath in next_page_xpath:
                next_button = find_next_button(xpath)
                if next_button:
                    next_button.click()

    else:
        # 현재 페이지가 10 이하인 경우, 직접 페이지 번호를 클릭
        if current_page <= 10:
            next_page_xpath = [f'/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[{current_page}]',
                               f'/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/button[{current_page}]']
            for xpath in next_page_xpath:
                next_button = find_next_button(xpath)
                if next_button:
                    next_button.click()

        else:
            # 현재 페이지가 10 초과이고, 마지막 페이지 범위에 있지 않은 경우, '다음' 버튼 클릭
            page_position_in_group = (current_page - 1) % 10 + 1
            if page_position_in_group < 10:
                next_page_xpath = [f'/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[{page_position_in_group + 1}]',
                                   f'/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/button[{page_position_in_group + 1}]']
                for xpath in next_page_xpath:
                    next_button = find_next_button(xpath)
                    if next_button:
                        next_button.click()

            else:
                # 페이지 그룹의 마지막 페이지에서는 '다음' 버튼(11번째 버튼)을 클릭
                next_page_xpath = [f'/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[{page_position_in_group + 1}]',
                                   f'/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/button[{page_position_in_group +1}]']
                for xpath in next_page_xpath:
                    next_button = find_next_button(xpath)
                    if next_button:
                        next_button.click()

all_done = False 

for dise in dise_list:
# 파일이 존재하며 내용이 있는지 확인
    if os.path.isfile('last_processed_naver.txt') and os.path.getsize('last_processed_naver.txt') > 0:
        with open('last_processed_naver.txt', 'r', encoding='utf-8') as f:
            last_info = f.read().strip()
        if last_info:  # 파일에 내용이 있는 경우
            dise_name, last_page = last_info.split(',')
            last_page = int(last_page)  # 페이지 번호를 정수로 변환
            # dise_list에서 읽은 dise_name에 해당하는 dise_code 찾기
            found = False
            for dise in dise_list:
                if dise_name in dise:
                    dise_code = dise[dise_name]
                    found = True
                    break
            # 만약 dise_list에서 해당하는 dise_name을 찾지 못했다면, 오류 처리
            if not found:
                print(f"Error: '{dise_name}' is not found in dise_list.")
                # 필요한 경우 여기서 추가적인 오류 처리를 수행할 수 있습니다.
    else:
        # 파일이 없거나 비어있는 경우, dise_list의 첫 번째 항목 사용 및 last_page를 1로 초기화
        dise_name = list(dise_list[0].keys())[0]
        dise_code = list(dise_list[0].values())[0]
        last_page = 1
    # 웹사이트 열기
    if dise_name:
       driver.get(f"https://section.cafe.naver.com/ca-fe/home/search/articles?q={dise_name}")
    time.sleep(2)
    totals = driver.find_element(by=By.CSS_SELECTOR, value ="#mainContainer > div.content > div.section_home_search > div.search_item_wrap > div.board_head > div.sub_text").text
    totals = totals.replace(",","")
    total = int(totals)
    counts = math.ceil(total / 12)
    
    if counts == 1:
        table = driver.find_elements(by=By.CSS_SELECTOR, value ="#mainContainer > div.content > div.section_home_search")
        articles = driver.find_elements(by=By.CSS_SELECTOR, value ="div.search_item_wrap > div.item_list > div > div")
        origin_tab = driver.current_window_handle
        for article in articles:
            cafe = article.find_element(by=By.CSS_SELECTOR, value ="#mainContainer > div.content > div > div.search_item_wrap > div.item_list > div > div > div > a.cafe_info > span.cafe_name").text
            con_title = article.find_element(by=By.CSS_SELECTOR, value ="div.search_item_wrap > div.item_list > div > div > div > a:nth-child(1) > strong")
            con_title.click()
            all_tabs = driver.window_handles
            new_tab = [tab for tab in all_tabs if tab != origin_tab][0]
            try:
                WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.NAME, 'cafe_main'))
                )
            except TimeoutException:
                # 시간 초과 발생 시 수행할 동작
                print("시간 초과로 인해 대기하지 않고 다음 작업으로 넘어갑니다.")
                driver.close()
                driver.switch_to.window(origin_tab)  # 원래의 탭으로 돌아감
                continue  # 다음 article로 넘어감
            try:
                try : 
                    driver.switch_to.alert.dismiss()
                    driver.close()
                    driver.switch_to.window(origin_tab)  
                    continue
                except :
                    pass
                try:
                    WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > a > strong'))
                    )
                except UnexpectedAlertPresentException:
                    time.sleep(3)
                    driver.close()
                    driver.switch_to.window(origin_tab)  
                    continue
                time.sleep(2)
                elements_switched_tab = driver.find_elements(by=By.CSS_SELECTOR,value="#app > div > div > div.ArticleContentBox")
                for items in elements_switched_tab:
                    try:
                        time.sleep(2)
                        title = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_header > div.ArticleTitle > div > h3').text
                        name = items.find_element(by=By.CSS_SELECTOR, value='.nickname').text
                        date = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_header > div.WriterInfo > div.profile_area > div.article_info > span.date').text
                        try:
                            contents = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_container > div.article_viewer > div > div.content.CafeViewer > div > div').text
                        except:
                            contents = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_container > div.article_viewer > div > div').text
                        num = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > a > strong').text
                        num = int(num)
                        reply_list = []
                        if num != 0:
                            for j in range(num):
                                paths = [
                                        f'/html/body/div/div/div/div[2]/div[2]/div[6]/ul/li[{j+1}]/div/div/div[2]/p/span',
                                        f'/html/body/div/div/div/div[2]/div[2]/div[5]/ul/li[{j+1}]/div/div/div[2]/p/span',
                                        f'/html/body/div/div/div/div[2]/div[2]/div[7]/ul/li[{j+1}]/div/div/div[2]/p/span'
                                    ]
                                reply = None
                                for path in paths:
                                    try:
                                        reply = items.find_element(by=By.XPATH, value=path).text
                                        break  # 성공적으로 reply를 찾으면 반복문 탈출
                                    except NoSuchElementException:
                                        continue  # 현재 경로로 찾지 못하면 다음 경로 시도

                                # 찾은 reply가 있으면 reply_list에 추가
                                if reply is not None:
                                    reply_list.append(reply)
                        else:
                            reply_list = ""
                    except:
                        pass
                    data = {
                        'dise_name': dise_name,
                        'dise_code': dise_code,
                        'cafe': cafe,
                        'title': title,
                        'name': name,
                        'date': date,
                        'contents': contents,
                        'review': reply_list
                    }
                collection.insert_one(data)
                driver.close()
                title = ""
                name = ""
                date = ""
                contents = ""
                reply_list = []
                driver.switch_to.window(origin_tab)
                time.sleep(2)
                pass
            except TimeoutException:
                # 시간 초과 발생 시 수행할 동작
                print("시간 초과로 인해 대기하지 않고 다음 작업으로 넘어갑니다.")
                driver.close()
                driver.switch_to.window(origin_tab)  # 원래의 탭으로 돌아감
                continue  # 다음 article로 넘어감
        if current_page == counts:
            current_index = None
            for i, dise in enumerate(dise_list):
                if dise_name in dise:
                    current_index = i
                    break
            
            # 다음 dise_name과 dise_code 가져오기
            if current_index is not None:
                next_index = current_index + 1
                if next_index < len(dise_list):  # 리스트의 끝에 도달하지 않았다면
                    next_dise = dise_list[next_index]
                    dise_name = list(next_dise.keys())[0]
                    dise_code = next_dise[dise_name]
                    last_page = 1  # last_page 초기화
                    # 파일 업데이트
                    with open('last_processed_naver.txt', 'w', encoding='utf-8') as f:
                        f.write(f'{dise_name},{last_page}')
                else:
                    print("리스트의 끝에 도달했습니다.")
            break


    elif counts > 1:
        current_page = 1
        while current_page <= counts and current_page <= 100:  # 여기를 수정했습니다.
            if current_page != last_page and current_page < last_page+1:
                time.sleep(1)
                move_to_next_page(driver, current_page, counts)
                current_page += 1
            elif current_page == counts+1:
                current_index = None
                for i, dise in enumerate(dise_list):
                    if dise_name in dise:
                        current_index = i
                        break
                
                # 다음 dise_name과 dise_code 가져오기
                if current_index is not None:
                    next_index = (current_index + 1) % len(dise_list)  # 리스트의 끝에 도달하면 처음으로 돌아감
                    next_dise = dise_list[next_index]
                    dise_name = list(next_dise.keys())[0]
                    dise_code = next_dise[dise_name]
                    last_page = 1  # last_page 초기화               
                    # 파일 업데이트
                    with open('last_processed_naver.txt', 'w', encoding='utf-8') as f:
                        f.write(f'{dise_name},{last_page}')
                break
            
            elif current_page <= counts:
                time.sleep(1)
                table = driver.find_elements(by=By.CSS_SELECTOR, value ="#mainContainer > div.content > div.section_home_search")
                articles = driver.find_elements(by=By.CSS_SELECTOR, value ="div.search_item_wrap > div.item_list > div > div")
                origin_tab = driver.current_window_handle
                for article in articles:
                    cafe = article.find_element(by=By.CSS_SELECTOR, value ="#mainContainer > div.content > div > div.search_item_wrap > div.item_list > div > div > div > a.cafe_info > span.cafe_name").text
                    con_title = article.find_element(by=By.CSS_SELECTOR, value ="div.search_item_wrap > div.item_list > div > div > div > a:nth-child(1) > strong")
                    con_title.click()
                    all_tabs = driver.window_handles
                    new_tab = [tab for tab in all_tabs if tab != origin_tab][0]
                    driver.switch_to.window(new_tab)
                    try:
                        WebDriverWait(driver, 10).until(
                        EC.frame_to_be_available_and_switch_to_it((By.NAME, 'cafe_main'))
                        )
                    except TimeoutException:
                        # 시간 초과 발생 시 수행할 동작
                        print("시간 초과로 인해 대기하지 않고 다음 작업으로 넘어갑니다.")
                        driver.close()
                        driver.switch_to.window(origin_tab)  # 원래의 탭으로 돌아감
                        continue  # 다음 article로 넘어감
                    try:
                        try : 
                            driver.switch_to.alert.dismiss()
                            driver.close()
                            driver.switch_to.window(origin_tab)  
                            continue
                        except :
                            pass
                        try:
                            WebDriverWait(driver, 15).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > a > strong'))
                            )
                        except UnexpectedAlertPresentException:
                            time.sleep(3)
                            driver.close()
                            driver.switch_to.window(origin_tab)  
                            continue
                        time.sleep(2)
                        elements_switched_tab = driver.find_elements(by=By.CSS_SELECTOR,value="#app > div > div > div.ArticleContentBox")
                        for items in elements_switched_tab:
                            try:
                                time.sleep(2)
                                title = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_header > div.ArticleTitle > div > h3').text
                                name = items.find_element(by=By.CSS_SELECTOR, value='.nickname').text
                                date = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_header > div.WriterInfo > div.profile_area > div.article_info > span.date').text
                                try:
                                    contents = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_container > div.article_viewer > div > div.content.CafeViewer > div > div').text
                                except:
                                    contents = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_container > div.article_viewer > div > div').text
                                num = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > a > strong').text
                                num = int(num)
                                reply_list = []
                                if num != 0:
                                    for j in range(num):
                                        paths = [
                                                f'/html/body/div/div/div/div[2]/div[2]/div[6]/ul/li[{j+1}]/div/div/div[2]/p/span',
                                                f'/html/body/div/div/div/div[2]/div[2]/div[5]/ul/li[{j+1}]/div/div/div[2]/p/span',
                                                f'/html/body/div/div/div/div[2]/div[2]/div[7]/ul/li[{j+1}]/div/div/div[2]/p/span'
                                            ]
                                        reply = None
                                        for path in paths:
                                            try:
                                                reply = items.find_element(by=By.XPATH, value=path).text
                                                break  # 성공적으로 reply를 찾으면 반복문 탈출
                                            except NoSuchElementException:
                                                continue  # 현재 경로로 찾지 못하면 다음 경로 시도
                                        # 찾은 reply가 있으면 reply_list에 추가
                                        if reply is not None:
                                            reply_list.append(reply)
                                else:
                                    reply_list = ""
                            except:
                                pass
                            data = {
                                'dise_name': dise_name,
                                'dise_code': dise_code,
                                'cafe': cafe,
                                'title': title,
                                'name': name,
                                'date': date,
                                'contents': contents,
                                'review': reply_list
                            }
                        collection.insert_one(data)
                        with open('last_processed_naver.txt', 'w', encoding='utf-8') as f:
                            f.write(f"{dise_name},{current_page}")
                        driver.close()
                        title = ""
                        name = ""
                        date = ""
                        contents = ""
                        reply_list = []
                        driver.switch_to.window(origin_tab)
                        time.sleep(2)
                        pass
                    except TimeoutException:
                        # 시간 초과 발생 시 수행할 동작
                        print("시간 초과로 인해 대기하지 않고 다음 작업으로 넘어갑니다.")
                        driver.close()
                        driver.switch_to.window(origin_tab)  # 원래의 탭으로 돌아감
                        continue  # 다음 article로 넘어감  
                if current_page < counts:
                    current_page += 1
                    move_to_next_page_for_last(driver,current_page,counts)
                    with open('last_processed_naver.txt', 'w', encoding='utf-8') as f:
                        f.write(f"{dise_name},{current_page}")
                    time.sleep(1)  # 페이지 로딩 대기
                elif current_page == counts:
                    current_index = None
                    for i, dise in enumerate(dise_list):
                        if dise_name in dise:
                            current_index = i
                            break
                    
                    # 다음 dise_name과 dise_code 가져오기
                    if current_index is not None:
                        next_index = current_index + 1
                        if next_index < len(dise_list):  # 리스트의 끝에 도달하지 않았다면
                            next_dise = dise_list[next_index]
                            dise_name = list(next_dise.keys())[0]
                            dise_code = next_dise[dise_name]
                            last_page = 1  # last_page 초기화
                            # 파일 업데이트
                            with open('last_processed_naver.txt', 'w', encoding='utf-8') as f:
                                f.write(f'{dise_name},{last_page}')
                        else:
                            print("리스트의 끝에 도달했습니다.")
                            all_done = True  # 모든 처리 완료
                            break
    if all_done:
        break  # 바깥쪽 반복문 종료


driver.quit()