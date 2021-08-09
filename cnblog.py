import requests
from bs4 import BeautifulSoup
import  re
# # 为了用xpath
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent': user_agent}
url="https://www.cnblogs.com/mayswind/p/15116918.html"
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
result=[]
###############标题处理##########################
soup=BeautifulSoup(r.text,'lxml')
print(soup.title.string.split()[0])
###############标题处理##########################


for i in soup.select('p, div[class^="cnblogs_code"]'):
# for i in soup.find_all(["p",["div",{'class':'cnblogs_code'}]]):
# for i in soup.find_all(['p',{'class':'cnblogs_code'}]):
# for i in soup.find_all('p'):
    print(i.text)
# for i in soup.findall(re.compile(r'(p|class="cnblogs_code")')):

#     result.append(i.text+'\n')
#     result_str = ''.join(result)
# print(result_str)



