from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager                # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://trainings.iptime.org:45003") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["data_analysis"] # 해당 포트에 접속해서 database에 연결
    collection = database['naver_cafe_Symptom'] # 데이터베이스에서 11st_comments 이라는 collection에 연결
    return collection # collection이 반환되도록 지정

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







driver.get("https://section.cafe.naver.com/ca-fe/home")











for page_num in range(1056938):
    driver.get(f"https://kin.naver.com/search/list.naver?query=%EC%A6%9D%EC%83%81&page={page_num+1}")
    origin_tab = driver.current_window_handle
    html = driver.page_source
    from selenium.webdriver.common.by import By
    main_board = "#s_content > div.section"
    element_body = driver.find_elements(by=By.CSS_SELECTOR, value=main_board) 
    main_body = driver.find_elements(by=By.CSS_SELECTOR, value=main_board) 
    main_question_title = "#s_content > div.section > ul > li > dl > dt > a"
    main_questions = driver.find_elements(by=By.CSS_SELECTOR,value=main_question_title)

    for question in main_questions:
        question.click()
        # driver.execute_script("window.open('https://www.google.com');")
        all_tabs = driver.window_handles
        new_tab = [tab for tab in all_tabs if tab != origin_tab][0]
        driver.switch_to.window(new_tab)
        elements_switched_tab = driver.find_elements(by=By.CSS_SELECTOR,value="#content")

        for items in elements_switched_tab:
            try:
                element_question_title = items.find_element(by=By.CSS_SELECTOR, value="div.c-heading._questionContentsArea.c-heading--default-old > div.c-heading__title > div > div.title")
                
                question_title = element_question_title.text
            except:
                question_title = ""
                pass
            finally:
                pass
            try:
                element_question_content  = items.find_element(by=By.CSS_SELECTOR, value="div.c-heading._questionContentsArea.c-heading--default-old > div.c-heading__content")
                question_content  = element_question_content.text
            except: # 조건에 맞지 않는 것이 나와도 다른 액션을 취하지 않고 그냥 흘러가도록 지정함
                question_content = ""
            finally:
                pass

            try:
                element_question_datetime = items.find_element(by=By.CSS_SELECTOR, value="div.c-userinfo__left > span:nth-child(2)")
                # 가져온 items의 내용물을 비교하여 value에 지정한 값과 같은 것을 찾는다면, 그것을 element_point라는 변수로 선언한다.
                question_datetime = element_question_datetime.text
                # element_point을 텍스트화 한 것을 comment라는 변수로 선언
            except:
                question_datetime = ""
                pass
            finally:
                pass
            
            answers = {}
            answer_elements = driver.find_elements(by=By.CSS_SELECTOR, value="div._endContents.c-heading-answer__content")
            for i in range(1, 4):
                if i <= len(answer_elements):
                    answer_element = answer_elements[i-1]
                    content_elements = answer_element.find_elements(by=By.CSS_SELECTOR, value="div._endContentsText.c-heading-answer__content-user")
                    if content_elements:
                        content = content_elements[0].text
                    else:
                        content = None

                    datetime_elements = answer_element.find_elements(by=By.CSS_SELECTOR, value="p.c-heading-answer__content-date")
                    if datetime_elements:
                        datetime = datetime_elements[0].text
                    else:
                        datetime = None
                else:
                    content = None
                    datetime = None

                # 답변의 순서를 컬럼 이름의 일부로 사용합니다.
                answers[f"answer{i}_content"] = content
                answers[f"answer{i}_datetime"] = datetime

        driver.close()
        driver.switch_to.window(origin_tab)
        collection = Connect()
        collection.insert_one({"question_title":question_title,"question_content":question_content,"question_datetime":question_datetime,**answers})
    # 페이지 로딩 대기

