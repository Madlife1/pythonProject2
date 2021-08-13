import requests
from bs4 import BeautifulSoup
import  zlib #crc32加密
list_cyc32=[]
import  re
# url="https://www.cnblogs.com/mayswind/default.html?page=3"
url = "https://www.cnblogs.com/kingreatwill/p/15138144.html"
def get_soup (url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    result=[]
    soup = BeautifulSoup(r.text, 'lxml')
    return  soup

for i in range(1,9999):
    url = "/".join(url.split("/")[0:4]) + "/default.html?page=" + str(i)
    if(get_soup(url).find_all(name='a', attrs={'class': 'postTitle2 vertical-middle'})==[]):
        break
    items= get_soup(url).find_all(name='a', attrs={'class': 'postTitle2 vertical-middle'})

    for i in items:
        print(i.get('href'))