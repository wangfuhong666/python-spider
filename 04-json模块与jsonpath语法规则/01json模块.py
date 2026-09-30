import requests
import json
#json.dumps() python 格式--->json格式
#int float string list tuple dist支持但set不支持
#json.dump()文件级的（文件写数据），和上述功能基本一样
#json.loads() json格式--->python格式
# json.load() 文件级的
data={
    '1':'1',
    '2':'2',
    '3':'3',
}
# with open('list.txt','w',encoding='utf-8') as f:
#     f.write()
print(type(data))
print(data)
json.dumps(data)
print(type(data))
print(data)
with open('list.json','w',encoding='utf-8') as f:
    f.write(json.dumps(data,ensure_ascii=False,indent=4))
with open('list1.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=4)
a=10
print(type(json.dumps(a)))
#print(a+json.dumps(a))
b=11112222
print(type(json.dumps(b)))
print(type(json.loads(json.dumps(b))+10))
list=[1,'2',3.1,("2","$",[1,3,7],{'1':2,'444':(1,5)})]
print(json.dumps(list))

with open('list1.json','r',encoding='utf-8') as f:
    tmp=json.load(f)
    print(type(tmp))
