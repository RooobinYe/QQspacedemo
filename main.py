import requests
from bs4 import BeautifulSoup
import re

from selenium import webdriver

cookie = 'your cookie'
# url = 'https://user.qzone.qq.com/2785545653'
url = 'https://user.qzone.qq.com/proxy/....'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    'cookie':cookie
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
content = response.text
soup = BeautifulSoup(content, "html.parser")
info = soup.findAll("div", attrs={"class": "f-info"})
first_info = info[0].get_text(strip=True) if info else None         #提取第一个推文
time = soup.findAll("span", attrs={"class": "ui-mr8 state"})
first_time = time[0].get_text(strip=True) if time else None         #提取第一个时间
print(first_info,first_time)
