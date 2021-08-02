import  re
# 数据清洗过滤器
def filter(i):
    if re.search("strong", str(i)) != None:
        return '\n'+"<!-- wp:paragraph -->"+'\n'+"<p>"+"<strong>"+i.text.strip('\n')+"</strong>"+"</p>"+'\n'+"<!-- /wp:paragraph -->"
    else :
        return "None"