a="111"
a+="10"
print(type(a))
print(a)
a='123 456'
#split()分割，以什么样子分割，默认以空格分割
b=a.split()
print(b)
c='123 456 789'
#replace方法用于替换字符串里面的的子字符串为其他的字符串
c=c.replace('123','111')
print(c)
#去除两边的空格
d="\n\t  111  \t\n"
print(d)
#去除两边的空白字符
d=d.strip()
print(d)
e="      111      "
print(e)
e=e.strip()
print(e)

a=[111,222,"333"]
print(a[1])
#切片区间左闭右开[开始索引:结束索引:步长]
#开始索引不写默认从0开始
#结束索引不写默认是
#左闭右开：能够取到开始索引的元素，但是取不到结束索引的元素，所以我们要结束索引加1
print(a[0:3])
list1=[]
list1.append(11)
list1.append(11)
list1.append(11)
print(list1.index(11))
#类与对象
class Text:
    def __init__(self,age):
        self.age=age

