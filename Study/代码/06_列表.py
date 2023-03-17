# region 插入
list = ['上海','北京','重庆','广州']

# 默认添加到列表最后
list.append('南京')
# 指定添加到列表位置
list.insert(0,'成都')
# n个列表合并
list.extend(['桂林','杭州'])
# endregion

# region 循环显示
for item in list:
    print(item)
# endregion

# region 循环删除
"""
需要将列表内容先赋值给一个临时列表变量
再循环临时列表删除目标列表
"""
temp = []
for item in list:
    temp.append(item)

for item in temp:
    list.remove(item)

print(list)
# endregion