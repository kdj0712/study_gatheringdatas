from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import os

def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://trainings.iptime.org:45003") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["data_analysis"] # 해당 포트에 접속해서 database에 연결
    collection = database['naver_cafe_Symptom'] # 데이터베이스에서 11st_comments 이라는 collection에 연결
    return collection # collection이 반환되도록 지정

if os.path.isfile('last_processed_naver.txt') and os.path.getsize('last_processed_naver.txt') > 0:
    with open('last_processed_naver.txt', 'r', encoding='utf-8') as f:
        last_info = f.read().strip()
        last_dise_name, last_page = last_info.split(',')
        last_page = int(last_page)  # 페이지 번호를 정수로 변환
else:
    last_dise_name = None  # 파일이 없거나 비어있는 경우 초기값 설정
    last_page = 0

webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
driver = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = driver.capabilities

dise_list = [
    {"척수공동증 및 연수공동증" : "G95.0"}, {"복합부위통증증후군":"G90.6"}, {"람베르트-이튼증후군":"G73.1"},{"봉입체근염" : "G72.4"},
    {"주기마비(가족성)저칼륨혈성" :"G72.3"}, {"유전성근병증NOS" : "G71.9"}, {"멜라스증후군" : "G71.3"}, {"네말린근병증" : "G71.2"},
    {"근세관성(중심핵성)근병증" :"G71.2"}, {"근섬유형 불균형":"G71.2"}, {"워커-워버그 증후군":"G71.2"}, {"선천성근병증" : "G71.2"},
    {"근디스트로피 NOS": "G71.2"}, {"근긴장증 NOS":"G71.1"}, {"근긴장장애":"G71.1"}, {"근긴장디스트로피[스타이너트]" :"G71.1"},
    {"우성 선천성 근긴장증" : "G71.1"}, {"열성 선천성 근긴장증" : "G71.1"}, {"선천성 이상근긴장증" : "G71.1"},
    {"근디스트로피": "G71.0"}, {"중증근무력증" : "G70.0"}, {"만성 염증성 탈수초성 다발신경병증" : "G61.8"},
    {"다초점 운동신경병증" : "G61.8"}, {"길랭바레증후군" : "G61.0"} , {"비골근위축" : "G60.0"}, {"샤르코 마리 투스" : "G60.0"},
    {"멜커슨증후군" : "G51.2"}, {"멜커슨-로젠탈증후군" : "G51.2"}, {"허탈발작" : "G47.4"}, {"하다드증후군" : "G47.31"},
    {"뇌전증" : "G41.0"}, {"웨스트증후군" : "G40.4"}, {"레녹스-가스토증후군" : "G40.4"}, {"시신경척수염" : "G36.0"},
    {"데빅병" : "G36.0"}, {"다발경화증" : "G35"}, {"아이카디-구티에레스 증후군" : "G31.88"}, {"아급성 괴사성 뇌병증" : "G31.81"},
    {"강직인간증후군" : "G25.8"}, {"파르병" : "G23.8"}, {"핵상안근마비" : "G23.1"}, {"스틸-리차드슨-올스제위스키" : "G23.1"},
    {"담창구변성" : "G23.0"}, {"할러포르덴-스파츠병" : "G23.0"}, {"척수성 근위축" : "G12.8"}, {"케네디 병" : "G12.28"},
    {"산발형 근위축측삭경화증" : "G12.21"}, {"루게릭병" : "G12.2"}, {"소뇌위축증" : "G12.1"}, {"유전성 강직성 하반신마비" : "G11.4"},
    {"모세혈관확장성운동실조" : "G11.3"}, {"X-연관 열성 척수소뇌성 운동실조" : "G11.1" }, {"헌팅톤무도병" : "G10"},
    {"헌팅톤병" : "G10"}, {"자가면역 뇌염" : "G04.8"}, {"라스무센 뇌염" : "G04.8"}
]
driver.get("https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsection.cafe.naver.com%2Fca-fe%2Fhome")

def move_to_next_page(driver, current_page, counts):
    # 현재 페이지가 10 이하인 경우, 직접 페이지 번호를 클릭
    if current_page <= 10:
        next_page_xpath = f'/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[{current_page + 1}]'
    else:
    # 현재 페이지가 10 초과이고, 마지막 페이지 범위에 있지 않은 경우, '다음' 버튼 클릭
        page_position_in_group = (current_page - 1) % 10 + 1
        if page_position_in_group < 10:
            next_page_xpath = f'/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[{page_position_in_group + 2}]'
        else:
            # 페이지 그룹의 마지막 페이지에서는 '다음' 버튼(11번째 버튼)을 클릭
            next_page_xpath = '/html/body/div/div/div[2]/div[2]/div/div[2]/div[3]/button[12]'
    next_button = driver.find_element(by=By.XPATH, value=next_page_xpath)
    next_button.click()


for dise in dise_list:
    dise_name = list(dise.keys())[0]  # 현재 사전의 첫 번째 키를 가져옴  
    dise_code = list(dise.values())[0]
    # 웹사이트 열기
    driver.get(f"https://section.cafe.naver.com/ca-fe/home/search/articles?q={dise_name}")
    time.sleep(2)
    totals = driver.find_element(by=By.CSS_SELECTOR, value ="#mainContainer > div.content > div.section_home_search > div.search_item_wrap > div.board_head > div.sub_text").text
    totals = totals.replace(",","")
    total = int(totals)
    counts = round(total / 12)
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
            driver.switch_to.window(new_tab)
            driver.switch_to.frame('cafe_main') #프레임 전환
            time.sleep(2)
            elements_switched_tab = driver.find_elements(by=By.CSS_SELECTOR,value="#app > div > div > div.ArticleContentBox")
            for items in elements_switched_tab:
                try :
                    time.sleep(2)
                    title=items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_header > div.ArticleTitle > div > h3').text # 글 제목 추출
                    name=items.find_element(by=By.CSS_SELECTOR, value='.nickname').text #작성자 추출
                    date=items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_header > div.WriterInfo > div.profile_area > div.article_info > span.date').text #작성일 추출
                    contents=items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_container > div.article_viewer > div > div.content.CafeViewer > div > div').text #글내용 추출
                    num = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > a > strong').text # 댓글 개수
                    num = int(num)
                    reply_list = []
                    if num != 0:
                        for j in range(num):
                            try:
                                reply = items.find_element(by=By.XPATH, value=f'/html/body/div/div/div/div[2]/div[2]/div[6]/ul/li[{j+1}]/div/div/div[2]/p/span').text
                            except:
                                reply = items.find_element(by=By.XPATH, value=f'/html/body/div/div/div/div[2]/div[2]/div[5]/ul/li[{j+1}]/div/div/div[2]/p/span').text
                            reply_list.append(reply)
                    else:
                        reply_list = ""
                except :
                    pass
                data={
                'dise_name' : dise_name,
                'dise_code' : dise_code,
                'cafe' : cafe,  # 카페 이름
                'title' : title,
                'name' : name,
                'date' : date,
                'contents' : contents,
                'review' : reply_list
                }
                collection = Connect()
                collection.insert_one(data)
                driver.close()
                driver.switch_to.window(origin_tab)
        with open('last_processed_naver.txt', 'w', encoding='utf-8') as f:
            f.write(f"{dise_name},{current_page}")

    elif counts > 1:
        current_page = 1
        while current_page <= counts and current_page <= 100:  # 여기를 수정했습니다.
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
                driver.switch_to.frame('cafe_main')
                time.sleep(2)
                elements_switched_tab = driver.find_elements(by=By.CSS_SELECTOR,value="#app > div > div > div.ArticleContentBox")
                for items in elements_switched_tab:
                    try:
                        time.sleep(2)
                        title = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_header > div.ArticleTitle > div > h3').text
                        name = items.find_element(by=By.CSS_SELECTOR, value='.nickname').text
                        date = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_header > div.WriterInfo > div.profile_area > div.article_info > span.date').text
                        contents = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_container > div.article_viewer > div > div.content.CafeViewer > div > div').text
                        num = items.find_element(by=By.CSS_SELECTOR, value='#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > a > strong').text
                        num = int(num)
                        reply_list = []
                        if num != 0:
                            for j in range(num):
                                try:
                                    reply = items.find_element(by=By.XPATH, value=f'/html/body/div/div/div/div[2]/div[2]/div[6]/ul/li[{j+1}]/div/div/div[2]/p/span').text
                                except:
                                    reply = items.find_element(by=By.XPATH, value=f'/html/body/div/div/div/div[2]/div[2]/div[5]/ul/li[{j+1}]/div/div/div[2]/p/span').text
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
                    collection = Connect()
                    collection.insert_one(data)

                    driver.close()
                    driver.switch_to.window(origin_tab)
                pass
            
            if current_page < counts:
                with open('last_processed_naver.txt', 'w', encoding='utf-8') as f:
                    f.write(f"{dise_name},{current_page}")
                move_to_next_page(driver,current_page,counts)
            current_page += 1
            time.sleep(1)  # 페이지 로딩 대기

















