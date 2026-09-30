import csv
#列表写入
data = [
    ['姓名', '年龄', '城市'], # 表头
    ['⼩明', '10', '北京'],  # 第⼀⾏数据
    ['⼩红', '12', '上海'] # 第⼆⾏数据
]
with open("学生.csv",'w',encoding='utf-8',newline='') as f:
    wr = csv.writer(f)#创造一个写入器（类似于流对象）
    wr.writerows(data)
#


#
#字典读取
title=['111','222','333']
data=[
    {
        '111':1,
        '222':2,
        '333':3
    },
    {
        '111': 11,
        '222': 22,
        '333': 33
    },
    {
        '111': 111,
        '222': 222,
        '333': 333
    }
]
with open('dic.csv','w',encoding='utf-8',newline='') as f:
    #创建字典写入对象
    wr = csv.DictWriter(f,title)
    wr.writeheader()
    wr.writerows(data)
with open("学生.csv",'r',encoding='utf-8') as f:
    rr=csv.reader(f)
    header=next(rr)
    print(rr)
    for i in rr:
        print(i)
    f.seek(0)
    dicr=csv.DictReader(f)
    for i in dicr:
        print(i)