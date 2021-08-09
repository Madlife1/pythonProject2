import requests
from bs4 import BeautifulSoup
import lxml# 为了用xpath
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent': user_agent}
url="https://www.toutiao.com/a6963529099482579467/?log_from=13800f17facf2_1627988539710"
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
soup=BeautifulSoup(r.text,'lxml')
print(r.text)