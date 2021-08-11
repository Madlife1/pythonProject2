import requests
from bs4 import BeautifulSoup
import  zlib #crc32加密
list_cyc32=[]
import  re
# # 为了用xpath
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent': user_agent}
url="https://www.cnblogs.com/mayswind/p/15116918.html"
# url="https://www.cnblogs.com/mayswind/default.html?page=3"
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
result=[]
soup=BeautifulSoup(r.text,'lxml')
for i in range(1, 9999):
    if (soup.select('div[class^="day"]')==''):
        break
    url = "/".join(url.split("/")[0:4]) + "/default.html?page=" + str(i)
    print(url)