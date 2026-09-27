from lxml import etree
div='''
<!DOCTYPE html> <html lang="en"> 
<head> <meta charset="UTF-8"> <title>电影信息</title> </head> 
<body> 
<div class="movie">
 <h2>电影名称：《阿凡达》</h2> 
<p>导演：詹姆斯·卡梅隆</p> 
<p>主演：萨姆·沃⾟顿，佐伊·索尔达娜</p>
<p>评分：8.8</p>
 <p>票房：27.88 亿美元</p> 
</div> 
</body> 
</html>
'''
#渲染数据
tree=etree.HTML(div)
print(tree)
'''
    /从根节点开始及下一级
    //跨多个层级定位标签
    .选取到当前节点
    ..选取当前节点的父节点
    @选取标签属性值
'''
data=tree.xpath("//div[@class='movie']/h2/text()")
print(data)
#xpath的索引是从1开始的(即第几个的含义)
data=tree.xpath("//div[@class='movie']/p[1]/text()")
print(data)
data=tree.xpath("//div[@class='movie']/p[3]/text()")
print(data)
