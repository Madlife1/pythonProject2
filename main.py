#过滤王道 修改标题黑体
import requests
from lxml import etree # 为了用xpath
from bs4 import BeautifulSoup
from filter import filter


# 指定我们的UserAgent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent': user_agent}
# requests库用来发送请求的语句是requests.get
r = requests.get("http://cskaoyan.com/thread-662402-1-1.html", headers=headers)
r.encoding = 'GBK'
result=[]
# print(r.text)
# html=etree.HTML(r) #初始化生成一个XPath解析对象
# m=etree.tostring(type(html),encoding='GBK')   #解析对象输出代码
soup=BeautifulSoup(r.text,'lxml')
m=0


for i in soup.find_all('font'):
 #   print(i.text)

    if(i.text!='\n' and i.text!='' and i.text!='王道论坛新道友' and i.text!='【官方公告】王道训练营2021年开班情况（短期班、Python[AI]、CC++、JAVA方向）! '):
       if filter(i) =='None':
        result.append('\n'+"<!-- wp:paragraph -->"+'\n'+"<p>"+i.text.strip('\n')+"</p>"+'\n'+"<!-- /wp:paragraph -->")
       else :
        result.append(filter(i))
        #结果放到列表中
result_str = ''.join(result)
#列表组成字符串
print(result_str)
# print(setting.c)
#print(soup.find_all('font').replace('<font style="color:rgb(0, 0, 0)">','<!-- wp:paragraph --><p>'))
# print(r.xpath("//@font style"))

#html.xpath()
# r.text.xp

