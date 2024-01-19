import courtauction_ui_select_selector_subfunction as subfunction



# 기본 function 형식 - stand-bying. 호출되었을 때만 기능.
def main(): 
    try :
        uri="https://www.courtauction.go.kr/"
        browser = subfunction.getBrowserFromURI(uri)    #  실제 동작을 하는 function을 기재하여 둔다.
        browser = subfunction.clickThingsCourt(browser)
        court_count = subfunction.selectCourts(browser=browser)
        print("court count : {}".format(court_count))
    except:
        pass   # 업무 코드가 문제 발생 시 대처 코드
    finally:
        subfunction.quitBrowser(browser)  # 언제나 수행되어야 할 업무
    return 0

if __name__ == "__main__":
    try :
        main()   # 업무 코드
    except:
        pass   # 업무 코드가 문제 발생 시 대처 코드
    finally:
        pass   # try나 except가 끝난 후 무조건 실행 코드
