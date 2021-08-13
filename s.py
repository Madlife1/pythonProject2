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
count=0
for i in range(1, 9999):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    soup1 = BeautifulSoup(r.text, 'lxml')
    url = "/".join(url.split("/")[0:4]) + "/default.html?page=" + str(i)
    if (soup1.find_all(name='div', attrs={'class': 'postTitle2 vertical-middle'})==[] and i==1):

        url = "/".join(url.split("/")[0:4]) + "/default.html?page=" + str(i)
    elif soup1.find_all(name='div', attrs={'class': 'postTitle2 vertical-middle'})==[]:
        break
    else:
        count+=1
        print(soup1.find_all(name='div', attrs={'class': 'postTitle2 vertical-middle'})==[])


    url = "/".join(url.split("/")[0:4]) + "/default.html?page=" + str(i)

print(count)
    #url 提取