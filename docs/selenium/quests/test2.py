from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# def get_css_selector_for_element(driver, element):
#     script = """
#     function getPathTo(element) {
#         if (element.id!=='')
#             return 'id("'+element.id+'")';
#         if (element===document.body)
#             return element.tagName;

#         var ix= 0;
#         var siblings= element.parentNode.childNodes;
#         for (var i= 0; i<siblings.length; i++) {
#             var sibling= siblings[i];
#             if (sibling===element)
#                 return getPathTo(element.parentNode)+'/'+element.tagName+'['+(ix+1)+']';
#             if (sibling.nodeType===1 && sibling.tagName===element.tagName)
#                 ix++;
#         }
#     }
#     return getPathTo(arguments[0]);
#     """
#     return driver.execute_script(script, element)

# driver = webdriver.Chrome()
# driver.get("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10206239/")

# 'introduction' 텍스트를 포함하는 요소 찾기


# 'abstract' 텍스트를 포함하는 요소 찾기
# element = find_element_by_text(driver, 'Abstract')
# if element:
#     css_selector = get_css_selector_for_element(driver, element)
#     print('CSS Selector:', css_selector)
#     # 여기서 요소로 스크롤할 수 있습니다.
#     element.location_once_scrolled_into_view
#     time.sleep(3) # 시각적 확인을 위해 잠시 대기
# element = find_element_by_text(driver, 'Introduction')
# if element:
#     css_selector = get_css_selector_for_element(driver, element)
#     print('CSS Selector:', css_selector)
#     # 여기서 요소로 스크롤할 수 있습니다.
#     element.location_once_scrolled_into_view
#     time.sleep(3) # 시각적 확인을 위해 잠시 대기
# driver.quit()
# def get_xpath_for_element(driver, element):
#     script = """
#     function getElementXPath(elt){
#          var path = '';
#          for (; elt && elt.nodeType == 1; elt = elt.parentNode)
#          {
#             idx = getElementIdx(elt);
#             xname = elt.tagName;
#             if (idx > 1) xname += '[' + idx + ']';
#             path = '/' + xname + path;
#          }
#          return path;
#     }
#     function getElementIdx(elt){
#         var count = 1;
#         for (var sib = elt.previousSibling; sib ; sib = sib.previousSibling){
#             if(sib.nodeType == 1 && sib.tagName == elt.tagName) count++
#         }
#         return count;
#     }
#     return getElementXPath(arguments[0]);
#     """
#     return driver.execute_script(script, element)

# 그 외의 코드는 동일하며, get_css_selector_for_element 대신 get_xpath_for_element 함수를 사용합니다.
# element = find_element_by_text(driver, 'Abstract')
# if element:
#     xpath = get_xpath_for_element(driver, element)
#     print('xpath:', xpath)
#     # 여기서 요소로 스크롤할 수 있습니다.
#     element.location_once_scrolled_into_view
#     time.sleep(3) # 시각적 확인을 위해 잠시 대기
# element = find_element_by_text(driver, 'Introduction')
# if element:
#     xpath = get_xpath_for_element(driver, element)
#     print('xpath:', xpath)
#     # 여기서 요소로 스크롤할 수 있습니다.
#     element.location_once_scrolled_into_view
#     time.sleep(3) # 시각적 확인을 위해 잠시 대기
# driver.quit()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10206239/")
# # 요소의 XPath를 가져오는 함수
# def get_full_xpath_for_element_improved(driver, element):
#     script = """
#     function getElementXPath(elt){
#         var path = '';
#         for (; elt && elt.nodeType == 1; elt = elt.parentNode)
#         {
#             var idx = getElementIdx(elt);
#             var xname = elt.tagName;
#             if (elt.id) {
#                 xname += "[@id='" + elt.id + "']";
#             } else if (elt.className) {
#                 var classes = elt.className.split(/\s+/).join('.');
#                 xname += "[contains(@class, '" + classes + "')]";
#             }
#             if (idx > 1) {
#                 xname += '[' + idx + ']';
#             }
#             path = '/' + xname + path;
#         }
#         return path;
#     }
#     function getElementIdx(elt){
#         var count = 1;
#         for (var sib = elt.previousSibling; sib ; sib = sib.previousSibling){
#             if(sib.nodeType == 1 && sib.tagName == elt.tagName) {
#                 count++;
#             }
#         }
#         return count;
#     }
#     return getElementXPath(arguments[0]);
#     """
#     return driver.execute_script(script, element)


# def find_element_by_text(driver, text):
#     elements = driver.find_elements(By.XPATH,value="//*[contains(text(), '{}')]".format(text))
#     return elements[0] if elements else None

# # 두 번째 스크립트를 사용하여 요소의 XPath를 가져온 후
# element_xpath = get_full_xpath_for_element_improved(driver, element)
# # XPath 내의 모든 태그 이름을 소문자로 변환
# element_xpath_lower = "/".join([segment.lower() if segment.isupper() else segment for segment in element_xpath.split("/")])

# # 요소와 그 자식 요소들의 텍스트를 가져오는 함수
# def get_element_text(browser, element):
#     script = """
#     var node = arguments[0];
#     var text = '';
#     for (var i = 0; i < node.childNodes.length; i++) {
#         if (node.childNodes[i].nodeType === Node.TEXT_NODE) {
#             text += node.childNodes[i].textContent.trim() + '\\n';
#         }
#     }
#     return text;
#     """
#     direct_text = browser.execute_script(script, element)
#     child_texts = [get_element_text(browser, child) for child in element.find_elements(By.XPATH, "./*")]
#     all_texts = [direct_text.strip()] + child_texts
#     return "\n".join(filter(None, all_texts))

# # 'abstract' 텍스트를 포함하는 요소 찾기
# # element = WebDriverWait(driver, 20).until(
# #     EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'abstract')]"))
# # )
# element = find_element_by_text(driver, 'abstract')
# # 위에서 찾은 요소의 XPath를 가져오기
# element_xpath = get_full_xpath_for_element(driver, element)

# # 해당 XPath의 한 단계 상위 요소의 XPath를 구성
# parent_xpath = "/".join(element_xpath.split('/')[:-1])

# # 상위 요소 찾기
# parent_element = driver.find_element(By.XPATH, parent_xpath)

# # 상위 요소와 그 하위 요소들의 모든 텍스트 가져오기
# all_text = get_element_text(driver, parent_element)
# print(all_text)

# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 웹 드라이버 초기화 및 웹 페이지 로드
driver = webdriver.Chrome()
driver.get("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10206239/")

# 요소의 전체 XPath를 가져오는 함수
def get_full_xpath_without_id_class(driver, element):
    script = """
    function getElementXPath(elt) {
        var path = '';
        for (; elt && elt.nodeType == 1; elt = elt.parentNode) {
            var idx = getElementIdx(elt);
            var xname = elt.tagName;
            // ID와 클래스를 XPath에서 제외
            if (idx > 1) {
                xname += '[' + idx + ']';
            }
            path = '/' + xname + path;
        }
        return path;
    }
    function getElementIdx(elt) {
        var count = 1;
        for (var sib = elt.previousSibling; sib; sib = sib.previousSibling) {
            // 같은 태그 이름을 가진 형제 요소만 카운트
            if(sib.nodeType == 1 && sib.tagName == elt.tagName) count++;
        }
        return count;
    }
    return getElementXPath(arguments[0]);
    """
    return driver.execute_script(script, element)


# 특정 텍스트를 포함하는 요소 찾기
def find_element_by_text(driver, text):
    elements = driver.find_elements(By.XPATH, "//*[contains(text(), '{}')]".format(text))
    return elements[0] if elements else None

# 요소와 그 자식 요소들의 텍스트를 가져오는 함수
def get_element_text(driver, element):
    script = """
    var node = arguments[0];
    var text = '';
    for (var i = 0; i < node.childNodes.length; i++) {
        if (node.childNodes[i].nodeType === Node.TEXT_NODE) {
            text += node.childNodes[i].textContent.trim() + '\\n';
        }
    }
    return text;
    """
    direct_text = driver.execute_script(script, element)
    child_texts = [get_element_text(driver, child) for child in element.find_elements(By.XPATH, "./*")]
    return "\n".join([direct_text.strip()] + child_texts).strip()


def get_full_xpath_lowercase(driver, element):
    xpath = get_full_xpath_without_id_class(driver, element)
    # XPath 내의 모든 태그 이름을 소문자로 변환
    xpath_lowercase = "/".join([segment.lower() if segment.isupper() else segment for segment in xpath.split("/")])
    return xpath_lowercase

# 'Abstract' 텍스트를 포함하는 요소 찾기
element = find_element_by_text(driver, 'Abstract')

# 요소의 전체 XPath를 가져오고, 대소문자 구분 없이 처리하기
element_xpath_lowercase = get_full_xpath_lowercase(driver, element)

# 해당 XPath의 한 단계 상위 요소의 XPath를 구성
parent_xpath = "/".join(element_xpath_lowercase.split('/')[:-1])

# 상위 요소 찾기 및 텍스트 가져오기
parent_element = driver.find_element(By.XPATH, parent_xpath)
all_text = get_element_text(driver, parent_element)

print(all_text)

driver.quit()
