import jsonpath
import json

# 老版的
# jsonpath.jsonpath(数据对象,语法规则)
dic = {
    'name': '111'
}
# dic=json.dumps(dic)
print(jsonpath.jsonpath(dic, '$.name'))
data = {"store":
            {"book":[
                {
                "category": "classics",
                "author": "施耐庵",
                "title": "⽔浒传",
                "price": 58.00
                },
                {
                "category": "classics",
                "author": "罗贯中",
                "title": "三国演义",
                "price": 68.00
                },
                {"category": "classics",
                "author": "吴承恩",
                "title": "⻄游记",
                "isbn": "978-7-5327-6543-2",
                "price": 78.00
                },
                {
                "category": "classics",
                "author": "曹雪芹",
                "title": "红楼梦",
                "isbn": "978-7-5302-1843-4",
                "price": 88.00
                }
                ],
                "bicycle":
                {
                "color": "red",
                "price": 19.95
                }
            }
}
#data=json.dumps(data)
print(jsonpath.jsonpath(data, '$.store.book[*].title'))
print(jsonpath.jsonpath(data, '$..author'))


