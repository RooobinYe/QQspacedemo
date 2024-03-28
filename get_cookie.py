from selenium import webdriver
from time import sleep
import json
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://qzone.qq.com/') # 需要自己扫码登录QQ空间
    input() # 扫码登录，等待网站完全加载后按回车
    dictCookies = driver.get_cookies()  # 获取list的cookies
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
    with open('Cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')

