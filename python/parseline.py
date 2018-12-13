import re
 
phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#*$', "", phone)
print("电话号码是: ", num)
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)

num = re.split(r'[\s\,]+', 'python, is greate!')
print("电话号码是 : ", num)

ret_search = re.search('\w*oo\w*','good food, is greate!'); #扫描整个字符串返回第一个匹配到的元素并结束，匹配不到返回None
if(ret_search):
    print("ret_search:"+ret_search.group());
