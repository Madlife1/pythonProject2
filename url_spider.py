import requests
from bs4 import BeautifulSoup
import  zlib #crc32加密
list_cyc32=[]
list_url=[]
import  re
# # 为了用xpath
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent': user_agent}
# url="https://www.cnblogs.com/mayswind/p/15116918.html"
url="https://www.cnblogs.com/mayswind/default.html?page=3"
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
result=[]
soup=BeautifulSoup(r.text,'lxml')
#############crc32加密 只需要传str类型就行################
def crc32(x_url):
       return zlib.crc32(bytes(x_url, "utf-8"))
#############crc32加密 只需要传str类型就行################
############ 传入url 得到soup###########################
def get_soup (url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    result=[]
    soup = BeautifulSoup(r.text, 'lxml')
    return  soup
############ 传入url 得到soup###########################
#############找到作者所有的文章##########################
def fd_all(url):
       global list_cyc32
       for i in range(1, 9999):
              url = "/".join(url.split("/")[0:4]) + "/default.html?page=" + str(i)
              if (get_soup(url).find_all(name='a', attrs={'class': 'postTitle2 vertical-middle'}) == []):
                     break
              items = get_soup(url).find_all(name='a', attrs={'class': 'postTitle2 vertical-middle'})

              for i in items:
                     list_cyc32 = crc32(i.get('href'))
                     list_url=i.get('href')
#############找到作者所有的文章##########################


print(crc32(url))
print(list_url)