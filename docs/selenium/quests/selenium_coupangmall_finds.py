from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

capabilities = browser.capabilities


browser.get("https://www.coupang.com/np/categories/497135")

pass
html = browser.page_source
print(html)
# 하나의 Elelemts만 가져오기
from selenium.webdriver.common.by import By

selector = "div.name"
elements_paths = browser.find_elements( by = By.CSS_SELECTOR , value = selector)

for webelements in elements_paths:
    title = webelements.text
    print("{}".format(title))
    pass

pass

browser.quit()
# 삼성전자 2021 노트북 플러스2 15.6, 퓨어 화이트, NT550XDA-K24AT, 펜티엄, 256GB, 8GB, WIN11 Pro
# Apple 2023 맥북 에어 15, 스페이스 그레이, M2 8코어, 10코어 GPU, 256GB, 8GB, 35W 듀얼, 한글
# HP 2023 노트북 15, Natural Silver, 라이젠5, 512GB, 16GB, WIN11 Home, 15-fc0072AU
# LG전자 2023 그램15, 256GB, 스노우 화이트, 15Z90RU-GAOWK, 코어i5, WIN11 Home, 16GB
# 에이수스 Vivobook Go 15, 쿨 실버, 라이젠5, 256GB, 16GB, Free DOS, E1504FA-BQ494
# LG 울트라PC 15U560 6세대 i5 8G SSD+HDD Win10, 8GB, SSD 128+HDD 500GB, 포함
# LG 2021 울트라PC 14, 화이트, 셀러론, 128GB, 4GB, WIN11 Home, 14U30P-LE12K
# A급중고 삼성 NT371B5L I5-6300HQ/16G/SSD256G/HD530/15.6/WIN10 풀스펙 노트북
# LG 노트북 그램 14Z980 가벼운 그램노트북 i5 DDR4 초고속 M.2 SSD 장착 윈도우10 프로, WIN10, 16GB, 256GB, 코어i5, 화이트
# 레노버 2022 아이디어패드 슬림 1 15AMN7 15.6, 256GB, Free DOS, 82VG002EKR, 라이젠3, Cloud Grey (82VG), 8GB
# 삼성 노트북3 NT371B5J I5-4310M/16G/SSD512G/HD4600/15.6/WIN10, WIN10 Pro, 16GB, 512GB, 코어i5, 블랙
# HP 2023 노트북 15, Jet Black, 라이젠3, 256GB, 8GB, WIN11 Home, 15-fc0073AU
# 주연테크 2023 캐리북T 13.3, 메탈, 펜티엄 실버, 128GB, 4GB, WIN11 Pro, J3GP Pro
# 베이직스 2022 베이직북 14 3세대, BB1422SS, 256GB, White, WIN11 Pro, 셀러론, 8GB
# 레노버 2023 아이디어패드 슬림 5 라이트 14ABR8 14, CLOUD GREY, 라이젠5, 512GB, 16GB, Free DOS, 82XS001CKR
# HP 2023 노트북 15, Natural Silver, 라이젠5, 512GB, 16GB, Free DOS, 15-fc0065AU
# LG 8세대 GRAM 14Z980 코어i5 16GB SSD256GB Win10, WIN10 Pro, 256GB, 화이트
# 레노버 아이디어패드 슬림 5 16IRL 16, Cloud Grey, 512GB, 16GB, Free DOS, 82XF001RKR
# 레노버 2023 아이디어패드 슬림 3 15ABR8 15.6, 82XM0039KR, Free DOS, 16GB, 256GB, 라이젠5, ARCTIC GREY
# 삼성전자 갤럭시북2/3 15.6 재택근무 학습용 노트북 한컴오피스팩 및 국내 정품 윈도우 패키지 동봉, NT550-I5, WIN11 Home, 16GB, 250GB, 코어i5, 그라파이트
# 레노버 2023 V15 G4 AMN 15.6, ARCTIC GREY, 라이젠5, 256GB, 8GB, Free DOS, 82YU000BKR
# 아이뮤즈 스톰북 노트북 N4020 35.81cm, White, 셀러론, 64GB, 4GB, WIN10 Home, StormBooK14
# LG 15UB470 I5-6200/8G/SSD128G/HD520/15.6/WIN10
# Apple 2022 맥북 에어 13 M2, 실버, M2 8코어, GPU 8코어, 256GB, 8GB, 30W, 한글, MLXY3KH/A
# 삼성전자 갤럭시북3 15.6인치 인텔 13세대 I5 인텔 Iris Xe 그래픽스 한컴오피스팩 무선마우스 증정, T-A51AG, WIN11 Home, 16GB, 500GB, 코어i5, 그라파이트
# 삼성 NT501R5L I5-6200/8G/SSD256G/15.6/WIN10, WIN10 Pro, 8GB, 256GB, 코어i5, 화이트
# LG 2023 그램16, 스노우 화이트, 코어i5, 256GB, 16GB, WIN11 Home, 16Z90R-GA5JK
# 레노버 2022 ThinkPad E15 G4 15.6, 256GB, Black, 라이젠5, 21ED004EKD, Free DOS, 8GB
# 레노버 2023 아이디어패드 슬림 3 16ABR8 16, Arctic Grey (82XR), 라이젠5, 256GB, 16GB, Free DOS, 82XR000HKR
# 삼성전자 갤럭시북2/3 15.6 재택근무 학습용 노트북 한컴오피스팩 및 국내 정품 윈도우 패키지 동봉, NT550-I3, WIN11 Home, 8GB, 250GB, 코어i3, 실버
# 삼성 LG HP 노트북 i5 가정 업무 게임 포토샵 주식용 Win10 무상1년 사은품, 실버/블랙, 삼성NT371B5J, i5 4200, 500GB, 8GB
# HP 2023 노트북 15, Jet Black, 라이젠5, 512GB, 8GB, Free DOS, 15-fc0079AU
# 애플 아이패드 6세대 미니 WIFI 64GB, Purple
# 삼성전자 갤럭시북3 15.6인치 인텔 13세대 I5 인텔 Iris Xe 그래픽스 한컴오피스팩 무선마우스 증정, T-A51AG, WIN11 Home, 16GB, 1TB, 코어i5, 그라파이트
# 삼성 게이밍노트북 NT871Z5G 인텔i5 램12G 지포스 GT750M 15.6형 윈10, WIN10, 12GB, 512GB, 코어i5, 블랙
# 삼성전자 2021 노트북 플러스2 15.6, 그라파이트, NT550XED-K24A, 펜티엄, 256GB, 16GB, WIN11 Pro
# HP 2023 노트북 15, Natural Silver, 코어i5, 512GB, 16GB, WIN11 Home, 15-fd0096tu
# 삼성전자 2022 갤럭시북 2 15.6, 256GB, 실버, NT550XED-K78AS, 코어i7, 16GB, WIN11 Home
# LG 울트라PC 15U560 6세대 i5 8G SSD+HDD Win10, 8GB, SSD 256+HDD 500GB, 포함
# LG 그램 14Z960 인텔 4G 128G Windows10 GRAM 980g
# MSI 2023 모던 14, 매트블랙, 라이젠5, 512GB, 8GB, Free DOS, MODERN 14 C7M-237XKR
# 레노버 2022 ThinkPad E15 G4, 256GB, Black, 라이젠5, 21ED004EKD, Free DOS, 16GB
# 삼성 갤럭시북3 360 15.6인치 i5 13세대 16GB 256GB S펜 태블릿 2in1 최신 대학생 사무용 업무용 NT750QFG-KH51G/S 노트북, 미스틱 실버, 코어i5, 1TB, WIN11 Home
# 삼성전자 2022 갤럭시북 2 15.6, 500GB, 실버, NT550XED-K78AS, 코어i7, 16GB, WIN11 Home
# 삼성전자 2021 노트북 플러스2 15.6, 실버(D-K24AS), NT550XED-K24A, 펜티엄, 128GB, 16GB, WIN11 Pro
# LG그램 17인치 17Z90N 10세대 i5 i7 8G SSD512G Win10 고사양 인강용 사무용 노트북, 화이트, 코어i5, 512GB, 8GB, WIN10 Pro
# 삼성전자 노트북 NT550XED-K24A 한컴오피스 증정(펜티엄 39.6cm Win11Pro RAM (8GB/16GB) SSD 378/628GB), 그라파이트(D-K24AG), 펜티엄, 628GB, 16GB, WIN11 Pro
# Apple 2023 맥북 에어 15, 미드나이트, M2 8코어, 10코어 GPU, 512GB, 16GB, 35W 듀얼, 한글
# 레노버 2023 아이디어패드 슬림 5 16ABR8 16, CLOUD GREY, 라이젠5, 512GB, 16GB, Free DOS, 82XG002QKR
# 레노버 2022 V15 G3 ABA 15.6, Iron Gray, 256GB, Free DOS, 82TV0030KR, 라이젠5, 4GB
# 레노버 아이디어패드 슬림 1 15IJL7 15.6, CLOUD_GREY, 82LX0086KR, 셀러론, 128GB, 4GB, WIN11 Home
# LG전자 2023 울트라PC 15, 화이트, 라이젠5, 256GB, 8GB, WIN11 Home, 15U40R-GR56K
# 삼성전자 2021 노트북 플러스2 15.6, 퓨어 화이트, 셀러론, NVMe128GB, 8GB, WIN10 Pro, NT550XDA-K14AW
# 삼성전자 삼성노트북 NT200B5C/i5-3210/4G/SSD128G/DVD멀티/15.6/1600*900/윈도우10/2.3kg/무상보증1년, NT200B5C, WIN10 Pro, 4GB, 128GB, 코어i5, 블랙
# LG전자 2023 울트라PC 15UD40R-GX56K *사은품증정*, WIN11 Home, 16GB, 512GB, 라이젠5, W
# LG 그램 14Z960 14ZB970 I5-6200U/8G/SSD512 슬림한 노트북 무게 980g, WIN10 Home, 8GB, 512GB, 코어i5, 화이트
# 이태원클라쓰북 그램스타일 노트북 넥스트북 풀패키지미개봉 NB141LTN41 8세대 14 IPS FHD 윈11 프로 탑재, NB144LTN41, WIN11 Pro, 4GB, 64GB, 셀러론, 화이트
# HP 2023 노트북 15, Jet Black, 코어i3, 256GB, 8GB, Free DOS, HP 15-fd0102TU
# LG 울트라PC 15U560 6세대 코어i5 8G SSD128+500G Win10 화이트, WIN10 Home, 8GB, 128GB
# 레노버 2023 아이디어패드 슬림 5i 14IRL 14, Cloud Grey, 코어i5, 512GB, 16GB, Free DOS, 82XD002XKR