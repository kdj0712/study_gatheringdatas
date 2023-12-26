from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()

chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
# 잦은 접속으로 로봇 호출이 나오기 전에 user-agent를 알려주어, 접속의 패널티의 가능성을 줄이는 기능

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory),options=chrome_options)

capabilities = browser.capabilities

from selenium.webdriver.common.by import By

for page_number in range(1,11) :  # page number
    url = "https://www.coupang.com/np/campaigns/348?page={}".format(page_number)
    browser.get(url)
    time.sleep(3)
    html = browser.page_source        
    pass                                 


