import requests
from bs4 import BeautifulSoup
import re
import time
import json
import sys # 用于退出程序
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


QQspace_url = 'https://user.qzone.qq.com/'
njupt_youth_volunteer_association_url = 'https://user.qzone.qq.com/2785545653'

def browser_initial():
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # browser = webdriver.Chrome(options=chrome_options)
    browser = webdriver.Chrome()
    browser.get(QQspace_url)
    return browser

def log_qqspace(browser):
    browser.delete_all_cookies()
    with open('cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())

    # 往browser里添加cookies
    for cookie in listCookies:
        cookie_dict = {
            'domain': '.qq.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        browser.add_cookie(cookie_dict)
    browser.refresh()  # 刷新网页,cookies才成功

def log_njupt_youth_volunteer_association():
    browser.get(njupt_youth_volunteer_association_url)

def get_url_of_message():
    page_content = browser.page_source
    matches = re.search(r'<iframe[^>]+src="([^"]+)"', page_content)
    if matches:
        link = matches.group(1)
        # 将链接中的 HTML 实体 '&' 替换为 '&'
        link = 'https:' + link.replace('&amp;', '&')
        return link
    else:
        print("No link found")
        sys.exit(1)
    
def get_message(link):
    browser.get(link)
    page_content = browser.page_source
    with open('test.txt', 'w', encoding='utf8') as f:
        f.write(page_content)
    soup = BeautifulSoup(page_content, "html.parser")
    info = soup.findAll("div", attrs={"class": "f-info"})
    first_info = info[0].get_text(strip=True) if info else None         #提取第一个推文
    time = soup.findAll("span", attrs={"class": "ui-mr8 state"})
    first_time = time[0].get_text(strip=True) if time else None         #提取第一个时间
    return first_info, first_time

if __name__ == "__main__":
    browser = browser_initial()
    log_qqspace(browser)
    log_njupt_youth_volunteer_association()
    link = get_url_of_message()
    first_info, first_time = get_message(link)
    browser.quit()
    print(first_info, first_time)













# driver.get("https://user.qzone.qq.com/2785545653")
# # 确保页面加载完成
# driver.implicitly_wait(10)  # 例如，等待10秒
# driver.add_cookie(cookie)
# driver.get("https://user.qzone.qq.com/2785545653")
# time.sleep(10)


# # url = 'https://user.qzone.qq.com/2785545653'
# url = 'https://user.qzone.qq.com/proxy/....'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
#     'cookie':cookie
# }

# response = requests.get(url, headers=headers)
# response.encoding = 'utf-8'
# content = response.text
# soup = BeautifulSoup(content, "html.parser")
# info = soup.findAll("div", attrs={"class": "f-info"})
# first_info = info[0].get_text(strip=True) if info else None         #提取第一个推文
# time = soup.findAll("span", attrs={"class": "ui-mr8 state"})
# first_time = time[0].get_text(strip=True) if time else None         #提取第一个时间
# print(first_info,first_time)
